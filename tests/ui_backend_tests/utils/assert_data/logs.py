def seed_logs_data():
    """Mock db logs data"""
    return {
        "test_logs": {
            "api_path": "/api/v1/logs/",
            "case1": {
                "status_code": 200,
                "response_data": {
                    "items": [
                        {
                            "log_date": "2022-09-26 07:41:42.907000",
                            "status": "INFO",
                            "message": '127.0.0.1:47378 - "GET /openapi.json HTTP/1.1" 200',
                        },
                        {
                            "log_date": "2022-09-26 07:41:42.411000",
                            "status": "INFO",
                            "message": '127.0.0.1:47378 - "GET /docs HTTP/1.1" 200',
                        },
                        {
                            "log_date": "2022-09-23 07:43:59.753000",
                            "status": "INFO",
                            "message": "Waiting for application startup.",
                        },
                        {
                            "log_date": "2022-09-23 07:43:59.753000",
                            "status": "INFO",
                            "message": "Application startup complete.",
                        },
                        {
                            "log_date": "2022-09-23 07:43:59.752000",
                            "status": "INFO",
                            "message": "Started server process [41482]",
                        },
                    ],
                    "total_count": 5,
                },
            },
            "case2": {
                "status_code": 200,
                "request_data": {
                    "query": {
                        "count": 2,
                        "offset": 0,
                        "search": "",
                        "sort_by": "log_date",
                        "sort_direction": "DESC",
                    }
                },
                "response_data": {
                    "items": [
                        {
                            "log_date": "2022-09-26 07:41:42.907000",
                            "status": "INFO",
                            "message": '127.0.0.1:47378 - "GET /openapi.json HTTP/1.1" 200\nconnection Closed\n\nKilled',
                        },
                        {
                            "log_date": "2022-09-26 07:41:42.907000",
                            "status": "INFO",
                            "message": "WebSocket - connection open",
                        },
                    ],
                    "total_count": 7,
                },
            },
            "case3": {
                "status_code": 200,
                "request_data": {
                    "query": {
                        "count": 10,
                        "offset": 4,
                        "search": "",
                        "sort_by": "log_date",
                        "sort_direction": "DESC",
                    }
                },
                "response_data": {
                    "items": [
                        {
                            "log_date": "2022-09-23 07:43:59.753000",
                            "status": "INFO",
                            "message": "Waiting for application startup.",
                        },
                        {
                            "log_date": "2022-09-23 07:43:59.753000",
                            "status": "INFO",
                            "message": "Application startup complete.",
                        },
                        {
                            "log_date": "2022-09-23 07:43:59.752000",
                            "status": "INFO",
                            "message": "Started server process [41482]",
                        },
                    ],
                    "total_count": 7,
                },
            },
            "case4": {
                "status_code": 200,
                "request_data": {
                    "query": {
                        "count": 5,
                        "offset": 0,
                        "search": "favicon",
                        "sort_by": "log_date",
                        "sort_direction": "DESC",
                    }
                },
                "response_data": {
                    "items": [
                        {
                            "log_date": "2022-09-26 07:41:42.907000",
                            "status": "INFO",
                            "message": '127.0.0.1:47378 - "GET /favicon.ico HTTP/1.1" 404',
                        }
                    ],
                    "total_count": 1,
                },
            },
            "case5": {"status_code": 200, "response_data": {"items": [], "total_count": 0}},
        },
        "test_download_logs": {"api_path": "/api/v1/logs/download", "case1": {"status_code": 200}},
    }
