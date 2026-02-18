import math


try:
  price = float(input("กรอกราคา : "))
  if price % 10 == 0:
    print("ต้องการสนับสนุนเพิ่มไหม")
    Q1 = input("ต้องการ / ไม่ต้องการ y / n : ")
    if Q1 == "y":
      try:
        donate = int(input("กี่บาทดี : "))
        print(f"ขอบคุณที่สนับสนุนเราจำนวน {donate} บาท")
      except ValueError:
        print("กรอกอะไรมาเนี่ย" + ValueError)
    elif Q1 == "n":
      print(f"ราคา {price}")
    else:
      print("Fuk u")
  else:
    bigPrice = 0
    for i in range(math.floor(price),10000):
      if i % 10 == 0:
        bigPrice = i
        break
    pteron = bigPrice - price
    print(f"ต้องการบริจาคจำนวน {pteron:.2f} บาทไหม")
    Q2 = input("ต้องการ / ไม่ต้องการ y / n : ")
    if Q2 == "y":
      print(f"ต้องจ่ายเงินจำนวน {pteron + price} บาท")
    elif Q2 == "n":
      print(f"ต้องจ่ายการเงินจำนวน {price} บาท")
except Exception as e:
  print(e)
  print("Try again")

