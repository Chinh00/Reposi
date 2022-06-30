while 1 < 2:
    d = int(input("Nhap vao ngay: "))
    m = int(input("Nhap vao thang: "))
    y = int(input("Nhap vao nam: "))
    if d >= 1 and d <= 31 and m >= 1 and m <= 12 and y // 1000 > 0:
        break
    else:
        print("Dữ liệu vào không hợp lệ.")
        exit()
if d == 31 and m == 12:
    print(1, 1, y + 1, sep=" - ")
    exit()
if m <= 7:
    if m % 2 == 0:
        if d == 31:
            print("Khong ton tai ngay nay trong thang")
            exit()
        if d <= 29:
            d_res = d + 1
            m_res = m
        else:
            d_res = 1
            m_res = m + 1
    else:
        if d <= 30:
            d_res = d + 1
            m_res = m
        else:
            d_res = 1
            m_res = m + 1
else: 
    if m % 2 == 1:
        if d == 31:
            print("Khong ton tai ngay nay trong thang")
            exit()
        if d <= 29:
            d_res = d + 1
            m_res = m
        else:
            d_res = 1
            m_res = m + 1
    else:
        if d <= 30:
            d_res = d + 1
            m_res = m
        else:
            d_res = 1
            m_res = m + 1
y_res = y
print(d_res, m_res, y_res, sep=" - ")
