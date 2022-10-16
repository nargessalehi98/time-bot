from typing import Literal

from pydantic import BaseModel

from rubika_bot.models import Update, InlineMessage


class ReceiveUpdateSerializer(BaseModel):
    update: Update


class ReceiveInlineMassageSerializer(BaseModel):
    inline_message: InlineMessage
