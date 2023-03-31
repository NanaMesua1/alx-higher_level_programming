#!/usr/bin/python3
import requests


if __name__ == "__main__":
   url = "https://alx-intranet.hbtn.io/status"
   print("Body response:")
   print("\t- type: {}".format(type(url.text)))
   print("\t- content: {}".format(url.text))
