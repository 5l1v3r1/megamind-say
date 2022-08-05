'''
Megamind-say, A simple command line tool to make "memes" using the megamind "no bitches?" template
Copyright (C) 2022  Nexus/Nexuzzzz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import shutil, sys
from random import choice

terminal_size = shutil.get_terminal_size(fallback=(120, 50))

# format: (ascii art, padding character)
art = [
('''⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋
—————————————————————————————''', '—'),
(""".........','..........'',''''''''..................,:loddddddo;.........
............   ....'',,,,,,,',,,,,,''................;odxxxdddc.........        
..........  ...'',,,,,,,,,,,,,,,,,,,,,,,,'''''........:dkkxxxxo,......          
....',,..  ..',,,,,,,,;;,;;,,,,,,,,,,,,,,,,,,,,,''....'lxkkxxxd:......          
..';c:'.   .',;;;;;;,,;;;;;;,,;,,,,,,,,,,,,,,,,,,,,'...;dkkxxxxc.....           
,,;;;..   ..,;;;;;;;;;;;;;;;;;;;;,,;;;,,,,,,,,,,,,,,,,''cxkxxxxo'....           
c::,..   ..',;;;;;;;;;;;;;;;;;;;;,,,;;,,,,,,,,,,,,,,,,,,:dkkxxxo,...            
;;'..     .';;;;;;;;;;;;,,,,,;;;;,,,,,,,,,,,,,,,,,,,,,;;:oxkxdxd,...      .   ..
...        .,;;;;;;;;;,,,,,,,,;;;;,,,,,,,,,,,,,,,,,,,;;;:lxkxddd, ..        ....
.          .';;;;;;;,,,,,,,,,,;;;;;,,,,,,,,''''''',,,;,;:ldxxddo'  ...      ....
.      .    .';;;;;,,,,'''',,,,;;:::;,,,,''........',;;;:ldxxddl.  ..      .....
     ..'..   .';;;;,,'.......',;:cllc;,''....',,,,'..,;;:lxxxdo:.   .      .....
    .'''''..   .,;;,....','....,;codoc;,'..,cllllodl;';:cldxxdl'           .....
   .'''''''..   .,,'.,clllcc;...;coxxo:,'.':lc,..';oxc;clodxxo;.          ......
   .'''''''''..  .'':ol:;,'',,..,:oxxoc,..,cc,..   .ckocodxxxl'.          ......
   ..''''''.....  .;oo;..     ..':oxxdc,'.'cc,....  ,xkodxxkxl;,.         ......
..  .'''.......... ,dd:.  ..    .cdkkdl:,'.,:;'.''..;xdldkkkdl:'.         ......
''....''...........,do,. .',.  .,okOOkdlc;'.';:;;;;:clccdkkkoc:'          ......
'''................'ldc,.......'cxkOOOkddo:,''',;;;;;;:ldkkxl;,.          ......
''''................,colc:;;,',cdkOOOOOkkxdoc:;,,,,;;:codxxxoc'              ...
'...................'',;;;,'',cdxkOOOOOkkkxxdolcc::cclloddxxo;.               ..
...................';,'''''';codkkOOOOOOkkkkxxdollllllooddxd;                   
...................';;;;;;:clodxkOOOOOOkkkkkkkxoollllloodxo,                    
....................,;:::clodxxkOOOOOOOkxxxxkkxolllllloddxc.                    
.................. ..;::cloodxkOO0000OOkxxxxxxdlcccclooddx:.                    
...................  .;::ccoodxkOOOOOOkdoollloolccclloddxx:   .. ...            
.................     .;;;:llodxxxxxdlc:::::cooolllloddxxd,  ........     .'.   
................      .,;;;:clooolcc::ccllllooodooloodxxko.  ...........  .,,   
........................',;;::::;,,;clooooodddddddooodxkkl.  ..'..............  
.........     .......   .';;:;;;,,;:loddddxxxxxxxxddddxkk:.    .................
.......                  .,::::;;::cldxxxxkkkkkkkxxdddxkx,   ..    ........  ...
....          .          ..;:::cccllodxkkkOOO00OOkkxddxko.    ...               
..                        .,:cclllllodddxxxxxxxxxkkkxdxkc.                      
                       .....;::cc:::;;:::cclloddddxxxodd,                       
                      ...  .''.',,''''',,;;::clloddxdool.                       
                      ...   .'',,''......'',,;cloddxxdo:.                       
                     ...     .,,,'..   ...',;:clooddddo,.                  ..   
                             .',,'...  ...,;;:clloooooc..   .              .,.  
                              .,,,'......';;::cclloool;.......             .,.  
""", ' ')
]

def make(message) -> tuple:
    '''
    make(no arguments?) -> (title, ascii art)

    Creates the ASCII art with the given message

    :param message str: The text to display on top of the ASCII art
    :returns tuple: The centered title and the art
    '''

    ascii_art, padding_char = choice(art) # picks a random one
    length = len(ascii_art.split('\n')[0]) # gets the length of the first line

    title = message.center(length, padding_char)

    return title, ascii_art

if __name__ == '__main__':
    msg = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'no input?'
    title, ascii_art = make(msg)

    print(title) # prints the message
    print(ascii_art) # prints the art