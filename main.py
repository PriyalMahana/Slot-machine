import random

def spin_row():
    symbols = ['🪙', '🌸', '✨', '💣', '🔔']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results  

def print_row(row):
    print(" | ".join(row)) 

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🪙' :
            return int(bet * 10)
        elif row[0] == '🌸':
            return int(bet * 2)
        elif row[0] == '✨':
            return int(bet * 5)
        elif row[0] == '💣':
            return int(bet * 1)
        elif row[0] == '🔔': 
            return int(bet * 3)
    return 0

balance = 100

print("____________________________")
print("Welcome to the Slot Machine!")
print("Symbols: 🪙  🌸 ✨ 💣 🔔")
print("____________________________")
    
while balance > 0:
    print(f"Current Balance: ${balance}")
    bet = input("Enter your bet amount (or 0 to quit): ")
    if not bet.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue
        
    bet = int(bet)

    if bet == 0:
        print("Thank you for playing! Goodbye!")
        break

    elif bet > balance:
        print("Insufficient balance. Please enter a smaller bet.")
        continue

    elif bet < 1:
        print("Bet must be greater than zero.")
        continue

    balance -= bet
            
    row = spin_row()
    print_row(row)
    payout = get_payout(row, bet)
    if payout > 0:
        print(f"Hurrahh !! You won ${payout}.")
    else:
        print("Sorry you lost this round!")
    balance += payout

    
    play_again = input('Do you wanna spin again? If yes type "Yes" else "No". Any other input will be considered No: ').strip().upper()
    if play_again != "YES" or balance == 0:
        break 
print(f"GAME OVER! Your final balance is {balance}")
print("______________________________________")