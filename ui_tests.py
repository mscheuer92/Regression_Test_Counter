import os


class UiTests:
    dsp_path = "/Users/w504327/tests/pythonTests/ps-cbs-developer-service-portal/tests/features"
    apigee_path = "/Users/w504327/tests/pythonTests/ps-cbs-apigee-manager/tests/features"
    service_path = "/Users/w504327/tests/pythonTests/ps-sre-service-status/tests/features"

    def dsp_occurrences(self):
        os.chdir(self.dsp_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Developer Service Portal:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")

    def apigee_occurrences(self):
        os.chdir(self.apigee_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Apigee Manager:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")

    def service_occurrences(self):
        os.chdir(self.service_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Wex Status:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")
