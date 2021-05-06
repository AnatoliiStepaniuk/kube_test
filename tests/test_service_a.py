import requests
import os


def test_service_a_response_status_200():
    host = os.getenv('SERVICE_A_HOST')
    response = requests.get(f"{host}/a")
    assert response.status_code == 200


def test_service_b_response_status_200():
    host = os.getenv('SERVICE_A_HOST')
    response = requests.get(f"{host}/ab")
    assert response.status_code == 200


def test_service_a_reply():
    host = os.getenv('SERVICE_A_HOST')
    reply = os.getenv('SERVICE_A_REPLY')
    response = requests.get(f"{host}/a")
    print(f"host = {host}")
    print(f"reply = {reply}")
    print(f"response = {response.text}")
    assert response.text.find(reply) != -1


def test_service_b_reply():
    host = os.getenv('SERVICE_A_HOST')
    reply = os.getenv('SERVICE_B_REPLY')
    response = requests.get(f"{host}/ab")
    assert response.text.find(reply) != -1

