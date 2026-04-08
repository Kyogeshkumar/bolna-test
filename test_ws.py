import asyncio
import websockets

async def test_ws():
    uri = "wss://bolna-test-production.up.railway.app/chat/v1/ae5ee10b-436a-4e62-983d-1ff724a7a7df"
    print(f"Testing connection to: {uri}")
    try:
        async with websockets.connect(uri) as websocket:
            print("Successfully connected to the Brain!")
            await websocket.close()
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(test_ws())
