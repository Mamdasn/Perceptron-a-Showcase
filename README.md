# Perceptron
This snippet of code is a showcase on how a Perceptron works. In more details, This program gets N latest inputs of the user, which are 1s and 0s, and feeds them to a Perceptron, which in turn, tries to figure out a general pattern in the input sequence. Eventually, After getting enough inputs from the user, the weights stop changing. In that point, if the hit rate frequency is above 50%, it is an indication that there is a recognizable pattern in the input sequence and the Perceptron has found it.  

## Usage
Simply type 1s and 0s to insert new inputs into the program:  
`111011011101101110110111011...`  
  

Control Keys:
*    n for reset
*    e for exit
*    1 for a green input (1)
*    0 for a red input (-1)
  

![screenshot-of-the-program.jpg](https://raw.githubusercontent.com/Mamdasn/Perceptron-a-Showcase/main/assets/screenshot-of-the-program.jpg "screenshot-of-the-program.jpg")  

## Exploitation
Try your best to exploit the program.
See if you can figure these out:
* find a sequence in which the hit frequency is zero
* produce a random sequence and try to have a hit frequency of under 50%
* use a computer generated random sequence as the input and check if the hit frequency is about 50%
