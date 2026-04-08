import os
import json
import requests
import uuid
from twilio.twiml.voice_response import VoiceResponse, Connect
from twilio.rest import Client
from dotenv import load_dotenv
import redis.asyncio as redis
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()
load_dotenv()
port = int(os.getenv('PORT', 8001))

twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(twilio_account_sid, twilio_auth_token)


import os

def populate_ngrok_tunnels():
    # Use environment variables for Railway, fallback to localhost for others
    telephony_url = os.getenv('TELEPHONY_HOST', 'https://gentle-recreation-production-4113.up.railway.app')
    bolna_url = os.getenv('BOLNA_HOST', 'wss://bolna-test-production.up.railway.app')
    
    print(f"Using telephony_host: {telephony_url}")
    print(f"Using bolna_host: {bolna_url}")
    return telephony_url, bolna_url


@app.post('/call')
async def make_call(request: Request):
    try:
        call_details = await request.json()
        agent_id = call_details.get('agent_id', None)

        if not agent_id:
            raise HTTPException(status_code=404, detail="Agent not provided")
        
        if not call_details or "recipient_phone_number" not in call_details:
            raise HTTPException(status_code=404, detail="Recipient phone number not provided")

        telephony_host, bolna_host = populate_ngrok_tunnels()

        print(f'telephony_host: {telephony_host}')
        print(f'bolna_host: {bolna_host}')

        try:
            call = twilio_client.calls.create(
                to=call_details.get('recipient_phone_number'),
                from_=twilio_phone_number,
                url=f"{telephony_host}/twilio_connect?bolna_host={bolna_host}&agent_id={agent_id}",
                method="POST",
                record=True
            )
        except Exception as e:
            print(f'make_call exception: {str(e)}')

        return PlainTextResponse("done", status_code=200)

    except Exception as e:
        print(f"Exception occurred in make_call: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post('/twilio_connect')
async def twilio_connect(bolna_host: str = Query(...), agent_id: str = Query(...)):
    try:
        response = VoiceResponse()

        connect = Connect()
        bolna_websocket_url = f'{bolna_host}/chat/v1/{agent_id}'
        connect.stream(url=bolna_websocket_url)
        print(f"websocket connection done to {bolna_websocket_url}")
        response.append(connect)

        return PlainTextResponse(str(response), status_code=200, media_type='text/xml')

    except Exception as e:
        print(f"Exception occurred in twilio_callback: {e}")
