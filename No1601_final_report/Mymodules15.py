def getDF1503(DF1,DF2,sNation,StartTime,EndTime):
    import Mymodules20200721

    DF1=Mymodules20200721.SetDateIndexDF(DF1)
    DF2=Mymodules20200721.SetDateIndexDF(DF2)
    

    Sdate=Mymodules20200721.GetS(Mymodules20200721.DataExtract(DF1,StartTime,EndTime),"date")

    S_n_1_n=Mymodules20200721.GetS(Mymodules20200721.DataExtract(DF1,StartTime,EndTime),sNation)
    S_n_1_n.name="{}_cases".format(S_n_1_n.name)
    S_n_2_n=Mymodules20200721.GetS(Mymodules20200721.DataExtract(DF2,StartTime,EndTime),sNation)
    S_n_2_n.name="{}_deaths".format(S_n_2_n.name)

    DF3=Mymodules20200721.GetDFfromS(S_n_1_n,S_n_2_n)
    return DF3


def myPlot1504(DF4):
    import Mymodules20200721
    import matplotlib.pyplot as plt
    str=["cases","deaths"]
    for i in range(len(DF4.columns)):
        plt.plot(DF4.index,DF4.iloc[:,i],label="{}".format(DF4.columns.values[i]))
        plt.legend()
    axes = plt.gca()
    axes.set_xlabel("date")
    axes.set_ylabel("the number of people [people]")
    plt.show()



def myPlot1505(L1):
    import Mymodules20200721
    import matplotlib.pyplot as plt
    str=["cases","deaths"]

    for i in range(len(L1)):
        ax=plt.subplot(1,len(L1),i+1)
        for j in range(len(L1[i].columns)):
            plt.plot(L1[i].index,L1[i].iloc[:,j],label="{}".format(L1[i].columns.values[j]))
            plt.legend()
            axes = plt.gca()
    plt.show()
   
    



def seriesPartCor(s1,s2,n1):
    import Mymodules20200721
    import pandas as pd
    s3=pd.Series()
    
    for i in range(len(s1)-n1):
        s1a=pd.Series(s1.iloc[i:i+n1])
        s2a=pd.Series(s2.iloc[i:i+n1])
        
        #print(pd.Series(s1.index).dt.date)
       
        #s3["{}".format(s1.index[i+n1])]=Mymodules20200721.GetCorr(Mymodules20200721.GetDFfromS(s1a,s2a)).iloc[0,1]
        s3["{}".format(pd.Series(s1.index).dt.date[i+n1])]=Mymodules20200721.GetCorr(Mymodules20200721.GetDFfromS(s1a,s2a)).iloc[0,1]
        
    
    return s3
