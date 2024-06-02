import json
# # # Lưu data vào JSON và Đọc ra gán vào biến : data_users
# with open("tinh_trang.json", "w") as f:
#     json.dump(data_original, f, indent=4)
with open('tinh_trang.json', 'r') as f:
  data = json.load(f)

print(data)

# Viết thành chương trình các chức năng.

# 1. Lọc ra danh sách những người > sổ tuổi nhập. ( Dùng input)
#2.  Lọc ra danh sách những người đang làm .... Dùng input
#3.  Hiển thị thông tin của
# 4. Hiển thị người thân của  Dùng input nhập tên người nào đó.
#5.  Hiển thị thông tin của người là đảng viên ( "dang_vien": 1)
#6.  Hiển thị danh sách những người đã kết hôn


print("----------Chương trình với các chức năng-----------")


print("1. Lọc ra danh sách người có có độ tuổi lớn hơn bạn muốn ")
print("2. Lọc ra danh sách những người đang làm công việc ")
print("3. Hiển thị thông tin của người bạn muốn ")
print("4. Hiển thị người thân của người bạn muốn ")
print("5. Hiển thị thông tin của người là đảng viêc  ")
print("6. Hiển thị danh sách những người đã kết hôn ")
print("7. Thêm người dùng")
print("8. Thoát ")



while True:
    lc = int(input("Mời nhập chức năng bạn muốn: "))
    if lc == 1:
        so_tuoi = int(input("Số tuổi bạn muốn nhập: "))
        for user in data:
            if user['age'] > so_tuoi:
                print("Số người bạn cần tìm là:", user)
    elif lc == 2:
        cong_viec = str(input("Công việc bạn muốn nhập: "))
        for user in data:
            if user['job'] == cong_viec:
                print("Công việc bạn cần tìm là:", user)
    elif lc == 3:
        thong_tin = str(input("Người bạn muốn hiển thị: "))
        for user in data:
            if user['name'] == thong_tin:
                print("Thông tin bạn muốn tìm là:", user)
    elif lc == 4:
        thong_tin_nguoi_than = str(input("Người bạn muốn hiển thị: "))
        for user in data:
            if user['name'] == thong_tin_nguoi_than:
                print("Thông tin người thân bạn muốn tìm là: ", user['nguoi_than'])
    elif lc == 5:
        print("NẾU LÀ ĐẢNG VIÊN CHỌN SỐ 1 ")
        print("NẾU LÀ KHÔNG PHẢI LÀ ĐẢNG VIÊN CHỌN SỐ 0 ")
        dang_vien = int(input("Số bạn muốn nhập là: "))
        if dang_vien == 1:
            text = "Danh sách đảng viên là:"
        else:
            text = "Danh sách không phải là đảng viên là:"
        list = []
        for user in data:
            if user['dang_vien'] == dang_vien:
                list.append(user)
        print(f"{text}", list)
    elif  lc == 6:
        print("NẾU ĐÃ KẾT HÔN CHỌN SỐ 1 ")
        print("NẾU CHƯA KẾT HÔN CHỌN SỐ 0 ")
        hon_nhan = int(input("Tình trạng hôn nhân bạn muốn nhập: "))
        if hon_nhan == 1:
            text = "Danh sách người đã kết hôn là: "
        else:
            text = "Danh sách những người chưa kết hôn là: "
        for user in data:
            user["da_ket_hon"] = 0
            nhung_nguoi_than = user["nguoi_than"]
            for nguoi_than in nhung_nguoi_than:
                if nguoi_than in ["chồng", "vợ"]:
                    user["da_ket_hon"] = 1
                    break
        list2 = []
        for user in data:
            if user['da_ket_hon'] == hon_nhan:
                list2.append(user)
        print(f"{text}", list2)
    elif lc == 7:
        list3 = {}
         name = str(input("Mời Nhập Tên:"))
         age = int(input("Mời Nhập Tuổi:"))
         address = str(input("Mời Nhập Nơi Ở:"))
         job = str(input("Mời Nhập Nghề:"))
         nguoi_than = str(input(""))
         danh_sach_nguoi_than = nguoi_than.split("")
         dang_vien = int(input("Mời Nhập số:"))
         print(list3)
    elif lc == 8:
        print("Cảm ơn bạn đã sử dụng")
        break
    else:
        print("Mời Nhập Lại")

