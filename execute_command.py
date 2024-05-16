# Copyright Will Keel

import paramiko

class ExecuteCommand:
    """
    A class to establish an SSH connection and execute commands on a remote server.

    Attributes:
    -----------
    ssh : paramiko.SSHClient
        An instance of the SSHClient class to manage the SSH connection.

    Methods:
    --------
    __init__(hostname, port, username, password):
        Initializes the SSH connection with the provided credentials.

    execute_command(command):
        Executes a command on the remote server and returns the output or error.

    close_session():
        Closes the SSH connection.
    """

    def __init__(self, hostname, port, username, password):
        """
        Initializes the ExecuteCommand class with the given connection parameters and attempts to establish an SSH connection.

        Parameters:
        -----------
        hostname : str
            The hostname or IP address of the SSH server.
        port : int
            The port number of the SSH server.
        username : str
            The username to authenticate with the SSH server.
        password : str
            The password to authenticate with the SSH server.
        """
        print("Requesting connection...")
        # Create an SSH client instance
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the server
            self.ssh.connect(hostname, port, username, password)
            print("Connection established successfully")
        except paramiko.AuthenticationException:
            print("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as e:
            print("Unable to establish SSH connection:", e)
        except Exception as e:
            print("Error:", e)

    def execute_command(self, command):
        """
        Executes a command on the remote server and returns the output or error message.

        Parameters:
        -----------
        command : str
            The command to execute on the remote server.

        Returns:
        --------
        str
            The output of the command if available, or the error message if an error occurred.
        """
        try:
            # Execute the command
            stdin, stdout, stderr = self.ssh.exec_command(command)

            # Read the output of the command (if any)
            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                return f"Output:\n{output}"
            if error:
                return f"Error:\n{error}"

            return "Command executed with no output."

        except paramiko.AuthenticationException:
            return "Authentication failed. Please check your credentials."
        except paramiko.SSHException as e:
            return f"Unable to establish SSH connection: {e}"
        except Exception as e:
            return f"Error: {e}"

    def close_session(self):
        """
        Closes the SSH connection.
        """
        self.ssh.close()
