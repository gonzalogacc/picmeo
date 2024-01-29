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
sample_text_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0ExNzRFRTcyRDc3MTAzNjM3RkEA', 'timestamp': '1705880589', 'text': {'body': 'ping'}, 'type': 'text'}]}, 'field': 'messages'}]}]}
sample_audio_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0EyQUNGNkNCRkUyQzBERURDNjEA', 'timestamp': '1706481016', 'type': 'audio', 'audio': {'mime_type': 'audio/ogg; codecs=opus', 'sha256': 'n4EKagtCwv9j+qtbhfD6c106h4JJ3cfLgbAzLHDQ/Ck=', 'id': '235930636150989', 'voice': True}}]}, 'field': 'messages'}]}]}
sample_image_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0E2RjFDNUM3ODY5RDRFRkI4QTYA', 'timestamp': '1706483496', 'type': 'image', 'image': {'mime_type': 'image/jpeg', 'sha256': '3NFMXSCkCF+Np+yvEPwWQnqGVsE0DFYRsJsHERVcdIo=', 'id': '3689457254710849'}}]}, 'field': 'messages'}]}]}
sample_image_message2 = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0FCNTg0NEEzODQyNEYwMEQ5ODMA', 'timestamp': '1706483587', 'type': 'image', 'image': {'caption': 'Datada', 'mime_type': 'image/jpeg', 'sha256': 'LCy79W950HRfWpCYDk55vVr64m2Uhz293ZPsgEkoelg=', 'id': '324590983900923'}}]}, 'field': 'messages'}]}]}
sample_reaction_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0ExQkQ4M0VGMjdDOTdCQjU4RTEA', 'timestamp': '1706484719', 'type': 'reaction', 'reaction': {'message_id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0FCNTg0NEEzODQyNEYwMEQ5ODMA', 'emoji': '👍'}}]}, 'field': 'messages'}]}]}
sample_sticker_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0E0QzUwQTA2ODA0Q0NDQzREMzIA', 'timestamp': '1706485772', 'type': 'sticker', 'sticker': {'mime_type': 'image/webp', 'sha256': 'nJIBtyjSnvBIP+DtaUBLa83BtgILozltp/egbk6jhpo=', 'id': '348507881406793', 'animated': False}}]}, 'field': 'messages'}]}]}
sample_location_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0ExNERCNzkzNzZFNzZBMzIzOUUA', 'timestamp': '1706485860', 'location': {'latitude': 41.381443023682, 'longitude': 2.1878256797791}, 'type': 'location'}]}, 'field': 'messages'}]}]}
sample_contact_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '111111111111111', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '11111111111', 'phone_number_id': '111111111111111'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '111111111111111'}], 'messages': [{'from': '111111111111111', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0EwNzJCNjNBMjJDRTU3NkI5RTgA', 'timestamp': '1706486483', 'type': 'contacts', 'contacts': [{'name': {'first_name': 'Jane', 'last_name': 'Doe', 'formatted_name': 'Jane doe'}, 'phones': [{'phone': '+44 3333 333333', 'wa_id': '333333333333', 'type': 'IPHONE'}]}, {'name': {'formatted_name': '\u202a+44\xa07472\xa0333333\u202c'}, 'phones': [{'phone': '+44 7472 333333', 'wa_id': '447472333333', 'type': 'IPHONE'}]}]}]}, 'field': 'messages'}]}]}

def test_text_message():
    wm = WebHookNotification(**sample_text_message)
    assert wm.object == "whatsapp_business_account"


def test_audio_message():
    wm = WebHookNotification(**sample_audio_message)
    assert wm.object == "whatsapp_business_account"


def test_image_message():
    wm = WebHookNotification(**sample_image_message)
    assert wm.object == "whatsapp_business_account"

    wm = WebHookNotification(**sample_image_message2)
    assert wm.object == "whatsapp_business_account"


def test_reaction_message():
    wm = WebHookNotification(**sample_reaction_message)
    print(wm.entry[0].changes[0].value.messages[0])
    assert wm.object == "whatsapp_business_account"


def test_sticker_message():
    wm = WebHookNotification(**sample_sticker_message)
    assert wm.object == "whatsapp_business_account"


def test_location_message():
    wm = WebHookNotification(**sample_location_message)
    assert wm.object == "whatsapp_business_account"

def test_contact_message():
    wm = WebHookNotification(**sample_contact_message)
    assert wm.object == "whatsapp_business_account"
