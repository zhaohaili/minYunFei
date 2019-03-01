# encoding:utf-8 
import math
import sys


class YunFei:
    def __init__(self):
        pass
    @classmethod
    def minWeight(cls,
                   price1='',
                   price2='',
                   price3='',
                   weight1='',
                   weight2='',
                   weight3='',
                   weighttotal=''):

        #单价
        price1 = price1
        price2 = price2
        price3=  price3
        #载重
        weight1=weight1
        weight2=weight2
        weight3=weight3
        #交接单总重量
        weighttotal=weighttotal
        chexing1=list(range(int(math.ceil(float(weighttotal.strip())/float(weight1.strip()))+1)))
        chexing2=list(range(int(math.ceil(float(weighttotal.strip())/float(weight2.strip()))+1)))
        chexing3=list(range(int(math.ceil(float(weighttotal.strip())/float(weight3.strip()))+1)))
        listweight=[]
        list1=[]
        list2=[]
        list3=[]
        for i in chexing1:
            for j in chexing2:
                for m in chexing3:
                    if(i==0):
                        chexing1price=0
                    else:
                        chexing1price=i*float(price1)
                    if(j==0):
                        chexing2price=0
                    else:
                        chexing2price=j*float(price2)
                    if(m==0):
                        chexing3price=0
                    else:
                        chexing3price=m*float(price3)
                    if(i*float(weight1)+j*float(weight2)+m*float(weight3)>=float(weighttotal)):
                        listweight.append(chexing1price+chexing2price+chexing3price)
                        list1.append(i)
                        list2.append(j)
                        list3.append(m)
        print('最小运费为:'+str(min(listweight)))
        print('车型1数量为：'+str(list1[listweight.index(min(listweight))]))
        print('车型2数量为：'+str(list2[listweight.index(min(listweight))]))
        print('车型3数量为：'+str(list3[listweight.index(min(listweight))]))
        # print((u'最小运费为:').encode('gbk')+str(min(listweight)))
        # print((u'车型1数量为：').encode('gbk')+str(list1[listweight.index(min(listweight))]))
        # print((u'车型2数量为：').encode('gbk')+str(list2[listweight.index(min(listweight))]))
        # print((u'车型3数量为：').encode('gbk')+str(list3[listweight.index(min(listweight))]))



if __name__ == '__main__':
    YunFei.minWeight(price1=sys.argv[1],
                      price2=sys.argv[2],
                      price3=sys.argv[3],
                      weight1=sys.argv[4],
                      weight2=sys.argv[5],
                      weight3=sys.argv[6],
                      weighttotal=sys.argv[7])
