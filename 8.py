
while 1 < 2:
    n = int(input("Điểm trung bình học tập của sinh viên đó là: "))
    if (n >= 0 and n <= 10): break
if n < 3.5: 
    res = "Yếu"
elif n >= 3.5 and n < 5:
    res = "Kém"
elif n >= 5 and n < 6.5:
    res = "Trung bình"
elif n >= 6.5 and n < 8:
    res = "Khá"
elif n >= 8 and n < 9:
    res = "Giỏi"
else: res = "Xuất xắc"
print("Thành tích học tập là: ", res)