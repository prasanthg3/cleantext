import pytest
from cleantext import clean, clean_words
from cleantext.exceptions import CleanTextEmptyString


@pytest.mark.parametrize('text', ['This is A s$ample !!!! tExt3% to   cleaN566556+2+59*/133'])
def test_clean(text: str):
    """Test for clean function

    :param text: raw text
    :return:
    """

    assert clean(text) == 'sampl text clean'


@pytest.mark.parametrize('text', ['This is A s$ample !!!! tExt3% to   cleaN566556+2+59*/133'])
def test_clean_words(text: str):
    """Test for clean function

    :param text: raw text
    :return:
    """

    assert clean_words(text) == ['sampl', 'text', 'clean']


def test_empty_string():
    """Test for clean function

    :param text: raw text
    :return:
    """

    with pytest.raises(CleanTextEmptyString):
        clean('')
