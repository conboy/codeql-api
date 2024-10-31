# codeql-api

Start FastAPI with

```bash
cd api
fastapi dev main.py
```

To send Sarif files to the API using curl do

```bash
curl -X POST "http://127.0.0.1:8000/upload-sarif/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "sarif_file=@test.sarif"
```

Issues Table

id (hash)| 