import pytest

from src.temperature_alerter import classify_temperature_breach, check_and_alert, infer_breach


@pytest.mark.parametrize(
    "value, lower_limit, upper_limit, expected",
    [
        (25, 50, 100, "LOW"),
        (50, 50, 100, "NORMAL"),
        (75, 50, 100, "NORMAL"),
        (100, 50, 100, "NORMAL"),
        (125, 50, 100, "HIGH"),
        
    ]
)
def test_infer_breach(value, lower_limit, upper_limit, expected):
    assert(infer_breach(value, lower_limit, upper_limit) == expected)


@pytest.mark.parametrize(
    "cooling_type,temperature_range",
    [
        ("PASSIVE_COOLING", (0,35)),
        ("HI_ACTIVE_COOLING", (0,45)),
        ("MED_ACTIVE_COOLING", (0,40))

    ]
)
def test_classify_temperature_breach(cooling_type, temperature_range, mocker):
    temperature_value = 10
    m = mocker.patch(f"src.temperature_alerter.infer_breach")
    classify_temperature_breach(cooling_type,temperature_value)
    m.assert_called_once_with(temperature_value, *temperature_range)


def test_check_and_alert(mocker):
    alert_target = "TO_EMAIL"
    battery_char = {"coolingType":"PASSIVE_COOLING"}
    temperature_in_C = 10

    classify_temperature_breach_mock = mocker.patch(f"src.temperature_alerter.classify_temperature_breach")
    alert_transmitter_mock = mocker.patch(f"src.temperature_alerter.AlertTransmitter")
    
    check_and_alert(alert_target, battery_char, temperature_in_C)
    classify_temperature_breach_mock.assert_called_once_with("PASSIVE_COOLING", 10)
    alert_transmitter_mock.assert_called_once_with("TO_EMAIL")










# _breachType = None
# _alertTarget = None

# class AlertTransmitterStub():
#     def __init__(self,alertTarget):
#         global _alertTarget
#         _alertTarget = alertTarget
    
#     def send_alert(self, breachType):
#         global _breachType
#         _breachType = breachType

# def test_check_and_alert(monkeypatch):
#     monkeypatch.setattr(temperature_alerter, "AlertTransmitter", AlertTransmitterStub)
#     alertTarget = "TO_EMAIL"
#     batteryChar = {"coolingType" : "PASSIVE_COOLING"}
#     temperatureInC = 15
#     check_and_alert(alertTarget, batteryChar, temperatureInC)
#     assert(_alertTarget == "TO_EMAIL")
#     assert(_breachType == "NORMAL")



