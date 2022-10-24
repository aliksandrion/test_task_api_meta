from srvc.config import DEFAULT_DIRECTORY

from django.http import JsonResponse
import os


def answer(request):
    path = DEFAULT_DIRECTORY

    names = os.listdir(path)
    types = [i.is_file() for i in os.scandir(path)]
    times = [int(os.path.getctime(j)) for j in os.scandir(path)]

    data_list = []

    for i in zip(names, types, times):
        data_list.append(
            {
                "name": i[0],
                "type": "file" if i[1] else "folder",
                "time": i[2]
            }
        )

    data_list.sort(key=lambda x: x.get("time"))
    response = {"data": data_list}

    return JsonResponse(response)
