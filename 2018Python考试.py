
# coding: utf-8

# In[8]:


def transfer():
    Temperature = input("输入带符号的温度(C/F):")
    if Temperature[-1] in ['F', 'f']:
        C = (eval(Temperature[0:-1]) - 32) / 1.8
        print("转换后的温度是{:.2f}C".format(C))
    elif Temperature[-1] in ['C', 'c']:
        F = eval(Temperature[0:-1]) * 1.8 + 32
        print("转换后的温度是{:.2f}F".format(F))
    else:
        print("输入错误")
transfer()        


# In[9]:


import re

# 第一题(匹配百度网址)
url = 'http://www.baidu.com'
re.match(r'http:\/\/www\.baidu\.com', url).group()


# In[10]:


# 第二题(匹配基因序列中长度为5的有重复的序列)

gene = 'ATCCCATCGATTACGGAGCGTATCAATAGCTAATCCC'
re.search(r'([ATCG]{5}).*\1', gene).group(1)
# 返回的字符串为有重复的基因序列


# In[11]:


# 第三题  (匹配长度为5的回文碱基序列)

gene = 'ATCCCATCGATTACGGAGCGTATCAATAGCTAATCCC'
re.search(r'([ATCG])([ATCG])([ATCG])([ATCG])([ATCG]).*\5\4\3\2\1', gene).group()
# 返回的字符串开头五个和结尾五个是回文碱基序列


# In[12]:


# 第四题(匹配 UGC 或 UGU)
gene = 'AUCGAUGCAUUUCACACAUAGUCUGCAUUUCCCAAAUCUAUCUAUCGUGGAUCAAUCUAUCUAGCAUGUCAC'
re.findall(r'UG[UC]', gene)


# In[3]:


class Gene(object):
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def tell(self):
        print("基因名称: " + self.name)
        print("基因ID: " + str(self.ID))
class NonCodingGene(Gene):
    def __init__(self, name, ID, a):     # a属性为非编码基因的特有属性，具体看是字符串还是数字
        super(NonCodingGene, self).__init__(name, ID)
        self.a = a
    def tell(self):
        super(NonCodingGene, self).tell()
        print ("a: " + a)              #  a如果是数字  后面的a 就是  str(a) 
class CodingGene(Gene):
    def __init__(self, name, ID, b):   #  b同a
        super(CodingGene, self).__init__(name, ID)
        self.b = b
    def tell(self):
        super(CodingGene, self).tell()
        print ("b: " + b)    
# 创建3个实例
gene1 = Gene('A', 1)
gene2 = NonCodingGene('B',2,'a')
gene3 = CodingGene('C', 3, 'b')
gene1.tell()
gene2.tell()
gene3.tell()

