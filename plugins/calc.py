def init(plugin):
    return [plugin, ["calc"]]

def on_command(command, text):
    if(command == "calc"):
        try:
            result = str(eval(text))
            return "", result
        except:
            return "", "Input was not a valid math equation :("