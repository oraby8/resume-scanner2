import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import textdistance as td

stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def scan(seg_list01,seg_list02):
    try:

        item01_list = re.sub('[^a-zA-Z]',' ',seg_list01)
        item01 =item01_list.lower().split()
        item01=[word for word in item01 if not word in stopwords]

        item02_list = re.sub('[^a-zA-Z]',' ',seg_list02)
        item02 =item02_list.lower().split()
        item02=[word2 for word2 in item02 if not word2 in stopwords]

        documents = [item01, item02]

        count_vectorizer = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)
        sparse_matrix = count_vectorizer.fit_transform(documents)

        doc_term_matrix = sparse_matrix.todense()
        df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=['item01', 'item02'])

        answer = cosine_similarity(df, df)
        answer = pd.DataFrame(answer)
        answer = answer.iloc[[1],[0]].values[0]
        answer = round(float(answer),4)*100
    except:
        answer=0
    return answer

def scan2(seg_list01,seg_list02):
	item01_list = re.sub('[^a-zA-Z]',' ',seg_list01)
	item01 =item01_list.lower().split()
	item01=[word for word in item01 if not word in stopwords]
	resume=' '.join(item01)

	item02_list = re.sub('[^a-zA-Z]',' ',seg_list02)
	item02 =item02_list.lower().split()
	item02=[word for word in item02 if not word in stopwords]
	job_des=' '.join(item02)

	j = td.jaccard.similarity(resume, job_des)
	s = td.sorensen_dice.similarity(resume, job_des)
	c = td.cosine.similarity(resume, job_des)
	o = td.overlap.normalized_similarity(resume, job_des)
	total = (j+s+c+o)/4
    # total = (s+o)/2
	return total*100
