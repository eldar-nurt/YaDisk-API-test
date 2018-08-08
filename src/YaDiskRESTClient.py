import requests

from src.YaDiskException import YaDiskException
from src.misc import token


class YaDiskRESTClient:

    _base_url = "https://cloud-api.yandex.net/v1/disk"

    def __init__(self):
        self.token = token

        self.base_headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + self.token,
            "Host": "cloud-api.yandex.net"
        }

    @staticmethod
    def _check_code(req):
        if not str(req.status_code).startswith("2"):
            raise YaDiskException(req.status_code, req.text)

    def get_disk_information(self):
        base_url = self._base_url

        base_response = requests.get(base_url, headers=self.base_headers)

        json_base_response = base_response.json()

        print("Общапя информация:\n" + "Объём корзины: " + str(json_base_response["trash_size"]) + " byte \n" +
              "Объём диска: " + str(json_base_response["total_space"]) + " byte \n" +
              "Использованное пространство: " + str(json_base_response["used_space"]) + " byte \n")

    def root_content(self):
        resource_url = self._base_url + "/resources"

        payload = {'path': '/'}

        resource_response = requests.get(resource_url, headers=self.base_headers, params=payload)

        json_resource_response = resource_response.json()

        files_and_dirs = json_resource_response["_embedded"]["items"]
        count_of_files = len(files_and_dirs)

        print("Всего файлов в директорий : " + str(count_of_files) + "\n")

        for item in files_and_dirs:
            if item["type"] == "file":
                type = "Файл"
            else:
                type = "Папка"
            print("Имя: " + item["name"] + "\n" + "Тип: " + type + "\n" + "Путь до файла: " + item["path"] + "\n")
