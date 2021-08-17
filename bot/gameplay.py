from bot import bot
import messages, objects

def join(user_id, game_id):
    error_id, free = objects.status.add_user(user_id, game_id)   
    if error_id == 1:
        bot.send_message(user_id, messages.NO_GAME.format(game_id=game_id))
    elif error_id == 0:
        bot.send_message(user_id, messages.JOINED_GAME.format(game_id=game_id, free_count=free))


def create(user_id, roles):
    game_id = objects.status.new_game(user_id, roles)    
    bot.send_message(user_id, messages.GAME_CREATED.format(
        user_count=len(roles),
        roles=", ".join(roles),
        game_id=game_id
    ))
