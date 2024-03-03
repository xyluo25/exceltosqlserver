# -*- coding:utf-8 -*-
##############################################################
# Created Date: Sunday, March 3rd 2024
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import pytest
from exceltosqlserver import ExcelToDB

import sqlalchemy
import pyodbc
import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))


def test_db_connection():
    """This function is used to test the database connection."""
    excel2db = ExcelToDB(filePath="test_data/test_data.xlsx",
                         host_ip="localhost",
                         usrID="sa",
                         pwd="123456",
                         db_name="TestDB",
                         rename_table="TestTable")

    excel2db.connect2DB()
    assert excel2db.dbType == ["sqlserver"]
    assert excel2db.host_ip == "localhost"
    assert excel2db.db_name == "TestDB"
    assert excel2db.usrID == "sa"
    assert excel2db.pwd == "123456"
    assert excel2db.rename_table == "TestTable"
    assert excel2db.engine is not None