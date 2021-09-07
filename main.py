from ui_tests import UiTests
from api_tests import ApiCount


def output():
    a = ApiCount()
    b = UiTests()

    a.address_occurrences()
    b.apigee_occurrences()
    a.auth_occurrences()
    b.dsp_occurrences()
    a.exchange_occurrences()
    a.ggg_occurrences()
    a.notification_occurrences()
    b.service_occurrences()


output()
