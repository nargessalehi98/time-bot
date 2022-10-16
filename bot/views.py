from rest_framework import status
from rest_framework.response import Response
from rubika_bot.requests import send_message, delete_message
from rubika_bot.models import Keypad

from bot.buttons import start_bot_keypad, stop_bot_keypad, Buttons
from bot.messages import started_bot_message, stopped_bot_message, message_has_been_removed
from bot.serializers import (
    ReceiveUpdateSerializer,
    ReceiveInlineMassageSerializer
)
from config.decorators import validate_input
from config.settings import BOT_TOKEN
from bot.utils import to_jalali


@validate_input()
def receive_update(request, obj: ReceiveUpdateSerializer):
    if obj.update.type == 'NewMessage':
        send_message(token=BOT_TOKEN, chat_id=obj.update.chat_id, text=to_jalali(obj.update.new_message))

    if obj.update.type == 'UpdatedMessage':
        ...

    if obj.update.type == 'RemovedMessage':
        delete_message(token=BOT_TOKEN, chat_id=obj.update.chat_id, message_id=obj.update.removed_message_id)

    if obj.update.type == 'StartedBot':
        if obj.update.new_message.aux_data.button_id:
            if '1' == obj.update.new_message.aux_data.button_id:
                ...
            elif '2' == obj.update.new_message.aux_data.button_id:
                ...

        send_message(token=BOT_TOKEN, chat_id=obj.update.chat_id, text=started_bot_message,
                     inline_keypad=start_bot_keypad)

    if obj.update.type == 'StoppedBot':
        send_message(token=BOT_TOKEN, chat_id=obj.update.chat_id, text=stopped_bot_message,
                     chat_keypad=stop_bot_keypad)

    if obj.update.type == 'UpdatedPayment':
        #      not yet
        ...
    return Response(status=status.HTTP_200_OK)


@validate_input()
def receive_inline_massage(request, obj: ReceiveInlineMassageSerializer):
    ...
