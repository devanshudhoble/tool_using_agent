from google.adk.agents import Agent

# -------------------------
# TOOL 1: GENERAL CALCULATOR
# -------------------------
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression.
    Example: "12 * (4 + 6) / 2"
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid mathematical expression."


# -------------------------
# TOOL 2: WORD COUNTER
# -------------------------
def word_counter(text: str) -> str:
    """
    Counts the number of words in a given text.
    """
    count = len(text.split())
    return f"Word count: {count}"


# -------------------------
# AGENT DEFINITION
# -------------------------
root_agent = Agent(
    name="tool_using_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a helpful assistant.\n"
        "- If the user asks to calculate or evaluate an expression, use the calculator tool.\n"
        "- If the user asks to count words, use the word_counter tool.\n"
        "- Otherwise, answer normally."
    ),
    tools=[calculator, word_counter]
)
