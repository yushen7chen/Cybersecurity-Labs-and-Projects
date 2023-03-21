import random

def pass_len():
    length = 0
    while length < 8 or length > 24:
        try:
            length = int(input("Provide password length (8-24): "))
        except:
            print("Please enter a valid input")
        else:
            if length < 8 or length > 24:
                print("Please enter a valid length")
            else:
                break
    return length

def uppercase():
    upper = ''
    while upper not in ['y','n']:
        try:
            upper = input("Use uppercase letters? (y/n): ").lower()
        except:
            print("Please enter a valid input.")
        else:
            if upper not in ['y','n']:
                print("Please enter a valid input.")
            else:
                pass

    return upper

def digits():
    digits = ''
    while digits not in ['y', 'n']:
        try:
            digits = input("Use digits? (y/n): ").lower()
        except:
            print("Please enter a valid input.")
        else:
            if digits not in ['y','n']:
                print("Please enter a valid input.")
            else:
                pass
    return digits

def special():
    special_c = ''
    while special_c not in ['y', 'n']:
        try:
            special_c = input("Use special characters? (y/n): ").lower()
        except:
            print("Please enter a valid input.")
        else:
            if special_c not in ['y','n']:
                print("Please enter a valid input.")
            else:
                pass
    return special_c

while True:
    try:
        print('\n-- Password Generator --')
        print("Choose option: \n1: generate password\n2: exit the program")
        choice = int(input("Your choice:"))
    except:
        print("Please enter a correct value")
    else:
        if choice == 1:
            leng = pass_len()
            use_up = uppercase()
            use_dig = digits()
            use_sp = special()
            alpha = "abcdefghijklmnopqrstuvwxyz"
            upper_alpha = alpha.upper()
            num = "0123456789"
            special_cha = "!@#$%^&*()_+|"
            password = ''
            for i in range(leng):
                if use_up == 'y' and use_dig == 'y' and use_sp == 'y':
                    password = password + random.choice(alpha+upper_alpha+special_cha+num)
                elif use_up == 'y' and use_dig == 'y':
                    password = password + random.choice(alpha+upper_alpha+num)
                elif use_up == 'y' and use_sp == 'y':
                    password = password + random.choice(alpha+upper_alpha+special_cha)
                elif use_up == 'y':
                    password = password + random.choice(alpha+upper_alpha)
                elif use_dig == 'y' and use_sp =='y':
                    password = password + random.choice(num+special_cha)
                elif use_dig == 'y':
                    password = password + random.choice(alpha+num)
                else:
                    password = password + random.choice(alpha+special_cha)
            print(f"\nGenerated password: {password}")

        elif choice == 2:
            print("Bye!")
            break
        else:
            print("Please enter a correct value")

