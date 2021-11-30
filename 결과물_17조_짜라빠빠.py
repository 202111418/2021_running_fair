print("뮤지컬 티켓을 예매하시겠습니까?")

print("좌석을 선택해주세요")

sit = input("VIP석 150000원 R석 130000원 S석 100000원 A석 70000원 ex)석을 제외하고 입력하세요")

if (sit == "VIP"):
   price = 150000

elif (sit== "R"):
   price = 130000

elif (sit == "S"):
   price = 100000

elif (sit == "A"):
   price = 70000

many = int(input("수량을 입력하세요"))

cost = price*many
print("총",cost,"입니다")
