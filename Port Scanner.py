import socket

while True:
	try:
		host = raw_input("\n 	HOST: ")
		print '\n 	IP:', socket.gethostbyname(host), '\n'
		portas = [1,5,7,9,11,13,17,18,19,20,21,22,23,25,37,39,42,43,49,50,53,63,67,68,69,70,71,72,73,79,80,88,95,101,105,107,109,110,111,113,115,117,119,123,137,138,139,143,161,162,163,164,174,177,178,179,191,194,199,201,202,204,206,209,210,213,220,245,347,363,369,370,372,389,427,434,435,443,444,445,464,468,487,488,496,500,538,546,547,554,563,565,587,610,611,612,631,636,674,694,749,750,765,767,873,992,993,994,995,8080]

		for port in portas:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(0.1)
			connection = client.connect_ex((host, port))
			if connection == False:
				print ' OPEN', port
	except:
		print ' ERRO\n'

