#!/usr/bin/env python

# This is a curses version of Borges.
# Based on Jorge Luis Borges' story The Library in Babel
# This program creates books and runs programs all based on stories by Borges

import os
from os import system
import curses

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print ""
    if a != 0:
        print "Command terminated with error"
    raw_input("Press enter")
x = 0

while x != ord('4'):
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    screen.addstr(1, 1, " ____________________________________________________")
    screen.addstr(2, 1, "| __     __   ____   ___ ||  ____    ____     _  __  |")
    screen.addstr(3, 1, "||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | | ")
    screen.addstr(4, 1, "||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |  The Library In Babel")
    screen.addstr(5, 1, "||  |##||  | | || | |JLB|||-|  | |==|+|+||-|-|~||__| | ")
    screen.addstr(6, 1, "||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_| ")
    screen.addstr(7, 1, "||_______________________||__________________________| ")
    screen.addstr(8, 1, "| _____________________  ||      __   __  _  __    _ |    (b)rowse books")
    screen.addstr(9, 1, "||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|    (g)enerate a book")
    screen.addstr(10, 1, "|| | | | | | | | | | | |/\ \  \\\|++|=|  || ||==| / / |    (a)bout")
    screen.addstr(11, 1, "||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|    (q)uit ")
    screen.addstr(12, 1, "|____________________ /\~()/()~//\ __________________|")
    screen.addstr(13, 1, "| __   __    _  _     \_  (_ .  _/ _    ___     _____|")
    screen.addstr(14, 1, "||~~|_|..|__| || |_ _   \ //\\\ /  |=|__|~|~|___| | | |")
    screen.addstr(15, 1, "||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|")
    screen.addstr(16, 1, "||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|")
    screen.addstr(17, 1, "|_________________ _/    \/\/\/    \_ _______________|")
    screen.addstr(18, 1, "| _____   _   __  |/      \../      \|  __   __   ___|")
    screen.addstr(19, 1, "||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||")
    screen.addstr(20, 1, "||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||")
    screen.addstr(21, 1, "||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||")
    screen.addstr(22, 1, "|_________ __________\___\____/___/___________ ______|")
    #screen.addstr(23, 1, "|__    _  /    ________     ______           /| _ _ _|")
    #screen.addstr(24, 1, "|\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|")
    #screen.addstr(25, 1, "| \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|")
    #screen.addstr(26, 1, "|  \/\|/   /(____|/ //                    /  /||~|~|~|")
    #screen.addstr(27, 1, "|___\_/   /________//   ________         /  / ||_|_|_|")
    #screen.addstr(28, 1, "|___ /   (|________/   |\_______\       /  /| |______|")
    #screen.addstr(29, 1, "    /                  \|________)     /  / | |")
    screen.refresh()
    x = screen.getch()
    if x == ord("q"): break
    elif x == ord('b'):
        curses.endwin()
        execute_cmd("ls books")
    elif x == ord('g'):
        curses.endwin()
        title = raw_input('Enter a book title: ')
        content = raw_input('Enter your book text: ')
        book = open(title+".txt","w") #how to file this inside /books
        book.write(content)
        book.close()
        
    elif x == ord('f'):
        curses.endwin()
        execute_cmd("fortune | cowsay")
    elif x == ord('b'):
        curses.endwin()
        execute_cmd("python ~/Documents/pythonprograms/blackjack.py")
    elif x == ord('s'):
        curses.endwin()
        execute_cmd("ncmpcpp")
    elif x == ord('w'):
        curses.endwin()
        execute_cmd("lynx -dump -term=vt100 https://weather.yahoo.com/united-states/pennsylvania/philadelphia-12765511/")
    elif x == ord('c'):
        curses.endwin()
        execute_cmd("google calendar list | less -FX")
    elif x == ord('l'):
        curses.endwin()
        execute_cmd("sl")
    elif x == ord('t'):
        curses.endwin()
        execute_cmd("google calendar list --date today")
curses.endwin()
execute_cmd("clear")
