
# Tạo 1 chương trình với các chứ năng:
# 1. Tính tổng 2 số
# 2. Tính hiệu 2 số
# 3. Tính tích 2 số
# 4. Tích thương 2 số
# 5. Thoát.
#
# Nhập khác 1-5 thì hiển thị người dùng nhập lại.
#
# Chỉ dừng khi chọn số 5

print("----------Chương trình với các chức năng-----------")


print("1. Tính tổng 2 số bạn muốn")
print("2. Tính hiệu 2 số bạn muốn")
print("3. Tính tích 2 số bạn muốn")
print("4. Tính thương 2 số bạn muốn")
print("5. Thoát ")

while True:
    lc = int(input("Mời nhập chức năng bạn muốn: "))
    if lc > 0 and lc < 5:
        so_thu_1 = int(input("Nhập số thứ nhất: "))
        so_thu_2 = int(input("Nhập số thứ hai: "))
        if lc == 1:
            tong = so_thu_1 + so_thu_2
            print("Tổng của 2 số là: ", tong)
        elif lc == 2:
            hieu = so_thu_1 - so_thu_2
            print("Hiệu của 2 số là: ", hieu)
        elif lc == 3:
            tich = so_thu_1 * so_thu_2
            print("Tích của 2 số là: ", tich)
        elif lc == 4:
            thuong = so_thu_1 / so_thu_2
            print("Tổng của 2 số là: ", thuong)
    elif lc == 5:
        print("Thoát chương trình.")
        break
    else:
        print("Mời bạn nhậm lại trương trình:")
