import discord
import openai
import os
# export DISCORD_KEY=dummy_discord_token
# export OPENAI_API_KEY=dummy_openai_token
openai.api_key = os.getenv("OPENAI_API_KEY")
discord_token = os.getenv("DISCORD_KEY")

intent = discord.Intents.default()
intent.messages = True
intent.message_content = True
client = discord.Client(intents=intent)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    prompt = message.content[9:]
    print(prompt)
    if message.author == client.user or not str(message.content).startswith('/Eldrida'):
        return

    openai_prompt = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=openai_prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=.7,
    )
    output_message = response.choices[0]['message']['content']
    print(output_message)

    await message.channel.send(output_message)

if __name__ == '__main__':
    client.run(discord_token)
