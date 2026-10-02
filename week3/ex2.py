# Bài 2: Khuyến mãi đơn hàng (if)
# Nhập tổng tiền đơn hàng (VNĐ). Nếu tổng tiền > 500000 thì giảm 10%.
# In ra số tiền khách phải thanh toán (nếu không đủ điều kiện giảm thì vẫn in số tiền gốc).
payment = int(input('Enter total payment (VND): '))
# edge case (defensive programming): check if payment is valid
if payment <= 0:
    print('Invalid payment')
    exit()

# happy case
if payment > 500000:
    payment = payment * 0.9
    
print(f'You have to pay: {payment} VND')