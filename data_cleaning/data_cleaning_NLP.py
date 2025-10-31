text = "Salman Md Sultan"

print(text.lower())

#tokenization

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt_tab')

tokens = word_tokenize(text)
print(tokens)

nltk.download('stopwords')

# Get English stopwords
english_stopwords = stopwords.words('english')

# Print all stopwords
print(english_stopwords)

# Optional: print total count
print("\nTotal stopwords:", len(english_stopwords))

stop_words = set(stopwords.words('english'))

custom_words = ['please', 'thank', 'hello', 'example']
stop_words.update(custom_words)

# Print some examples
print("Total stopwords:", len(stop_words))
print("Sample stopwords:", list(stop_words)[:20])

text1 = ['i','love','nlp','task']
new_text = []
for i in text1:
    if i not in stop_words:
        new_text.append(i)
print(new_text)

#stemming: running ->run
#Studies -> 

from nltk.stem import PorterStemmer,WordNetLemmatizer


stem = PorterStemmer()
words= ['running','studies']
stem_w = []
for i in words:
    stem_w.append(stem.stem(i))
print(stem_w)

lem = WordNetLemmatizer()
nltk.download('wordnet')
for i in words:
    stem_w.append(lem.lemmatize(i))
print(stem_w)

#task: space removal
#task: punctuation removal
#contaction expansion: i don't-> i do not
#spell correction
#duplicate value handling
#outlier removal
#data type conversion