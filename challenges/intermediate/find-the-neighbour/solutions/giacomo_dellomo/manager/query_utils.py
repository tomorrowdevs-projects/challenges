import re


class QueryUtils:
    commands = {0: "right", 1: "left", 2: "upstairs", 3: "downstairs"}

    @staticmethod
    def parser(query):

        arguments = {'name': re.findall(r".+?(?=:)", query), 'command_key': []}

        # get command
        for key, value in QueryUtils.commands.items():
            if value in query:
                arguments['command_key'].append(key)

        # if the command is incorrect, add a -1 to command key dict
        if len(arguments['command_key']) == 0:
            arguments['command_key'].append(-1)

        return arguments
