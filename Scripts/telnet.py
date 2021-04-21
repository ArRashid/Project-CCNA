import getpass
import telnetlib

HOST = input("Host Address : ")
user = input("Your Telnet User name : ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
enpass = input("Enter Enable Password : ")

tn.write(enpass.encode('ascii')+ b"\n")
tn.write(b"conf t\n")
tn.write(b"hostname ArRashid\n")
tn.write(b"end \n")
tn.write(b"exit \n")


print(tn.read_all().decode('ascii'))