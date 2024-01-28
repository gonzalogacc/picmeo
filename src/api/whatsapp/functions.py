from src.api.whatsapp.schema import MissingParametersException, VerificationException, WebHookNotification


def veryify_webhook(request):
    """ Endpoint to verify the webhook
    """
    if 'hub.mode' not in request.query_params or \
            'hub.challenge' not in request.query_params or \
            'hub.verify_token' not in request.query_params:
        raise MissingParametersException()

    mode = request.query_params['hub.mode']
    challenge = int(request.query_params['hub.challenge'])
    token = request.query_params['hub.verify_token']

    ## TODO:  verif secret from secret manager
    if mode == 'subscribe' and token == 'verif':
        print(f'Webhook verified!!! {challenge}')
        return challenge

    raise VerificationException()


def process_message(message: WebHookNotification):
    print(f"-->{message.entry[0].changes[0].value}")
    return message.model_dump()
