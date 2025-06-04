import tiktoken

def count_tokens(text: str, model_name="gpt-4o"):
    enc = tiktoken.encoding_for_model(model_name)
    return len(enc.encode(text))


def estimate_cost(token_count):

    # gpt-4o, as of now:
    # Input: $5.00 per 1M tokens
    # Output: $15.00 per 1M tokens
    # Assume 90% input, 10% output
    
    input_tokens = int(token_count * 0.9)
    output_tokens = token_count - input_tokens

    input_cost = (input_tokens / 1_000_000) * 5.0
    output_cost = (output_tokens / 1_000_000) * 15.0

    return round(input_cost + output_cost, 5)
