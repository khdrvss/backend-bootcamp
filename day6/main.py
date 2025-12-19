def adding(new_text):
    with open("notes.txt", "a") as file:
        file.write(new_text + '\n')

def show_notes():
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

print ("<- My notes app ->")

while True:
    print('1. Add new note')
    print('2. Show notes')
    print('3. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        new_text = input('Enter ur note: ')
        adding(new_text)
    elif choice == 2:
        show_notes()
    elif choice == 3:
        break
    else:
        print('invalid typo!')
