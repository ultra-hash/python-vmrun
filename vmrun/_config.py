executable="vmrun.exe"
default_location="C:\Program Files (x86)\VMware\VMware Workstation"
commands = {
    # Power - commands
    "power" : {
        "start" : {
            "command" : "start",
            "parameters" : {
                "vmx_path" : {
                    "optional" : False,
                    "command" : "PATH_TO_VM", 
                    "desc": "Enter the complete Path to the vmx file of the virtal machine"
                },
                "gui": {
                    "optional" : True,
                    "command" : "gui",
                    "desc" : "VM will start and visible on Forground",   
                },
                "nogui": {
                    "optional" : True,
                    "command" : "nogui",
                    "desc" : "VM will start and run on Background"
                }
            },
            "desc" : "Start a VM or Team"
        },  
        "stop" : {
            "command" : "stop",
            "parameter" : {
                "vmx_path" : {
                    "optional" : False,
                    "command" : "PATH_TO_VM", 
                    "desc": "Enter the complete Path to the vmx file of the virtal machine"
                },
                "soft" : {
                    "optional" : True,
                    "command" : "soft",
                    "desc" : "Workstation Pro sends a shut-down signal to the guest operating system. An operating system that recognizes the signal shuts down gracefully. Not all guest operating systems respond to a shut-down signal from Workstation Pro. If the guest operating system does not respond to the signal, shut down from the guest operating system as you would a physical machine"
                },
                "hard" : {
                    "optional" : True,
                    "command" : "hard",
                    "desc" : "Workstation Pro powers off the virtual machine abruptly with no consideration for work in progress."
                }
            },
            "desc" : "Stop a VM or Team"
        },  
        "reset" : {
            "command" : "reset",
            "parameter" : {
                "vmx_path" : {
                    "optional" : False,
                    "command" : "PATH_TO_VM", 
                    "desc": "Enter the complete Path to the vmx file of the virtal machine"
                },
                "soft" : {
                    "optional" : True,
                    "command" : "soft",
                    "desc" : "Workstation Pro shuts down and restarts the guest operating system gracefully. VMware Tools runs scripts before the virtual machine shuts down and when the virtual machine starts up."
                },
                "hard" : {
                    "optional" : True,
                    "command" : "hard",
                    "desc" : "Workstation Pro resets the virtual machine abruptly with no consideration for work in progress."
                }
            },
            "desc" : "Reset a VM or Team"
        },  
        "suspend" : {
            "command" : "suspend",
            "parameter" : {
                "vmx_path" : {
                    "optional" : False,
                    "command" : "PATH_TO_VM", 
                    "desc": "Enter the complete Path to the vmx file of the virtal machine"
                },
                "soft" : {
                    "optional" : True,
                    "command" : "soft",
                    "desc" : "Workstation Pro suspends the virtual machine and disconnects it from the network. VMware Tools runs a script in the guest operating system. On Windows guests, if the virtual machine is configured to use DHCP, the script releases the IP address of the virtual machine. On Linux, FreeBSD, and Solaris guests, the script stops networking for the virtual machine."
                },
                "hard" : {
                    "optional" : True,
                    "command" : "hard",
                    "desc" : "Workstation Pro suspends the virtual machine and leaves it connected to the network."
                }
            },
            "desc" : "Suspend a VM or Team"
        },  
        "pause" : {
            "command": "pause",
            "parameter" : {
                "vmx_path" : {
                    "optional" : False,
                    "command" : "PATH_TO_VM", 
                    "desc": "Enter the complete Path to the vmx file of the virtal machine"
                }
            },
            "desc" : "Pause a VM"
        },  
        "unpause" : {
            "command": "unpause",
            "parameter" : {
                "vmx_path" : {
                    "optional" : False,
                    "command" : "PATH_TO_VM", 
                    "desc": "Enter the complete Path to the vmx file of the virtal machine"
                }
            },
            "desc" : "Unpause a VM"
        },  
    }
}