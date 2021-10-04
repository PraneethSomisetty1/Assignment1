from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import string
import random
import sys

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users/<id>', methods=['GET','DELETE'])
def get_user(id):
   if request.method == 'GET' :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   if request.method == 'DELETE':
      for user in users['users_list']:
         if id in user.values():
            users['users_list'].remove(user)
      resp = jsonify(success=True)
      resp.status_code = 204
      return resp


@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username :
               if search_job :
                  if user['job'] == search_job :
                     subdict['users_list'].append(user)
               else :
                  subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      idToAdd = Id_Generator()
      userToAdd['id'] = idToAdd
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201
      return resp

#stackoverflow/internet
def Id_Generator(size = 6, chars=string.ascii_lowercase + string.digits) :
   return ''.join(random.choice(chars) for _ in range(size)) 