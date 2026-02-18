class commands:
    documentation = {}
    def __init__(self):
        pass
    def dummy(arg):
        print("dummy print")
    documentation["dummy"] = "A dummy argument to test the functionality of the help function"
    def getdocumentation(key):
        return commands.documentation[key]
command_prompts = {} #Initial command serialization

def help(arg):
        #no argument case: list all functions
        if len(arg) == 0: 
             print(f"placeholder :D")
        #1 argument case: list 
        if len(arg) == 1:
             print(f"{arg[0]}:\n{commands.getdocumentation(arg[0])}")
command_prompts["help"] = help
command_prompts["dummy"] = commands.dummy
#ask for user input
#if input corresponds to key, run function stored at key values

while True: # Super-Loop
    userInput = input('')
    #split command into arguments
    args = userInput.split(' ')
    command = args[0]
    args.remove(args[0])
    if command == "exit":
        print("Exiting Program...")
        break
    #run the function at the location of the hash
    command_prompts[command](args)
    
    