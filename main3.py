from flask import Flask, request
from lxml import etree
from io import StringIO

app = Flask(__name__)

@app.route('/vulnerable_xml_handler', methods=['POST'])
def vulnerable_xml_handler():
    if request.method == 'POST':
        xml_data = request.data

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


        return response_data
    else:
        return "Méthode de requête invalide"