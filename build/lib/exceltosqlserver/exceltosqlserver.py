# -*- coding:utf-8 -*-
##############################################################
# Created Date: Monday, December 28th 2020
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import pandas as pd
import pyodbc
from sqlalchemy import create_engine
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


class ExcelToDB:
    def __init__(self,
                 filePath: str,
                 host_ip: str = "",
                 usrID: str = "",
                 pwd: str = "",
                 db_name: str = "",
                 rename_table: str = ""):
        """This class is used to save excel or csv file into sql server database.

        Args:
            filePath (str): your file path.
            host_ip (str, optional): your local machine host or ip address. Defaults to "".
            usrID (str, optional): sql server user id . Defaults to "".
            pwd (str, optional): sql server password. Defaults to "".
            db_name (str, optional): database name in sql server. Defaults to "".
            rename_table (str, optional): rename your input table.
                if "", will use exact the same table name of your input file. Defaults to "".

        Raises:
            Exception: Partially inputs, please check your inputs...

        """

        if not any([host_ip, db_name, usrID, pwd]):
            raise Exception("Partially inputs, please check your inputs...")

        self.filePath = filePath
        self.host_ip = host_ip
        self.db_name = db_name
        self.usrID = usrID
        self.pwd = pwd
        self.rename_table = rename_table

        self.dbType = ["sqlserver"]

    def connect2DB(self) -> None:  # sourcery skip: assign-if-exp, extract-method
        # This will test whether a sql server database or a mysql database
        sqlserverDriver = ["{SQL Server}",
                           "{SQL Native Client}",
                           "{SQL Server Native Client 10.0}",
                           "{SQL Server Native Client 11.0}",
                           "{ODBC Driver 11 for SQL Server}",
                           "{ODBC Driver 13 for SQL Server}",
                           "{ODBC Driver 13.1 for SQL Server}",
                           "{ODBC Driver 17 for SQL Server}",
                           "{ODBC Driver 18 for SQL Server}"]

        for i in sqlserverDriver:
            driveString = i.replace(" ", "+").replace("{", "").replace("}", "")

            try:
                # connect to sql server
                self.engine = create_engine(
                    f"mssql+pyodbc://{self.usrID}:{self.pwd}@{self.host_ip}/{self.db_name}?driver={driveString}?")

                print("Successfully connected to SQL Server...")
                return None
            except Exception:
                self.engine = False
                continue

        raise Exception(
            "Can not save table to sql server, please check your inputs.")

    def readData(self) -> None:
        if self.filePath.split(".")[-1] in ["xlsx", "xls"]:
            self.file_data = pd.read_excel(self.filePath)
            print("Successfully load excel data...")
        elif self.filePath.split(".")[-1] in ["csv"]:
            self.file_data = pd.read_csv(self.filePath)
            print("Successfully load csv data...")
        else:
            raise Exception("Unable to load input file...")

    def save2db(self) -> None:
        """Save your data into sql server database.
        """

        self.readData()
        self.connect2DB()

        # specify the table name
        if self.rename_table:
            tableName = self.rename_table
        elif "/" in self.filePath:
            tableName = self.filePath.split("/")[-1].split(".")[0]
        else:
            tableName = self.filePath.split(".")[0]

        if self.engine:
            try:
                self.file_data.to_sql(tableName, con=self.engine)
                print("Successfully saved %s into SQL Server..." % tableName)

            except Exception as e:
                raise Exception(
                    "Can not save table to sql server, please check your inputs."
                ) from e
        else:
            raise Exception(
                "Can not save table to sql server, please check your inputs."
            )