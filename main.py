from ui_tests import UiTests
from api_tests import ApiCount


def output():
    a = ApiCount()
    a.address_occurrences()
    a.auth_occurrences()
    a.exchange_occurrences()
    a.ggg_occurrences()
    a.notification_occurrences()
    a.transporterator_occurrences()

    b = UiTests()
    b.dsp_occurrences()
    b.apigee_occurrences()
    b.service_occurrences()


output()
