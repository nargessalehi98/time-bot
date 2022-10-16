from typing import Literal

from pydantic import BaseModel


class Chat(BaseModel):
    chat_id: str
    chat_type: Literal['User', 'Bot', 'Group', 'Channel']
    user_id: str
    first_name: str
    last_name: str
    title: str
    username: str


class AuxDate(BaseModel):
    start_id: str
    button_id: str


class NewMessage(BaseModel):
    message_id: str
    text: str
    time: str
    is_edited: bool
    sender_type: str
    aux_data: AuxDate
