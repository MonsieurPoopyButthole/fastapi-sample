### Setup project

```bash
cd fastapi-sample/
python3/python/py -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run project

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Start Container
```bash
docker compose -f docker-compose.yml up --build
```