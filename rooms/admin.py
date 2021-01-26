from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):

    """ Item ADmin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo ADmin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room ADmin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Space",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "Spaces",
            {
                "classes": ("collapse",),
                # 접을 수 있는 섹션을 만들어 준다
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                ),
            },
        ),
        ("Last Detail", {"fields": ("host",)}),
    )
    # 생성, 수정 화면을 구성할 때 사용!

    ordering = ("name", "price")
    # ordering 을 사용하면 정렬을 사용할 수 있다.
    # name 앞에 -를 붙여주면 내림차순으로 정렬할 수 있다.

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )
    # 어드민 패널에서 Room 패널에 위에 정의된 내용이 나오게 하기 위해서 사용!
    # count_amenities 과 같이 함수 이름을 넣으면 return 값이 나오게 된다.

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    # 어드민 패널에서 필터를 걸기위해서 사용한다!

    search_fields = ["city", "host__username"]
    # 어드민 패널에서 검색을 할 떄 사용된다.
    # 만약 앞에 ^를 넣으면(^city) 해당 단어로 시작, =를 넣으면 똑같아야한다.
    # 또한 host의 username으로 검색하고 싶다면 __명칭 을 붙여주면 된다.

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    # filter_horizontal 은 튜플을 만들 때, many to many 관계의 경우 선택할 수 있게 만들어준다.

    def count_amenities(self, obj):
        # self 는 RoomAdmin을 말하고 obj는 현재 행을 나타낸다.

        return "Potato"

    count_amenities.short_description = "Hello!"
    # short_description 은 속성명을 변경시켜준다.