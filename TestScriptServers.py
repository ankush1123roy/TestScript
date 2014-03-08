''' Script to Check Server Client Protocol
	
	The Servers are ought to follow HTTP 1.1. Protocol

	Three servers to test 

	1. Forked server - server_f
	2. Threaded server - server_p
	3. Select server - server_s


	Input from command line should be as follows
	--------------------------------------------

	./server_f port /path_of_docs /path_of_log_file

	QUERY TEST
	-----------

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

class run_server():
	
	def __init__(self, F, P, S, LF, LP, LS, PATH):
		self.path = PATH
		self.PORT_SERV_F = F
		self.PORT_SERV_P = P
		self.PORT_SERV_S = S
		self.LOG_SERV_F  = LF
		self.LOG_SERV_P  = LP
		self.LOG_SERV_S  = LS

		
	def untar(self):
		
		Submissions = os.listdir(self.path)
		os.chdir(self.path)

		for i in Submissions:
			print 'Extracting individual Submissions%s'%i,'\n'
			os.system('tar -xvf %s'%i)
			os.system('rm -r %s'%i)
		
	def run_server(self,NAME):
		import pdb;pdb.set_trace()
		print "Running Forked Server of %s"%NAME
		os.system('./server_f' + ' ' + self.PORT_SERV_F + ' ' + self.path + NAME+ '/'+ ' ' + self.path + NAME + '/' + self.LOG_SERV_F)

		print "Running Threaded Server of %s"%NAME
		os.system('./server_p' + ' ' + self.PORT_SERV_P + ' ' + self.path + NAME+ '/'+ ' ' + self.path + NAME + '/' + self.LOG_SERV_P)
		
		print "Running Select Server of %s"%NAME
		os.system('./server_s' + ' ' + self.PORT_SERV_S + ' ' + self.path + NAME+ '/'+ ' ' + self.path + NAME + '/' + self.LOG_SERV_S)
		
	def kill_server(self):
		os.system('pkill server_f') 
		os.system('pkill server_p')
		os.system('pkill server_s')

		
class check_servers():
	
	def __init__(self, NO_CONN, DELAY):
		self.no_conn = NO_CONN
		self.delay = DELAY
		
	def check_fork(PORT):


		for i in range(self.no_conn):
			
			print 'Testing for Small files'
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

			print 'Testing for Small files'
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

			print 'Testing for Small files'
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



def main():
	PATH = '/cshome/ankush2/Desktop/TEST/TestScript/TEST_SIMULATE/'
	RUN  = run_server('8000', '8001', '8002', 'flog.txt', 'plog.txt', 'slog.txt', PATH )
	import pdb;pdb.set_trace()
#	RUN.untar()
	Individual_Submissions = os.listdir(PATH)
	CHECK = check_servers(10, 4)
	for i in Individual_Submissions:
		print 'Enter Directory of %s'%i
		print '\n'
		os.chdir(PATH  + i)
		os.system('make')
		RUN.run_server(i)
		print 'Checking FORK server'
		CHECK.check_fork('8000')
		
		print 'Checking Thread server'
		CHECK.check_thread('8001')
		
		print 'Checking Select server'
		CHECK.check_select('8002')


		RUN.kill_server()
		os.chdir('../')
	
	
	print 'Checking server_f ....'

if __name__ == '__main__':
	main()
	




