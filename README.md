# Overview

This program was built so that I could learn more about software architecture and it's interaction with networks. I wanted to build a remote desktop application because it is a fun way to learn more about both programming and networking. This program runs from command-ui.py and will open a GUI which allows the user to enter a hostname, username, port, and password to initialize an SSH connection with the server. From there, the GUI can also take in commands from the user to perform actions on the remote server via SSH. Any output or errors returned from the server will be displayed to the user in the GUI.

This is a functional remote desktop application.

I decided to write this software because I wanted to learn more about the interaction between software and networking. My father is a network engineer and it has always been of interest to me so I wanted to research and learn how software (my world) interacts with network (his world).

[Software Demo Video](https://youtu.be/am_f6_QzLH0)

# Network Communication

I used a client-server connection that relies on SSH to initialize connections with a server and send commands to the terminal (this is what SSH was built for). Although there is not a program running on both the client and the server the program utilizes SSH commands to execute commands from the server and receive responses (output and errors) back from the server to the client, the program (main).

SSH is built on TCP, not UDP. TCP works good for my application because it verifies that the application is ready to receive files before sending them, it handles errors, and it returns output from the server to my application so the user can have visibility into what is happening.

The messages sent are sent using the SSH protocol which typically happens on port 22 or 2222 if you are utilizing port forwarding. My code here utilizes paramiko because I determined that it would help make best use of the object-oriented programming priciple of abstraction so that I don't have to write custom messages to send to the server.

# Development Environment

I used VSCode to develop this application.

To develop this tool I used python because of it's inherent integration with libraries such as paramiko which make sending and receiving SSH packets so easy. Python also has a handy GUI builder that builds simple UI's called Tkinter. I also utilized this because I wanted to refresh my memory on Tkinter.

# Useful Websites

- [python.org](https://docs.python.org/3/library/socket.html)
- [linode.com](https://www.linode.com/docs/guides/use-paramiko-python-to-ssh-into-a-server/)
- [paramiko.org](https://docs.paramiko.org/en/2.4/api/client.html)

# Future Work

- I'd like to keep track of the directory in my program to alter the commands being sent so it works more like a traditional terminal
- I'd like to make the GUI better so it actually looks like a terminal. This would be fun.
- I'd like to make a better way to display to the user that the connection is established and then remove all of the input for the connection initialization so that the user doesn't have to see it once the connection is initialized.
