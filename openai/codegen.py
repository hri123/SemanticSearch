from openai import OpenAI

from openai.types import Completion, CompletionChoice, CompletionUsage

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key="My API Key",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "# Create a Python dictionary of 6 countries and their capitals\ncountries =",
        },
        {
            "role": "user",
            "content": "# Loop through them and print the name of each country and their capital\n",
        }

    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)