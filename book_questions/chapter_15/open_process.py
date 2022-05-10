import os
import subprocess
import time
import psutil


lab_process = subprocess.Popen('C:\TrakCare\Lab2014\LabLIVE.bat')
lab_process.wait()

#calc = subprocess.run(['C:\TrakCare\Lab2014\LabLIVE.bat'], capture_output=True, shell=True, text=True)
# print(lab_process.pid)

# output = os.popen('wmic process get processid').read()
# print(output)

def check_process(processid):
    all_process = os.popen('wmic process get processid').read()
    #print(f'The process: {all_process}')
    if str(processid) in all_process:
        print('Found it')
        return True
    print('Dont found it')
    return False


alive = check_process(lab_process.pid)
print(f'LABID: {lab_process.pid}')

last_t = time.perf_counter()
while alive:
    t = time.perf_counter()
    if (t - last_t)*1000 > 1000:
        print('entrou')
        alive = check_process(lab_process.pid)
        last_t = time.perf_counter()
    

print('Done\nProcess killed')
