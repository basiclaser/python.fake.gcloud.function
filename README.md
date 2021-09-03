to run this project on your computer:

```
cd myProjectsFolder
git clone git@github.com:basiclaser/python.fake.gcloud.function.git
cd python.fake.gcloud.function
pip install -r requirements.txt
python server.py
```

to use:
go to `http://127.0.0.1:5000/about` in your browser, or use CURL, or `REST client` plugin for VSC (recommended, example in HTTP folder).

# API APPLICATION PROGRAMMING INTERFACE

Physically, a server is just a computer that we call a "server". Servers are always on.

On the software level - we can write "servers" or "server programs" AKA APIs ( AKA webhooks )

### a server program is a program that is designed to listen for requests and respond or act in some way.

examples of different kindsa servers:

- web server - HTTP
- file server - FTP
- email server - SMTP / IMAP POP3

## servers/apis in pretty much every programming language just look like this:

```
app.route("GET", "/", (req,res)=> res.send("homepage.html"))
app.route("POST", "/message", (req,res)=> database.createNewMessage(req.body.message))
```

The first "route" or "endpoint" there will deliver a HTML file called "homepage.html" to the person who requests it.

The second route accepts POST requests with a "message" value, to be written into a database.
