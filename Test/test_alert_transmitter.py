from src.alert_tramsitter import AlertTransmitter


def test_Alerter_initialization():
    alertTargets = ["TO_EMAIL", "TO_CONTROLLER"]
    for alertTarget in alertTargets:
        alerter = AlertTransmitter(alertTarget)
        assert alerter.alertTarget == alertTarget


def test_Alerter_set_alerter_function():
    alertTargets = ["TO_EMAIL", "TO_CONTROLLER"]
    for alertTarget in alertTargets:
        alerter = AlertTransmitter(alertTarget)
        output_alerter_function_name = alerter.alerter_function.__name__
        desired_alerter_function_name = f"alert_{alertTarget.lower()}"
        assert output_alerter_function_name == desired_alerter_function_name
        
    


