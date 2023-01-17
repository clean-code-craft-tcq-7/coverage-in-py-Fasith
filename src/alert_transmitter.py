class AlertTransmitter():

    def __init__(self, alertTarget):
        self.alertTarget = alertTarget
        self.alerter_function = self.set_alerter_function()

    def set_alerter_function(self,):
        alerter_function_name = f"alert_{self.alertTarget.lower()}"
        alerter_function = getattr(AlertTransmitter, alerter_function_name)
        return alerter_function

    def send_alert(self, breachType):
        self.alerter_function(breachType)

    @staticmethod
    def alert_to_email(breachType):
        recepient = "a.b@c.com"
        print(f"To :{recepient}")
        if breachType != "NORMAL":
            print(f"Hi, the temperature is too {breachType}")

    @staticmethod
    def alert_to_controller(breachType):
        header = 0xfeed
        print(f'{header}, {breachType}')
