from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\n=========================================")
    print("********************Menu*******************")
    print("**   1. Nhap sinh vien                   **")
    print("**   2. Cap nhap thong tin sinh vien boi ID      **")
    print("**   3. Xoa sinh vien boi ID             **")
    print("**   4. Tim kiem sinh vien theo ten     **")
    print("**   5. Sap xep sinh vien theo DiemTB       **")
    print("**   6. Sap xep sinh vien theo ten chuyen nganh **")
    print("**   7. Hien thi danh sach sinh vien     **")
    print("**   0. Thoat chuong trinh               **")
    print("=========================================")
    
    key = int(input("Nhap lua chon cua ban: "))
    if (key == 1):
        print("\n1. Them sinh vien ")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhap thong tin sinh vien ")
            ID = int(input("Nhap ID: "))
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien ")
            ID = int(input("Nhap ID: "))
            ID = int(input())
            if (qlsv.deleteByID(ID)):
                print("Sinh vien co ID = ",ID, "da bi xoa.")
            else:
                print("Sinh vien co ID = ",ID, "khong ton tai.")
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten ")
            keyword = input("Nhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo DiemTB (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten ")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien ")
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 0):
        print("\nThoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("Lua chon khong hop le. Vui long chon lai!")