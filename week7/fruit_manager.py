fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
prices = [1.2, 0.5, 2.5, 1.0, 1.5, 0.8]

# Tim loại trái cây có giá rẻ nhất
def cheapest_fruit(fruits, prices):
    min_price = prices[0]
    i_min = 0
    # tìm vị trí mà giá nhỏ nhất
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            i_min = i
    # trả về loại trái cây tại vị trí đó
    return fruits[i_min]

# Tìm giá của loại trái cây
def get_price(fruits, prices, fruit_name):
    for i in range(len(fruits)):
        if fruits[i] == fruit_name:
            return prices[i]

# In ra danh sách các loại trái cây và giá của chúng
def print_fruits(fruits, prices):
    print('+', '-' * 20, '+', '-' * 10, '+')
    print(f'| {"Fruit":<20} | {"Price":<10} |')
    print('+', '-' * 20, '+', '-' * 10, '+')

    for i in range(len(fruits)):
        print(f'| {fruits[i]:<20} | {prices[i]:>10} |')
    
    print('+', '-' * 20, '+', '-' * 10, '+')

# Tìm các loại trái cây có giá cao hơn giá trung bình
def over_price(fruits, prices):
    avg_price = sum(prices) / len(prices)
    
    over_fruits = []
    over_prices = []

    for i in range(len(prices)):
        if prices[i] > avg_price:
            over_fruits.append(fruits[i])
            over_prices.append(prices[i])

    print('Over average price fruits:')
    print(f'Average price: {avg_price:.2f}')
    print_fruits(over_fruits, over_prices)


def print_menu():
    print('FRUIT MANAGEMENT')
    print('----------------')

    print('1. Print all fruits.')
    print('2. Print over priced fruits.')
    print('3. Find cheapest fruit.')
    print('4. Find price of a fruit.')
    print('5. Exit.')

def main():
    running = True

    while running:
        print_menu()
        choice = int(input('Enter your choice: '))

        if choice == 1: 
            print_fruits(fruits, prices)
        elif choice == 2: 
            over_price(fruits, prices)
        elif choice == 3: 
            print(f'The cheapest fruit is: {cheapest_fruit(fruits, prices)}')
        elif choice == 4: 
            fruit = input('Enter fruit name: ')
            price = get_price(fruits, prices, fruit)
            if price is not None:
                print(f'The price of {fruit} is: {price}')
            else:
                print(f'{fruit} not found.')
        elif choice == 5:
            running = False
        else:
            print('Invalid choice. Please try again.')

## MAIN PROGRAM
main()