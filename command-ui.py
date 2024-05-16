# Copyright Will Keel

import tkinter as tk
from tkinter import ttk
from execute_command import ExecuteCommand

def main():
    """
    Initializes the main Tkinter application, creates the main frame, and starts the Tkinter event loop.
    """
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main frame
    frm_main = tk.Frame(root)
    frm_main.master.title("Remote Desktop Application")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    
    # Populate main frame with fields, buttons, labels, etc.
    fill_main_frame(frm_main)
        
    # Start the tkinter loop that processes user events
    root.mainloop()

def fill_main_frame(frm_main):
    """
    Populate the main window with labels, text entry boxes, and buttons.

    Parameters:
    -----------
    frm_main : tkinter.Frame
        The main frame (window) to populate with widgets.

    Returns:
    --------
    None
    """
    # Create a label that displays "Remote Desktop Control"
    lbl_title = ttk.Label(frm_main, text="Remote Desktop Control")
    lbl_title.grid(column=0, row=0, padx=0, pady=5)

    # Create a label that displays instructions
    lbl_instructions = ttk.Label(frm_main, text="Welcome to my Remote Desktop App. Follow the instructions to successfully use the app:\n\t1. Enter your session credentials\n\t2. Initiate the session with the server\n\t3. Send commands to the server\n\t4. Close the session with the server")
    lbl_instructions.grid(column=0, row=1, columnspan=4, pady=10, padx=10)

    # Create a label that indicates hostname and gets input
    ttk.Label(frm_main, text="Hostname: ").grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
    ent_hostname = ttk.Entry(frm_main)
    ent_hostname.grid(row=3, column=1, padx=5, pady=5)

    # Create a label that indicates port and gets input
    ttk.Label(frm_main, text="Port: ").grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)
    ent_port = ttk.Entry(frm_main)
    ent_port.grid(row=4, column=1, padx=5, pady=5)

    # Create a label that indicates username and gets input
    ttk.Label(frm_main, text="Username: ").grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)
    ent_username = ttk.Entry(frm_main)
    ent_username.grid(row=5, column=1, padx=5, pady=5)

    # Create a label that indicates password and gets input
    ttk.Label(frm_main, text="Password: ").grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)
    ent_password = ttk.Entry(frm_main, show='*')
    ent_password.grid(row=6, column=1, padx=5, pady=5)
    
    def initialize_connection():
        """
        Initializes the SSH connection using the provided credentials and updates the output label.

        Returns:
        --------
        None
        """
        hostname = ent_hostname.get()
        port = int(ent_port.get())
        username = ent_username.get()
        password = ent_password.get()
        frm_main.session = ExecuteCommand(hostname, port, username, password)
        lbl_output.config(text="Connection initialized")

    style = ttk.Style()
    style.configure('IBtn.TButton', background='green')
    style.map('IBtn.TButton', background=[('active', 'lightgreen')])
    
    # Create a button that initiates a session
    btn_initiate = ttk.Button(frm_main, text="Initialize Connection", command=initialize_connection, style='IBtn.TButton')
    btn_initiate.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

    # Create a label that indicates the command and gets input
    ttk.Label(frm_main, text="Command: ").grid(row=8, column=0, sticky=tk.E, padx=5, pady=5)
    ent_command = ttk.Entry(frm_main)
    ent_command.grid(row=8, column=1, padx=5, pady=5)

    # Create a label that displays output if it exists
    lbl_output = ttk.Label(frm_main, text="Output will be displayed here")
    lbl_output.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    def execute_command():
        """
        Executes the command entered in the command entry box and updates the output label with the result.

        Returns:
        --------
        None
        """
        command = ent_command.get()
        if hasattr(frm_main, 'session'):
            try:
                output = frm_main.session.execute_command(command)
                lbl_output.config(text=output)
            except Exception as e:
                lbl_output.config(text=f"Error: {e}")
        else:
            lbl_output.config(text="Connection not initialized")

    # Create a button to execute commands
    btn_execute = ttk.Button(frm_main, text="Execute Command", command=execute_command, style='IBtn.TButton')
    btn_execute.grid(row=9, column=0, columnspan=2, padx=5, pady=10)

if __name__ == "__main__":
    main()
