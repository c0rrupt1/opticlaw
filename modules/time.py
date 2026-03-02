import core
import datetime

class Time(core.module.Module):
    async def on_system_prompt(self):
        time = datetime.datetime.now().isoformat()
        return f"Current time/date is {time}"
