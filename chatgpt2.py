import requests

def chatgpt(text):
  headers = {"X-Wp-Nonce": "adcdfad787"}
  data = {
      "botId": "default",
      "newMessage": text,
  }

  req = requests.post(
      f"https://chatgpt4online.org/wp-json/mwai-ui/v1/chats/submit",json=data,headers=headers)
  try:
    text = req.json()['reply']
  except:
    text = "حدثت مشكلة في السيرفر"
  return text