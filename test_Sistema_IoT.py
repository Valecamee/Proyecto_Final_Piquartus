import pytest
from unittest.mock import MagicMock, patch
from grovepi import *
from Sistema_IoT import *

@pytest.fixture(autouse=True)
def mock_dependencies():

    patch_analogRead = patch('grovepi.analogRead', MagicMock(return_value=500))
    patch_digitalRead = patch('digitalRead', MagicMock(return_value=1))
    patch_dht = patch('dht', MagicMock(return_value=[25, 50]))  # Mocking temperature and humidity values
    with patch_analogRead, patch_digitalRead, patch_dht:
        yield

def test_button_status():
    # Call the function you want to test
    result = collect_sensor_data()

    # Perform assertions to check the expected behavior
    assert result == expected_result

    # Check if the mocked functions were called with the expected arguments
    grovepi.digitalRead.assert_called_once_with(button)

# Add more test cases for other functions or scenarios

if __name__ == '__main__':
    pytest.main()