from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from jobs import refresh_microsoft_oauth_tokens

scheduler = BlockingScheduler(jobtimezone=utc)  # , jobstore=MemoryJobStore)

scheduler.add_job(
    refresh_microsoft_oauth_tokens,
    "interval",
    minutes=5,
    id="refresh_microsoft_oauth_tokens",
)

if __name__ == "__main__":
    scheduler.start()
