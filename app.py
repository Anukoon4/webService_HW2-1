from flask import Flask,request
from flask_restful import Resource ,Api,reqparse
import json ,time
from datetime import datetime,date

app= Flask (__name__)
api=Api(app)

parser =  reqparse.RequestParser()
parser.add_argument('birth')


def cal_age(birth):
	today = date.today()
	if today.month > birth.month and today.day> birth.day :
		return today.year-birth.year
	

	return (today.year-birth.year)-1


class Hello(Resource):
	def get(self):
		return {"message":"Plese sent birthdate."}
	def post(self):
		args=parser.parse_args()
		birth=args['birth']
		birthDate = datetime.strptime(birth,'%d-%m-%Y')
		age = int(cal_age(birthDate))
		return {"birthdate":birth,"age":age}

api.add_resource(Hello,'/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5501)
