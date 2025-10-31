import time

list_q = [
    ["What is the capital of France?", "Delhi", "Dubai", "Hyderabad", "Paris", 4],
    ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 3],
    ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "H2", 1],
    ["What is the smallest country in the world?", "Vatican City", "Monaco", "Nauru", "San Marino", 1],
    ["What is the hardest natural substance on Earth?", "Gold", "Diamond", "Iron", "Platinum", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["What is the main ingredient in guacamole?", "Tomato", "Avocado", "Onion", "Pepper", 2],
    ["What is the capital of Japan?", "Seoul", "Tokyo", "Beijing", "Bangkok", 2],
    ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
    ["What is the currency of the United States?", "Dollar", "Euro", "Pound", "Yen", 1],
]

prize = 69
total = 0

for i in range(len(list_q)):
    print(f"Q{i+1}. {list_q[i][0]}")
    print("1.", list_q[i][1])
    print("2.", list_q[i][2])
    print("3.", list_q[i][3])
    print("4.", list_q[i][4])

    try:
        ans = int(input("Enter correct option number: "))
        if 1 <= ans <= 4:
            if ans == list_q[i][-1]:
                total += prize
                print(f"You Won prize {total}!! Still want to continue?")
                decision = input("Enter Y/N: ").strip().lower()
                if decision == "y":
                    continue
                else:
                    print(f"Take your {total} and go home NooB")
                    break
            else:
                print("Nice try NooB")
                print("------- Game Over -------")
                break
        else:
            print("Options range (1-4) only")
        print("------- Moving towards next question -------")
        time.sleep(1)
    except ValueError:
        print("Please Enter a valid option")
