from sinhvien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def genarateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0].getId()
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId += 1
        return maxId
    
def soLuongSinhVien(self):
    return self.listSinhVien._len_()
def nhapSinhVien(self):
    svId = self.genarateID()
    name = input("Nhap ten sinh vien: ")
    sex = input("Nhap gioi tinh: ")
    major = input("Nhap nganh hoc: ")
    diemTB = float(input("Nhap diem trung binh: "))
    sv = SinhVien(svId, name, sex, major, diemTB)
    self.XepLoaiHocLuc(sv)
    self.listSinhVien.append(sv)

def updateSinhVien(self, ID):
    sv: SinhVien = self.findById(ID)
    if (sv != None):
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap nganh hoc: ")
        diemTB = float(input("Nhap diem trung binh: "))
        sv._name = name
        sv._sex = sex
        sv._major = major
        sv._diemTB = diemTB
        self.XepLoaiHocLuc(sv)
    else:
        print("sinh vien co Id = {} khong ton tai".format(ID))
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)
    
    def findById(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findById(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocluc = "Gioi"
        elif(sv._diemTB >= 6.5):
            sv._hocluc = "Kha"
        elif(sv._diemTB >= 5):
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"
    
    def showSinhVien(self, listSV):
        print("{:<8} {:18} {:<8} {:<8} {:<8} {:<8}".format("Id", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if (listSV._len_() > 0):
            for sv in listSV:
                print("{:<8} {:18} {:<8} {:<8} {:<8} {:<8}".format("Id", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        print("\n")
    def getListSinhVien(self):
        return self.ListSinhVien