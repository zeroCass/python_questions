import os
import subprocess
import time
import sys
import psutil
import json
import wmi
import datetime


# old_process = {p.pid for p in psutil.process_iter()}
# for p in psutil.process_iter():
#     pinfo = p.as_dict(attrs=['pid', 'name'])
#     print(pinfo)
# calc_process = subprocess.Popen('C:\Windows\System32\calc')
# print('\n\n')
# for p in psutil.process_iter():
#     pinfo = p.as_dict(attrs=['pid', 'name'])
#     print(pinfo)
# new_process = {p.pid for p in psutil.process_iter()}
# process = list(new_process - old_process)[0]

# print(process)
# print(psutil.Process(process).name())
# print(psutil.pid_exists(process))
# for p in psutil.process_iter():
#     if p.pid == process:
#         print(f'{p}: name:{p.name()} - pid: {p.pid}')


# print(psutil.pid_exists(process))
# while psutil.pid_exists(process):
#     print('Process running')
# print('Done')

process = subprocess.Popen(['start', '/w', 'calc.exe'], shell=True)

while psutil.pid_exists(process.pid):
    print('Process running')
print('Done')





# all_process = []
# for p in psutil.process_iter():
#     #pinfo = p.as_dict(attrs=['pid', 'name', 'create_time'])
#     all_process.append(p.pid)

# all_process = os.popen('wmic process get processid').read()



process = subprocess.Popen('C:\Windows\System32\calc', creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP, shell=False)
#process = subprocess.Popen('C:\Windows\System32\calc', creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#os.startfile('C:\Windows\System32\calc')


process_name = 'calculator.exe'
# esse pid deixara de existir quando process.poll() == 0
print(process.pid)
process.wait()

running = True
while running:
    running = process.pid in (p.pid for p in psutil.process_iter())
    print('Running')
print('Done')

# loop para verifica os processos criados recentemente

for p in psutil.process_iter():
    create_h = datetime.datetime.fromtimestamp(p.create_time())
    t = datetime.datetime.now() - datetime.timedelta(minutes=5)
    # verifica se o tempo de criacao do processo eh maior do 5min atras
    if create_h > t:
        # mostra os processos recentes
        print(p)

# gera a lista de processos filhos
current_p = psutil.Process()
children = current_p.children(recursive=True)
print(children) # lista retorna vazia
for child in children:
    print(f'Child pid: {child.pid}')


print('Done')

# ESTE FUNCIONA
# c = wmi.WMI()
# process_watcher = c.Win32_Process.watch_for("creation")
# lab_process = subprocess.Popen('C:\TrakCare\Lab2014\LabLIVE.bat')
# while True:
#     new_process = process_watcher()
#     print(new_process.Caption,new_process.ProcessId)




# with open('otuput.txt', 'w') as f:
#     for line in all_process:
#         for key, value in line.items():
#             f.write(f'{key}:{value}\t')
#         f.write('\n')



sys.exit(0)

#calc = subprocess.run(['C:\TrakCare\Lab2014\LabLIVE.bat'], capture_output=True, shell=True, text=True)
# print(lab_process.pid)




    
