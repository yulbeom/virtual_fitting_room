#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p> Hello World </p>" \
           "<p> test run </p>"

if __name__ == "__main__":
    app.run()


# In[ ]:




