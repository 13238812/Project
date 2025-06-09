#Flask Application that can submit simple calculations
from flask import Flask, redirect, render_template, request

# Launches Flasks with default setting
app = Flask(__name__)