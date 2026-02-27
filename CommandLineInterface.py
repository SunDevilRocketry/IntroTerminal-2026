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
            try:
                print(f"{arg[0]}    ----    {self.getdocumentation(arg[0])}")
            except:
                print("\nError: Unrecognized function for help command\n")
        else:
            print("Error: incorrect argument count.\n")
        
class DUMMY:
    def __init__(self):
        pass
    def dummy(self,args):
        if len(args) == 0:
            print("dummy print")
        else:
            print("NO.")

    def dummy3(self,arg):
        if len(arg) != 3:
            print("\nError: incorrect argument count.\nPlease Enter 3 arguments\n")
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
        print("\nThank You for Using LeOS\n")
        break
    #run the function at the location of the hash
    try:
        command_prompts[command](args)
    except:
        print("\nError: Unrecognized function \n")
    

    
    