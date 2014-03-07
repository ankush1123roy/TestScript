''' Script to Check Server Client Protocol
	
	The Servers are ought to follow HTTP 1.1. Protocol

	Three servers to test 

	1. Forked server - server_f
	2. Threaded server - server_p
	3. Select server - server_s


	Input from command line should be as follows
	--------------------------------------------

	./server_f port /path_of_docs /path_of_log_file

	QUERY
	------

	(echo -ne "GET /small_file.txt HTTP/1.1\nFrom: someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n" && sleep 5) | nc 127.0.0.1 8000

	Details of the QUERY

	small_file.txt - File to be asked by client 
					 1) Small File
				     2) Large File
					 3) File that doesnot Exist
					 4) File that doesnot have permission to be downloaded
    
    Multiple Instances would of these would be run to check for multiple client handling by the server

'''
import os
import time
class check_servers():
	
	def __init__(self, NO_CONN, DELAY):
		self.no_conn = NO_CONN
		self.delay = DELAY
		
	def check_fork(PORT):
		for i in range(self.no_conn):
			os.system('(echo -ne "GET /small_file.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Large File', '\n'

			os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Missing File', '\n'

			os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Wrong Query', '\n'
			
			os.system('(echo -ne "GET /largefile.txt HP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n" \
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

		os.system('pkill server_f')
		
		
	def check_thread(PORT):
		
		for i in range(self.no_conn):
			os.system('(echo -ne "GET /small_file.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Large File', '\n'

			os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Missing File', '\n'

			os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Wrong Query', '\n'
			
			os.system('(echo -ne "GET /largefile.txt HP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n" \
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

		os.system('pkill server_p')
		
	def check_select(PORT):

		for i in range(self.no_conn):
			os.system('(echo -ne "GET /small_file.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Large File', '\n'

			os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Missing File', '\n'

			os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

			print 'Testing for Wrong Query', '\n'
			
			os.system('(echo -ne "GET /largefile.txt HP/1.1\nFrom: \
				someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n" \
				&& sleep 5) | nc 127.0.0.1 ' + PORT)

		os.system('pkill server_s')
		
		

import pdb

path = '/home/ankush/Cmput379W/TEST'


# Ports and names of log files

PORT_SERV_F, PORT_SERV_P, PORT_SERV_S = '8000', '8001', '8002'
LOG_SERV_F, LOG_SERV_P, LOG_SERV_S = 'flog.txt', 'plog.txt', 'slog.txt'


# Untaring the tarfile containing all submissions

Submissions = os.listdir(path)
os.chdir(path)
print 'Extracting individual Submissions','\n'

for i in Submissions:
	os.system('tar -xvf %s'%i)
	os.system('rm -r %s'%i)

Individual_Submissions = os.listdir(path)
for i in Individual_Submissions:
	
	print 'Enter Directory of %s'%i
	print '\n'
	os.chdir(i)
	os.system('make')
	SERV_PATH = path
	
	
	print 'Checking server_f ...'
	
	
	os.system('./server_f' + ' ' + PORT_SERV_F + ' ' + SERV_PATH + '/'+	' ' + SERV_PATH + '/' + i + '/' +LOG_SERV_F)
	''' Query to test server_f whose contents are written in flog.txt'''

	print 'Testing for Small File', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /small_file.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_F)

	print 'Testing for Large File', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_F)

	print 'Testing for Missing File', '\n'
	for i in range(2):
		os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_F)

	print 'Testing for Wrong Query', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /largefile.txt HP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n" \
			&& sleep 5) | nc 127.0.0.1 ' + PORT_SERV_F)

	os.system('pkill server_f')



	print 'Checking server_p ...'
	
	os.system('./server_p' + ' ' + PORT_SERV_P + ' ' + SERV_PATH + '/'+ ' ' + SERV_PATH+ '/' +i + '/' +LOG_SERV_P)
	''' Query to test server_f whose contents are written in flog.txt'''

	print 'Testing for Small File', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /small_file.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_P)

	print 'Testing for Large File', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_P)

	print 'Testing for Missing File', '\n'
	for i in range(2):
		os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_P)

	print 'Testing for Wrong Query', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /largefile.txt HP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n" \
			&& sleep 5) | nc 127.0.0.1 ' + PORT_SERV_P)

	os.system('pkill server_p')




	print 'Checking server_s ...'
	
	os.system('./server_s' + ' ' + PORT_SERV_S + ' ' + SERV_PATH + '/'+ ' ' + SERV_PATH + '/'+ i + '/' + LOG_SERV_S)
	''' Query to test server_f whose contents are written in flog.txt'''

	print 'Testing for Small File', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /small_file.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_S)

	print 'Testing for Large File', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_S)

	print 'Testing for Missing File', '\n'
	for i in range(2):
		os.system('(echo -ne "GET /largefile.txt HTTP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n"\
			 && sleep 5) | nc 127.0.0.1 ' + PORT_SERV_S)

	print 'Testing for Wrong Query', '\n'
	for i in range(10):
		os.system('(echo -ne "GET /largefile.txt HP/1.1\nFrom: \
			someuser@somewhere.org\nUser-Agent: Bloatzilla/7.0\n\n" \
			&& sleep 5) | nc 127.0.0.1 ' + PORT_SERV_S)

	os.system('pkill server_s')
	os.chdir('../')



