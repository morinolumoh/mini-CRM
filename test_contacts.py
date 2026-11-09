def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_create_and_list_contact(client):
    payload = {"first_name": "Ada", "last_name": "Lovelace", "email": "ada@example.com"}
    created = client.post("/contacts", json=payload)
    assert created.status_code == 201
    assert created.json()["email"] == "ada@example.com"

    listed = client.get("/contacts")
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_duplicate_email_rejected(client):
    payload = {"first_name": "Ada", "last_name": "Lovelace", "email": "ada@example.com"}
    client.post("/contacts", json=payload)
    res = client.post("/contacts", json=payload)
    assert res.status_code == 409


# TODO (Week 1): write tests FIRST for get/patch/delete, watch them fail, then
# implement the endpoints until they pass. This is test-driven development.
def test_get_contact(client):
    payload = {"first_name": "Ada", "last_name": "Lovelace", "email": "Ada@example.com""}
    client.get("/contacts", json=payload)
    res= client.get("/contacts", json=payload)
    assert res.status_code = 409
    

.github/workflows/ci.yml
.gitignore
README.md
docker-compose.yml
.env.example
backend/   (app/, tests/, requirements.txt, pytest.ini)
db/        (schema.sql, seed.sql)
docs/      (ROADMAP.md, LEARNING_LOG.md)

