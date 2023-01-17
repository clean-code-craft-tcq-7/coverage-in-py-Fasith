import pytest

from src.alert_transmitter import AlertTransmitter


alertTargets = ["TO_EMAIL", "TO_CONTROLLER"]

@pytest.fixture(params=alertTargets)
def alert_transmitter_test_data(request):
    return (AlertTransmitter(request.param), request.param)


def test_AlertTransmitter_initialization(alert_transmitter_test_data):
    alert_transmitter, alertTarget = (alert_transmitter_test_data)
    assert alert_transmitter.alertTarget == alertTarget


def test_AlertTransmitter_set_alerter_function(alert_transmitter_test_data):
    alert_transmitter, alertTarget = (alert_transmitter_test_data)
    output_alerter_function_name = alert_transmitter.alerter_function.__name__
    expected_alerter_function_name = f"alert_{alertTarget.lower()}"
    assert output_alerter_function_name == expected_alerter_function_name


def test_AlertTransmitter_send_alert(mocker):
    for alertTarget in alertTargets:
        m = mocker.patch(f"src.alert_transmitter.AlertTransmitter.alert_{alertTarget.lower()}", return_value = None)
        alerter = AlertTransmitter(alertTarget)
        alerter.send_alert("LOW")
        m.assert_called_once_with("LOW")



        



    


