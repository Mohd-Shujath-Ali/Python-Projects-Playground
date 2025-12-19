from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
load_dotenv('.env')
client = InferenceClient(
    api_key=os.getenv("API_KEY"),
)

HF_ERROR_CATALOG = {
    400: {
        "name": "Bad Request",
        "description": "Invalid request payload or parameters sent to the model."
    },
    401: {
        "name": "Unauthorized",
        "description": "Invalid or missing API key."
    },
    403: {
        "name": "Forbidden",
        "description": "You do not have permission to access this model."
    },
    404: {
        "name": "Not Found",
        "description": "Model or endpoint does not exist."
    },
    408: {
        "name": "Request Timeout",
        "description": "Inference request took too long to complete."
    },
    409: {
        "name": "Conflict",
        "description": "Request conflict or invalid model state."
    },
    422: {
        "name": "Unprocessable Entity",
        "description": "Request is syntactically correct but semantically invalid."
    },
    429: {
        "name": "Rate Limit Exceeded",
        "description": "Too many requests. Retry after some delay."
    },
    500: {
        "name": "Internal Server Error",
        "description": "Hugging Face server error."
    },
    502: {
        "name": "Bad Gateway",
        "description": "Invalid response from upstream model provider."
    },
    503: {
        "name": "Service Unavailable",
        "description": "Model is loading, unavailable, or overloaded."
    },
    504: {
        "name": "Gateway Timeout",
        "description": "Inference service did not respond in time."
    },

    None: {
        "name": "Unknown Error",
        "description": "Unexpected error. Could be SDK, network, or system issue."
    }
}

PY_ERROR_CATLOG={
    "ConnectError": {
        "name": "ConnectionError",
        "description": "Failed to connect to Hugging Face servers. Check internet."
    },
    "TimeoutError": {
        "name": "Timeout Error",
        "description": "Network timeout while contacting inference API."
    },
    "SSLError": {
        "name": "SSL Error",
        "description": "SSL handshake failed. Certificate or network issue."
    },
    "DNSLookupError": {
        "name": "DNS Resolution Error",
        "description": "Could not resolve Hugging Face domain."
    },
    "NetworkUnreachable": {
        "name": "Network Unreachable",
        "description": "No network route to host."
    },

    None: {
        "name": "Unknown Error",
        "description": "Unexpected error. Could be SDK, network, or system issue."
    }
}

while True:
    ask=input("Enter prompt: [Type: 'quit' to exit")
    if ask.lower()=="quit":
        break
    try:

        completion = client.chat.completions.create(
            model="google/gemma-2-2b-it:nebius",
            messages=[
                {
                    "role": "user",
                    "content": ask
                }
            ],
        )
        print(completion.choices[0].message.content)
    except Exception as e:
        try:

            error=e.response.status_code
            print(HF_ERROR_CATALOG[error]["name"])
            print(HF_ERROR_CATALOG[error]["description"])
            break
        except:
            error=type(e).__name__
            print(PY_ERROR_CATLOG[error]["name"])
            print(PY_ERROR_CATLOG[error]["description"])
            break
