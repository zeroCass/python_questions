import os
import subprocess
import time
import sys
import psutil
import json
import wmi
import datetime


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




#calc = subprocess.run(['C:\TrakCare\Lab2014\LabLIVE.bat'], capture_output=True, shell=True, text=True)
# print(lab_process.pid)




    
