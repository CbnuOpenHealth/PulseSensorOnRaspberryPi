from pulsesensor import Pulsesensor
import time
import pymysql.cursors


p = Pulsesensor()
p.startAsyncBPM()
i = 0
bpmavg = 0
f = open('pulseChek.txt','w')
try:
    while True:
        conn = pymysql.connect(host='localhost', user='ktw', password='12345678', db='testDB') 
        curs = conn.cursor()
        sql = 'insert into pulse (datas) values (%s)'
        bpm = p.BPM
        if bpm > 50 and bpm < 160 :
            print("BPM: %d" % bpm)
            i += 1
            bpmavg += bpm
        else:
            print("No Heartbeat found")
        time.sleep(1)
        if i == 15:
            bpmavg /= 15
            curs.execute(sql, bpmavg)
            conn.commit()
            conn.close()
            print("Check Pulse")
            i=0
except:
    p.stopAsyncBPM()
