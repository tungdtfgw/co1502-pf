# Bài 3: Chẵn lẻ số phòng (if else)
# Khách sạn quy định phòng có số chẵn nằm ở tầng hướng biển, phòng số lẻ hướng thành phố.
# Nhập số phòng, in "Huong bien" hoặc "Huong thanh pho".
# Giả sử phòng hợp lệ là 100 - 999
room_no = int(input('Enter room number (100-999): '))
if room_no < 100 or room_no > 999:
    print('Invalid room number')
    exit()

if room_no % 2 == 0:
    print(f'Room {room_no} is Ocean view')
else:
    print(f'Room {room_no} is City view')