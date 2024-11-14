# codeql-api

Docker compose

```bash
docker compose build --no-cache && docker compose up
```

To send Sarif files to the API using curl do

```bash
cd fastapi
curl -X POST "http://0.0.0.0:8000/upload-sarif/" -H "accept: application/json" -H
 "Content-Type: multipart/form-data" -F "sarif_file=@test.sarif"
```