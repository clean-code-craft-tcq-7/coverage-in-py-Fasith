from src.temperature_alerter import classify_temperature_breach, check_and_alert
from pytest import MonkeyPatch


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


def test_check_and_alert():
    pass
