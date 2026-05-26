import json
from curl_cffi import requests

class Request_Data:
  def __init__(self, url=None, headers=None, path=None):
    self.url = url
    self.headers = headers
    self.path = path
  
  def fetch_request(self, method=None):
    if self.url:
      res = requests.request(method=method, url=self.url, headers=self.headers, impersonate="chrome120")
      
      if res.status_code == 200:
        return {
          "status": res.status_code,
          "is_success": True,
          "body": res.content.decode("utf-8"),
          "error": None
        }
      else:
        return {
          "status": res.status_code,
          "is_success": False,
          "body": "",
          "error": res.reason
        }
    else:
      raise ValueError("url not given.")
  
  
  def save_data_into_file(self, content ,file_name):
    full_path = self.path + file_name
    print(full_path)
    if file_name.split(".")[-1] == "json":
      with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4,ensure_ascii=False)
    else:
      with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    