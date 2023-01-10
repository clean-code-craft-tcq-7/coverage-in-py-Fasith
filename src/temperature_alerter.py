from .temperature_constants import battery_temperature_range
from .alert_tramsitter import AlertTransmitter


def infer_breach(value, lowerLimit, upperLimit):
    if value < lowerLimit:
        return 'LOW'
    if value > upperLimit:
        return 'HIGH'
    return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
    ideal_temperature_range = battery_temperature_range[coolingType]
    return infer_breach(temperatureInC, *ideal_temperature_range)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType =\
        classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    alert_transmitter = AlertTransmitter(alertTarget)
    alert_transmitter.send_alert(breachType)
