import requests

def chatgpt(text):
  data = {
    "_wpnonce": "4cd0694f0e",
    "post_id": 6,
    "action": "wpaicg_chat_shortcode_message",
    "message": text,
  }
  #https://chatgptfree.ai/wp-admin/admin-ajax.php

  req = requests.post(f"https://chataigpt.org/wp-admin/admin-ajax.php", data=data)
  try:
    if req.json()['status'] == "success":
      text = req.json()['data']
  except:
    text = "حدثت مشكلة في السيرفر"
  return text
