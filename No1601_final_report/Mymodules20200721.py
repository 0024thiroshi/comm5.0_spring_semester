import pandas as pd
import matplotlib.pyplot as plt
import copy
from scipy import fftpack
import numpy as np
import networkx as nx


def GetDF(FileName,SheetName):
    df=pd.read_excel(FileName,sheet_name=SheetName)
    return df

def GetS(DF,s1):
    ser1=DF[s1]
    return ser1


def GetDFfromS(s1,s2):
    df=pd.concat([s1,s2],axis=1)
    return df

def CombinedDF(DF,s1):
    df2=pd.concat([DF,s1],axis=1)
    return df2


def PlotSingleG(DF):
    for i in range(1,len(DF.columns)):
        plt.plot(DF.iloc[:,0],DF.iloc[:,i],label=DF.columns.values[i])
        plt.legend()
    axes = plt.gca()
    #axes.set_yscale("log")
    plt.show()

def PlotMultipleG(L1):

    print(L1[0])
    for i in range(len(L1)):
        plt.plot(L1[i].iloc[:,0],L1[i].iloc[:,1],label=L1[i].columns.values[1])
       # plt.legend()
    axes = plt.gca()
    axes.set_xlabel("date")
    axes.set_ylabel("Ratio of dead people to population")
    #axes.set_yscale("log")
    plt.show()



def SetDateIndexDF(DF):
    DF.index = pd.to_datetime(DF.date)
    
    return DF

def ResetIndexDF(DF):
    DF2= DF.reset_index(drop=True) 
    return DF2

def DataExtract (DF,s1,s2):
    DF2=DF.loc[s1:s2,:] 
    return DF2


def GetDailyData(s1):

    s2=copy.deepcopy(s1)
    s2[0]=0
    for i in range(1,len(s2)):
        s2[i]=s1[i]-s1[i-1]
    return s2


def ExtractDF(DF,L1):
    DF2=pd.DataFrame(index=DF.index)
    for name in L1:
        DF2[name]=DF.loc[:,name]
    return DF2


def Plot2020060201(s1,n1):
    plt.hist(s1,bins=n1)
    plt.show()


def  GetZScore (s1):
    s2=pd.Series(index=s1.index,name=s1.name)
    for i in range(len(s1)):
        s2[i]=(s1[i]-s1.mean())/s1.std()
    return s2

def GetRollingMean (s1,n1):
    s2=pd.Series(index=s1.index,name=s1.name)
    s2= s1.rolling(n1).mean()
    return s2

def DeleteNaN(DF):
    DF2=pd.DataFrame(index=DF.index,columns=DF.columns)
    DF2=DF.dropna()
    return DF2

def GetCorr(DF):    
    return DF.corr(method="pearson")

def DataExtractLineN(DF,n1,n2):
    DF2=DF.iloc[n1:(n1+n2),:]
    return DF2



def getTimeVec(nsample,timeStep):

    numpyVector = np.arange(0,nsample*timeStep,timeStep)
    return numpyVector

def getSin(timeVec,f,a):
   
    y = a*np.sin(2*np.pi*f*timeVec)  
    return y

def getSin2(timeVec,f1,a1,f2,a2):
    y1 = a1*np.sin(2*np.pi*f1*timeVec)  
    y2 = a2*np.sin(2*np.pi*f2*timeVec)
  

    y=y1+y2

    return y


def getAmplitudeSpectrum(x,startNumber,sampleNumber):
    
    x2=x[startNumber:(startNumber+sampleNumber)]
    X = fftpack.fft(x2) 

    AS=[np.sqrt(c.real ** 2 + c.imag ** 2) for c in X] 
    AS2=np.array(AS)

    return AS2

def getPhaseSpectrum(x,startNumber,sampleNumber):
    
    x2=x[startNumber:(startNumber+sampleNumber)]
    X = fftpack.fft(x2) 

    PS=[np.arctan2(int(c.imag), int(c.real)) for c in X]
    PS2=np.array(PS)
   
    return PS2

def  getDataN1N2(data,lowcut,highcut,fs,order):
    from scipy.signal import butter,lfilter 
    def butter_bandpass(lowcut,highcut, fs, order=order): 
        nyq = 0.5*fs 
        low = lowcut/nyq 
        high = highcut/nyq 
        b,a = butter(order,[low, high],btype='band') 
        return b,a

    def butter_bandpass_filter(data,lowcut,highcut, fs, order=order): 
        b, a = butter_bandpass(lowcut,highcut, fs, order=order) 
        y = lfilter(b, a, data) 
        return y

    data2 = butter_bandpass_filter(data,lowcut,highcut,fs,order=order)
    return data2


def getTVAS (data,fs):
    a=getAmplitudeSpectrum(data,0,len(data))
    sum=0
    for i in range(len(data)):
        sum=sum+a[i]
    return sum

def getfALFF(data,fs):
    lowdata=getDataN1N2(data,0.01,0.08,fs)
    totaldata=getDataN1N2(data,0.0000001,0.25,fs)

    low_amp=getTVAS(lowdata,fs)
    total_amp=getTVAS(totaldata,fs)

    ALFF=low_amp/total_amp
    return ALFF


def GetColor(n1):#5人分のデータまで対応可能
    color=[np.array([1,0.3,0.3]),np.array([1,1,0.3]),np.array([0.3,1,0.3]),np.array([0.3,0.3,1]),np.array([0.6,0.3,0.8])]  
    color2=[]
    for i in range(2*n1):
        color2.append(color[i%n1])
        color2.append(color[i%n1]-np.array([0.3,0.3,0.3]))

    return color2

def GetSize(n1):
    size=[]
    for i in range(2*n1):
        size.append(800)
    for i in range(2*n1):
        size.append(200)
    return size

def DrowGraph(data,color,size):
    
    G = nx.Graph()
    for i in range(len(data.columns)):
        G.add_node(data.columns.values[i])

    for i in range(len(data)):
        for j in range(len(data.columns)):
            G.add_edge(data.index.values[i],data.columns.values[j],weight=data.iloc[i,j])

    pos = nx.spring_layout(G)

    nx.draw_networkx(G,pos,node_color=color,node_size=size) 
    plt.show()



