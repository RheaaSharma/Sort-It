from .models import Square
from asgiref.sync import async_to_sync, sync_to_async


@sync_to_async
def create_square(data):
    print('Running Python')
    res = Square.objects.create(filename=data, coffee=1, number=1)
    print(f'Success: Created object {data} on Square!')
