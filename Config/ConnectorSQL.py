# SQL Server Lib Class For Nexus
# By Roland Antonius
# 03-11-2017
#
#
#

import pyodbc
import time


# import pandas as pd
# import numpy as np

class ConnectorSQL:

    def __init__(self, libName, serverName, databaseName, user, password, automaticDS):
        try:
            ret = False
            self.DSEnabled = automaticDS
            if automaticDS == True:
                self.DBLibName = libName
                self.DBName = databaseName
                self.SVRName = serverName

            else:
                self.DBLibName = libName
                self.DBName = databaseName
                self.SVRName = serverName
                self.DBUser = user
                self.DBPassword = password
            ret = True
            return ret
        except Exception:
            print
            'SQL INIT ERROR'
            if self.debugMode == 'ON':
                print
                'There Are Problems Connecting Initiating SQL Database'
        finally:
            return ret

    def checkLibraryInstalled(self):
        print
        pyodbc.drivers()

    def connectToDB(self):

        try:
            ret = False
            if self.DSEnabled == True:
                self.conn = pyodbc.connect(
                    r'DRIVER={' + self.DBLibName + '};'
                    r'SERVER=' + self.SVRName + ';'
                    r'DATABASE=' + self.DBName + ';'
                    r'Trusted_Connection=yes;'
                )
            else:
                self.conn = pyodbc.connect(
                    r'DRIVER={' + self.DBLibName + '};'
                    r'SERVER=' + self.SVRName + ';'
                    r'DATABASE=' + self.DBName + ';'
                    r'UID=' + self.DBUser + ';'
                    r'PWD=' + self.DBPassword + ''
                )

            if self.conn == None and self.debugMode == 'ON':
                print
                'Connecting Failed'
            elif self.conn != None and self.debugMode == 'ON':
                print
                'Connected To :' + self.SVRName + ' DB Name : ' + self.DBName
                print
                self.conn
            ret = True
            return ret
        except Exception:
            if self.debugMode == 'ON':
                print
                'There Are Problems Connecting To DB Please Check Connection String'
        finally:
            return ret

    def debugMode(self, modeSelection):
        if modeSelection == 'ON':
            self.debugMode = 'ON'
        else:
            self.debugMode = 'OFF'




