import pytest

@pytest.fixture
def product_details():
    return {"sku": "GLOBAL-CAN-10X10",
                   "description": "Standard canvas on quality stretcher bar, 25x25cm",
                   "productDimensions": {
                       "width": 10.0000,
                       "height": 10.0000,
                       "units": "in"
                   },
                   "attributes": {
                       "wrap": [
                           "Black",
                           "ImageWrap",
                           "MirrorWrap",
                           "White"
                       ]
                   },
                   "printAreas": {
                       "default": {
                           "required": true
                       }
                   },
                   "variants": [
                       {
                           "attributes": {
                               "wrap": "Black"
                           },
                           "shipsTo": [
                               "IM",
                               "LU",
                               "ID",
                               "CI",
                               "GR",
                               "FK",
                               "AL",
                               "LA",
                               "KY"
                           ],
                           "printAreaSizes": {
                               "default": {
                                   "horizontalResolution": 1522,
                                   "verticalResolution": 1522
                               }
                           }
                       },
                       {
                           "attributes": {
                               "wrap": "ImageWrap"
                           },
                           "shipsTo": [
                               "IM",
                               "LU",
                               "ID",
                               "CI",
                               "GR",
                               "FK",
                               "AL",
                               "LA",
                               "KY"
                           ],
                           "printAreaSizes": {
                               "default": {
                                   "horizontalResolution": 2137,
                                   "verticalResolution": 2137
                               }
                           }
                       },
                       {
                           "attributes": {
                               "wrap": "MirrorWrap"
                           },
                           "shipsTo": [
                               "IM",
                               "LU",
                               "ID",
                               "CI",
                               "GR",
                               "FK",
                               "AL",
                               "LA",
                               "KY"
                           ],
                           "printAreaSizes": {
                               "default": {
                                   "horizontalResolution": 1522,
                                   "verticalResolution": 1522
                               }
                           }
                       },
                       {
                           "attributes": {
                               "wrap": "White"
                           },
                           "shipsTo": [
                               "IM",
                               "LU",
                               "ID",
                               "CI",
                               "GR",
                               "FK",
                               "AL",
                               "LA",
                               "KY"
                           ],
                           "printAreaSizes": {
                               "default": {
                                   "horizontalResolution": 1522,
                                   "verticalResolution": 1522
                               }
                           }
                       }
                   ]
                   }