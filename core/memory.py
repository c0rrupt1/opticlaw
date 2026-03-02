import core
import json
import datetime

class Memory(core.storage.Storage):
    """manages the AI's memory"""
    # TODO: rewrite in progress

    def create(self, content: str, tags: list, pinned: bool = False):
        mem = {
            "content": content,
            "tags": tags,
            "pinned": pinned,
            "date_created": datetime.datetime.now().isoformat()
        }
        self.append(mem)
        self.save()

    def edit(self, index: int, content: str = None, tags: list = None):
        if index > len(self) or index < 0:
            return False

        if content:
            self[index]["content"] = content
        if tags:
            self[index]["tags"] = tags

        self.save()

    def delete(self, index: int):
        if index >= len(self) or index < 0:
            print("index not found")
            return False
        self.pop(index)
        self.save()
        return True

    def pin(self, index: int):
        if index >= len(self) or index < 0:
            return False
        self[index]["pinned"] = True
        self.save()
        return True
    def unpin(self, index: int):
        if index >= len(self) or index < 0:
            return False
        self[index]["pinned"] = False
        self.save()
        return True

    def get_pinned(self):
        found = []
        for index, mem in enumerate(self):
            if mem.get("pinned"):
                # add ID to it.. ID = index in the list
                mem_copy = mem.copy()
                mem_copy["id"] = index
                found.append(mem_copy)

        return found

    def search(self, query: str, search_in_content: bool = False):
        found = []
        for index, mem in enumerate(self):
            # add ID to it.. ID = index in the list
            mem_copy = mem.copy()
            mem_copy["id"] = index

            # search based on tags first
            if mem.get("tags"):
                if any(query.lower() in tag.lower() for tag in mem["tags"]):
                    found.append(mem_copy)
                    continue

            # search the content if requested
            if search_in_content:
                if query.lower() in mem.get("content").lower():
                    found.append(mem_copy)
                    continue

        return found
