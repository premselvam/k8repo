from fastapi import fastapi, request , from
from fastapi.templating import jinja2templates

app = fastapi()
#templates = jinja2templates (directory="/code")
templates = jinja2templates (directory="C:\Users\Lenovo\Desktop\k8 project")

@app.get("/")
def form_post(request: request) :
    return templates.templateresponse('form html', context={'request' : request})
    

