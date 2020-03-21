import string
from nltk.corpus import stopwords
from library import clean_text_simple, GraphOfWordsUtils

stpwds = stopwords.words('english')
punct = string.punctuation.replace('-', '')

my_doc = '''A method for solution of systems of linear algebraic equations 
with m-dimensional lambda matrices. A system of linear algebraic 
equations with m-dimensional lambda matrices is considered. 
The proposed method of searching for the solution of this system 
lies in reducing it to a numerical system of a special kind.'''

my_doc = my_doc.replace('\n', '')

# pre-process document
my_tokens = clean_text_simple(my_doc,my_stopwords=stpwds,punct=punct, remove_stopwords=False, stemming=True, pos_filtering=False)
                              
gow = GraphOfWordsUtils()
graph = gow.convert_terms_to_graph(my_tokens, w=4)

keywords = gow.get_main_core_keywords(graph, weighted=True)
print(keywords)
