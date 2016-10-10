
import sys, datetime
from pprint import pprint

events = {}
times = {'max_end_time':None,'min_start_time':None}

def main():

	solution_part_a()


def solution_part_b():
	'''
	For an arbitrarily large stream of events, I would change my approach from part a.
	I may not be able to store all the processed events in a hashmap in main memory.
	
	My general approach would be to parallel process events in chunks. The chunk size would
	be depedent on my machine(s) total RAM. Each chunk of processed
	events should be stored in an always sorted collection outside of the program 
	- perhaps some sort of distributed data store which uses a balanced binary search tree. 
	This would be good data structure since insertion worst case is O(log n) making
	the total time to process the data ~ O(nlogn). An event should be stored
	as a JSON object so that we can run query ops on the data store later. 
	Along with each chunk we would keep track of the chunks max_end_time and 
	min_start_time. At the end of preprocessing, we could run a simple algorithm 
	to find the global max_end_time and min_start_time and store those.

	Then once we are finished processing a chunk (its been inserted into the tree), we could
	do a query for all events in the data store whose overlap = 0. 
	Then run the overlap check on these events and print the events accordingly to stdout. 
	Once again, this might need to be done in chunks as well since the number of events that
	need to be processed might be very large.
	'''
	pass

def solution_part_a():
	'''
	Assumptions:
	I wasn't sure if these strings were actually supposed to be valid JSON formatted strings. I decided
	not to assume they were JSON strings. I assumed they were utf-8 unicode strings and parsed them.

	Description:
	Read n event strings from stdin and mark the events which overlap in time with 1
	'''

	# Read in number of lines
	num_lines = sys.stdin.readline()
	
	# Validate number of lines argument
	try:
		num_lines = num_lines.strip()
		num_lines = int(num_lines)
	except TypeError:
		print 'First argument must be positive integer!'

	# Process lines	
	count = 0	
	while count < num_lines:
		event_string = sys.stdin.readline()
		if event_string:
			process_line(event_string)
		count += 1

	process_events()

def process_events():
	'''
	Sort events by start time. Mark overlapping events. Print all events to stdout
	'''

	max_end_time = times['max_end_time']
	min_start_time = times['min_start_time']

	# Process unique events	
	# Sort events by start time
	for start_time in sorted(events.keys()):
		event = events[start_time]

		# Overlap check	
		if (start_time <= max_end_time) and (start_time != min_start_time) and (event['end_time'] > min_start_time):
			print set_overlap(event["event_string"],True)
		else:
			print event["event_string"]

def process_line(event_line):
	'''
	Parse the event string to extract start, end times. Keep track of max end time and min start time.
	Only store unique events. Assume events with equal start times are overlapping. 
	Print these events to stdout right away.
	'''

	max_end_time = times['max_end_time']
	min_start_time = times['min_start_time']

	# Assume events are utf-8 (based on sample)
	# Decode to ascii to make it easier to parse
	line = event_line.decode('utf-8').encode('ascii','ignore')

	# Extract start and end times
	parts = line.split(",")

	try:

		# Convert start time to datetime
		start_time = parts[0].split(" ")
		start_datetime = str_to_datetime(start_time[-2].strip(),start_time[-1].strip())

		# Convert end time to datetime
		end_time = parts[1].split(" ")
		end_datetime = str_to_datetime(end_time[-2].strip(),end_time[-1].strip())

		# Update min start time
		if min_start_time is None:
			times['min_start_time'] = start_datetime
		else:	
			if start_datetime <= min_start_time:
				times['min_start_time'] = start_datetime

		# Update max end time
		if max_end_time is None:
			times['max_end_time'] = end_datetime
		else:	
			if end_datetime >= max_end_time:
				times['max_end_time'] = end_datetime
			
		# If event already exists, mark overlap and print
		if start_datetime in events:
			print set_overlap(event_line,True)

		# Insert into events hash map	
		else:
			events[start_datetime] = {"event_string":event_line,"end_time":end_datetime}
		
	except IndexError:
		print 'Line not formatted as expected! Skipping %s' % line
		return

def str_to_datetime(ymd, hms):
	'''
	Utility function to convert from string to datetime objects
	'''

	ymd = map(int,ymd.split("-"))
	hms = map(int,hms.split(":"))

	return datetime.datetime(ymd[0],ymd[1],ymd[2],\
		hms[0],hms[1],hms[2])

def set_overlap(line,overlap):
	'''
	Utility function to set overlap field in event string.
	'''

	prefix = line.split(",")[0:-1]
	return "".join(prefix) + ", 'overlap': " + str(int(overlap)) + "}"


if __name__ == '__main__':
	main()