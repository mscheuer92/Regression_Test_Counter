from ui_tests import UiTests
from api_tests import ApiCount


def output():
    print("*** MICROSERVICE TESTS *** \n")
    a = ApiCount()
    a.address_occurrences()
    a.auth_occurrences()
    a.exchange_occurrences()
    a.ggg_occurrences()
    a.notification_occurrences()
    a.transport_occurrences()

    print("*** UI TESTS *** \n")
    b = UiTests()
    b.dsp_occurrences()
    b.apigee_occurrences()
    b.service_occurrences()

output()
