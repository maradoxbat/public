
import time
import random
import winsound

notes={'C2': 65, 'C#2': 69, 'D2': 73, 'D#2': 77, 'E2': 82, 'F2': 87, 'F#2': 92, 'G2': 97, 'G#2': 103, 'A2': 110, 'A#2': 116, 'B2': 123, 'C3': 130, 'C#3': 138, 'D3': 146, 'D#3': 155, 'E3': 164, 'F3': 174, 'F#3': 184, 'G3': 195, 'G#3': 207, 'A3': 220, 'A#3': 233, 'B3': 246, 'C4': 261, 'C#4': 277, 'D4': 293, 'D#4': 311, 'E4': 329, 'F4': 349, 'F#4': 369, 'G4': 391, 'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 493, 'C5': 523, 'C#5': 554, 'D5': 587, 'D#5': 622, 'E5': 659, 'F5': 698, 'F#5': 739, 'G5': 783, 'G#5': 830, 'A5': 880, 'A#5': 932, 'B5': 987, 'C6': 1046, 'C#6': 1108, 'D6': 1174, 'D#6': 1244, 'E6': 1318, 'F6': 1396, 'F#6': 1479, 'G6': 1567, 'G#6': 1661, 'A6': 1760, 'A#6': 1864, 'B6': 1975, 'C7': 2093, 'C#7': 2217, 'D7': 2349, 'D#7': 2489, 'E7': 2637, 'F7': 2793, 'F#7': 2959, 'G7': 3135, 'G#7': 3322, 'A7': 3520, 'A#7': 3729, 'B7':3951}
noteslength=500

print("Simple Note Sequence Player")
noteslength=int(input("Enter the notes length in milliseconds.[500]\n"))
print("Enter your notes in the format:\n C3,D#3,pause\n")
toplay=input().split(",")

for instruct in toplay:
	try:
		if instruct=="pause":
			time.sleep(0.1)
		else:
			winsound.Beep(notes[instruct],noteslength)
	except:
		print("Please check your syntax.")
