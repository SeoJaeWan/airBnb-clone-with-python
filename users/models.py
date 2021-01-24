from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # User 모델은 django.contrib.auth.models 을 상속 받는다.
    # django.contrib.auth.models 가 유저에 대한 정보를 가지고 있는 장고의 모델이다.

    """ Custom User Models """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Male"),
        (GENDER_OTHER, "other"),
    )

    LANGAUGE_ENGLISH = "en"
    LANGAUGE_KOREAN = "kr"

    LANGAUGE_CHOICES = ((LANGAUGE_ENGLISH, "English"), (LANGAUGE_KOREAN, "Korean"))

    CURERNCY_USD = "usd"
    CURERNCY_KRW = "krw"

    CURERNCY_CHOICES = ((CURERNCY_USD, "USD"), (CURERNCY_KRW, "KRW"))

    avatar = models.ImageField("프로필 사진", null=True, blank=True)
    gender = models.CharField(
        "성별", choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField("사용자 정보", default="", blank=True)
    birthdate = models.DateField("생년월일", null=True)
    langauge = models.CharField(
        "언어 유형", choices=LANGAUGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        "화폐유형", choices=CURERNCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField("호스트권한", default=False)
