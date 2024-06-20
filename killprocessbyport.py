import os
import sys
import signal
import subprocess

def get_process_id(port, platform):
    if platform == "win32":
        cmd = f"netstat -ano | findstr :{port}"
    else:
        cmd = f"lsof -i :{port} -t"

    try:
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        if platform == "win32":
            pid = output.strip().split()[-1]
        else:
            pid = output.strip().split("\n")[0]
        return int(pid)
    except (subprocess.CalledProcessError, IndexError):
        return None

def kill_process(pid, platform):
    if platform == "win32":
        cmd = f"taskkill /PID {pid} /F"
    else:
        cmd = f"kill -9 {pid}"

    try:
        subprocess.check_output(cmd, shell=True, universal_newlines=True)
        print(f"Process with PID {pid} has been terminated.")
    except subprocess.CalledProcessError as e:
        print(f"Error terminating process: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <port_number>")
        sys.exit(1)

    port = sys.argv[1]
    platform = sys.platform
    pid = get_process_id(port, platform)
    if pid:
        kill_process(pid, platform)
    else:
        print(f"No process found listening on port {port}.")