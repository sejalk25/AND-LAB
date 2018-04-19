import getpass
import telnetlib

user = raw_input("Enter your username: ")
password = getpass.getpass()


HOST = ("172.16.126.136","172.16.126.134","172.16.126.137")

for i in HOST:
    print("\n\nconnecting to" +i)
    tn = telnetlib.Telnet(i,timeout = 15)
    if i is "172.16.126.136":
        tn.read_until("login")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("sh configuration | display set\n")
        tn.write("exit\n")

    elif i is "172.16.126.134":
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("terminal length 0\n")
        tn.write("show runni\n")
        tn.write("exit\n")

    elif i is "172.16.126.137":
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("terminal length 0\n")
        tn.write("show runn\n\n")
        tn.write("exit\n\n")
        #print(tn.read_all())
    readall = tn.read_all()
    File = open("File"+str(i),"w")
    File.write(readall)
    File.write("\n")
    File.close()
    print("Backup of "+i+"completed")








