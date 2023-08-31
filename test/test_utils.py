import pytest
import utils


def test_text_input() :
    
    assert type(utils.text_input(value = "test")) == str
     
 
def test_btn_meteo():
    print(utils.btn_meteo())
    assert utils.btn_meteo() == False
   