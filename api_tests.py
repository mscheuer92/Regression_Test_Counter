import os


class ApiCount:
    address_path = "/Users/w504327/tests/goTests/src/github.com/wexinc/ps-cbs-address-service/test/features"
    auth_path = "/Users/w504327/tests/goTests/src/github.com/wexinc/ps-cbs-auth-service/test/features"
    exchange_path = "/Users/w504327/tests/goTests/src/github.com/wexinc/ps-cbs-exchange-rate-service/test/features"
    ggg_path = "/Users/w504327/tests/goTests/src/github.com/wexinc/ps-cbs-gogogithub-service/tests/features"
    notification_path = "/Users/w504327/tests/goTests/src/github.com/wexinc/ps-cbs-notification-service/test/features"

    def address_occurrences(self):
        os.chdir(self.address_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Address Service:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")

    def auth_occurrences(self):
        os.chdir(self.auth_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Auth Service:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")

    def exchange_occurrences(self):
        os.chdir(self.exchange_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Exchange Service:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")

    def ggg_occurrences(self):
        os.chdir(self.ggg_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("GoGoGithub Service:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")

    def notification_occurrences(self):
        os.chdir(self.notification_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Notification Service:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")

    def transport_occurrences(self):
        os.chdir(self.transporterator_path)
        result = os.popen('cat *.feature | grep -c Scenario:')
        num1 = result.read()
        print("Transporterator Service:\n Scenario:", num1.replace("\n", ""))
        result2 = os.popen('cat *.feature | grep -c Outline:')
        num2 = result2.read()
        if num2 != 0:
            result3 = os.popen('cat *.feature | grep -c "|"')
            num3 = result3.read()
            outline_total = int(num3) - int(num2)
            total = outline_total + int(num1)
            print(" Scenario Outline:", outline_total)
            print(" total: ", total, "\n")
