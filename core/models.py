from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ TIme Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add는 모델이 생성된 날짜를 알아서 구해주는 속성이고,
    # auto_now는 업데이트된 날짜를 알아서 구해준다.

    class Meata:
        abstract = True
        # abstract 는 데이터베이스에 등록되지 않는 속성이다.
        # 즉 상속을 위해서만 사용되고 독자적으로 데이터베이스에 등록되길 원하지 않는다!