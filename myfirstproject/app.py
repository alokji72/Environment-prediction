from flask import Flask, render_template
from flask import Flask
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

def image():
	x=[1,3,4,56,70,34,21,1.2,1.7,1.9,2.3,3.0,9.5,8.5,7.6,6.1,9.1,11,12.4,18.3,19.3,16.4]
	y=[2,3,4,40,69,35,20,1.2,1.6,1.8,2.1,2.8,9,8,7,6,9.4,11.3,12,18,19.2,16]

	def plot_web_traffic(x, y, models=None):
		plt.figure(figsize=(12,6)) # width and height of the plot in inches
		plt.scatter(x, y, s=10)
		plt.title("temperature Increase")

		plt.xlabel("year")
		plt.ylabel("temperature in degree celcius")
		plt.xticks([w*7*24 for w in range(5)],
					['week %i' %(w+1) for w in range(5)])
		if models:
			colors = ['g', 'k', 'b', 'm', 'r']
			linestyles = ['-', '-.', '--', ':', '-']

			mx = sp.linspace(0, x[-1], 1000)
			for model, style, color in zip(models, linestyles, colors):
				plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

				plt.legend(["d=%i" % m.order for m in models], loc="upper left")
		plt.autoscale(tight=True)
		plt.grid()
	plot_web_traffic(x,y)
	plt.savefig("static/images/web_traffic.png")
	return "done"


@app.route("/analysis")
def analysis():
	image()
	return "<img src='../static/images/web_traffic.png'/>"








@app.route("/checkData")
def checkData():
	# plt.savefig("static/images/web_traffic.png")
	return render_template('about.html')

if __name__=='__main__':
	app.run(debug = True)
