# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8

#ADD / . marche mais pas conseillé 
# repertoire actuel du contener 
WORKDIR /app 
COPY . .
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

#COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3","app.py"]
