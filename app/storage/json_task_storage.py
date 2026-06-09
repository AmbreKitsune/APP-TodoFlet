from pathlib import Path
import json

from app.models.task import Task


class JsonTaskStorage:
    def __init__(self):
        self.path_tasks = Path("data/tasks.json")

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
        data = []
        for item in tasks:
            data.append({"id": item.id, "title": item.title})

        with open(self.path_tasks, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
