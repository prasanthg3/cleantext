import pytest
from cleantext import clean, clean_words
from cleantext.exceptions import CleanTextEmptyString


@pytest.mark.parametrize('text', ["This is 'A s$ample, !!!! tExt3% to   cleaN566556+2+59*/133"])
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
    :return:
    """

    with pytest.raises(CleanTextEmptyString):
        clean('')


@pytest.mark.parametrize('text', ["SAMple 23TeXt"])
def test_case(text: str):
    assert clean(text, lowercase=True) == "sample 23text"


@pytest.mark.parametrize('text', ["SAMple    23Te  Xt"])
def test_spaces(text: str):
    assert clean(text, extra_spaces=True) == "SAMple 23Te Xt"


@pytest.mark.parametrize('text', ["Sam4789ple to 345rem1ove 5nu534m2bers"])
def test_reg(text: str):
    assert clean(text, reg=r'\d', clean_all=False) == "Sample to remove numbers"


@pytest.mark.parametrize('text', ["my id, name1@dom1.com and your, name2@dom2.in"])
def test_reg_1(text: str):
    assert clean(text, reg=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", reg_replace='email',
                 clean_all=False) == "my id, email and your, email"


@pytest.mark.parametrize('text', ["my id, name1@dom1.com and your, name2@dom2.in"])
def test_reg_list(text: str):
    assert clean_words(text, reg=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", reg_replace='email') == ['id', 'email',
                                                                                                      'email']


@pytest.mark.parametrize('text', ["my id: name1@dom1.com and your id: name2@dom2.in"])
def test_reg_list(text: str):
    assert clean_words(text, reg=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",
                       clean_all=False) == ['my', 'id:', 'and', 'your', 'id:']
