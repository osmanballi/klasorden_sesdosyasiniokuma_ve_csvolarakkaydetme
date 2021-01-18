import os
from scipy.io import wavfile
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
path = "ses" #klasörün adı
myList = os.listdir(path)
print("Total Classes Detected:",len(myList)) #klasörde bulunan klasör sayısı
print(myList) #klasör adları
for voice in myList:
    rate, data = wav.read(path+"/"+voice) #ses dosyasını okuma
    plt.plot(data) #sesi görselleştirme
    plt.show()
    data = data.tolist()
    print(voice)
    print(rate)
    print(len(data))
    csvpath = ("csv_files"+"/"+str(voice)+".csv")
    with open(csvpath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)