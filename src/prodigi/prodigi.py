

PRODIGI_API_KEY=""

class Prodigi:

    def __init__(self):
        pass

    def _httpx_client(self):

        return httpx.Client()

    def product_details(self, product_code: str):
        """ Get the product details for a particular product code

        :param product_code:
        :return:
        """
        pass

    def upload_image(self):
        """
        Upload the image to a bucket and makes it available for prodigy to download
        :return:
        """
        pass

    def place_order(self):
        "/v4.0/orders/"
        # curl "https://api.sandbox.prodigi.com/v4.0/Orders"
        # -X POST -H "X-API-Key: your-rest-api-key" -H "Content-Type: application/json"
        # -d
        # '
        # {
        #     "shippingMethod": "Budget",
        #     "recipient": {
        #         "address": {
        #             "line1": "14 test place",
        #             "line2": "test",
        #             "postalOrZipCode": "12345",
        #             "countryCode": "US",
        #             "townOrCity": "somewhere",
        #             "stateOrCounty": "somewhereelse"
        #         },
        #         "name": "John Testman",
        #         "email": "jtestman@prodigi.com"
        #     },
        #     "items": [
        #         {
        #             "sku": "GLOBAL-FAP-16x24",
        #             "copies": 1,
        #             "sizing": "fillPrintArea",
        #             "assets": [
        #                 {
        #                     "printArea": "default",
        #                     "url": "https://your-image-url/image.png"
        #                 }
        #             ]
        #         }
        #     ]
        # }