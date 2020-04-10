import subprocess

# Using shell=True is not recommended
subprocess.run("cat metaclasses.py | grep class", shell=True)

command = "ls aasds"
proc = subprocess.run(command.split(), capture_output=True)
# proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc.stderr.decode())

with open('out.txt', 'wb') as f:
    subprocess.run('ls -alh'.split(), stdout=f)


grep_input = """
hello
bye
hello world
"""
proc = subprocess.run('grep hello'.split(), input=grep_input.encode(), capture_output=True)
print(proc.stdout.decode(), proc.stderr.decode())


proc = subprocess.Popen('sleep 1'.split())
print(proc.pid)
proc.wait()
print(proc.returncode)

# proc.join()  # waits for proc to end; blocking
# proc.poll()  # polls proc status; non-blocking

# while proc.poll() is None:
#     print('Waiting for proc to execute...')
