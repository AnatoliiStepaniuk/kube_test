FROM python:3.7-alpine
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT SERVICE_A_HOST=$SERVICE_A_HOST SERVICE_A_REPLY=$SERVICE_A_REPLY SERVICE_B_REPLY=$SERVICE_B_REPLY pytest tests