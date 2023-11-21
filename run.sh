#!/bin/bash
cd $(dirname "$(realpath "$0")")
docker cp gulf_django:/app/media .
docker cp gulf_django:/app/db.sqlite3 .
docker compose up -d --build