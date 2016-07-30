from collections import OrderedDict

class OptionsCollection:
    INITIAL_PROMPT_MESSAGE = "What would you like to do?\n{}(Choose an option): "
    INVALID_OPTION_SELECTED_MESSAGE = "That is not an option. Please choose again: "

    def __init__(self, commands, prompt_message=INITIAL_PROMPT_MESSAGE, invalid_option_message=INVALID_OPTION_SELECTED_MESSAGE):
        self.prompt_message = prompt_message
        self.invalid_option_message = invalid_option_message
        self.commands = OrderedDict()
        for command in commands:
            key, value = command
            self.commands[key] = value

    def prompt(self):
        while True and len(self.commands) > 0:
            selection = input(self.prompt_message.format(self))

            while selection not in self.keys():
                selection = input(self.invalid_option_message)

            selected_command = self.commands[selection]
            print() # Just a newline for formatting
            if not selected_command.loop:
                return self.commands[selection].execute()
            else:
                self.commands[selection].execute()

    def add_option(self, option_to_add):
        key, value = option_to_add
        self.commands[key] = value

    def keys(self):
        return self.commands.keys()

    def get(self, id):
        return self.commands[id]

    def __str__(self):
        result = ""
        for key in self.commands:
            result += str(self.commands[key]) + "\n"
        return result

    def __len__(self):
        return len(self.commands)

class Command:
    def __init__(self, label, function=None, loop=False):
        self.label = label
        self.function = function
        self.loop = loop

    def execute(self, *args):
        if self.function is not None:
            return self.function(*args)
        else:
            return

    def __repr__(self):
        return self.label