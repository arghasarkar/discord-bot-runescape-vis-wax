import os
import json

import urllib.parse
import urllib.request
import ssl
import os

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

from VisWax import VisWax

PUBLIC_KEY = os.environ["PUBLIC_KEY"]  # found on Discord Application -> General Information page

PING_PONG = {"type": 1}
RESPONSE_TYPES = {
    "PONG": 1,
    "ACK_NO_SOURCE": 2,
    "MESSAGE_NO_SOURCE": 3,
    "MESSAGE_WITH_SOURCE": 4,
    "ACK_WITH_SOURCE": 5
}


def verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event['params']['header'].get('x-signature-ed25519')
    auth_ts = event['params']['header'].get('x-signature-timestamp')

    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    verify_key.verify(message, bytes.fromhex(auth_sig))  # raises an error if unequal


def ping_pong(body):
    if body.get("type") == 1:
        return True
    return False


def lambda_handler(event, context):
    print(f"event {event}")  # debug print
    # verify the signature
    try:
        verify_signature(event)
    except Exception as e:
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")

    # Check if message is a ping
    body = event.get('body-json')
    if ping_pong(body):
        return PING_PONG

    v = VisWax()
    viswax_combo_result = v.get_viswax_combo(True)

    return {
        "type": RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
        "data": {
            "tts": False,
            "content": viswax_combo_result,
            "embeds": [],
            "allowed_mentions": []
        }
    }
