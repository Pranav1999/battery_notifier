import subprocess
import time

def get_battery_percent():
	command = "cat /sys/class/power_supply/BAT0/capacity"		#command to get battery percentage
	batteryPercent = subprocess.Popen(["/bin/bash","-c" ,command], stdout=subprocess.PIPE)		#execute command through bash
	return batteryPercent.communicate()[0].decode("utf-8").replace("\n","")		#returns battery percentage

def get_battery_status():
	command = "cat /sys/class/power_supply/BAT0/status"		#command to get battery percentage
	batteryPercent = subprocess.Popen(["/bin/bash","-c" ,command], stdout=subprocess.PIPE)		#execute command through bash
	return batteryPercent.communicate()[0].decode("utf-8").replace("\n","").strip()		#returns battery percentage

def main():
	commandPlug = "notify-send 'Plug the Adapter'"		#command to show plug adapter notification
	commandUnplug = "notify-send 'Unplug the Adapter'"		#command to show plug adapter notification
	while True:
		charge = int(get_battery_percent())		#calls function and get battery percentage
		status = get_battery_status()		#calls function and get battery status

		if (charge >= 90) and (status == 'Charging'):
			subprocess.Popen(["/bin/bash", "-c", commandUnplug])		#execute command to show plug adapter notification
		elif (charge <= 50) and (status == 'Discharging'):
			subprocess.Popen(["/bin/bash", "-c", commandPlug])		#execute command to show plug adapter notification

		time.sleep(10)

main()