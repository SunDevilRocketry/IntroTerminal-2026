import terminalserial

class CLI: 
    documentation = {}
    def __init__(self):
        self.documentation = {
             "help": "List of Available Commands in the Command Line Interface (CLI) or one specific command",
             "connect":"Connects a Serial Port to the CLI 'Connect <comport> <baud rate>'",
             "get_ports":"Prints all available comports"
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

cli = CLI()
serial = terminalserial.SerialTerminal()

command_prompts ={
     "help":cli.help,
     "connect":serial.connect,
     "get_ports":serial.get_available_ports
    }

if __name__ == "__main__":

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
        command_prompts[command](args)