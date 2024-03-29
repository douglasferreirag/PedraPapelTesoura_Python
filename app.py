import random






def start(): 

    print('')

    print('')

    print('')

    print('Mini-Game JokenPo')

    print('')

    print('')
    
    print('')

  

def game():

    options = ["rock", "paper", "scissors"]

    userPoints = 0

    computerPoints  = 0

    print('Choose between rock, paper or scissors.')

    print('')

    userChoose = input()


    while(True):
   

        if(userChoose in options):
        
            computerChoose = random.choice(options)

            if(winner(userChoose, computerChoose) ==  0): 

                print("Draw")

            if(winner(userChoose, computerChoose) ==  1): 

                print('') 
                
                print('User win!')

                print('')

                userPoints += 1
            
            if(winner(userChoose, computerChoose) ==  2): 

                print('')
                 
                print('Computer win!')

                print('')

                computerPoints += 1



        else:
            print("escoheu errado. Encerrando")

            print('')

            print('')
    
            print('')

            break

        
        print('')

        print('')
        
        print('')

        print('Choose between rock, paper or scissors.')

        print('')

        userChoose = input()
        
    print('User points: ' + str(userPoints))
    print('Computer points : ' + str(computerPoints)) 


def winner(user,computer):

    if  ( ( (user == 'rock' ) and (computer == 'scissors') ) or
         ( (user == 'scissors' ) and (computer == 'paper') ) or
         ( (user == 'paper' ) and (computer == 'rock') )
        ):
       
            return 1
    
    if  ( ( (computer == 'rock' ) and (user == 'scissors') ) or
         ( (computer == 'scissors' ) and (user == 'paper') ) or
         ( (computer == 'paper' ) and (user == 'rock') )
        ):
         
            return 2
    
    return 0

        


            





if __name__ == '__main__':

    start()

    game()