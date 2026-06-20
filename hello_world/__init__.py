class HelloClass:
    def __init__(self):
        self.name = ""

    def hello_world_msg(self, inName: str):
        if inName == "":
            return "Hello world!"
        else:
            return f"Hello 2 {inName}"
