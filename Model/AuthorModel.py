from Config import DataBases

class AuthorModel():

    dbObject = ''

    def __init__(self):
        self.dbObject = DataBases.DataBases()

    def GetAllAuthor(self):
        self.ret = ('''Select IDAuthor,AuthorName,AuthorBirth From M_Author''')
        self.dataReturn = self.conn.execute(self.ret)
        self.data = self.dataReturn.fetchall()
        self.conn.commit()

