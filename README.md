# cleantext

[![Downloads](https://static.pepy.tech/personalized-badge/cleantext?period=month&units=international_system&left_color=grey&right_color=green&left_text=Downloads/month)](https://pepy.tech/project/cleantext)

**cleantext** is a an open-source python package to clean raw text data. Source code for the library can be found [here.](https://github.com/prasanthg3/cleantext)



## Features 

cleantext has two main methods,
* **clean**: to clean raw text and return the cleaned text
* **clean_words**: to clean raw text and return a list of clean words

cleantext can apply all, or a selected combination of the following cleaning operations:
* Remove extra white spaces
* Convert the entire text into a uniform lowercase
* Remove digits from the text
* Remove punctuations from the text
* Remove or replace the part of text with custom regex
* Remove stop words, and choose a language for stop words
( Stop words are generally the most common words in a language with no significant meaning such as is, am, the, this, are etc.)
* Stem the words
(Stemming is a process of converting words with similar meaning into a single word. For example, stemming of words run, runs, running will result run, run, run)

## Installation

cleantext requires [Python 3](https://www.python.org/downloads/) and [NLTK](http://www.nltk.org/install.html) to execute. 

To install using pip, use

`pip install cleantext`

## Usage

* **Import the library**:

``` python
import cleantext
```

* **Choose a method:**

 To return the text in a string format, 
 
``` python
cleantext.clean("your_raw_text_here") 
```
 
 To return a list of words from the text,
 
``` python
cleantext.clean_words("your_raw_text_here") 
```
 
 To choose a specific set of cleaning operations,

``` python
cleantext.clean_words("your_raw_text_here",
clean_all= False # Execute all cleaning operations
extra_spaces=True ,  # Remove extra white spaces 
stemming=True , # Stem the words
stopwords=True ,# Remove stop words
lowercase=True ,# Convert to lowercase
numbers=True ,# Remove all digits 
punct=True ,# Remove all punctuations
reg: str = '<regex>', # Remove parts of text based on regex
reg_replace: str = '<replace_value>', # String to replace the regex used in reg
stp_lang='english'  # Language for stop words
)
```

## Examples

``` python
import cleantext
cleantext.clean('This is A s$ample !!!! tExt3% to   cleaN566556+2+59*/133', extra_spaces=True, lowercase=True, numbers=True, punct=True)
```

returns,

``` Python
'this is a sample text to clean'
```

----

``` Python
import cleantext
cleantext.clean_words('This is A s$ample !!!! tExt3% to   cleaN566556+2+59*/133')
```

returns,

``` Python
['sampl', 'text', 'clean']
```

----

``` Python
import cleantext
text = "my id, name1@dom1.com and your, name2@dom2.in"
clean(text, reg=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", reg_replace='email', clean_all=False)

```

returns,

``` Python
"my id, email and your, email"
```

## License

##### MIT

For any questions, issues, bugs, and suggestions please visit [here](https://github.com/prasanthg3/cleantext/issues)
