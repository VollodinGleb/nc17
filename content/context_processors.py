from .models import Promotion


def add_promotion_texts_to_context(request):
    return {"promotions": Promotion.objects.all()}


def lang_context_processor(request):
    return {'LANG': request.LANGUAGE_CODE}
