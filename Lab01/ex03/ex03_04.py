def truy_cap_phan_tu(tulpe_data):
    fisrt_element = tulpe_data[0]
    last_element = tulpe_data[-1]
    return fisrt_element, last_element
input_tuple = eval(input("Nhap tuple: "))
first, last = truy_cap_phan_tu(input_tuple)
print("phan tu dau tien: ",first)
print("phan tu cuoi cung: ",last)