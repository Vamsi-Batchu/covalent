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
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.

# Relief from the License may be granted by purchasing a commercial license.

"""DB Config"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from covalent_dispatcher._db.dispatchdb import DispatchDB

# dispatch_db = DispatchDB()
# SQLALCHEMY_DATABASE_URL = dispatch_db._get_data_store()
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
engine = DispatchDB()._get_data_store(initialize_db=True).engine
Base = declarative_base()