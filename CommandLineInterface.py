class CLI:
    documentation = {}
    def __init__(self):
        self.documentation = {
             "dummy": "A dummy argument to test the functionality of the help function",
             "dummy3": "Another dummy argument to test the functionality of our code",
             "help": "List of Available Commands, or one specific command"
        }
        pass
    
    def getdocumentation(self,key):
        return self.documentation[key]
    
    def help(self,arg):
        #no argument case: list all functions
        if len(arg) == 0: 
            keys = list(command_prompts.keys())
            
            print(f"\nAvailable Command Prompts: \n")
            for k in keys:
                print(f"{k}    ----    {self.getdocumentation(k)}")
        #1 argument case: list 
        elif len(arg) == 1:
            print(f"{arg[0]}    ----    {self.getdocumentation(arg[0])}")
        else:
            print("Error: incorrect argument count.\n")
        print("")
        
class DUMMY:
    def __init__(self):
        pass
    def dummy(self):
        print("dummy print")
    def dummy3(self,arg):
        if len(arg) != 3:
            print("Error: incorrect argument count.\n\n Please Enter 3 arguments")
        else:
            print(f"{arg[0]} {arg[1]} {arg[2]}")

cli = CLI()
dumdum = DUMMY()

command_prompts ={
     "help":cli.help,
     "dummy":dumdum.dummy,
     "dummy3":dumdum.dummy3
    }


#ask for user input
#if input corresponds to key, run function stored at key values

print("Welcome to LeOS")

while True: # Super-Loop
    userInput = input('LeOS>> ')
    #split command into arguments
    args = userInput.split(' ')
    command = args[0]
    args.remove(args[0])
    if command == "exit":
        print("Thank You for Using LeOS")
        break
    #run the function at the location of the hash
    command_prompts[command](args)
    
    