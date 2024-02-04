from django.http import HttpResponse, HttpRequest
from lxml import etree

def xxe_fonction(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        xml_data = request.body.decode('utf-8')

        # Process the XML data without proper validation
        try:
            root = etree.fromstring(xml_data)
            cmd = root.findtext('command/shell')
            rtn = eval(cmd)

            response_data = f"Command {cmd} processed successfully : {rtn}"
        except etree.XMLSyntaxError:
            response_data = "Invalid XML format"

        return HttpResponse(response_data)
    else:
        return HttpResponse("Invalid request method")
