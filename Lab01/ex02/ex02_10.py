def dao_nguoc_chuot(chuoi):
    return chuoi[::-1]
input_str = input("nhap chuoi can dao nguoc: ")
print(f"chuoi dao nguoc la: {dao_nguoc_chuot(input_str)}")