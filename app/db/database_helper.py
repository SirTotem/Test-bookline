import json

DB_FILE = "app/db/database.json"


class DatabaseHelper:
    def read_database():
        try:
            with open(DB_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"cars": {}, "bookings": {}}

    def write_database(data) -> None:
        with open(DB_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
