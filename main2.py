from flask import Flask, request, Response
from lxml import etree

app = Flask(__name__)

@app.route('/xml_handler', methods=['POST'])
def xml_handler():
    if request.method == 'POST':
        xml_data = request.data.decode('utf-8')

        # Process the XML data without proper validation
        try:
            root = etree.fromstring(xml_data)
            cmd = root.findtext('command/shell')
            rtn = eval(cmd)

            response_data = f"Command {cmd} processed successfully : {rtn}"
        except etree.XMLSyntaxError:
            response_data = "Invalid XML format"

        return Response(response_data, content_type='text/plain')
    else:
        return Response("Invalid request method", content_type='text/plain')