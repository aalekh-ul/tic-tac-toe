import os


board=['-','-','-','-','-','-','-','-','-']


def print_board():
	print(board[0],'|',board[1],'|',board[2])
	print(board[3],'|',board[4],'|',board[5])
	print(board[6],'|',board[7],'|',board[8])

def winner():

	if board[0]==board[1]==board[2]!='-':
		return True
	elif board[3]==board[4]==board[5]!='-':
		return True
	elif board[6]==board[7]==board[8]!='-':
		return True
	elif board[0]==board[3]==board[6]!='-':
		return True
	elif board[1]==board[4]==board[7]!='-':
		return True
	elif board[2]==board[5]==board[8]!='-':
		return True
	elif board[0]==board[4]==board[8]!='-':
		return True
	elif board[2]==board[4]==board[6]!='-':
		return True
	else:
		False
	

def input_value():
	global board
	n=0
	print("Player1 is 'x' --------------------- Player2 is 'o' ")
	print_board()
	while n<9:
		
		p1=int(input("Player1 , Enter the value you want to fill-> "))
		os.system('cls')
		if(board[p1]=="-" and p1<=8):
			board[p1]='x'
			print_board()
			if(winner()==True):
				print("***********player1 won***********")
				break
			

			
		else:
			n=n-1
			print('wrong input')


		if(n==8):
			break

		
		p2=int(input("Player2 , Enter the value you want to fill-> "))
		os.system('cls')
		if(board[p2]=="-" and p2<=8):
			board[p2]='o'
			print_board()
			if(winner()==True):
				print("***********player2 won***********")
				break
			
			n=n+2
		else:
			n=n-1
			print('wrong input')

#hello i am aalekh motani and i made this game
#tic tac toe	
		

input_value()
