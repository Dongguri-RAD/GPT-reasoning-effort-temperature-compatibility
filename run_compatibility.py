# run_compatibility.py

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)

models = ["gpt-5.4", "gpt-5.5"]
efforts = ["none", "low", "medium", "high", "xhigh"]

for model in models:
    print(f"\n================ {model} ================")

    for effort in efforts:
        print(f"\n--- reasoning.effort={effort}, temperature=0.0 ---")

        try:
            response = client.responses.create(
                model=model,
                reasoning={"effort": effort},
                temperature=0.0,
                input="Return exactly: compatibility test",
            )

            print("ACCEPTED")
            print("output:", response.output_text)

        except Exception as e:
            print("REJECTED")
            print("error_type:", type(e).__name__)
            print("error_message:", str(e))
