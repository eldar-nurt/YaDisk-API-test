from src.YaDiskRESTClient import YaDiskRESTClient


def main():
    new_ya_work = YaDiskRESTClient()
    new_ya_work.get_disk_information()
    new_ya_work.root_content()


if __name__ == '__main__':
    main()