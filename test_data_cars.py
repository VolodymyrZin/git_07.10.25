import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("test_search.log")
    ]
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def auth_session():
    """auth and creating session"""
    session = requests.Session()
    url = "http://127.0.0.1:8888/auth"
    response = session.post(url, auth=HTTPBasicAuth("test_user", "test_pass"))
    assert response.status_code == 200, "Auth failed"
    access_token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {access_token}"})
    yield session
    session.close()


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("brand", 3),
    ("year", 4),
    ("engine_volume", 10),
    ("year", None),
    (None, 4),
    (None, None),
]
                         )
def test_get_cars(auth_session, sort_by, limit):
    """Testing /cars with different params"""
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    url = "http://127.0.0.1:8888/cars"
    response = auth_session.get(url, params=params)

    logger.info(f"Request: sort_by={sort_by}, limit={limit}")
    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response: {response.json()}")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if limit:
        assert len(data) <= limit
