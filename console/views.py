from django.http import JsonResponse
from console.models import Version
from django.forms.models import model_to_dict


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def version_list(request):
    versions = Version.objects.get_queryset()
    result = list()
    if versions:
        for version in versions:
            result.append(
                {'id': version.id,
                 'version': version.version,
                 'product_name': version.product.product_name,
                 'module_name': version.module.module_name,
                 'customer_name': version.customer.customer_name,
                 'update_at': version.update_at
                 }
            )

    return JsonResponse(result, safe=False)
