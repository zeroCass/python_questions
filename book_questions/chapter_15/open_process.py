import os
import subprocess
import time
import sys
import psutil
import json
import wmi


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


def check_process(processid):
    process = os.popen('wmic process get processid').read()
    #print(f'The process: {all_process}')
    if str(processid) in process:
        print('Found it')
        return True
    print('Dont found it')
    return False



last_t = time.perf_counter()
alive = check_process(processid)
while alive:
    t = time.perf_counter()
    if (t - last_t)*1000 > 1000:
        alive = check_process(processid)
        last_t = time.perf_counter()
    
