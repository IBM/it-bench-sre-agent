# Source: https://docs.together.ai/docs/llama-3-function-calling
FOR_NON_NATIVE_FUNCTION_CALLING = """
If you choose to call a function ONLY reply in the following format with no prefix or suffix:

<function=example_function_name>{\"example_name\": \"example_value\"}</function>

Please remember to:
- Follow the specified format, start with <function= and end with </function>
- Required parameters MUST be specified
- Only call one function at a time
- Put the entire function call reply on one line
- If there is no function call available, answer the question like normal with your current knowledge and do not tell the user about function calls
"""
