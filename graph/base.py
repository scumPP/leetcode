
class Graph_AdMatrix:
    def __init__(self,vertex,edge,num_vertex,num_egde):
        self.vertex=[0 for _ in range(10)]  ##顶点表
        self.edge=[[0 for _ in range(10)] for _ in range(10)]
        self.num_vertex=num_vertex
        self.num_egde=num_egde


class ArcNode:
    def __init__(self,vertex,nextArc):
        self.vertex=vertex ##如果是有向图，就是指向谁
        self.nextArc=nextArc

class VerNode:
    def __init__(self,vertex,nextVer):
        self.vertex=vertex
        self.nextVer=nextVer

class Graph_AdList:
    def __init__(self,vernum,arcnum):
        vernode=VerNode(0,None)
        self.AdList=[vernode for _ in range(vernum)]
        self.arcnum=arcnum
        self.vernum=vernum
    
    def createGraph(self):
        


if __name__ == "__main__":
    vertex=[1,2,3,4,5,6]
    edge=[
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [1,0,0,0,0,1],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [1,0,0,0,1,0]
    ]
    num_vertex=6
    num_edge=9
    g=Graph_AdMatrix(vertex,edge,num_vertex,num_edge)   


    


