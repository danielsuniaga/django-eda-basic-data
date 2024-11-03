from unittest import TestCase, mock

import apis.services.data as cases_data

class TestServicesData(TestCase):

    mock_cursor = None

    services = None

    def setUp(self): 

        self.mock_cursor = mock.MagicMock()

        self.services = cases_data.cases_data()

    def test_check_data(self):

        result = self.services.check_data()

        print(result)