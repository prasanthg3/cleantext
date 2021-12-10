"""cleantext"""
import re
import string
import nltk
from nltk.corpus import stopwords as sw

from .exceptions import CleanTextEmptyString

ps = nltk.PorterStemmer()


def clean(text: str,  # pylint: disable=too-many-arguments, too-many-branches
          clean_all: bool = True,
          extra_spaces: bool = False,
          stemming: bool = False,
          stopwords: bool = False,
          lowercase: bool = False,
          numbers: bool = False,
          punct: bool = False,
          reg: str = '',
          reg_replace: str = '',
          stp_lang: str = 'english') -> str:
    """Given a raw string, return cleaned text

    :param text: Input text to clean
    :param clean_all: Execute all cleaning operations
    :param extra_spaces: Remove extra white spaces
    :param stemming: Stem the words
    :param stopwords: Remove stop words
    :param lowercase: Convert to lowercase
    :param numbers: Remove all digits
    :param punct: Remove all punctuations
    :param reg: Regular expression for removing or replacing
    :param reg_replace: Replace the part with regular expression(reg)
    :param stp_lang: Language for stop words
    :return: Cleaned text
    """
    if clean_all is True:
        active_actions = [k for k, v in locals().items() if k != 'clean_all' and v is True]
        if len(active_actions) > 0:
            clean_all = False

    try:
        stop_words = sw.words(stp_lang)
    except LookupError:
        nltk.download('stopwords')
    finally:
        stop_words = sw.words(stp_lang)

    if not text:
        raise CleanTextEmptyString("No text is provided to clean")

    if reg != '':
        text = re.sub(reg, reg_replace, text)

    if clean_all:
        while '  ' in text.strip():
            text = text.replace("  ", " ")
        text = "".join([word.casefold() for word in text
                        if word not in string.punctuation])
        text = "".join([_ for _ in text if not _.isdigit()])
        tokens = text.split()
        text = " ".join([ps.stem(word) for word in tokens
                         if word not in stop_words])
        return text.strip()

    if extra_spaces:
        while '  ' in text.strip():
            text = text.replace("  ", " ")
    if lowercase:
        text = text.casefold()
    if numbers:
        text = "".join([_ for _ in text if not _.isdigit()])
    if punct:
        text = "".join([word for word in text
                        if word not in string.punctuation])

    if stopwords:
        text = text.split()
        text = " ".join([word for word in text if word not in stop_words])
    if stemming:
        text = text.split()
        text = " ".join([ps.stem(word) for word in text])

    return text.strip()


def clean_words(text: str,  # pylint: disable=too-many-arguments
                clean_all: bool = True,
                extra_spaces: bool = False,
                stemming: bool = False,
                stopwords: bool = False,
                lowercase: bool = False,
                numbers: bool = False,
                punct: bool = False,
                reg: str = '',
                reg_replace: str = '',
                stp_lang: str = 'english') -> list:
    """Given a raw string, return list of clean words

    :param text: Input text to clean
    :param clean_all: Execute all cleaning operations
    :param extra_spaces: Remove extra white spaces
    :param stemming: Stem the words
    :param stopwords: Remove stop words
    :param lowercase: Convert to lowercase
    :param numbers: Remove all digits
    :param punct: Remove all punctuations
    :param reg: Regular expression for removing or replacing
    :param reg_replace: Replace the part with regular expression(reg)
    :param stp_lang: Language for stop words
    """
    text = clean(text, clean_all, extra_spaces, stemming, stopwords, lowercase,
                 numbers, punct, reg, reg_replace, stp_lang)

    return text.split()
