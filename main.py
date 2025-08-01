import os
from dotenv import load_dotenv
import openai

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

def get_openai_response(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    client = openai.OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[OpenAI Error: {e}] Returning mock response.")
        return "Quantum computing is like a super-fast calculator that can solve really hard problems by using special rules of physics. Imagine if you had a magic coin that could be both heads and tails at the same time—quantum computers use this magic to do things regular computers can't!"

def get_claude_response(prompt):
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not ANTHROPIC_AVAILABLE or not api_key:
        print("[Claude API not available. Returning mock response.]")
        return "Quantum computing is like having a superpowerful brain that can think about many possibilities at once, instead of just one at a time. It's like if you could try every key on a keyring at the same time to open a lock!"
    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-3-opus-20240229",  # or another available model
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"[Claude Error: {e}] Returning mock response.")
        return "Quantum computing is like having a superpowerful brain that can think about many possibilities at once, instead of just one at a time. It's like if you could try every key on a keyring at the same time to open a lock!"

def main():
    load_dotenv()
    prompt = "Explain quantum computing to a 10-year-old."
    print(f"Prompt: {prompt}\n")

    print("Querying OpenAI GPT-3.5...")
    openai_output = get_openai_response(prompt)
    print("OpenAI GPT-3.5 Response:\n", openai_output, "\n")

    print("Querying Anthropic Claude...")
    claude_output = get_claude_response(prompt)
    print("Anthropic Claude Response:\n", claude_output, "\n")

    # Save to Markdown
    with open("llm_comparison_report.md", "w", encoding="utf-8") as f:
        f.write(f"# LLM Output Comparison\n\n")
        f.write(f"**Prompt:** {prompt}\n\n")
        f.write(f"## OpenAI GPT-3.5 Response\n\n{openai_output}\n\n")
        f.write(f"## Anthropic Claude Response\n\n{claude_output}\n\n")
        f.write("## Discussion\n\n")
        f.write("- Compare the reasoning, clarity, and formatting of the two responses here.\n")

    print("\nComparison report saved to llm_comparison_report.md")

if __name__ == "__main__":
    main() 