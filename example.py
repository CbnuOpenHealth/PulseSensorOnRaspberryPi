from pulsesensor import Pulsesensor
import time

p = Pulsesensor()
p.startAsyncBPM()
i = 0
bpmavg = 0
f = open('pulseChek.txt','w')
try:
    while True:
        bpm = p.BPM
        if bpm > 50 and bpm < 120 :
            print("BPM: %d" % bpm)
            i += 1
            bpmavg += bpm
        else:
            print("No Heartbeat found")
        time.sleep(1)
        if i == 15:
            bpmavg /= 15
            f.write("%d\n" % bpmavg)
            f.close()
            sys.exit(1)
except:
    p.stopAsyncBPM()
