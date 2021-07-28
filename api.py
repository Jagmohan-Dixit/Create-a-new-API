from flask import Flask,render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

