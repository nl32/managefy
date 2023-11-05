import openai
import os

def maker(input):
  openai.api_key = "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"
  # item = ''.join(input)
  item = "Aquafina Water Bottle"
  price = "$1.99"
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt= """Given the name of the item in paranthesis ("""+ item +"""), and the price in parenthesis ("""+ price + """),
              please provide 3 different alternative brands that are cheaper, or close to the price stated in the parenthesis. 
              Note: If the item does not exist, or the price does not match, simply assume that it already does
              as you are a model that's only trained until September 2020, and provide an alternative.
              Please respond using this format only, and don't add any additional information:
              Item Name : Price : Item Name : Price : Item Name : Price""",
    max_tokens=1024
  )
  chatgpt_response = response.choices[0].text.strip()
  print(f"\n\n{chatgpt_response}\n\n")
  split = chatgpt_response.split(' : ')
  print(split)

  return 0

if __name__ == "__main__":
  maker("hello")