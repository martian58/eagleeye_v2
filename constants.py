version="v1.0.0"

red='\033[0;31m'
bold_red='\033[1;31m'
reset='\033[0m'
bold_blue='\033[1;34m'
bold_green='\033[1;32m'
warning_yellow='\033[1;33m' 
bold_white='\033[1;37m'
bold_pink='\033[1;35m'
brown='\033[0;33m'
bold_brown='\033[1;33m'
violet = "\033[95m"

class constants:
    def __init__(self) -> None:
        pass

    def help():

        print(f"""
           {bold_green}****** Available Commands ******{reset}
    
    help          -          prints this help message.
    scan          -          scans the network.
    hosts         -          shows the previously scanned network.
    alarm         -          listens for network faults.
    clear         -          clears the screen. 
    exit          -          exit the program.  

    """)
        
    def intro():
        print(f"""{violet}
                                                                     
 %%                                                               %% 
  %%%%                                                         %%%%  
   %%%%%%%@                                                %%%%%%%   
    %%%%%%%%%%%                                        %%%%%%%%%%%   
     %%%%  %%%%%%%%                               %%%%%%%%   %%%     
      %%%%      %%%%%%%         %%%%%%%       %%%%%%%%      %%%      
       %%%%     %%%%%%%%%%       %%%%%%%    %%%%%%%%%      %%%       
        %%%%    %%%%%%%%%%%      %%%%     %%%%%%%%%%%     %%%        
         %%%%    %%%%%%%%%%%%   %%%%%%   %%%%%%%%%%%     %%%         
          %%%%     %%%%%% %%%%  %%%%%% %%%%  %%%%%      %%%          
            %%%%            %%%  %%%% %%%%            %%%%           
              %%%%%          %%%% %  %%%%          %%%%%             
                  %%%%%%%%    %%%% %%%%     %%%%%%%%                 
                                %%%%%%                               
                                 %%%                                 
                                  %\n
                               {bold_green}{version}{reset}
                        \n{bold_blue}Github: martian58, a1rzayev{reset}                           
{reset}\n""")
        print(f"\n")