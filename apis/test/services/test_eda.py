from unittest import TestCase, mock

import apis.services.eda as cases_eda

class TestServicesEda(TestCase):

    mock_cursor = None

    services = None

    def setUp(self): 

        self.mock_cursor = mock.MagicMock()

        self.services = cases_eda.cases_eda()

    def test_check_status_account_with_gender(self):

        result = self.services.check_status_account_with_gender()

        return result