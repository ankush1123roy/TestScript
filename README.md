Test Script to Check Clinet Server Protocol in C
-------------------------------------------------

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
    
    Multiple Instances would of these would be run to check for multiple client handling by the server"")
    
    Two test files
    
    1. Large (8995 Characters) test file 
    2. Small (42 Characters ) test file
