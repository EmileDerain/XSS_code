from django.http import HttpResponse, HttpRequest import html

def input_sanitizer(input):
  return html.unescape(input)

def vulnerable_endpoint(request: HttpRequest) -> HttpResponse:
  user_input = input_sanitizer (request.GET("input"))
  return HttpResponse(f"<p>User input: {user_input}</p>")