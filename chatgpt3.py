import requests, json

def chatgpt(text):
  headers = {"X-Wp-Nonce": "adcdfad787"}
  data = {"botId":"default","customId":None,"session":"6568aa8e0582a","chatId":"05a7ena163uw","contextId":9,"newMessage":text,"newImageId":None,"stream":True}

  req = requests.post(
      f"https://onlinegpt.org/chatgpt/wp-json/mwai-ui/v1/chats/submit",json=data)
  try:
    text = json.loads(json.loads(str(req.text).split("data: ")[-1])['data'])['reply']
  except:
    text = "حدثت مشكلة في السيرفر"
  return text