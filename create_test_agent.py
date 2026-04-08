import requests
import json

url = "https://bolna-test-production.up.railway.app/agent"
payload = {
    "agent_config": {
        "agent_name": "TestAgent",
        "tasks": [
            {
                "task_type": "conversation",
                "toolchain": {
                    "execution": "parallel",
                    "pipelines": [["transcriber", "llm", "synthesizer"]]
                },
                "tools_config": {
                    "llm_agent": {
                        "agent_type": "simple_llm_agent",
                        "agent_flow_type": "streaming",
                        "llm_config": {
                            "provider": "groq",
                            "model": "llama-3.3-70b-versatile"
                        }
                    },
                    "transcriber": {
                        "provider": "deepgram",
                        "model": "nova-2",
                        "language": "en",
                        "stream": True
                    },
                    "synthesizer": {
                        "provider": "cartesia",
                        "provider_config": {
                            "voice": "Default",
                            "voice_id": "9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
                            "model": "sonic-3",
                            "language": "en"
                        },
                        "stream": True,
                        "audio_format": "pcm"
                    }
                }
            }
        ],
        "agent_welcome_message": "Hi, I am your test assistant. How can I help you today?"
    },
    "agent_prompts": {
        "task_1": {
            "system_prompt": "You are a helpful assistant. Keep your responses short and sweet."
        }
    }
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
