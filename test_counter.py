import os


class TestCounter:
    def __init__(self):
        self.path_dict = {
            1: "<project_feature_path>",
            2: "<project_feature_path>",
            # delete this comment and  add as many key values as you need

        }

        self.name_dict = {
            # These names should match the project order in self.path_dict.
            1: "Address Service",
            2: "Apigee Manager",
            3: "Auth Service",
            4: "Developer Service Portal",
            5: "Event Hub API",
            6: "Exchange Rate Service",
            7: "GoGoGithub Service",
            8: "Notification Hub API",
            9: "Notification Service",
            10: "Organization Service",
            11: "PAL API",
            12: "Payee Service",
            13: "Payer Service",
            14: "Relationship Account API",
            15: "Wex Status",

        }

    def count_occurrences(self):
        length = len(self.path_dict)
        for i in range(1,length):
            os.chdir(self.path_dict.get(i))
            result = os.popen('cat *.feature | grep -c Scenario:')
            num1 = result.read()
            print(self.name_dict.get(i) + " Scenario:", num1.replace("\n", ""))
            result2 = os.popen('cat *.feature | grep -c Outline:')
            num2 = result2.read()
            if num2 != 0:
                result3 = os.popen('cat *.feature | grep -c "|"')
                num3 = result3.read()
                outline_total = int(num3) - int(num2)
                total = outline_total + int(num1)
                print(" Scenario Outline:", outline_total)
                print(" total: ", total, "\n")
