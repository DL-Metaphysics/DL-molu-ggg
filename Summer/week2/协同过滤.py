# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:24:53 2019

@author: 陌路放歌
"""

import random
import math
from operator import itemgetter


class ItemBasedCF():
    # 初始化参数
    def __init__(self):
        # 找到相似的20部电影，为目标用户推荐10部电影
        self.n_sim_movie = 20
        self.n_rec_movie = 10

        # 将数据集划分为训练集和测试集
        self.trainSet = {}
        self.testSet = {}

        # 用户相似度矩阵
        self.movie_sim_matrix = {}
        self.movie_popular = {}
        self.movie_count = 0

        print('Similar movie number = %d' % self.n_sim_movie)
        print('Recommneded movie number = %d' % self.n_rec_movie)


    # 读文件得到“用户-电影”数据，确定训练集，检验集
    def get_dataset(self, filename, pivot=0.75):#这个0.75有什么作用那？
        trainSet_len = 0#10万个样本中小于随机数0.75的个数，也就是说，
        #从样本中75%当做训练集，25%当做检验集
        
        testSet_len = 0
        m=0#
        for line in self.load_file(filename):
            m+=1
            
          
            user, movie, rating, timestamp = line.split(',')
            if(random.random() < pivot):
                self.trainSet.setdefault(user, {})
                self.trainSet[user][movie] = rating
                trainSet_len += 1
            else:
                self.testSet.setdefault(user, {})
                self.testSet[user][movie] = rating
                testSet_len += 1
      
        print('Split trainingSet and testSet success!')
        print('TrainSet = %s' % trainSet_len)
        print('TestSet = %s' % testSet_len)


    # 读文件，返回文件的每一行
    def load_file(self, filename):
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i == 0:  # 去掉文件第一行的title
                    continue
                yield line.strip('\r\n')
        print('Load %s success!' % filename)


    ###################计算电影之间的相似度，算法替换部分#####################
    def calc_movie_sim(self):
        for user, movies in self.trainSet.items():#训练集，一个用户评价过好多个
            
            #movies中含有 电影名 以及 评分 
            
            for movie in movies:
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                    #self.moive_popular  字典中有  [movie,次数] 
                    #创建一个新字典，里面有电影名字号，以及出现次数
                self.movie_popular[movie] += 1
            
                
        

        self.movie_count = len(self.movie_popular)##所有电影数量
        print("Total movie number = %d" % self.movie_count)

        for user, movies in self.trainSet.items():
            #测试集，以下部分是看过m1的所有用户的所有观影记录放在一个集合里，最后一行+=1是次数
            for m1 in movies:
                for m2 in movies:
                    if m1 == m2:#两个电影之间
                        continue
                    self.movie_sim_matrix.setdefault(m1, {})#也相当于键值对的添加
                    self.movie_sim_matrix[m1].setdefault(m2, 0)
                    
                    self.movie_sim_matrix[m1][m2] += 1  #matrix 是矩阵的意思,这句话是字典的意思，        
        
        print("Build co-rated users matrix success!")

        # 计算电影之间的相似性
        print("Calculating movie similarity matrix ...")
        
        for m1, related_movies in self.movie_sim_matrix.items():#电影 与所有评过分的电影：观影次数
            
            
            for m2, count in related_movies.items():#电影名号以及观影次数
                 
                
                
                # 注意0向量的处理，即某电影的用户数为0
                if self.movie_popular[m1] == 0  or  self.movie_popular[m2] == 0:
                    self.movie_sim_matrix[m1][m2] = 0 #0做分母会报错，所以这里考虑了0的情况
                else:#m1,m2两个电影的相似度，每两个电影之间的相似度
                    
                    
         ##############
                    self.movie_sim_matrix[m1][m2] =count/ math.sqrt(self.movie_popular[m1]*self.movie_popular[m2])
            
        
        
 
      
        ######self.movie_sim_matrix是吗我不知道#############
        print('Calculate movie similarity matrix success!')


    # 针对目标用户U，找到  K部相似的电影，并推荐其N部电影
    def recommend(self, user):
        K = self.n_sim_movie
        N = self.n_rec_movie
        rank = {}
        watched_movies = self.trainSet[user]
        
        for movie, rating in watched_movies.items():
            for related_movie, w in sorted(self.movie_sim_matrix[movie].items(), key=itemgetter(1), reverse=True)[:K]:
                if related_movie in watched_movies:
                    continue
                rank.setdefault(related_movie, 0)
                rank[related_movie] += w * float(rating)
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]

######
    # 产生推荐并通过准确率、召回率和覆盖率进行评估
    def evaluate(self):
        print('Evaluating start ...')
        N = self.n_rec_movie
        # 准确率和召回率
        hit = 0
        rec_count = 0
        test_count = 0
        # 覆盖率
        all_rec_movies = set()

        for i, user in enumerate(self.trainSet):
            test_moives = self.testSet.get(user, {})
            rec_movies = self.recommend(user)
        
            for movie, w in rec_movies:
                if movie in test_moives:
                    hit += 1
                all_rec_movies.add(movie)
            rec_count += N
            test_count += len(test_moives)
        print(rec_movies)
        precision = hit / (1.0 * rec_count)
        recall = hit / (1.0 * test_count)
        coverage = len(all_rec_movies) / (1.0 * self.movie_count)
        print('precisioin=%.4f\trecall=%.4f\tcoverage=%.4f' % (precision, recall, coverage))#准确率，站汇率，覆盖率率


if __name__ == '__main__':
    rating_file = 'C:\\Users\陌路放歌\Desktop\ml-latest-small\\ratings.csv'
    itemCF = ItemBasedCF()
    itemCF.get_dataset(rating_file)
    itemCF.calc_movie_sim()
    itemCF.evaluate()
