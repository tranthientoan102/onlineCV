import random
from math import sqrt

import pandas
import seaborn as sns
import matplotlib.pyplot as plt

# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
# plt.style.use('seaborn-whitegrid')

class KMeans:
    def __init__(self,k):
        self.K = k
        self.cluster = list(map(lambda x: [], range(self.K)))
        self.centroid = list(map(lambda x: (), range(self.K)))
        self.data = []
        self.round = -1

    def fit(self, data):
        self.data = data
        self.__init()
        keepGoing = True

        while (keepGoing):
            keepGoing = self.__fittingProcess()
            plotCurrentState(self)

        return self.cluster
    def __init(self):
        for cid in range(self.K):
            val = random.choice(self.data)
            self.cluster[cid].append(val)
            self.data.remove(val)
            print(f'init: {val} -> cluster[{cid}]')

        self.__calcCentroid()

    def __calcCentroid(self):
        for id in range(self.K):
            result = [0] * len(self.cluster[id][0])
            for i in range(len(result)):
                result[i] = sum(map(lambda x: x[i], self.cluster[id]))/len(self.cluster[id])
            self.centroid[id] = tuple(x for x in result)
        # return result
    def __calcDistance_pointToClusterCentroid(self, point, centroid):
        result = 0.0
        for i in range(len(centroid)):
            result += (point[i] - centroid[i]) **2
        return sqrt(result)

    # def test_calcDistance(self,point, centroid):
    #     return self.__calcDistance_pointToClusterCentroid(point, centroid)

    def __fittingProcess(self)->bool:
        """


        :return: continue indicator
        """
        self.round +=1
        if len(self.data) >0:
            for point in self.data:
                distance = []
                for clusterId in range(len(self.cluster)):
                    distance.append((clusterId
                                     , self.__calcDistance_pointToClusterCentroid(point,self.centroid[clusterId]))
                                    )
                # distance = {k:v for k,v in sorted(distance.items(), key = lambda x: x[1])}
                distance = sorted(distance, key= lambda x: x[1])
                self.cluster[distance[0][0]].append(point)
            self.data = []
            self.__calcCentroid()
            return True
        else:
            for clusterId in range(len(self.cluster)):
                for point in self.cluster[clusterId]:
                    distance = []
                    for centroidId in range(len(self.centroid)):
                        d = self.__calcDistance_pointToClusterCentroid(point, self.centroid[centroidId])
                        distance.append((point, centroidId, d))
                    distance = sorted(distance, key = lambda x: x[2])
                    refDis = self.__calcDistance_pointToClusterCentroid(point, self.centroid[clusterId])
                    if distance[0][2].__lt__(refDis):
                        self.cluster[distance[0][1]].append(distance[0][0])
                        self.cluster[clusterId].remove(distance[0][0])
                        self.__calcCentroid()
                        return True
            return False
    def __calcDistanceToCluster(self, point):
        pass

def plotCurrentState(km):
    result = []
    result2 =[]
    for cid in range(len(km.cluster)):
        for x in km.cluster[cid]:
            result.append((x[0], x[1], cid, 0))
        result2.append((km.centroid[cid][0],km.centroid[cid][1],cid,1))

    df = pandas.DataFrame(result, columns=['X','Y','id','isCentroid'])
    df2 = pandas.DataFrame(result2, columns=['X','Y','id','isCentroid'])

    # plt.

    sns.scatterplot(x='X', y='Y', data=df, hue='id',style='id', palette='viridis')
    sns.scatterplot(x='X', y='Y', data=df2, marker='D', s=50)

    plt.xlim((0,11))
    plt.ylim((0,11))
    plt.savefig(f'./fig/{km.round}.png')
    plt.show()

if __name__ == '__main__':
    km = KMeans(4)


    input = list(map(lambda _: (random.random()*10,random.random()*10), range(100)))
    # input = [[1],[2],[4],[5],[8],[9],[10]]
    print(f'{input=}')
    km.fit(input)
    print(f'{km.cluster=}')
    print(f'{km.data=}')
    print(f'{km.centroid=}')

    # result = []
    # result2 =[]
    # for cid in range(len(km.cluster)):
    #     for x in km.cluster[cid]:
    #         result.append((x[0], x[1], cid, 0))
    #     result2.append((km.centroid[cid][0],km.centroid[cid][1],cid,1))
    #
    # df = pandas.DataFrame(result, columns=['X','Y','id','isCentroid'])
    # df2 = pandas.DataFrame(result2, columns=['X','Y','id','isCentroid'])
    # sns.scatterplot(x='X', y='Y', data=df, hue='id', palette='viridis')
    # sns.scatterplot(x='X', y='Y', data=df2, marker='D', s=200)
    #
    # plt.show()

    a = [0,3,1]
    b = None
    c = [0]*3
    print(sorted(a))
