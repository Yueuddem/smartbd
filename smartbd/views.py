import datetime
import json
from django.db.models import Case, When, Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt