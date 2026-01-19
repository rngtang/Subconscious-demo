from subconscious import Subconscious
import os
import dotenv

dotenv.load_dotenv()

client = Subconscious(api_key=os.getenv("SUBCONSCIOUS_API_KEY"))

run = client.run(
    engine="tim-large",
    input={
        "instructions": """
        You are a local event discovery agent in Durham, NC.
        Find public events happening nearby in the next 7 days and recommend only the best ones (e.g. nightlife, concerts, college sports, talks).

        Rules:
        - Do not invent events.
        - Return date, time, location
        """,
        "tools": [ 
            {"type": "platform", "id": "web_search"},
        ],
    },
    options={"await_completion": True},
)

print(run.result.answer)