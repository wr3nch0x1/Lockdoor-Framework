import os
import sys
from lockdoors import main
from pathlib import Path
from datetime import datetime
from time import sleep
##########SHRT
def oktocont():
    ans = input("\033[0;36mPress Enter to Continue...\033[0m")
def clr():
    os.system('clear')
def spc():
    print("")
def prilogspc():
    main.printlogo()
    spc()
def clscprilo():
    clr()
    main.printlogo()
############
def show():
    clscprilo()
    print("""

    #############################################################
    #                   Lockdoor Framework                      #
    #  A Penetration Testing framework with CyberSec Resources  #
    #############################################################
    #    -- Version: v2.2.4 15/08/2020                          #
    #    -- Developer: Sofiane Hamlaoui                         #
    #    -- Thanks: No One                                      #
    #############################################################

                        \033[94m-[!]-Description-[!]-\033[91m
   LockDoor is a Framework aimed at helping penetration testers,
   bug bounty hunters And cyber security engineers.
   This tool is designed for Debian/Ubuntu/ArchLinux based
   distributions to create a similar and familiar distribution
   for Penetration Testing. But containing the favorite and the most used tools by
   Pentesters.
   As pentesters, most of us has his personal ' /pentest/ ' directory so this
   Framework is helping you to build a perfect one.
    """)
    oktocont()
    main.menu()
