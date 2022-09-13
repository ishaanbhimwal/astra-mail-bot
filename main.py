import yagmail
from apscheduler.schedulers.background import BackgroundScheduler

from keep_alive import keep_alive
from special_holidays import calc_res


def send_msg():
    if calc_res() != None:
        yag = yagmail.SMTP("astramailbot@gmail.com", "fgtujuffnsaqfycg")
        contents = [calc_res()]
        yag.send(
            # add more receiptents
            ["ishaanbhimwal@gmail.com"], "[astra-mail-bot] Upcoming Event", contents
        )
    else:
        pass


sched = BackgroundScheduler(daemon=True)

keep_alive()

while True:
    sched.add_job(
        send_msg, timezone="Asia/Kolkata", trigger="cron", hour="07", minute="30"
    )
    sched.start()
