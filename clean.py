import nltk
import re
import string
ps=nltk.PorterStemmer()

def clean(text,all=False, extra_spaces=False, stemming=False, stopwords=False,lowercase=False, numbers=False, punct=False, stp_lang='english'):
	
	stopwords = nltk.corpus.stopwords.words(stp_lang)
	
	if text=None:
		text=''
	text=str(text)
	
	if all:
		text=text.strip(' ')
		text = "".join([word.lower() for word in text if word not in string.punctuation])
		tokens = re.split('\W+', text)
		text = "".join([ps.stem(word) for word in tokens if word not in stopwords])
		return text

	else:
		if lowercase:
			text = text.lower()
		if numbers:
			text =re.sub("\d+", "", text)
		if punct:
			text = "".join([word for word in text if word not in string.punctuation])
		if stemming:
			text=re.split(" ",text)
			text=" ".join([ps.stem(word) for word in text])
		if stopwords:
			text=re.split(" ",text)
			text=" ".join([word for word in text if word not in stopwords])
		if extra_spaces:
			text=text.strip(' ')
		return text
		