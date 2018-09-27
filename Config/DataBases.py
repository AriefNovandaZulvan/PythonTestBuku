import pandas
from Config import ConnectorSQL

class DataBases():

    def __init__(self):
        pass

    def LoadDefault(self):
        DBLibName = 'SQL Server'
        dfserverName = ''
        dfdatabaseName = ''
        dfuserID = ''
        dfpassword = ''
        oConnector = ConnectorSQL.ConnectorSQL(DBLibName, dfserverName, dfdatabaseName, dfuserID, dfpassword,False)
        oConnector.connectToDB()


