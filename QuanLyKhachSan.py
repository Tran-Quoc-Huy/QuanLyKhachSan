#========REGISTER=========

name_tk = input("Enter your nick name: ")
password_tk = input("Enter your password: ")

#========LOGIN========

def login():
    SoLanThu = 0
    print("DANG NHAP!")
    while SoLanThu < 3:
        nick_name = input("Enter your nick name: ")
        password = input("Enter your password: ")
        if nick_name == name_tk and password == password_tk:
            print("Dang nhap thanh cong")
            return True
        else:
            print(f"Dang nhap that bai (so lan thu con {3 - SoLanThu}) \n ")
            SoLanThu += 1
    print("Dang nhap that bai!")
    return False

if __name__ == "__main__":
    login()