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

"""Electron test"""

import tests.covalent_ui_backend_tests.utils.main as main
from tests.covalent_ui_backend_tests.utils.assert_data.electrons import seed_electron_data
from tests.covalent_ui_backend_tests.utils.client_template import MethodType, TestClientTemplate

object_test_template = TestClientTemplate()
output_data = seed_electron_data()


def test_electrons():
    """Test electrons"""
    test_data = output_data["test_electrons"]["case1"]
    response = object_test_template(
        api_path=output_data["test_electrons"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_function_string():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_function_string_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        path=test_data["path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_executor():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_executor_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_result():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_result_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_value():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_value_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_stdout():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_stdout_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_deps():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_deps_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_call_before():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_call_before_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_call_after():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_call_after_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_call_error():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_error_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_info():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_info_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]


def test_electrons_details_inputs():
    """Test overview"""
    test_data = output_data["test_electrons_details"]["case_inputs_1"]
    response = object_test_template(
        api_path=output_data["test_electrons_details"]["api_path"],
        app=main.fastapi_app,
        method_type=MethodType.GET,
        path=test_data["path"],
    )
    assert response.status_code == test_data["status_code"]
    if "response_data" in test_data:
        assert response.json() == test_data["response_data"]
