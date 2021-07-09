import statistics
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import pandas as panda
import random 
import scipy.stats as stats
df = panda.read_csv("mediumData.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
print("Mean: "+ str(mean))

std = statistics.stdev(data)
print("Stdev: "+str(std))



def randMean(counter):
    dataset=[]
    for i in range(0,counter):
        randomMean = random.randint(0,len(data)-1)
        value = data[randomMean]
        dataset.append(value)
    mm = statistics.mean(dataset)
    
    return mm

def plotGraph(meanlist):
    df = meanlist
    
    print("df:"+str(df))
    fig = ff.create_distplot([data],["Reading Time"], show_hist = False)
    fig.add_trace(go.Scatter(x=[df,df],y=[0,.15],mode="lines",name = "New Mean"))

    std1 = mean-std
    print("Std1: "+str(std1))

    std01 = mean+std
    print("Std1: "+str(std01))
    std2 = mean-std*2
    print("Std1: "+str(std2))

    std02 = mean+std*2
    print("Std1: "+str(std02))

    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,.15],mode="lines",name = "Mean"))
    fig.add_trace(go.Scatter(x=[std1,std1],y=[0,.11],mode="lines",name = "Standard Deviation -1"))
    fig.add_trace(go.Scatter(x=[std01,std01],y=[0,.05],mode="lines",name = "Standard Deviation +1"))
    fig.add_trace(go.Scatter(x=[std02,std02],y=[0,.02],mode="lines",name = "Standard Deviation +2"))

    fig.show()
    
def setup():
    meanList = []
    
    for i in range(0,100):
        clap = randMean(30)
        meanList.append(clap)
    mofm = statistics.mean(meanList)
    plotGraph(mofm)
    zScore = (clap-mean)/std
    print("Z Score: "+str(zScore))  
setup()


