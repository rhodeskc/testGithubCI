class HelloClass:
    def __init__(self):
        self.name = ""

    def hello_world_msg(self, inName: str | list[str] | tuple[str, ...]) -> str:
        if isinstance(inName, str):
            if inName == "":
                return "Hello world!"
            return f"Hello {inName}"
        
        if isinstance(inName, (list, tuple)):
            cleaned_names = [name.strip() for name in inName if name and name.strip()]
            if not cleaned_names:
                return "Hello world!"
            
            if len(cleaned_names) == 1:
                return f"Hello {cleaned_names[0]}"
            elif len(cleaned_names) == 2:
                return f"Hello {cleaned_names[0]} and {cleaned_names[1]}"
            else:
                joined_names = ", ".join(cleaned_names[:-1]) + f", and {cleaned_names[-1]}"
                return f"Hello {joined_names}"
        
        raise TypeError("inName must be a string, list, or tuple of strings")


