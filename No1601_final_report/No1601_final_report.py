import Mymodules20200721 as my21
import Mymodules15 as my15
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl

def DrowGraph2(data):
    G=nx.Graph()
    for i in range(len(data.columns)):
        G.add_node(data.columns.values[i])

    for i in range(len(data)):
        for j in range(len(data.columns)):
            G.add_edge(data.index.values[i],data.columns.values[j],weight=round(data.iloc[i,j],2))

    pos = nx.spring_layout(G,k=1.2)
   
    edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
    
    nx.draw_networkx(G,pos, with_labels=True)
    #nx.draw_networkx(G)
    axes = plt.gca()
    axes.set_xlabel("date")
    axes.set_ylabel("the number of daily new cases")
    plt.show()

def DrowGraph3cases(data):#全ての国の感染者の状況を見る
    Location=my21.GetDF("locations.xlsx","locations")
    #print(data)
    LD={}
    c=[]
    G=nx.Graph()
    Location=Location.set_index("location")
    for i in range(1,len(data.columns)):
        name="{}".format(data.columns.values[i].replace("_cases",""))
        #print(name)
        G.add_node(name)

        #print("{}".format(data.columns[i].replace("_cases","")))
        #print(Location.loc[:,"location"])
        #print(Location.loc["{}".format(data.columns[i].replace("_cases","")),"continent"])
        #print(Location)
        if "{}".format(data.columns[i].replace("_cases","")) in Location.index.values:
            st="{}".format(data.columns[i].replace("_cases",""))            
            LD["{}".format(data.columns[i].replace("_cases",""))]=Location.loc[st,"continent"]
            if LD.get("{}".format(data.columns[i].replace("_cases","")))=="Europe":
                c.append("purple")
            elif LD.get("{}".format(data.columns[i].replace("_cases","")))=="Asia":
                c.append("red")
            elif LD.get("{}".format(data.columns[i].replace("_cases","")))=="Africa":
                c.append("green")
            elif LD.get("{}".format(data.columns[i].replace("_cases","")))=="North America":
                c.append("yellow")
            elif LD.get("{}".format(data.columns[i].replace("_cases","")))=="South America":
                c.append("orange")
            elif LD.get("{}".format(data.columns[i].replace("_cases","")))=="Oceania":
                c.append("blue")
            else:
                c.append("black")

            
    #print(LD)
    #print(c)

    #print(len(LD))
    #print(len(c))

    for i in range(1,len(data)):
        for j in range(1,len(data.columns)):
            name1="{}".format(data.columns.values[i].replace("_cases",""))
            name2="{}".format(data.columns.values[j].replace("_cases",""))
            G.add_edge(name1,name2,weight=round(data.iloc[i,j],2))

    pos = nx.spring_layout(G,k=1.2)
   
    #edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
    #nx.draw_networkx_edge_labels(G,pos)
   

    nx.draw_networkx(G,pos,node_color=c,edge_color="white")
    #nx.draw_networkx(G)
    plt.show()


def DrowGraph3deaths(data):#全ての国の感染者の状況を見る
    Location=my21.GetDF("locations.xlsx","locations")
    #print(data)
    LD={}
    c=[]
    G=nx.Graph()
    Location=Location.set_index("location")
    for i in range(1,len(data.columns)):
        name="{}".format(data.columns.values[i].replace("_deaths",""))
        #print(name)
        G.add_node(name)

        #print("{}".format(data.columns[i].replace("_cases","")))
        #print(Location.loc[:,"location"])
        #print(Location.loc["{}".format(data.columns[i].replace("_cases","")),"continent"])
        #print(Location)
        if "{}".format(data.columns[i].replace("_deaths","")) in Location.index.values:
            st="{}".format(data.columns[i].replace("_deaths",""))            
            LD["{}".format(data.columns[i].replace("_deaths",""))]=Location.loc[st,"continent"]
            if LD.get("{}".format(data.columns[i].replace("_deaths","")))=="Europe":
                c.append("purple")
            elif LD.get("{}".format(data.columns[i].replace("_deaths","")))=="Asia":
                c.append("red")
            elif LD.get("{}".format(data.columns[i].replace("_deaths","")))=="Africa":
                c.append("green")
            elif LD.get("{}".format(data.columns[i].replace("_deaths","")))=="North America":
                c.append("yellow")
            elif LD.get("{}".format(data.columns[i].replace("_deaths","")))=="South America":
                c.append("orange")
            elif LD.get("{}".format(data.columns[i].replace("_deaths","")))=="Oceania":
                c.append("blue")
            else:
                c.append("black")

            
    #print(LD)
    #print(c)

    #print(len(LD))
    #print(len(c))

    for i in range(1,len(data)):
        for j in range(1,len(data.columns)):
            name1="{}".format(data.columns.values[i].replace("_deaths",""))
            name2="{}".format(data.columns.values[j].replace("_deaths",""))
            G.add_edge(name1,name2,weight=round(data.iloc[i,j],2))

    pos = nx.spring_layout(G,k=1.2)
   
    #edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
    #nx.draw_networkx_edge_labels(G,pos)
    

    nx.draw_networkx(G,pos,node_color=c,edge_color="white")
    #nx.draw_networkx(G)
    plt.show()


DF_n_cases=my21.GetDF("new_cases.xlsx","new_cases")
DF_n_deaths=my21.GetDF("new_deaths.xlsx","new_deaths")
DF_n_locations=my21.GetDF("locations.xlsx","locations")
DF_n_locations.index=DF_n_locations.location
#print(DF_n_locations)


start="20200101"
end="20200720"

DFJapan=my15.getDF1503(DF_n_cases,DF_n_deaths,"Japan",start,end)
DFChina=my15.getDF1503(DF_n_cases,DF_n_deaths,"China",start,end)
DFUS=my15.getDF1503(DF_n_cases,DF_n_deaths,"United States",start,end)

DFTaiwan=my15.getDF1503(DF_n_cases,DF_n_deaths,"Taiwan",start,end)
DFKorea=my15.getDF1503(DF_n_cases,DF_n_deaths,"South Korea",start,end)

DFBrazil=my15.getDF1503(DF_n_cases,DF_n_deaths,"Brazil",start,end)
DFSweden=my15.getDF1503(DF_n_cases,DF_n_deaths,"Sweden",start,end)
DFSingapore=my15.getDF1503(DF_n_cases,DF_n_deaths,"Singapore",start,end)

DFCAR=my15.getDF1503(DF_n_cases,DF_n_deaths,"Central African Republic",start,end)
DFTurkey=my15.getDF1503(DF_n_cases,DF_n_deaths,"Turkey",start,end)

DFIceland=my15.getDF1503(DF_n_cases,DF_n_deaths,"Iceland",start,end)

DFGermany=my15.getDF1503(DF_n_cases,DF_n_deaths,"Germany",start,end)
DFItaly=my15.getDF1503(DF_n_cases,DF_n_deaths,"Italy",start,end)

DFWorld=my15.getDF1503(DF_n_cases,DF_n_deaths,"World",start,end)

##全ての国を分析する場合、こちらを実行
L=[]
for i in range(len(DF_n_cases.columns)):
    L.append(my15.getDF1503(DF_n_cases,DF_n_deaths,"{}".format(DF_n_cases.columns[i]),start,end))

#移動平均をとる
for i in range(1,len(L)):
    for j in range(len(L[i].columns)):
        L[i].iloc[:,j]=my21.GetRollingMean(my21.GetS(L[i],L[i].columns.values[j]),7)
        #print(L[i])

#10カ国くらいを分析する場合、こちらを実行

#L=[DFSingapore,DFWorld,DFJapan,DFChina,DFUS,DFBrazil,DFSweden,DFTaiwan,DFKorea,DFIceland,DFCAR,DFTurkey,DFGermany,DFItaly]

##移動平均をとる
#for i in range(len(L)):
#    for j in range(len(L[i].columns)):
#        L[i].iloc[:,j]=my21.GetRollingMean(my21.GetS(L[i],L[i].columns.values[j]),7)
#        #print(L[i])



##2.2の分析
##感染者と死者の相関係数を求める


#for i in range(len(L)):
  
#    df=my15.seriesPartCor((my21.GetS(L[i],"{}".format(L[i].columns.values[0]))),(my21.GetS(L[i],"{}".format(L[i].columns.values[1]))),30)
 
#    print(df)


#    ax=plt.gca()
    
#    ax.xaxis.set_major_locator(mpl.ticker.IndexLocator(30, 0))
#    ax.set_xlabel("date")
#    ax.set_ylabel("Correlation coefficient")
#    plt.plot(df.index,df.iloc[:])
#    plt.show()
#    my15.myPlot1504(L[i])
  
    

    



#2.3の分析
#A国とB国の感染者の相関係数を求める

#cases=pd.DataFrame()
#for i in range(len(L)):
#    #print(L[i].iloc[:,0])
#    cases=my21.GetDFfromS(cases,L[i].iloc[:,0])
    
#pd.set_option("display.max_columns",500)
##print(my21.GetCorr(cases))
##(my21.GetCorr(cases)).to_csv("相関係数.csv")
##my15.myPlot1505(L)

#DrowGraph2(my21.GetCorr(cases))


##全ての国を描画してみる
#cases=pd.DataFrame()
#for i in range(len(L)):
#    #print(L[i].iloc[:,0])
#    cases=my21.GetDFfromS(cases,L[i].iloc[:,0])
    
#pd.set_option("display.max_columns",500)
#print(my21.GetCorr(cases))
##(my21.GetCorr(cases)).to_csv("相関係数.csv")
##my15.myPlot1505(L)


#DrowGraph3cases(my21.GetCorr(cases))
##DrowGraph3deaths(my21.GetCorr(cases))



#人口を考慮した感染者数の比較


#国名とその人口を辞書に登録
jinkou={}
L2=[]
L3=[]
maxrate={}
maxint=0
maxint2=0
maxint3=0
maxint4=0
maxint5=0
max=""
max2=""
max3=""
max4=""
max5=""
##感染者数
#for i in range(len(L)):
#    #for j in range(len(L[i].columns)):
#    if "{}".format(L[i].columns[0].replace("_cases","")) in DF_n_locations.index.values:
#        st="{}".format(L[i].columns[0].replace("_cases",""))
#        jinkou["{}".format(L[i].columns[0].replace("_cases",""))]=DF_n_locations.loc[st,"population"]


#        ##人口そのものを算出する
#        #ser1=pd.Series(pd.array(L[i].iloc[:,0]),index=L[i].index,name=st)

#        #割合を算出する
#        ser1=pd.Series(pd.array(L[i].iloc[:,0])/jinkou.get("{}".format(L[i].columns[0].replace("_cases",""))),index=L[i].index,name=st)
        
#        #全ての国の感染者数をグラフに描画する
#        sert=pd.Series(ser1.index)
#        sert.index = pd.to_datetime(sert)
#        df1t=my21.GetDFfromS(sert,ser1)
#        df1t.index = pd.to_datetime(df1t.date)
#        maxrate["{}".format(L[i].columns[0].replace("_cases",""))]=df1t.iloc[:,1].max()
#        if maxrate["{}".format(L[i].columns[0].replace("_cases",""))]>maxint:
#            maxint5=maxint4
#            maxint4=maxint3
#            maxint3=maxint2
#            maxint2=maxint
#            maxint=maxrate["{}".format(L[i].columns[0].replace("_cases",""))]
#            max5=max4
#            max4=max3
#            max3=max2
#            max2=max
#            max="{}".format(L[i].columns[0].replace("_cases",""))
#        elif maxrate["{}".format(L[i].columns[0].replace("_cases",""))]>maxint2:
#            max5=max4
#            max4=max3
#            max3=max2
#            max2="{}".format(L[i].columns[0].replace("_cases",""))
#            maxint5=maxint4
#            maxint4=maxint3
#            maxint3=maxint2
#            maxint2=maxrate["{}".format(L[i].columns[0].replace("_cases",""))]
#        elif maxrate["{}".format(L[i].columns[0].replace("_cases",""))]>maxint3:
#            max5=max4
#            max4=max3
#            max3="{}".format(L[i].columns[0].replace("_cases",""))
#            maxint5=maxint4
#            maxint4=maxint3
#            maxint3=maxrate["{}".format(L[i].columns[0].replace("_cases",""))]
#        elif maxrate["{}".format(L[i].columns[0].replace("_cases",""))]>maxint4:
#            max5=max4
#            max4="{}".format(L[i].columns[0].replace("_cases",""))
#            maxint5=maxint4
#            maxint4=maxrate["{}".format(L[i].columns[0].replace("_cases",""))]
#        elif maxrate["{}".format(L[i].columns[0].replace("_cases",""))]>maxint5:
#            max5="{}".format(L[i].columns[0].replace("_cases",""))
#            maxint5=maxrate["{}".format(L[i].columns[0].replace("_cases",""))]
#        else:
#            pass
#        #print(df1t)




#        L3.append(df1t)
#        L2.append(ser1)

#死者数
#感染者数
for i in range(len(L)):
    #for j in range(len(L[i].columns)):
    if "{}".format(L[i].columns[1].replace("_deaths","")) in DF_n_locations.index.values:
        st="{}".format(L[i].columns[1].replace("_deaths",""))
        jinkou["{}".format(L[i].columns[1].replace("_deaths",""))]=DF_n_locations.loc[st,"population"]


        ##人口そのものを算出する
        #ser1=pd.Series(pd.array(L[i].iloc[:,0]),index=L[i].index,name=st)

        #割合を算出する
        ser1=pd.Series(pd.array(L[i].iloc[:,1])/jinkou.get("{}".format(L[i].columns[1].replace("_deaths",""))),index=L[i].index,name=st)
        
        #全ての国の感染者数をグラフに描画する
        sert=pd.Series(ser1.index)
        sert.index = pd.to_datetime(sert)
        df1t=my21.GetDFfromS(sert,ser1)
        df1t.index = pd.to_datetime(df1t.date)
        maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]=df1t.iloc[:,1].max()
        if maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]>maxint:
            maxint5=maxint4
            maxint4=maxint3
            maxint3=maxint2
            maxint2=maxint
            maxint=maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]
            max5=max4
            max4=max3
            max3=max2
            max2=max
            max="{}".format(L[i].columns[1].replace("_deaths",""))
        elif maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]>maxint2:
            max5=max4
            max4=max3
            max3=max2
            max2="{}".format(L[i].columns[1].replace("_deaths",""))
            maxint5=maxint4
            maxint4=maxint3
            maxint3=maxint2
            maxint2=maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]
        elif maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]>maxint3:
            max5=max4
            max4=max3
            max3="{}".format(L[i].columns[1].replace("_deaths",""))
            maxint5=maxint4
            maxint4=maxint3
            maxint3=maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]
        elif maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]>maxint4:
            max5=max4
            max4="{}".format(L[i].columns[1].replace("_deaths",""))
            maxint5=maxint4
            maxint4=maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]
        elif maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]>maxint5:
            max5="{}".format(L[i].columns[1].replace("_deaths",""))
            maxint5=maxrate["{}".format(L[i].columns[1].replace("_deaths",""))]
        else:
            pass
        #print(df1t)




        L3.append(df1t)
        L2.append(ser1)
#死者数の場合ここまで       


#ここから再開
print(maxrate)  
print(max)
print(max2)
print(max3)
print(max4)
print(max5)


my21.PlotMultipleG(L3)

#cases=pd.DataFrame()
#for i in range(len(L2)):
#    #print(L[i].iloc[:,0])
#    cases=my21.GetDFfromS(cases,L2[i].iloc[:])
#print(my21.GetCorr(cases))
#DrowGraph3deaths(my21.GetCorr(cases))