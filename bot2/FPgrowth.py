
import csv
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}
 
    def inc(self, numOccur):
        self.count += numOccur
 
    def disp(self, ind=1):
#        print(' ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)
def createTree(dataSet,minSup=1):
    # 统计每个项目出现的次数
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item,0)+dataSet[trans]
 
    #支持度小于要求的删去。
    for k in list(headerTable.keys()):
        if headerTable[k] < minSup:
            del(headerTable[k])
 
    #构造频繁1项集，若集合为空，则返回空树
    freqItemSet = set(headerTable.keys())
    if len(freqItemSet)==0:
        return None,None
 
    #将headerTable扩展一维，一维存放各个事件频数的同时，另一维存放该事件第一个节点的指针
    for k in headerTable:
        headerTable[k] = [headerTable[k],None]
 
    #创建树根
    retTree = treeNode('Null Set',1,None)
 
    #枚举数据中每次评价tranSet 和它出现的次数 count
    #对于每个清单，从中选择频繁的事物放入字典localID
    #对localID字典中键值按照频繁程度由大到小排序后放入列表orderedItem
    #通过updateTree将orderedItem中事件更新到树上
    
    for tranSet,count in dataSet.items():
        localID = {}
        for item in tranSet:
            if item in freqItemSet:
                localID[item] = headerTable[item][0]
        if len(localID) > 0:
            orderedItem = [v[0] for v in sorted(localID.items(),key=lambda p:p[1],reverse=True)]
            updateTree(orderedItem,retTree,headerTable,count)
 
    #返回结果
    return retTree,headerTable

def updateTree(items,inTree,headerTable,count):
 
    #采用递归的方式，对清单内逐个元素进行处理
    #如果列表内当前节点在fp树当前位置的孩子列表里，只需让对应孩子节点计数加count
    #否则需要新增一个孩子节点，并且需要修改链表
    #递归处理下一个元素
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = treeNode(items[0],count,inTree)
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1],inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::],inTree.children[items[0]],headerTable,count)

def updateHeader(nodeToTest,targetNode):
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

def ascendTree(leafNode,prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent,prefixPath)

def findPrefixPath(basePat,treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode,prefixPath)
        if len(prefixPath) > 1:
             condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats
 

def mineTree(inTree,headerTable,minSup,preFix,freqItemList):
 
    #将当前事物按频繁程度排序后放入列表bigL
    bigL = [v[0] for v in sorted(headerTable.items(),key=lambda p: str(p[1]))]
 
    #枚举每个事物，将其固定到前缀，然后执行fp递归算法
    for basePat in bigL:
        newFreSet = preFix.copy()
        newFreSet.add(basePat)
        freqItemList.append(newFreSet)
        condpattBases = findPrefixPath(basePat,headerTable[basePat][1])
        myCondTree,myHead = createTree(condpattBases,minSup)
        if myHead != None:            #打印各模式基的fp树
#            print('condition tree for: ',newFreSet)
            myCondTree.disp(1)
            mineTree(myCondTree,myHead,minSup,newFreSet,freqItemList)
def loadSimpData():
    simpDat = []
    return simpDat
 
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1  #retDict.get(frozenset(trans),0)
    return retDict
 

def transData(dataSet):
    retDict = {}
    (m,n) = dataSet.shape
#    print(m,n)
    for i in range(m):
        st=set([])
        for j in range(n):
            if dataSet[i][j] == True:
                st.add(j)
        retDict[frozenset(st)] = retDict.get(frozenset(st),0)+1
    return retDict
 

def associationAnalysis(dataSet,T):
#    print(dataSet)
    myFPtree, myHeaderTab = createTree(dataSet, T)
    if(type(myFPtree) == None):
        return []
    freqItems = []
    mineTree(myFPtree, myHeaderTab,T, set([]), freqItems)
 
    ans = []
    for i in freqItems:
        if len(i) > 1:
            ans.append(i)
    return ans




with open('user_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = reader = csv.reader(csvfile)
    lst1 = [];
    lst2 = [];
    lst3 = [];
    for row in reader:
        if row[0]=='1 'and row[26]=='1':
            lst1.append(row[1:-1])
        elif row[0]=='2 ' and row[26]=='1':
            lst2.append(row[1:-1])
        elif row[0]=='3 'and row[26]=='1':
            lst3.append(row[1:-1])
#    品牌1
    simpDat = lst1
    initSet = createInitSet(simpDat)
    myFPtree,myHeaderTab = createTree(initSet,4)
    print(type(myHeaderTab))
    #myFPtree.disp()
    #print(findPrefixPath('r',myHeaderTab['r'][1]))
    freqItems1 = []
    mineTree(myFPtree,myHeaderTab,4,set([]),freqItems1)
    print(freqItems1)
#    品牌2
    simpDat = lst2
    initSet = createInitSet(simpDat)
    myFPtree,myHeaderTab = createTree(initSet,4)
    print(type(myHeaderTab))
    #myFPtree.disp()
    #print(findPrefixPath('r',myHeaderTab['r'][1]))
    freqItems2 = []
    mineTree(myFPtree,myHeaderTab,4,set([]),freqItems2)
    print(freqItems2)
#    品牌3
    simpDat = lst3
    initSet = createInitSet(simpDat)
    myFPtree,myHeaderTab = createTree(initSet,4)
    print(type(myHeaderTab))
    #myFPtree.disp()
    #print(findPrefixPath('r',myHeaderTab['r'][1]))
    freqItems3 = []
    mineTree(myFPtree,myHeaderTab,4,set([]),freqItems3)
    print(freqItems3)













