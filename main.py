while True:
    print("Menu")
    print("1. Nhập sách")
    print("2. Mượn sách")
    print("3. Tìm kiếm sách") 
    print("0. Thoát")
    chon = int(input("Chọn chức năng: "))
    if chon==0:
        break
    elif chon ==1:
        print("Nhập thông tin sách")
    elif chon ==2:
        print("Mượn sách")
    elif chon==3:
        print("Tìm kiếm sách")
    else:
        print("Vui lòng chọn chức năng từ 0..2")

        