from db import DBConnection as mydb

class perawat:

    def __init__(self):
        self.__id=None
        self.__nip=None
        self.__namaperawat=None
        self.__jk=None
        self.__tempatbertugas=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def __namaperawat(self):
        return self.__namaperawat

    @__namaperawat.setter
    def __namaperawat(self, value):
        self.__namaperawat = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def __tempatbertugas(self):
        return self.__tempatbertugas

    @__tempatbertugas.setter
    def kode_prodi(self, value):
        self.__tempatbertugas = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__namaperawat, self.__jk, self.__tempatbertugas)
        sql="INSERT INTO perawat (nip, namaperawat, jk, tempatbertugas) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__namaperawat, self.__jk, self.__tempatbertugas, id)
        sql="UPDATE perawat SET nip = %s, namaperawat = %s, jk=%s, tempatbertugas=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nip):
        self.conn = mydb()
        val = (self.__namaperawat, self.__jk, self.__tempatbertugas, nip)
        sql="UPDATE perawat SET namaperawat = %s, jk=%s, tempatbertugas =% s WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM perawat WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nip):
        self.conn = mydb()
        sql="DELETE FROM perawat WHERE nip='" + str(nip) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM perawat WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__namaperawat = self.result[2]
        self.__jk = self.result[3]
        self.__tempatbertugas = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nip):
        a=str(nip)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM perawat WHERE nim='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__namaperawat = self.result[2]
            self.__jk = self.result[3]
            self.__tempatbertugas = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__namaperawat = ''
            self.__jk = ''
            self.__tempatbertugas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM perawat"
        self.result = self.conn.findAll(sql)
        return self.result

# tampil Data
A = perawat()
B = A.getAllData()
print(B)