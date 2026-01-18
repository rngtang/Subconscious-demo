from subconscious import Subconscious

client = Subconscious(api_key="sk-91e41165db34bcfbba8de0dc47f02612312a8b9ae632c2839edeb60ca145ce76")

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