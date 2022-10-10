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


def seed_summary_data():
    """Mock db sumary data"""
    return {
        "test_overview": {
            "api_path": "/api/v1/dispatches/overview",
            "case1": {
                "status_code": 200,
                "response_data": {
                    "total_jobs": 1,
                    "total_jobs_running": 0,
                    "total_jobs_completed": 1,
                    "total_jobs_failed": 0,
                    "total_jobs_cancelled": 0,
                    "total_jobs_new_object": 0,
                    "latest_running_task_status": "COMPLETED",
                    "total_dispatcher_duration": 0,
                },
            },
            "case2": {"status_code": 404},
        },
        "test_list": {
            "api_path": "/api/v1/dispatches/list",
            "case1": {
                "status_code": 200,
                "request_data": {
                    "query": {
                        "count": 10,
                        "offset": 0,
                        "sort_by": "runtime",
                        "sort_direction": "DESC",
                        "status_filter": "ALL",
                    }
                },
                "response_data": {
                    "items": [
                        {
                            "dispatch_id": "78525234-72ec-42dc-94a0-f4751707f9cd",
                            "lattice_name": "workflow",
                            "runtime": 0,
                            "total_electrons": 6,
                            "total_electrons_completed": 6,
                            "started_at": "2022-09-23T15:31:11",
                            "ended_at": "2022-09-23T15:31:11",
                            "status": "COMPLETED",
                            "updated_at": "2022-09-23T15:31:11",
                        }
                    ],
                    "total_count": 1,
                },
            },
            "case2": {
                "status_code": 200,
                "request_data": {
                    "query": {
                        "count": 1,
                        "offset": 0,
                        "sort_by": "status",
                        "sort_direction": "ASC",
                        "status_filter": "ALL",
                    }
                },
                "response_data": {
                    "items": [
                        {
                            "dispatch_id": "78525234-72ec-42dc-94a0-f4751707f9cd",
                            "lattice_name": "workflow",
                            "runtime": 0,
                            "total_electrons": 6,
                            "total_electrons_completed": 6,
                            "started_at": "2022-09-23T15:31:11",
                            "ended_at": "2022-09-23T15:31:11",
                            "status": "COMPLETED",
                            "updated_at": "2022-09-23T15:31:11",
                        }
                    ],
                    "total_count": 1,
                },
            },
            "case3": {
                "status_code": 200,
                "request_data": {
                    "query": {
                        "count": 1,
                        "offset": 0,
                        "sort_by": "status",
                        "sort_direction": "ASC",
                        "search": "30",
                        "status_filter": "ALL",
                    }
                },
                "response_data": {"items": [], "total_count": 0},
            },
            "case4": {
                "status_code": 422,
                "request_data": {
                    "query": {
                        "count": 0,
                        "offset": 0,
                        "sort_by": "status",
                        "sort_direction": "ASC",
                        "search": "30",
                        "status_filter": "ALL",
                    }
                },
                "response_data": {
                    "detail": [
                        {
                            "loc": ["query", "count"],
                            "msg": "ensure this value is greater than 0",
                            "type": "value_error.number.not_gt",
                            "ctx": {"limit_value": 0},
                        }
                    ]
                },
            },
        },
        "test_delete": {
            "api_path": "/api/v1/dispatches/delete",
            "case1": {
                "status_code": 200,
                "request_data": {"body": {"dispatches": ["78525234-72ec-42dc-94a0-f4751707f9cd"]}},
                "response_data": {
                    "success_items": ["78525234-72ec-42dc-94a0-f4751707f9cd"],
                    "failure_items": [],
                    "message": "Dispatch(es) have been deleted successfully!",
                },
            },
            "case2": {
                "status_code": 200,
                "request_data": {"body": {"dispatches": ["f7eeb4ad-5262-49a5-aabc-cea10c6c1071"]}},
                "response_data": {
                    "success_items": [],
                    "failure_items": ["f7eeb4ad-5262-49a5-aabc-cea10c6c1071"],
                    "message": "No dispatches were deleted",
                },
            },
            "case3": {
                "status_code": 200,
                "request_data": {
                    "body": {
                        "dispatches": [
                            "78525234-72ec-42dc-94a0-f4751707f9cd",
                            "f7eeb4ad-5262-49a5-aabc-cea10c6c1071",
                            "f7eeb4ad-5262-49a5-aabc-cea10c6c1071",
                            "f7eeb4ad-5262-49a5-aabc-cea10c6c1071",
                        ]
                    }
                },
                "response_data": {
                    "success_items": ["78525234-72ec-42dc-94a0-f4751707f9cd"],
                    "failure_items": [
                        "f7eeb4ad-5262-49a5-aabc-cea10c6c1071",
                        "f7eeb4ad-5262-49a5-aabc-cea10c6c1071",
                        "f7eeb4ad-5262-49a5-aabc-cea10c6c1071",
                    ],
                    "message": "Some of the dispatches could not be deleted",
                },
            },
        },
    }