from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bot.views import receive_update, receive_inline_massage

urls = {
    'receiveUpdate': receive_update,
    'receiveInlineMessage': receive_inline_massage,
}


@api_view(http_method_names=['POST'])
def bot_routing(request, *args, **kwargs):
    return urls[request.api_method](request, *args, **kwargs)
    # if request.api_method not in urls.keys():
    #     return not_found(request, *args, **kwargs)
    # try:
    #     return urls[request.api_method](request, *args, **kwargs)
    # except Exception:
    #     return Response(status=status.HTTP_409_CONFLICT)


def not_found(request, *args, **kwargs):
    return Response(status=status.HTTP_404_NOT_FOUND)
