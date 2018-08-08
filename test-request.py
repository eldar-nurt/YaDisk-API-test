import requests

base_url = "https://cloud-api.yandex.net/v1/disk"
resource_url = base_url + "/resources"
token = "AQAAAAAn8Ch3AADLW4jTqG2w403Gh1u3YlA6-w81488"

payload = {'path': '/'}

print(resource_url)

base_headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + token,
            "Host": "cloud-api.yandex.net"
}

base_response = requests.get(base_url, headers=base_headers)
resource_response = requests.get(resource_url, headers=base_headers, params=payload)

json_base_response = base_response.json()
json_resource_response = resource_response.json()

print("Объём корзины: " + str(json_base_response["trash_size"]) + " byte \n" + "Объём диска: " +
      str(json_base_response["total_space"]) + " byte \n" + "Использованное пространство: " +
      str(json_base_response["used_space"]) + " byte \n")

files_and_dirs = json_resource_response["_embedded"]["items"]
count_of_files = len(files_and_dirs)

print("Всего файлов и директорий : " + str(count_of_files))

for item in files_and_dirs:
    if item["type"] == "file":
        type = "Файл"
    else:
        type = "Папка"
    print("Имя: " + item["name"] + "\n" + "Тип: " + type + "\n" + "Путь до файла: " + item["path"] + "\n")
