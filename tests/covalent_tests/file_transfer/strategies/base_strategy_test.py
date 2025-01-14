# Copyright 2021 Agnostiq Inc.
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

from unittest.mock import Mock

import pytest

from covalent._file_transfer import File
from covalent._file_transfer.file_transfer import FileTransfer
from covalent._file_transfer.strategies.transfer_strategy_base import FileTransferStrategy


class MockStrategy(FileTransferStrategy):
    def cp(self, from_file: File, to_file: File) -> None:
        pass

    def download(self, from_file: File, to_file: File) -> File:
        pass

    def upload(self, from_file: File, to_file: File) -> None:
        pass


class TestBaseFileTransferStrategy:
    @pytest.mark.parametrize(
        "is_from_temp, is_to_temp",
        [(True, True), (True, False), (False, False), (False, True)],
    )
    def test_pre_transfer_hook_tmp_file_creation(self, mocker, is_from_temp, is_to_temp):
        strategy = MockStrategy()

        from_file = File() if is_from_temp else "/home/users.from.dat"
        to_file = File() if is_to_temp else "/home/users.to.dat"
        ft = FileTransfer(from_file, to_file, strategy=strategy)
        pre_transfer_hook_callable, file_transfer_callable = ft.cp()
        path_mock: Mock = mocker.patch(
            "covalent._file_transfer.strategies.transfer_strategy_base.Path"
        )
        pre_transfer_hook_callable()
        if is_from_temp:
            path_mock.assert_any_call(ft.from_file.filepath)
        if is_to_temp:
            path_mock.assert_any_call(ft.to_file.filepath)

        if is_from_temp and is_to_temp:
            assert path_mock().touch.call_count == 2
            assert path_mock().parent.mkdir.call_count == 2
        elif is_from_temp or is_to_temp:
            assert path_mock().touch.call_count == 1
            assert path_mock().parent.mkdir.call_count == 1

    @pytest.mark.parametrize(
        "is_from_remote, is_to_remote",
        [(True, True), (True, False), (False, False), (False, True)],
    )
    def test_pre_transfer_hook_return_values(self, mocker, is_from_remote, is_to_remote):
        # we do not support remote -> remote operations as of yet
        if is_from_remote and is_to_remote:
            return

        strategy = MockStrategy()
        from_file = File(is_remote=is_from_remote)
        to_file = File(is_remote=is_to_remote)
        ft = FileTransfer(from_file, to_file, strategy=strategy)
        pre_transfer_hook_callable, file_transfer_callable = ft.cp()
        return_value = pre_transfer_hook_callable()
        assert return_value == (from_file.filepath, to_file.filepath)
