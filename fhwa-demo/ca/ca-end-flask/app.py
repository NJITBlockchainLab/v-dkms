import requests, json, asyncio
from flask import Flask, flash, jsonify, request, redirect, url_for, render_template
from services import get_connections, get_schemas, get_credential_definitions, get_verkeys, get_json, handle_json
import ipfsApi
import logging
app = Flask(__name__)
app.secret_key = "abc"

api_url = 'http://localhost:8021'
api_key = 'put_web_agent_api_key_here'


# client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

@app.route("/",methods=["POST","GET"])
def home():
	connections = get_connections("http://localhost:8021/connections",{})
	schemas = get_schemas("http://localhost:8021/schemas/created",{})
	credential_definitions = get_credential_definitions("http://localhost:8021/credential-definitions/created",{})
	return render_template("index.html",schemas=schemas,connections=connections,credential_definitions=credential_definitions)

@app.route("/create-schema", methods=["GET","POST"])
def create_schema():
	try:
		data = request.form

		#convert form data to dictionary
		dataDict = data.to_dict(flat=False)
		
		#convert values in JSON to suitable format for the Web Agent API
		dataDict['schema_name'] = dataDict['schema_name'][0]
		dataDict['schema_version'] = dataDict['schema_version'][0]
		dataDict['attributes'] = dataDict['attributes'][0]
		dataDict['attributes'] = dataDict['attributes'].strip('][').split(', ')

		new_schema_json = json.loads(json.dumps(dataDict))

		handle_json("http://localhost:8021/schemas",new_schema_json)

	except:
		pass
	return redirect(url_for("home"))

@app.route("/create-credential-definition", methods=["GET","POST"])
def create_credential_definition():
	try:
		data = request.form

		#convert form data to dictionary
		data_dict = data.to_dict(flat=False)

		#convert values in JSON to suitable format for the Web Agent API
		data_dict['schema_id'] = data_dict['schema_id'][0]
		data_dict['connection_id'] = data_dict['connection_id'][0]

		new_schema_json = json.loads(json.dumps(data_dict))

		handle_json("http://localhost:8021/credential-definitions",new_schema_json)

	except:
		pass
	return redirect(url_for("home"))

@app.route("/get-verkey", methods=["GET","POST"])
def get_verkey():
	try:
		data = request.form
		data_dict = data.to_dict(flat=False)
		endpoint_did = data_dict['did'][0]
		response = requests.get('http://localhost:8021/ledger/did-verkey?did=' + endpoint_did).json()
		flash(response)
	except:
		print("failed")
		pass
	return redirect(url_for("home"))

@app.route("/issue-credential",methods=["POST"])
def issue_credential():
	try:
		data = request.form
		credential_attributes = []
		issue_credential = {"auto_remove": True,"comment": "string","trace": False, "credential_proposal":{"attributes":credential_attributes}}
		credential_dict = data.to_dict(flat=False)
		
		issue_credential['cred_def_id'] = credential_dict['cred_def_id'][0]
		issue_credential['connection_id'] = credential_dict['connection_id'][0]
		issue_credential["credential_proposal"]["attributes"] = [{'name':'vin','value':credential_dict['verkey'][0]}]
		#print(issue_credential)
		
		new_cred_json = json.loads(json.dumps(issue_credential))
		#print(new_cred_json)
		handle_json("http://localhost:8021/issue-credential/send",new_cred_json)
	except:
		pass
	return redirect(url_for("home"))

# @app.route("/verkey",methods=["GET"])
# def verkey():
# 	data = request.form.get('get_verkey_form')
# 	did_json = jsonify(data)
# 	get_json("http://localhost:8021/ledger/did-verkey",did_json)
# 	return redirect(url_for("home"))



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

