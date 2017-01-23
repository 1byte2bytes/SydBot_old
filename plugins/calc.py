def init(plugin):
    return [plugin, ["calc"]]

def on_command(command, text):
    print(command)
    if(command == "calc"):
        result = str(eval(text))
        return "", result