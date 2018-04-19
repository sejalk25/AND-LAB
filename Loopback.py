import getpass
import sys
import telnetlib

HOST = ("172.16.126.134","172.16.126.137","172.16.126.136")
user = raw_input("Enter your username: ")
password = getpass.getpass()

for x in range(5, 10):
    for i in HOST:
        if i is "172.16.126.134":
        tn=telnetlib.Telnet(HOST[0],timeout=15)
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("conf t\n")
        tn.write("int lo" + Str(1)\n")
        ip = str(1)"."+ str(1)"." + str(1)"." + str(1)
        tn.write("ip address" + ip + "255.255.255.255 \n")
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()

    elif i is "172.16.126.137":
        tn=telnetlib.Telnet(HOST[1],timeout=15)
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("conf t\n")
        tn.write("int lo" + str(1)+"\n")
        tn.write("ip add 1.1.1.1 255.255.255.255\n")
        tn.write("end\n")
        tn.write("exit\n")
print tn.read_all()

