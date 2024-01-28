from datetime import datetime

from src.api.whatsapp.schema import WebHookNotification

PHONE_NUMBER = "747312876"
PHONE_NUMBER_ID = "747312876"
TIMESTAMP = datetime.now()
LOCATION_LATITUDE = 1.20
LOCATION_LONGITUDE = 1.20
LOCATION_NAME = "casa"
LOCATION_ADDRESS = "juan capella 90"


## Messages coming from the real webhook
sample_text_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '104246805978102', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '34623508545', 'phone_number_id': '102033176202052'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '447472138610'}], 'messages': [{'from': '447472138610', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0ExNzRFRTcyRDc3MTAzNjM3RkEA', 'timestamp': '1705880589', 'text': {'body': 'ping'}, 'type': 'text'}]}, 'field': 'messages'}]}]}
sample_audio_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '104246805978102', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '34623508545', 'phone_number_id': '102033176202052'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '447472138610'}], 'messages': [{'from': '447472138610', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0EyQUNGNkNCRkUyQzBERURDNjEA', 'timestamp': '1706481016', 'type': 'audio', 'audio': {'mime_type': 'audio/ogg; codecs=opus', 'sha256': 'n4EKagtCwv9j+qtbhfD6c106h4JJ3cfLgbAzLHDQ/Ck=', 'id': '235930636150989', 'voice': True}}]}, 'field': 'messages'}]}]}


def test_text_message():
    wm = WebHookNotification(**sample_text_message)
    assert wm.object == "whatsapp_business_account"


def test_audio_message():
    wm = WebHookNotification(**sample_audio_message)
    assert wm.object == "whatsapp_business_account"


def test_image_message():
    wm = WebHookNotification(**image_message)
    assert wm.object == "whatsapp_business_account"


def test_reaction_message():
    wm = WebHookNotification(**reaction_message)
    assert wm.object == "whatsapp_business_account"


def test_sticker_message():
    wm = WebHookNotification(**sticker)
    assert wm.object == "whatsapp_business_account"


def test_location_message():
    wm = WebHookNotification(**location_message)
    assert wm.object == "whatsapp_business_account"
