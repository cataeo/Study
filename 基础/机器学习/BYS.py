from numpy import *
#%%
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec
word_test, kind = loadDataSet()
print(kind)
#%%

#%%
def createVocabList(dataSet):
    #创建词汇表：利用集合结构内元素的唯一性，创建一个包含所有词汇的词表。
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)
vacabList_test = createVocabList(word_test)
print(vacabList_test[:10])
#%%

#%%
def setOfWords2Vec(vocabList, inputSet):
    #把输入文本根据词表转化为计算机可处理的01向量形式
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print ("the word: %s is not in my Vocabulary!" % word)
    return returnVec
texts_test = []
for text_test in word_test:
    texts_test.append(setOfWords2Vec(vacabList_test, text_test))
print(texts_test)
#%%

#%%
def trainNB0(trainMatrix,trainCategory):
    #在训练样本中计算先验概率 p(Ci) 和 条件概率 p(x,y | Ci)，本实例有0和1两个类别，所以返回p(x,y | 0)，p(x,y | 1)和p(Ci)。 trainMatrix:文本词向量，trainCategory：分类s
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)  #
    p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
    p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:        
            p1Num += trainMatrix[i]  #统计类别为1的各单词出现的总次数
            p1Denom += sum(trainMatrix[i])  #统计类别为1的总单词书
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()

    return p0Vect,p1Vect,pAbusive

p0, p1 ,pA = trainNB0(texts_test, kind)
#%%

#%%
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    # 分类：根据计算后，哪个类别的概率大，则属于哪个类别
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
#%%


#%%
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(thisDoc)
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
testingNB()
#%%