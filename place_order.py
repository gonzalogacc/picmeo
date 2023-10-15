import sys

from src.prodigi.prodigi import Prodigi
from src.prodigi.schema import Recipient, Item, OrderBase, Address, SizingEnum, MoneyAmount, ItemAsset, ShippingMethodEnum
from src.utilities.files_utils import upload_blob

def place_order(image_url: str, image_md5: str):

    recipient = Recipient(
        name='Gonzalo Garcia',
        email='gonzalogacc@gmail.com',
        phoneNumber='+34623508545',
        address=Address(
            line1='Carrer de Ginebra 9',
            line2='Principal 2da',
            postalOrZipCode='08003',
            townOrCity='Barcelona',
            countryCode='ES'
        )
    )
    item = Item(
        merchantReference='referencia1',
        sku='GLOBAL-FAP-A5',
        copies=1,
        sizing=SizingEnum.fill_print_area,
        attributes={},
        recipientCost=MoneyAmount(amount='50', currency='USD'),
        assets=[ItemAsset(
            printArea='default',
            url=image_url,
            md5Hash=image_md5
        )]
    )

    order = OrderBase(
        merchantReference="Gonza Picture",
        shippingMethod=ShippingMethodEnum.budget,
        recipient=recipient,
        items=[item],
        # metadata=order_metadata
    )
    pd = Prodigi()
    ord = pd.create_order(order)
    return ord

if __name__ == "__main__":
    image_url, md5sum = upload_blob(sys.argv[1])
    order = place_order(image_url, md5sum)
    print(order)
