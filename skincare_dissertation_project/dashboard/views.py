from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
import calendar
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from django.shortcuts import render, get_object_or_404

@login_required
def main_dashboard(request):
    today = date.today()

    # ---------------- WEEKLY TRACKER ----------------
    week_days = []
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)

        logged_in = DailyLogin.objects.filter(
            user=request.user,
            date=day
        ).exists()

        week_days.append({
            "label": day.strftime("%a"),
            "logged_in": logged_in
        })

    # ---------------- MONTHLY TRACKER ----------------
    year = today.year
    month = today.month

    cal = calendar.Calendar(firstweekday=6)
    month_days = []

    for day in cal.itermonthdates(year, month):

        is_current_month = day.month == month

        logged_in = False
        if is_current_month:
            logged_in = DailyLogin.objects.filter(
                user=request.user,
                date=day
            ).exists()

        month_days.append({
            "date": day,
            "day_number": day.day,
            "current_month": is_current_month,
            "logged_in": logged_in
        })

    return render(request, "dashboard/dashboard.html", {
        "week_days": week_days,
        "month_days": month_days
    })


def user_info(request, username):
    user = get_object_or_404(CustomUser, username=username)

    return render(request, 'user_info.html', {
        'user': user
    })
