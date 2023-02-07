from django.contrib import admin


class WordFilter(admin.SimpleListFilter):
    title = "Word Filter"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return (
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        )

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
