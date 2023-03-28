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

"""Functions to convert node -> ElectronSchema"""


from .._shared_files.schemas.electron import ElectronAssets, ElectronMetadata, ElectronSchema
from .._shared_files.util_classes import RESULT_STATUS
from .serializers import AssetType, save_asset

ELECTRON_FUNCTION_FILENAME = "function.pkl"
ELECTRON_FUNCTION_STRING_FILENAME = "function_string.txt"
ELECTRON_VALUE_FILENAME = "value.pkl"
ELECTRON_STDOUT_FILENAME = "stdout.log"
ELECTRON_STDERR_FILENAME = "stderr.log"
ELECTRON_ERROR_FILENAME = "error.log"
ELECTRON_RESULTS_FILENAME = "results.pkl"
ELECTRON_DEPS_FILENAME = "deps.pkl"
ELECTRON_CALL_BEFORE_FILENAME = "call_before.pkl"
ELECTRON_CALL_AFTER_FILENAME = "call_after.pkl"
ELECTRON_STORAGE_TYPE = "file"


def _serialize_node_metadata(node_attrs: dict, node_storage_path: str) -> ElectronMetadata:
    task_group_id = node_attrs["task_group_id"]
    name = node_attrs["name"]
    executor = node_attrs["metadata"]["executor"]
    executor_data = node_attrs["metadata"]["executor_data"]

    # Optional
    status = node_attrs.get("status", RESULT_STATUS.NEW_OBJECT)

    start_time = node_attrs.get("start_time", None)
    if start_time:
        start_time = start_time.isoformat()

    end_time = node_attrs.get("end_time", None)
    if end_time:
        end_time = end_time.isoformat()

    return ElectronMetadata(
        task_group_id=task_group_id,
        name=name,
        executor=executor,
        executor_data=executor_data,
        status=status,
        start_time=start_time,
        end_time=end_time,
    )


def _serialize_node_assets(node_attrs: dict, node_storage_path: str) -> ElectronAssets:
    function = node_attrs["function"]
    function_asset = save_asset(
        function, AssetType.TRANSPORTABLE, node_storage_path, ELECTRON_FUNCTION_FILENAME
    )

    function_string = node_attrs.get("function_string", "")
    function_string_asset = save_asset(
        function_string, AssetType.TEXT, node_storage_path, ELECTRON_FUNCTION_STRING_FILENAME
    )

    node_value = node_attrs.get("value", None)
    value_asset = save_asset(
        node_value, AssetType.TRANSPORTABLE, node_storage_path, ELECTRON_VALUE_FILENAME
    )

    node_output = node_attrs.get("output", None)
    output_asset = save_asset(
        node_output, AssetType.TRANSPORTABLE, node_storage_path, ELECTRON_RESULTS_FILENAME
    )

    node_error = node_attrs.get("error", "")
    error_asset = save_asset(
        node_error, AssetType.TEXT, node_storage_path, ELECTRON_ERROR_FILENAME
    )

    node_stdout = node_attrs.get("stdout", "")
    stdout_asset = save_asset(
        node_stdout, AssetType.TEXT, node_storage_path, ELECTRON_STDOUT_FILENAME
    )
    node_stderr = node_attrs.get("stderr", "")
    stderr_asset = save_asset(
        node_error, AssetType.TEXT, node_storage_path, ELECTRON_STDERR_FILENAME
    )

    deps = node_attrs["metadata"]["deps"]
    deps_asset = save_asset(deps, AssetType.OBJECT, node_storage_path, ELECTRON_DEPS_FILENAME)

    call_before = node_attrs["metadata"]["call_before"]
    call_before_asset = save_asset(
        call_before, AssetType.OBJECT, node_storage_path, ELECTRON_CALL_BEFORE_FILENAME
    )

    call_after = node_attrs["metadata"]["call_after"]
    call_after_asset = save_asset(
        call_after, AssetType.OBJECT, node_storage_path, ELECTRON_CALL_AFTER_FILENAME
    )

    return ElectronAssets(
        function=function_asset,
        function_string=function_string_asset,
        value=value_asset,
        output=output_asset,
        deps=deps_asset,
        call_before=call_before_asset,
        call_after=call_after_asset,
        stdout=stdout_asset,
        stderr=stderr_asset,
        error=error_asset,
    )


def serialize_node(node_id: int, node_attrs: dict, node_storage_path) -> ElectronSchema:
    meta = _serialize_node_metadata(node_attrs, node_storage_path)
    assets = _serialize_node_assets(node_attrs, node_storage_path)
    return ElectronSchema(id=node_id, metadata=meta, assets=assets)
