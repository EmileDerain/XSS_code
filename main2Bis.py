from django.http import HttpResponse, HttpRequest
from lxml import etree

def xxe_fonction(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        xml_data = request.body.decode('utf-8')

        # Désactiver la résolution des entités
        parser = etree.XMLParser(
            dtd_validation=False,
            load_dtd=False,
            no_network=False,
            resolve_entities=True,
        )
        root = etree.fromstring(xml_data, parser=parser)
        exe = etree.tostring(root, pretty_print=True)
        # Faire quelque chose avec les données XML
        response_data = f"XML traité avec succès. Username: {exe}"

        return HttpResponse(response_data)
    else:
        return HttpResponse("Invalid request method")
