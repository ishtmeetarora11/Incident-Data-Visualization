import pytest
import urllib.request
from unittest.mock import patch, MagicMock
from fetchincidents import fetchIncidents

@patch('urllib.request.urlopen')
def test_fetch_incidents_with_headers(mock_urlopen):
    mock_response = MagicMock()
    mock_response.read.return_value = b"Ishtmeet"

    mock_urlopen.return_value = mock_response

    test_url = "http://example.com/test"

    result = fetchIncidents(test_url)

    request_args, _ = mock_urlopen.call_args
    request = request_args[0]

    assert isinstance(request, urllib.request.Request)
    assert request.full_url == test_url

    assert result == b"Ishtmeet"