import os

from .models import Employees, Positions
import datetime
from telegram import Bot
from users.models import User
from celery import shared_task


@shared_task
def get_brith_date():
    token = os.environ['TELEGRAM_TOKEN']
    today = datetime.date.today()
    this = today.month, today.day
    employees = Employees.objects.all()
    bot = Bot(token=token)
    admins = User.objects.filter(is_admin=True)
    for employee in employees:
        user_date = employee.brith_date.month, employee.brith_date.day
        if this == user_date:
            for admin in admins:
                bot.send_message(chat_id=admin.user_id,
                                 text=f"Bugun {employee.first_name} {employee.last_name} ning tug'ilgan kuni.")
