import os
import sys
import wmi
import win32api
import win32con
import win32security

def log_to_file(data):
    with open('mylogfile.csv','a') as f:
        f.write(f"{data}\r\n")

def monitoring():
    log_to_file("Command Line , Executable, Parent PID , PID, User, Privileges")

    c = wmi.WMI()
    process_watcher = c.Win32_Process.watch_for('creation')

    while True:
        try:
            newProcess = process_watcher()
            cmdline = newProcess.CommandLine
            creationDate = newProcess.CreationDate
            executablee = newProcess.ExecutablePath
            parentPID = newProcess.ParentProcessId
            pid = newProcess.ProcessId
            proc_owner = newProcess.GetOwner()
            privilege = 'N/A'
            log_message = (f"{cmdline},{creationDate},{executablee},{parentPID},{pid},{proc_owner},{privilege}")
            print(log_message)
            print()
            log_to_file(log_message)

        except Exception:
            pass


if __name__ == '__main__':
    monitoring()