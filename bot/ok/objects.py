from bot import bot
import random, messages

class Game:
    def __init__(self, i, r, p=[]):
        self.id = i
        self.players = p
        self.roles = r
        self.started = False
    def free(self):
        return len(self.roles) - len(self.players)
    def start(self):
        self.started = True
        random.shuffle(self.roles)
        for i in range(len(self.players)):
            user_id, role = self.players[i], self.roles[i]
            bot.send_message(user_id, messages.GAME_START.format(role=role))


class BotStatus:
    def __init__(self):
        self.games = {}
    def new_game(self, creator_id, roles):
        while True:
            game_id = str(random.randint(1, 100000))
            if game_id not in self.games:
                break
        self.games[game_id] = Game(game_id, roles, [creator_id])
        return game_id

    def add_user(self, user_id, game_id):
        print(self.games)
        if game_id not in self.games:
            return 1, -1
        self.games[game_id].players.append(user_id)
        free = self.games[game_id].free()
        if free == 0:
            self.games[game_id].start()
            del self.games[game_id]
        return 0, free

status = BotStatus()
