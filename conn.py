import pyodbc


class Server:
    def __init__(self, driver, server, database, uid, pwd):
        self.driver = f"DRIVER={driver};"
        self.server = f"SERVER={server};"
        self.database = f"DATABASE={database};"
        self.uid = f"UID={uid};"
        self.pwd = f"PWD={pwd};"

    def connection(self):
        return self.driver + self.server + self.database + self.uid + self.pwd
