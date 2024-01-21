from datetime import datetime

from src.api.whatsapp.schema import WebHookNotification

PHONE_NUMBER = "747312876"
PHONE_NUMBER_ID = "747312876"
TIMESTAMP = datetime.now()
LOCATION_LATITUDE = 1.20
LOCATION_LONGITUDE = 1.20
LOCATION_NAME = "casa"
LOCATION_ADDRESS = "juan capella 90"

text_message = {
    "object": "whatsapp_business_account",
    "entry": [{
        "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
        "changes": [{
            "value": {
                "messaging_product": "whatsapp",
                "metadata": {
                    "display_phone_number": PHONE_NUMBER,
                    "phone_number_id": PHONE_NUMBER_ID
                },
                "contacts": [{
                    "profile": {
                        "name": "NAME"
                    },
                    "wa_id": PHONE_NUMBER
                }],
                "messages": [{
                    "from": PHONE_NUMBER,
                    "id": "wamid.ID",
                    "timestamp": TIMESTAMP,
                    "text": {
                        "body": "MESSAGE_BODY"
                    },
                    "type": "text"
                }]
            },
            "field": "messages"
        }]
    }]
}

reaction_message = {
    "object": "whatsapp_business_account",
    "entry": [{
        "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
        "changes": [{
            "value": {
                "messaging_product": "whatsapp",
                "metadata": {
                    "display_phone_number": PHONE_NUMBER,
                    "phone_number_id": PHONE_NUMBER_ID
                },
                "contacts": [{
                    "profile": {
                        "name": "NAME"
                    },
                    "wa_id": PHONE_NUMBER
                }],
                "messages": [{
                    "from": PHONE_NUMBER,
                    "id": "wamid.ID",
                    "timestamp": TIMESTAMP,
                    "reaction": {
                        "message_id": "MESSAGE_ID",
                        "emoji": "EMOJI"
                    },
                    "type": "reaction"
                }]
            },
            "field": "messages"
        }]
    }]
}

image_message = {
    "object": "whatsapp_business_account",
    "entry": [{
        "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
        "changes": [{
            "value": {
                "messaging_product": "whatsapp",
                "metadata": {
                    "display_phone_number": PHONE_NUMBER,
                    "phone_number_id": PHONE_NUMBER_ID
                },
                "contacts": [{
                    "profile": {
                        "name": "NAME"
                    },
                    "wa_id": "WHATSAPP_ID"
                }],
                "messages": [{
                    "from": PHONE_NUMBER,
                    "id": "wamid.ID",
                    "timestamp": TIMESTAMP,
                    "type": "image",
                    "image": {
                        "caption": "CAPTION",
                        "mime_type": "image/jpeg",
                        "sha256": "IMAGE_HASH",
                        "id": "ID"
                    }
                }]
            },
            "field": "messages"
        }]
    }]
}

sticker = {
    "object": "whatsapp_business_account",
    "entry": [
        {
            "id": "ID",
            "changes": [
                {
                    "value": {
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "PHONE_NUMBER",
                            "phone_number_id": "PHONE_NUMBER_ID"
                        },
                        "contacts": [
                            {
                                "profile": {
                                    "name": "NAME"
                                },
                                "wa_id": "ID"
                            }
                        ],
                        "messages": [
                            {
                                "from": "SENDER_PHONE_NUMBER",
                                "id": "wamid.ID",
                                "timestamp": datetime.now(),
                                "type": "sticker",
                                "sticker": {
                                    "mime_type": "image/webp",
                                    "sha256": "HASH",
                                    "id": "ID"
                                }
                            }
                        ]
                    },
                    "field": "messages"
                }
            ]
        }
    ]
}

unknown_message = {
    "object": "whatsapp_business_account",
    "entry": [{
        "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
        "changes": [{
            "value": {
                "messaging_product": "whatsapp",
                "metadata": {
                    "display_phone_number": "PHONE_NUMBER",
                    "phone_number_id": "PHONE_NUMBER_ID"
                },
                "contacts": [{
                    "profile": {
                        "name": "NAME"
                    },
                    "wa_id": "WHATSAPP_ID"
                }],
                "messages": [{
                    "from": "PHONE_NUMBER",
                    "id": "wamid.ID",
                    "timestamp": "TIMESTAMP",
                    "errors": [
                        {
                            "code": 131051,
                            "details": "Message type is not currently supported",
                            "title": "Unsupported message type"
                        }],
                    "type": "unknown"
                }]
            },
            "field": "messages"
        }],
    }]
}

location_message = {
    "object": "whatsapp_business_account",
    "entry": [{
        "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
        "changes": [{
            "value": {
                "messaging_product": "whatsapp",
                "metadata": {
                    "display_phone_number": "PHONE_NUMBER",
                    "phone_number_id": "PHONE_NUMBER_ID"
                },
                "contacts": [{
                    "profile": {
                        "name": "NAME"
                    },
                    "wa_id": "WHATSAPP_ID"
                }],
                "messages": [{
                    "from": "PHONE_NUMBER",
                    "id": "wamid.ID",
                    "timestamp": datetime.now(),
                    "type": "location",
                    "location": {
                        "latitude": LOCATION_LATITUDE,
                        "longitude": LOCATION_LONGITUDE,
                        "name": LOCATION_NAME,
                        "address": LOCATION_ADDRESS,
                    }
                }]
            },
            "field": "messages"
        }]
    }]
}

audio_message = {}


def test_text_message():
    wm = WebHookNotification(**text_message)
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


def test_audio_message():
    wm = WebHookNotification(**audio_message)
    assert wm.object == "whatsapp_business_account"