import matplotlib.pyplot as plt
import cv2
from datetime import datetime
import numpy as np
import random

# data plotting
lstX = []
lstY1 = []

plt.ion()
fig1 = plt.figure(num='real-time plotting1')
sf1 = fig1.add_subplot(111)
plt.title('Watching Time')
plt.xticks([0, 1500000, 3000000, 4500000, 6000000])
plt.yticks([1,2,3,4,5,6,7,8,9])
line1, = sf1.plot([0, 6000000], [0,10], 'b-')

#channel = np.random.poisson(lam=3, size=1)

while True:
    channel = np.random.poisson(lam=3, size=1)
    
    c = datetime.now()
    d = c.strftime('%S%f')
    d = np.float32(d) / 10.0
    lstX.append(d)
    
    if d > 5900000: # 1분마다 플롯 초기화
        fig1.clf()
        fig1 = plt.figure(num='real-time plotting1')
        sf1 = fig1.add_subplot(111)
        plt.title('Watching Time')
        plt.xticks([0, 1500000, 3000000, 4500000, 6000000])
        plt.yticks([1,2,3,4,5,6,7,8,9])
        lstX=[]
        lstY1=[]
        line1, = sf1.plot([0, 6000000], [0,10], 'b-')
        line1.set_data(lstX, lstY1)
        
    else:
        """
        if d < 1500000:
            lstY1.append(5)
        elif d < 2000000:
            lstY1.append(3)
        elif d < 4500000:
            lstY1.append(5)
        else:
            lstY1.append(8)
        """
        lstY1.append(channel[0])
        
        line1.set_data(lstX, lstY1)
        plt.show()
        plt.pause(0.0001)
