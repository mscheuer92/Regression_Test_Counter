import os


class ApiCount:
    address_path = "<path>"
    auth_path = "<path>"
    exchange_path = "<path>"
    ggg_path = "<path>"
    notification_path = "<path>"
    transporterator_path = "<path>"

    def address_occurrences(self):
        os.chdir(self.address_path)
        result1 = os.popen('cat *.feature | grep -c Scenario')
        num = result1.read()
        print("Address Service:", num.replace("\n", ""))

    def auth_occurrences(self):
        os.chdir(self.auth_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("MicroAuth Service: ", num.replace("\n", ""))

    def exchange_occurrences(self):
        os.chdir(self.exchange_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("Exchange Rate Service: ", num.replace("\n", ""))

    def ggg_occurrences(self):
        os.chdir(self.ggg_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("GoGoGithub Service: ", num.replace("\n", ""))

    def notification_occurrences(self):
        os.chdir(self.notification_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("Notification Service: ", num.replace("\n", ""))

    def transporterator_occurrences(self):
        os.chdir(self.transporterator_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("Transporterator Service: ", num.replace("\n", ""),)