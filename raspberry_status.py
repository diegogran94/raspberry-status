#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import os
from flask_navigation import Navigation

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Status', 'status'),
])

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/status')
def status():
	
	f = os.popen('vcgencmd measure_temp')
	cpu_temp = f.read()
	f = os.popen('vcgencmd measure_clock arm')
	cpu_freq_arm = f.read()
	f = os.popen('vcgencmd measure_clock core')
	cpu_freq_core = f.read()
	f = os.popen('vcgencmd measure_volts core')
	cpu_volt = f.read()
	f = os.popen('uptime | grep -o "load.*"')
	load_average = f.read().split(" ",2)[2]
	f = os.popen('cat /proc/meminfo | grep -o "MemTotal.*"')
	total_mem = f.read().split(" ",1)[1]
	f = os.popen('cat /proc/meminfo | grep -o "MemFree.*"')
	free_mem = f.read().split(" ",1)[1]
		
	return render_template('status.html', tittle='RPI STATUS',temp=cpu_temp, freq_arm=cpu_freq_arm,
			freq_core=cpu_freq_core, volt=cpu_volt, load=load_average, t_mem=total_mem, f_mem=free_mem)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
