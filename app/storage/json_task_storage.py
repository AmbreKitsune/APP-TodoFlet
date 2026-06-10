import json
import os
import sys
from pathlib import Path

from app.models.task import Task


class JsonTaskStorage:
    def __init__(self) -> None:
        app_data_dir = os.getenv("FLET_APP_STORAGE_DATA")

        if app_data_dir:
            self.storage_dir = Path(app_data_dir)
        else:
            if getattr(sys, "frozen", False):
                app_dir = Path(sys.executable).resolve().parent
            else:
                app_dir = Path.cwd()

            self.storage_dir = app_dir / "data"

        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.path_tasks = self.storage_dir / "tasks.json"

    def load_tasks(self) -> list[Task]:
        if not self.path_tasks.exists():
            return []

        try:
            with open(self.path_tasks, "r", encoding="UTF-8") as file:
                json_data = json.load(file)
                if not json_data:
                    return []
        except json.decoder.JSONDecodeError:
            raise ValueError("Tasks JSON file is broken")

        data = []
        for item in json_data:
            data.append(Task(id=item['id'], title=item['title']))
        return data


    def save_tasks(self, tasks: list[Task])-> None:
        self.storage_dir.mkdir(parents=True, exist_ok=True)

        data = [
            {"id": item.id, "title": item.title}
            for item in tasks
        ]

        with open(self.path_tasks, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
