from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_detect_chair_1():
    files = {"file": open("./test_images/Chair/chair 1.png", "rb")}
    response = client.post("/predicts-image", files=files)
    assert response.status_code == 200
    assert response.json() == {"label": "Chair"}


def test_detect_chair_2():
    files = {"file": open("./test_images/Chair/chair 2.png", "rb")}
    response = client.post("/predicts-image", files=files)
    assert response.status_code == 200
    assert response.json() == {"label": "Chair"}


def test_detect_bed_1():
    files = {"file": open("./test_images/Bed/bed 1.jpg", "rb")}
    response = client.post("/predicts-image", files=files)
    assert response.status_code == 200
    assert response.json() == {"label": "Bed"}


def test_detect_bed_2():
    files = {"file": open("./test_images/Bed/bed 2.jpg", "rb")}
    response = client.post("/predicts-image", files=files)
    assert response.status_code == 200
    assert response.json() == {"label": "Bed"}


def test_detect_sofa_1():
    files = {"file": open("./test_images/Sofa/sofa 1.jpg", "rb")}
    response = client.post("/predicts-image", files=files)
    assert response.status_code == 200
    assert response.json() == {"label": "Sofa"}


def test_detect_sofa_2():
    files = {"file": open("./test_images/Sofa/sofa 2.jpg", "rb")}
    response = client.post("/predicts-image", files=files)
    assert response.status_code == 200
    assert response.json() == {"label": "Sofa"}
