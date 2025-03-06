from configs._def_main_ import *

@ryas('id')
def obtener_id(client, message):
    user_id = message.from_user.id
    reply_msg = message.reply_to_message.message_id if message.reply_to_message else message.id
    message.reply_text(idtext.format(user_id=user_id), reply_to_message_id=reply_msg)
