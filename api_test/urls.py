from django.urls import path
from .views import ApplicantViews
urlpatterns = [
    path('', ApplicantViews.as_view()),
    path('<int:id>', ApplicantViews.as_view())
]

# curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/applicant/ -d "{\"name\":\"pat\",\"age\":\"41\",\"qualification\":\"btech\",\"gender\":\"male\",\"acceptance\":\"\"}"

# curl -X PATCH http://127.0.0.1:8000/applicant/1 -H 'Content-Type: application/json' -d '{"age":25}'

# curl -X "DELETE" http://127.0.0.1:8000/applicant/1
