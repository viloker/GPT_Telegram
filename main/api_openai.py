from openai import OpenAI

API = 'Your api from openai'

client = OpenAI(api_key=API)

def get_gpt_text(content):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"user",'content': content}
        ]
    )

    return completion.choices[0].message.content
def get_gpt_image(prompt):
    image = client.images.generate(
        model='dall-e-3',
        prompt=str(prompt),
        n=1,
        size='1024x1024'
    )

    return image.data[0].url

