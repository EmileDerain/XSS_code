from django.http import HttpRequest, HttpResponse

def xss_fonction(request: HttpRequest) -> HttpResponse:
    data = str(request.GET.get("data", ""))

    return HttpResponse(f"<p>You searched for: {data}<p>")
