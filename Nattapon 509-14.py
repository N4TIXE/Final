print("1.รับค่า * เข้ามาหนึ่งครั้งจากนั้นรับตัวเลขจํานวนเต็ม แล้วให้แสดงผลลัพธ์ดังนี้")
print("Input = * เเละ 10     output **********")
print("หาผลลัพธ์")
variable = input("กรุณาใส่ค่าตัวเเปรของโจทย์ที่กำหนดให้: ")
times = int(input("จำนวนที่โจทย์กำหนดให้: "))
output = variable * times
print(output)
print("2.เขียนโปรแกรมรับจํานวนคะแนนสอบกลางภาคและปลายภาค ซึ่งแต่ละครั้งมีคะแนนและค่าเฉลี่ยของคะแนนนสอบทั้งสองครั้ง")
print("กำหนดค่า input = 50.5 เเละ 31.5")
midterm = float(input("กรุณากรอกคะแนน Midterm : "))
final = float(input("กรุณากรอกคะแนน Final: "))
if 0 <= midterm <= 60 and 0 <= final <= 60:
    total = midterm + final
    average = total / 2
    print("Total :", total)
    print("Average :", average)
print("3.กําหนดให้สระว่ายน้ํา เป็นรูปสี่เหลี่ยมผืนผ้า โดยเราต้องการเติมน้ําลงไปในสระให้เต็ม จงเขียนโปรแกรมเพื่อรับความกว้าง ความยาว และความลึกของสระในหน่วยเมตร เพื่อคํานวณว่าต้องใช้เวลากี่นาทีในการเติมน้ําลงในสระให้เต็ม เมื่อกําหนดให้ใช้เวลา 15 วินาทีในการเติมน้ํา 1ลูกบาศก์เมตร แสดงคําตอบด้วยทศนิยมสองตําแหน่ง")
print("กำหนด กว้าง = 18.5 , ยาว = 38.75 , ลึก = 1.35 ต้องใช้เวลาในการเติมนํ้า 241.95 นาที")
W = float(input("ระบุความกว้าง :"))
L = float(input("ระบุความยาว :"))
H = float(input("ระบุความลึก :"))
Area = W * L * H
print("ขนาดพื้นที่ของรูปสี่เหลี่ยม",Area,"ลูกบาศก์เมตร")
print("คำนวณระยะเวลาที่เติมนํ้าให้เต็ม\nกำหนดให้ใช้เวลา 15 วินาทีในการเติมนํ้า 1 ลบ.ม. เเสดงคำตอบด้วยทศนิยมสองตำเเหน่ง")
Times_ForMax = Area * 15 /60
print("ระยะเวลาที่เติมนํ้าให้เต็ม คือ","%.2f"%(Times_ForMax),"นาที")
