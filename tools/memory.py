import core
import os
import msgpack
import datetime
import re

cached_mem = None

class MemoryTool(core.tool.Tool):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    # TODO: rewrite in progress
    async def create(self, content: str, tags: list, pinned: bool = False):
        """
        Creates a new memory within your persistent memory storage.

        A memory should be pinned if it's:
        - Permanent preferences (favorite color, favorite shows, allergies, dietary restrictions)
        - A highly important fact that must always be remembered
        - User's core identity details (name, occupation, family)
        - Long-term goals or life circumstances
        - System configuration that never changes

        Args:
            content: the contents of the memory
            tags: a list of tags to associate with the memory for later lookup
            pinned: whether to pin a memory to the top of your context window
        """
        return self.result(self.manager.memory.create(content, tags, pinned))

    async def pin(self, id: int):
        """Pins a memory to the top of your context window. Makes it persistent across conversations."""
        return self.result(self.manager.memory.pin(id))
    async def unpin(self, id: int):
        """Unpins a memory from the top of your context window. An unpinned memory can only be reached by manually searching for it."""
        return self.result(self.manager.memory.unpin(id))

    async def edit(self, id: int, content: str = None, tags: list = None):
        """
        Edits an existing memory.

        CAUTION:
            - ONLY use if you can see the memory's ID
            - NEVER hallucinate or make up an ID
            - If you cannot see the memory, search for it first using memory_search()
        
        Reject if:
            - You cannot see the memory you are about to edit
            - You're not sure which memory to edit

        Args:
            content: the contents of the memory
            tags: optional - leave blank to leave it as-is. a list of tags to associate with the memory for later lookup
        """
        return self.result(self.manager.memory.edit(id, content, tags))

    async def delete(self, id: int):
        """
        Deletes a memory from your storage.
        DANGEROUS. HIGHEST RESTRICTIONS APPLY.

        ONLY delete a memory if:
            - You're sure you have the ID
            - You're sure user wants the memory deleted
            - You've verified the ID
        """
        # behind the scenes, this actually preserves the memory in a file the ai can't access
        # backups are useful!
        if id >= len(self.manager.memory) or id < 0:
            return self.result("memory did not exist", False)

        self.manager.deleted_memories.append(self.manager.memory[id])
        self.manager.deleted_memories.save()
        return self.result(self.manager.memory.delete(id))

    async def search(self, query: str, search_content: bool = False):
        """
        Searches your memories for a query.
        Defaults to searching within tags. Enable search_content to also search within the content of memories.
        """
        return self.result(self.manager.memory.search(query, search_content))
