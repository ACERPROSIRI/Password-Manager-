# Ask for access password
pwd = input('Enter the password to access: ')

# Check access
if pwd == 'KeyboardCat':
    print('Access granted!')
else:
    print('Access denied!')
    choice = input("Do you want to change the access password? (yes/no): ").lower()
    if choice == "yes":
        new_access = input("Enter the new access password: ")
        with open("access.txt", "w") as f:
            f.write(new_access)
        print("Access password changed! Restart the program and login again.")
    exit()  # stop program after handling

# Function to add a password
def add_password():
    new_pwd = input("Enter the new password to add: ")
    with open('passwords.txt', 'a') as f:
        f.write(new_pwd + '\n')
    print('Password added!')

# Function to change an existing password
def change_password():
    old_pwd = input("Enter the old password: ")
    new_pwd = input("Enter the new password: ")
    
    with open('passwords.txt', 'r') as f:
        passwords = f.readlines()
    
    if old_pwd + '\n' in passwords:
        with open('passwords.txt', 'w') as f:
            for p in passwords:
                if p.strip() != old_pwd:
                    f.write(p)
            f.write(new_pwd + '\n')
        print('Password changed!')
    else:
        print('Password not found!')

# Function to view all saved passwords
def view_passwords():
    try:
        with open('passwords.txt', 'r') as f:
            passwords = f.readlines()
        if passwords:
            print("\n--- Saved Passwords ---")
            for p in passwords:
                print(p.strip())
        else:
            print("No passwords saved yet!")
    except FileNotFoundError:
        print("No passwords file found yet!")

# Main program loop
while True:
    mode = input("\nChoose an option: add / change / view / quit: ").lower()
    if mode == 'add':
        add_password()
    elif mode == 'change':
        change_password()
    elif mode == 'view':
        view_passwords()
    elif mode == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please type add, change, view, or quit.")
