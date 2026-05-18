# Input ta nhập vào họ tên bệnh nhân ,Mã bệnh án ,Khoa
# Output in ra Phiếu khám gồm họ tên bệnh nhân , mã , chuyển tới khoa tiếp theo
# Ta sửa dụng f string để gán các giá trị biến vào phiếu 
# B1 : ta sửa tạo ra 3 biến để lưu trữ giá trị nhập vào 
# B2 : Ta lưu gọi biến vào trong phiếu để in giá trị vừa nhập ra và dùng print để in phiếu lên.

# Code 

name = input("Nhập tên bệnh nhân :")
patient_id = input("Nhập mã bệnh án : ")
department = input("Khoa/phòng khám :")

print("------Phiếu bệnh nhân ------")
print(f"Bệnh nhân : {name} - Mã BA: {patient_id} - Chuyển tỡi: {department}")


