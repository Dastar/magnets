import subprocess


class Printer:
    @staticmethod
    def list_all_printers() -> list:
        result = subprocess.run(['lpstat', '-p'], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
        return [i.split()[0]
                for i in result.split('printer')
                if i]

    @staticmethod
    def get_page_size():
        result = subprocess.run(['lpoptions', '-l'], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
        return result


if __name__ == '__main__':
    print(Printer.get_page_size())
