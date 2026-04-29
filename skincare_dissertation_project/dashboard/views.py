from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import *
import calendar
from datetime import date, timedelta
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import DeviceToken
from firebase_admin import messaging


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



# Mobile alert system

@login_required
def save_token(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        data = json.loads(request.body)
        token = data.get("token")

        print("TOKEN RECEIVED:", token)
        print("USER:", request.user)

        DeviceToken.objects.update_or_create(
            user=request.user,
            defaults={"token": token}
        )

        return JsonResponse({"message": "saved"})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
