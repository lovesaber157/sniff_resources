import colorama

def showSuccess(msg):
    print(colorama.Fore.GREEN,msg)
    return 1

def showError(msg):
    print(colorama.Fore.RED,msg)
    return 1

def showWarning(msg):
    print(colorama.Fore.YELLOW,msg)
    return 1