
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_message(time_type):
    prompt = f"""
    Ramazan için uzun, premium, şiirsel bir {time_type} mesajı yaz.
    Marka: ÜmitMod.

    Mesaj sonunda mutlaka şu imza olsun:

    ━━━━━━━━━━━━━━
    🔥 ÜmitMod
    💙 Gece Dua, Gündüz Duruş
    ━━━━━━━━━━━━━━

    Tekrar eden kalıplar kullanma.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    return response.choices[0].message.content
