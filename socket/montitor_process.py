import os
import sys
import wmi
import win32api
import win32con
import win32security



def log_to_file(data):
    with open('mylog.csv', 'a') as f:
        f.write(f"{data}\r\n")



def monitoring():
    log_to_file('Command Line, Execulatable, Parent PID, PID, User, Privileges')


    c = wmi.WMI()
    process_watcher = c.Win32_Process.watch_for('creation')

    while True:
        try:
            newProcess = process_watcher()
            cmdline = newProcess.CommandLine
            creationDate = newProcess.CreateDate
            execulatable = newProcess.ExcutablePath
            parentPID = newProcess.ParentProcessId
            pid = newProcess.ProcessId
            proc_owner = newProcess.GetOwner
            privilege_message = 'NA'
            log_message = (f"{cmdline},{creationDate},{execulatable},{parentPID},{pid},{proc_owner},{privilege_message}")
            print(log_message)
            print()
            log_to_file(log_message)
        except Exception:
            pass

if __name__ == '__main__':
    monitoring()

        