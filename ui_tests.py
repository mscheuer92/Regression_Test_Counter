import os


class UiTests:
    dsp_path = "<path>"
    apigee_path = "<path>"
    service_path = "<path>"

    def dsp_occurrences(self):
        os.chdir(self.dsp_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("Developer Service Portal: ", num.replace("\n", ""))

    def apigee_occurrences(self):
        os.chdir(self.apigee_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("Apigee Manager: ", num.replace("\n", ""))

    def service_occurrences(self):
        os.chdir(self.service_path)
        result = os.popen('cat *.feature | grep -c Scenario')
        num = result.read()
        print("Wex Service: ", num.replace("\n", ""))
