from src.temperature_alerter import classify_temperature_breach, check_and_alert
from pytest import MonkeyPatch

import src.temperature_alerter as temperature_alerter


temperature_classification_test_data = {
    ("PASSIVE_COOLING",-1,"LOW"), ("PASSIVE_COOLING",0,"NORMAL"),("PASSIVE_COOLING",10,"NORMAL"),
    ("PASSIVE_COOLING",35,"NORMAL"),("PASSIVE_COOLING",40,"HIGH"),

    ("HI_ACTIVE_COOLING",-1,"LOW"), ("HI_ACTIVE_COOLING",0,"NORMAL"), ("HI_ACTIVE_COOLING",10,"NORMAL"),
    ("HI_ACTIVE_COOLING",45,"NORMAL"), ("HI_ACTIVE_COOLING",50,"HIGH"),

    ("MED_ACTIVE_COOLING",-1,"LOW"), ("MED_ACTIVE_COOLING",0,"NORMAL"), ("MED_ACTIVE_COOLING",10,"NORMAL"),
    ("MED_ACTIVE_COOLING",40,"NORMAL"), ("MED_ACTIVE_COOLING",45,"HIGH"),


}

def test_classify_temperature_breach():
    for (coolingType, temperatureInC, breachStatus) in temperature_classification_test_data:
        try:
            output = classify_temperature_breach(coolingType, temperatureInC)
            assert(output == breachStatus)
        except AssertionError as e:
            e.args = (
                "Temperture: ", {temperatureInC},
                "Cooling Type: ",{coolingType},
                "Expected output: ", {breachStatus},
                "Actual output: ", {output}
                )
            raise



_breachType = None
_alertTarget = None

class AlertTransmitterStub():
    def __init__(self,alertTarget):
        global _alertTarget
        _alertTarget = alertTarget
    
    def send_alert(self, breachType):
        global _breachType
        _breachType = breachType

def test_check_and_alert(monkeypatch):
    monkeypatch.setattr(temperature_alerter, "AlertTransmitter", AlertTransmitterStub)
    alertTarget = "TO_EMAIL"
    batteryChar = {"coolingType" : "PASSIVE_COOLING"}
    temperatureInC = 15
    check_and_alert(alertTarget, batteryChar, temperatureInC)
    assert(_alertTarget == "TO_EMAIL")
    assert(_breachType == "NORMAL")



