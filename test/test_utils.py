import pytest
import utils


def test_text_input() :
    
    assert type(utils.text_input(value = "test")) == str
     
 
def test_btn_meteo():
    print(utils.btn_meteo())
    assert utils.btn_meteo() == False
   
def dropdown_menu():
    output = utils.drop_down_menu(value = {"température" : 10,
                                         "humidité" : 25})
    assert type(output) == dict