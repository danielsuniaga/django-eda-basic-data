from unittest import TestCase, mock

import apis.services.eda as cases_eda

class TestServicesEda(TestCase):

    mock_cursor = None

    services = None

    def setUp(self): 

        self.mock_cursor = mock.MagicMock()

        self.services = cases_eda.cases_eda()

    def test_check_price_with_brand_max(self):

        result = self.services.check_price_with_brand_max()

        print(result)

    def test_check_price_with_brand_min(self):

        result = self.services.check_price_with_brand_min()

        print(result)

    def test_check_price_max(self):

        result = self.services.check_price_max()

        print(result)

    def test_check_price_min(self):

        result = self.services.check_price_min()

        print(result)

    def test_check_moss_sold_brand(self):

        result = self.services.check_most_sold_brand()

        print(result)

    def test_check_most_sold_brands(self):

        result = self.services.check_most_sold_brands()

        print(result)