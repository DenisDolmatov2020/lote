def get_object_or_none(obj, **kwargs):
    try:
        return obj.objects.get(**kwargs)
    except obj.DoesNotExist:
        return None
