import requests, json, asyncio
from flask import Flask, flash, jsonify, request, redirect, url_for, render_template
from services import get_connections, get_schemas, get_credential_definitions, get_verkeys, handle_json
import ipfsApi
import logging
app = Flask(__name__)
app.secret_key = "abc"

api_url = 'http://localhost:8021'



# client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

@app.route("/",methods=["POST","GET"])
def home():
	connections = get_connections("http://localhost:8021/connections",{})
	schemas = get_schemas("http://localhost:8021/schemas/created",{})
	credential_definitions = get_credential_definitions("http://localhost:8021/credential-definitions/created",{})
	return render_template("index.html",schemas=schemas,connections=connections,credential_definitions=credential_definitions)

@app.route("/create_schema",methods=["POST"])
def create_schema():
	data = request.form.get('schema_form')
	new_schema_json = jsonify(data)
	handle_json("http://localhost:8021/schemas",new_schema_json)
	return redirect(url_for("home"))

# @app.route("/verkey",methods=["GET"])
# def verkey():
# 	data = request.form.get('get_verkey_form')
# 	did_json = jsonify(data)
# 	get_json("http://localhost:8021/ledger/did-verkey",did_json)
# 	return redirect(url_for("home"))

# @app.route("/create_crl", methods=["POST"])
# def create_crl():
# 	try:
# 		if request.method == 'POST':
# 			file = request.files['file']
# 			log.info("file name: {}".format(file.filename), {'app': 'dfile-up-req'})
# 			#client = ipfshttpclient.connect(app.config['IPFS_CONNECT_URL'])
# 			#res = client.add(file)
# 			ipfs_api = ipfsApi.client('127.0.0.1',5001)
# 			res = ipfs_api.add(file)
			
# 			log.info("create_crl res: {}".format(res), {'app': 'dfile-up-res'})
# 			url = app.config['DOMAIN'] + '/' + str(res['Hash'])
# 			return redirect(url_for("home"))

# 		#abort(400)

# 	except Exception as e:
# 		log.exception("Upload Error! exception:{}".format(str(e)))
# 		print("Upload Error! \n", 503)
# 		return redirect(url_for("home")) 


@app.route('/func',methods=['POST'])
def func():
	dataGet = '' if not request.get_json(force=True) else request.get_json(force=True)

	print(dataGet)
	dataReply = {"it works!": "win"}
	return jsonify(dataReply)

@app.route("/admin")
def admin():
	return redirect(url_for("home"))

if __name__ == "__main__":
	#app.debug = True
	app.run()

