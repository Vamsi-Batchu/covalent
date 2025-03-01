# Copyright 2023 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the GNU Affero General Public License 3.0 (the "License").
# A copy of the License may be obtained with this software package or at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html
#
# Use of this file is prohibited except in compliance with the License. Any
# modifications or derivative works of this file must retain this copyright
# notice, and modified files must contain a notice indicating that they have
# been altered from the originals.
#
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
#
# Relief from the License may be granted by purchasing a commercial license.

from unittest import mock

import pytest
from fastapi.responses import JSONResponse

from covalent.triggers import BaseTrigger


def test_register(mocker):
    """
    Testing whether the trigger is able
    to register itself to the Triggers server
    """

    mock_config = "mock-config"
    mock_json_data = "mock-json-data"
    mocker.patch("covalent.triggers.base.get_config", return_value=mock_config)
    mocker.patch("covalent.triggers.base.BaseTrigger.to_dict", return_value=mock_json_data)
    requests_mock = mocker.patch("covalent.triggers.base.requests")

    base_trigger = BaseTrigger()
    base_trigger.register()

    requests_mock.post.assert_called_once_with(
        f"http://{mock_config}:{mock_config}/api/triggers/register",
        json=mock_json_data,
    )


@pytest.mark.parametrize(
    "use_internal_func, mock_status",
    [
        (True, JSONResponse("mock")),
        (True, {"status": "mocked-status"}),
        (False, {"status": "mocked-status"}),
    ],
)
def test_get_status(mocker, use_internal_func, mock_status):
    """
    Testing whether get_status internally gets called with
    the right arguments in different conditions
    """

    base_trigger = BaseTrigger()
    base_trigger.use_internal_funcs = use_internal_func

    if use_internal_func:
        mocker.patch("covalent_dispatcher._service.app.get_result")

        mock_fut_res = mock.Mock()
        mock_fut_res.result.return_value = mock_status
        mock_run_coro = mocker.patch(
            "covalent.triggers.base.asyncio.run_coroutine_threadsafe", return_value=mock_fut_res
        )

        if not isinstance(mock_status, dict):
            mock_json_loads = mocker.patch(
                "covalent.triggers.base.json.loads", return_value={"status": "mocked-status"}
            )

        status = base_trigger._get_status()

        mock_run_coro.assert_called_once()
        mock_fut_res.result.assert_called_once()

        if not isinstance(mock_status, dict):
            mock_json_loads.assert_called_once()

    else:
        mock_get_status = mocker.patch("covalent.get_result", return_value=mock_status)
        status = base_trigger._get_status()
        mock_get_status.assert_called_once()

    assert status == "mocked-status"


@pytest.mark.parametrize("use_internal_func", [True, False])
@pytest.mark.parametrize("is_pending", [True, False])
def test_do_redispatch(mocker, use_internal_func, is_pending):
    """
    Testing whether the trigger's internal do_redispatch function
    with the right arguments in different conditions
    """

    base_trigger = BaseTrigger()
    base_trigger.use_internal_funcs = use_internal_func

    mock_redispatch_id = "test_dispatch_id"

    if use_internal_func:
        mocker.patch("covalent_dispatcher.run_redispatch")
        mock_fut_res = mock.Mock()
        mock_fut_res.result.return_value = mock_redispatch_id
        mock_run_coro = mocker.patch(
            "covalent.triggers.base.asyncio.run_coroutine_threadsafe", return_value=mock_fut_res
        )

        redispatch_id = base_trigger._do_redispatch(is_pending)

        mock_run_coro.assert_called_once()
        mock_fut_res.result.assert_called_once()
    else:
        mock_redispatch = mocker.patch("covalent.redispatch")()
        mock_redispatch.return_value = mock_redispatch_id
        redispatch_id = base_trigger._do_redispatch(is_pending)

        mock_redispatch.assert_called_once()

    assert redispatch_id == mock_redispatch_id


@pytest.mark.parametrize("lattice_dispatch_id", [None, "mock_id"])
@pytest.mark.parametrize("mock_status", [None, "some_status"])
def test_trigger(mocker, lattice_dispatch_id, mock_status):
    """
    Testing whether the trigger's internal trigger function
    with the right arguments in different conditions
    """

    base_trigger = BaseTrigger()
    base_trigger.lattice_dispatch_id = lattice_dispatch_id

    if not lattice_dispatch_id:
        err_str = "`lattice_dispatch_id` is None. Please attach this trigger to a lattice before triggering."
        with pytest.raises(RuntimeError) as re:
            base_trigger.trigger()
            assert re.match(err_str)

    else:
        mock_redispatch_id = "test_redispatch_id"

        mock_get_status = mocker.patch(
            "covalent.triggers.base.BaseTrigger._get_status", return_value=mock_status
        )
        mock_do_redispatch = mocker.patch(
            "covalent.triggers.base.BaseTrigger._do_redispatch", return_value=mock_redispatch_id
        )

        base_trigger.trigger()

        mock_get_status.assert_called_once()

        if mock_status is None:
            mock_do_redispatch.assert_called_with(True)
        else:
            mock_do_redispatch.assert_called_once()
            assert mock_redispatch_id in base_trigger.new_dispatch_ids
