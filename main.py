# Open the file in read mode
my_file = open("input.txt", "r")

# Initialize an empty list to store the numbers
numbers = []

# Read the file line by line
for line in my_file:
  # Split the line into numbers
  nums = line.strip().split()
  # Convert the numbers to float and add them to the list
  numbers.extend([float(num) for num in nums])

# Close the file
my_file.close()

money = 100
rates = []
for i in range(0, int(numbers[0]) * 2, 2):
   rates.append((numbers[1:][i], numbers[1:][i + 1]))

print(rates)


def exchange_money(money, n, into_currency, from_currency):
    if from_currency == "r":
        return (money / n, into_currency)
    else:
        return (money * n, into_currency)


def max_rubles(n, rates):
    money = (100, "r")
    for i in range(0, n):
        print(money)
        if i + 1 < n:
            if money[1] == "r":
                dollar = exchange_money((exchange_money(money[0], rates[i][0], "d", money[1]))[0], rates[i + 1][0], "r", "d")
                rubles = money
                euro = exchange_money((exchange_money(money[0], rates[i][1], "e", money[1]))[0], rates[i + 1][1], "r", "e")
                money = max([dollar, rubles, euro], key=lambda x:x[0])

            if money[1] == "d":
                dollar = (exchange_money(money[0], rates[i + 1][0], "r", money[1]))[0]
                rubles = (exchange_money(money[0], rates[i][0], "r", money[1]))[0]
                r_e = exchange_money((exchange_money(money[0], rates[i][0], "r", money[1]))[0], rates[i][1], "e", "r")
                euro = exchange_money((r_e)[0], rates[i + 1][1], "r", "e")
                money = max([dollar, rubles, euro], key=lambda x: x[0])

            if money[1] == "e":
                r_d = exchange_money((exchange_money(money[0], rates[i][0], "r", money[1]))[0], rates[i][1], "d", "r")
                dollar = exchange_money((r_d)[0], rates[i + 1][1], "r", "d")
                rubles = (exchange_money(money[0], rates[i][0], "r", money[1]))[0]
                euro = (exchange_money(money[0], rates[i + 1][0], "r", money[1]))[0]
                money = max([dollar, rubles, euro], key=lambda x: x[0])

        if i == n - 1:
            if money[1] == "d":
                money = exchange_money(money[0], rates[i][0], "r", money[1])
                continue
            if money[1] == "e":
                money = exchange_money(money[0], rates[i][1], "r", money[1])
    return money

with open("output.txt", "w") as f:
   f.write(f"{(max_rubles(int(numbers[0]), rates))[0]}")

# Now, 'numbers' is a list of all numbers in the file
print(max_rubles(int(numbers[0]), rates))

