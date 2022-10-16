from pydantic import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def validate_input(auth=False, perm=None):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if len(list(func.__annotations__.values())) != 0:
                serializer = list(func.__annotations__.values())[0]
                try:
                    obj = serializer(**request.api_data)
                except ValidationError as validation_error:
                    return Response(
                        data={'.'.join(e['loc']): e['msg'] for e in validation_error.errors()},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                    # return Response(data={'detail': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)

                kwargs['obj'] = obj

            return func(request, *args, **kwargs)

        return wrap

    return decorator
