import pytest
import utils
from utils import *
from unittest.mock import patch
import unittest
from io import BytesIO


def test_text_input() :

    assert type(utils.text_input(value = "test")) == str




 # Test de la fonction get_weather_data pour le cas réussi
@patch("os.getenv", return_value="mocked_api_key")
@patch("requests.get")
def test_get_weather_data_successful(mock_requests_get, mock_getenv):
    # Configuration des mocks
    mock_response = unittest.mock.Mock()
    mock_response.json.return_value = {
        "cod": 200,
        "coord": {"lon": 10, "lat": 20}
    }
    mock_requests_get.return_value = mock_response

    # Appel de la fonction à tester
    result = get_weather_data("Paris")

    # Assertions
    assert result == (10, 20)  # Vérifiez que les coordonnées sont renvoyées correctement
    mock_getenv.assert_called_once_with("API_KEY")
    mock_requests_get.assert_called_once_with("https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=mocked_api_key")



# def test_btn_meteo():

#     assert utils.btn_meteo() == False

# def test_dropdown_menu():
#     output = utils.drop_down_menu(value = {"température" : 10,
#                                          "humidité" : 25})

#     assert type(output) == dict
