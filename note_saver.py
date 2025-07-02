class FileHandling:
    def __init__(self):
            self.fileName = input("Enter a file name you want.: ")
        
    def save_note(self):
        
        try:
            note = input("Enter your note..")
            with open(self.fileName, "a") as f:
                f.write(note+ "\n")
            print("Note saved!")
        except Exception as e:
            print("error", e)

    def read_note(self):
        try:
            with open(self.fileName, 'r') as f:
                content = f.read()        
                print("saved notes " + "to =>" + self.fileName)
                print(".......................................")
                print(content)
                print(".......................................")
        except FileNotFoundError:
            print("File not found!❌")
        except Exception as e:
            print("error reading!👎")


    def menu(self):
        while True:
            print("Note saver---")
            print("1. Write a note")
            print("2. Read all notes")
            print("3. Exit")

            try:
                choice = int(input("Enter choice: "))
                match choice:
                    case 1:
                        self.save_note()
                    case 2:
                        self.read_note()
                    case 3:
                        print("Exiting..")
                        break       
                    case _:
                        print("Invalid choice!")
                
            except ValueError:
                print("Invalid option! Enter number only.")
fh = FileHandling()
fh.menu()
