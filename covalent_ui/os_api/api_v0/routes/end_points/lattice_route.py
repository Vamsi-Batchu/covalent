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

"""Lattice route"""

import uuid
from random import randrange

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from covalent_ui.os_api.api_v0.data_layer.lattice_dal import Lattices
from covalent_ui.os_api.api_v0.database.config.db import engine
from covalent_ui.os_api.api_v0.database.lattice_file_mock import file_read
from covalent_ui.os_api.api_v0.models.file_model import FileMapper, Filetype
from covalent_ui.os_api.api_v0.models.lattices_model import (
    FileOutput,
    LatticeDetailResponse,
    LatticeExecutorResponse,
    LatticeFileResponse,
)
from covalent_ui.os_api.api_v0.utils.file_handle import FileHandler

routes: APIRouter = APIRouter()


@routes.get("/{dispatch_id}", response_model=LatticeDetailResponse)
def get_lattice_details(dispatch_id: uuid.UUID):
    """Get lattice details

    Args:
        dispatch_id: To fetch lattice data with the provided dispatch id

    Returns:
        Returns the lattice data with the dispatch id provided
    """

    with Session(engine) as session:
        electron = Lattices(session)
        data = electron.get_lattices_id(dispatch_id)
        if data[0] is not None:
            return LatticeDetailResponse(
                dispatch_id=data.dispatch_id,
                status=data.status,
                total_electrons=data.total_electrons,
                total_electrons_completed=data.total_electrons_completed,
                started_at=data.start_time,
                ended_at=data.end_time,
                directory=data.directory,
                runtime=data.runtime,
            )
        raise HTTPException(status_code=400, detail=[f"{dispatch_id} does not exists"])


@routes.get("/{dispatch_id}/details/{name}")
def get_lattice_files(dispatch_id: uuid.UUID, name: FileOutput):
    """Get lattice file data

    Args:
        dispatch_id: To fetch lattice data with the provided dispatch id
        name: To fetch specific file data for a lattice

    Returns:
        Returns the lattice file data with the dispatch id and file_module provided provided
    """
    with Session(engine) as session:
        electron = Lattices(session)
        data = electron.get_lattices_id_storage_file(dispatch_id)
        if data[0] is not None:
            if name in ["result", "inputs"]:
                response = file_read()
                return LatticeFileResponse(data=str(response[name]))
            elif name == "function_string":
                response = file_read()
                return LatticeFileResponse(data=response[name][randrange(3)])
            elif name == "executor_details":
                response = file_read()
                return LatticeExecutorResponse(data=response[name], executor_name="dask")
            response = file_read()
            return LatticeFileResponse(data=response[name])
        raise HTTPException(status_code=400, detail=[f"{dispatch_id} does not exists"])