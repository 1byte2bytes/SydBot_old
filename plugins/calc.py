def init(plugin):
    return [plugin, ["calc"]]

def on_command(command, text):
    if(command == "calc"):
        result = eval(text)
        return ["", result]