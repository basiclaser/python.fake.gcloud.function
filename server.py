from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    # this emulates the basic behavior of a google cloud function ( internally gcloud python uses flask )
    print(request.json["table_id"])
    body = request.json
    print(body["data"], body["table_id"],
          body["project_id"])
    return request.json["table_id"]


# this is just an example of another API route ( cloud functions dont have these )
# open http://127.0.0.1:5000/about in your browser to see the HTML


@app.route("/about", methods=['GET'])
def about():
    # route handler function
    # returning a response
    return '''
    <html>
        <h1>YO WHATUP</h1>
        <script> alert("WADUP DINGUS")</script>
    </html>
    '''


app.run(debug=True)
