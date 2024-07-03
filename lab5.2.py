#หาพื้นที่สี่เหลี่ยมผืนผ้ากว้าง*ยาว
def rectangle (wide,long):
    area = wide * long
    print("พื้นที่สี่เหลี่ยมผืนผ้า %d" % area)
    return area

w = int(input("กว้าง:"))
l = int(input("ยาว:"))
print(rectangle(w,l))