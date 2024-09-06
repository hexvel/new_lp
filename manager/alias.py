class AliasManager:
    def __init__(self, user):
        self.user = user
        self.aliases = {}

    def initialize(self):
        aliases = self.user.aliases
        for name, command in aliases.items():
            self.aliases[name] = command
