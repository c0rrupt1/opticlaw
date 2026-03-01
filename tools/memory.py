import core
import os
import msgpack
import datetime
import re

cached_mem = None

class MemoryTool(core.tool.Tool):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    # async def get_history(self, from_days_ago: int = 30, to_days_ago: int = 0):
    #     """
    #     Retrieves information about events from the past. This is your ONLY source of past information about previous conversations - DO NOT assume you know anything from previous conversations unless you call this first.

    #     Information stored includes:
    #     - Past events and conversations

    #     Args:
    #         from_days_ago (int, optional): Number of days to remember from, relative to today
    #             if None, defaults to 30 days ago.
    #         to_days_ago (int, optional): Number of days to remember up to, relative to today
    #             if None, defaults to today.

    #     Examples:
    #         - get_history(30, 0) → Last 30 days
    #         - get_history(30, 1) → Last 30 days up until yesterday
    #         - get_history(30, 7) → Last 30 days up until 7 days before today
    #         - get_history(1, 1) → Only yesterday
    #         - get_history(365, 0) → A whole year up until today
    #         - get_history(730, 365) → Last year (730 days = 2 years ago, 365 days = 1 year ago)
    #         - get_history(7, 7) → Exactly 7 days ago, without any other days included
    #     """
    #     return self.result(self.manager.memory.get_history(from_days_ago, to_days_ago))

    async def store(self, content: str, persistent: bool = False):
        """
        Stores a memory for future use. You MUST use this to retain information across conversations.

        CRITICAL STORAGE RULES:
        1. ALWAYS use when user provides new personal information
        2. ALWAYS use for important conversation outcomes
        3. ALWAYS use for user preferences/changes
        4. ALWAYS summarize in 1-2 concise paragraphs
        5. ALWAYS refer to user as "user", never "you" or "i"

        IMPORTANT: Use edit_memory instead if modifying existing visible memories.

        PERSISTENT MEMORIES:
        • persistent=False (default): Memory is date-based and will only appear in get_history()
          when its date falls within the requested date range.
        • persistent=True: Memory is ALWAYS included in get_history() results, regardless of date range.
          Use this for evergreen information that should never be forgotten.

        When to use persistent=True:
        • User's core identity details (name, occupation, family)
        • Permanent preferences (allergies, dietary restrictions)
        • Long-term goals or life circumstances
        • System configuration that never changes

        When to use persistent=False:
        • Recent events or conversations
        • Temporary preferences or moods
        • Time-sensitive information
        • Context that might become outdated

        Examples:
        - store_memory("User's name is Rose and she has blue eyes", persistent=True)
        - store_memory("User mentioned feeling tired today and wants to reschedule", persistent=False)
        """
        id = self.manager.memory.store(content, persistent)
        return self.result(f"id: {id}")

    async def edit(self, id: int, content: str, persistent: bool = None):
        """
        Modifies an existing memory using its ID.

        Do not modify persistent flag unless explicitely requested.
        """
        result = self.manager.memory.edit(id, content, persistent)
        if not result:
            return self.result(f"Memory ID {id} not found.", False)
        return self.result(result)

    async def delete(self, id: int) -> dict:
        result = self.manager.memory.delete(id)
        if not result:
            return self.result(f"Memory ID {id} not found.", False)
        return self.result(result)

    # async def search_within_memories(self, query: str) -> dict:
    #     """
    #     Searches memory contents for specific terms. Returns matching memories with their IDs.

    #     USE WHEN:
    #     - User asks for something specific (e.g., "find memories about vacation")
    #     - You need to locate memories containing certain keywords
    #     - You want to filter memories by content

    #     NOTE: Results from this search become "visible" for editing/deleting.
    #     """
    #     found_memories = []
    #     query_lower = query.lower()

    #     for memory in self.manager.memory:
    #         content = memory.get("content", "").lower()
    #         date_str = memory.get("date", "").lower()

    #         if (query_lower in content) or (query_lower in date_str):
    #             found_memories.append(memory)

    #     return self.result(found_memories)
