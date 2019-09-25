import subprocess


class Printer:
    def __init__(self, printer: str, default: list = []):
        self.printer = printer
        self.default = default

    def run(self, file, options: list = []):
        """Prints file"""
        cmd = ['lp', '-d', self.printer]
        cmd += self.default
        cmd += options

        cmd.append(file)
        subprocess.run(cmd)

    def cancel(self, job=None):
        """Cancel the job"""""
        cmd = ['lprm', '-P', self.printer]
        if job is list:
            cmd += job
        elif job is not None:
            cmd.append(job)

        subprocess.run(cmd)

    @staticmethod
    def list_all_printers() -> list:
        """Returns result of shell-command lpstat -p"""
        result = subprocess.run(['lpstat', '-e'], stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8').split()

    @staticmethod
    def get_printer_options() -> dict:
        """Returns result of shell-command lpoptions -l"""
        result = subprocess.run(['lpoptions', '-l'], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
        return dict((k.strip(), v.strip())
                    for k, v in (item.split(':')
                                 for item in result.split('\n') if item))
