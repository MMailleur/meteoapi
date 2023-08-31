import pytest
from unittest.mock import Mock, patch
from app2 import find_current_weather, convert_to_celsius
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY= os.getenv("API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")

@pytest.fixture
def mock_requests_get():
    with patch('app2.requests.get') as mock_get:
        yield mock_get

def test_find_current_weather_success(mock_requests_get):
    # Create a mock response
    mock_response = Mock()
    mock_response.json.return_value = {
        'weather': [{'main': 'Cloudy'}],
        'main': {'temp': 298.15, 'temp_max': 301.15, 'feels_like': 295.15, 'humidity': 70},
        'coord': {'lat': 43.2134, 'lon': 2.3491}
    }
    mock_requests_get.return_value = mock_response

    # Call the function
    general, temperature, max_temperature, feels_temp, humidity, coords = find_current_weather('test_city')

    # Check the results
    assert general == 'Cloudy'
    assert temperature == 25
    assert max_temperature == 28
    assert feels_temp == 22
    assert humidity == 70
    assert coords == {'lat': 43.2134, 'lon': 2.3491}

# def test_find_current_weather_key_error(mock_requests_get):
#     # Create a mock response without the required keys
#     mock_response = Mock()
#     mock_response.json.return_value = {}
#     mock_requests_get.return_value = mock_response

#     # Call the function
#     with pytest.raises(SystemExit) as exc_info:
#         find_current_weather('non_existent_city')

#     # Check the exit code and message
#     assert exc_info.value.code == 1
