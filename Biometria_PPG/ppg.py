import os
import numpy as np
import heartpy as hp
import pandas as pd
import matplotlib.pyplot as plt

dir = "Damasceno_PPG/"
sample_rate = 100
interBeat = [] 
standDeviRR = []
standDeviSD = []
rootMeanSquareSD = []
propSD_20ms = []
propSD_50ms = []
medianAbsoluteRR = []
standDevi1 = []
standDevi2 = []
elipseArea = []
ratioSD1_SD2 = []
id = []

for filename in os.listdir(dir):
    file = dir
    file += str(os.fsdecode(filename))
    df = pd.read_csv(file)
    print(file)
    signal = df['hart'].values

    enhanced = hp.enhance_peaks(signal, iterations=2)
    #Let's run it through a standard butterworth bandpass implementation to remove everything < 0.8 and > 3.5 Hz.
    filtered = hp.filter_signal(enhanced, [0.7, 10], sample_rate = 100.0, 
                                order = 3, filtertype = 'bandpass')
    #run the analysis
    wd, m = hp.process(filtered, sample_rate = 100.0, high_precision = True, clean_rr = True)

    interBeat.append(m['ibi'])
    standDeviRR.append(m['sdnn'])
    standDeviSD.append(m['sdsd'])
    rootMeanSquareSD.append(m['rmssd'])
    propSD_20ms.append(m['pnn20'])
    propSD_50ms.append(m['pnn50'])
    medianAbsoluteRR.append(m['hr_mad'])
    standDevi1.append(m['sd1'])
    standDevi2.append(m['sd2'])
    elipseArea.append(m['s'])
    ratioSD1_SD2.append(m['sd1/sd2'])
    id.append(0)

# dictionary of lists  
dict = {'ibi': interBeat, 'sdnn': standDeviRR, 'sdsd': standDeviSD, 'rmssd': rootMeanSquareSD, 'pnn20': propSD_20ms,'pnn50': propSD_50ms, 
        'hr_mad': medianAbsoluteRR, 'sd1': standDevi1, 'sd2': standDevi2, 's': elipseArea, 'sd1/sd2': ratioSD1_SD2, 'id': id}  
df = pd.DataFrame(dict)
df.to_csv('samples.csv', index=False)
#and plot the result
#plt.figure(figsize=(12,6))
#plt.plot(signal)
#plt.plot(enhanced)
#hp.plotter(wd, m, title = 'analysed signal')
#hp.plot_poincare(wd, m)

#display measures computed
#for measure in m.keys():
#    print('%s: %f' %(measure, m[measure]))
