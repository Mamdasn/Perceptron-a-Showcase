import pygame
import sys

window = pygame.display.set_mode((620,450))
pygame.display.set_caption("Time Series Analysis")

WHITE = [255, 255, 255]
RED = [200,0,0]
GREEN = [0,200,0]
BLACK = [20,20,20]
GRAY = [128,128,128]

window.fill(WHITE)
pygame.display.flip()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
myfont_small = pygame.font.SysFont("Times New Roman", 11, bold=False, italic=False)


radius = 10

# Initilize the GUI
def initialize_screen(window):
    window.fill(WHITE)
    for i in range(10):
        pygame.draw.lines(window,  BLACK, False, [(27+28*(i+1),35), (177,150)], 1)
    for i in range(21):
        pygame.draw.circle(window,GRAY,(28*(i+1),20),radius) # DRAW 21 INPUT CIRCLES  
    pygame.draw.circle(window,GRAY,(177, 165),radius) # DRAW THE PREDICTION CIRCLE

    pygame.draw.circle(window,GREEN,(310, 100+8),radius) # HELPER
    window.blit(myfont.render('1=neuron active', True, BLACK),(330,100)) # HELPER

    pygame.draw.circle(window,RED,(310, 130+8),radius) # HELPER
    window.blit(myfont.render('0=neuron quiescent', True, BLACK),(330,130)) # HELPER

    window.blit(myfont_small.render('Prediction for the INPUT', True, BLACK),(117,185)) # HELPER
    pygame.draw.lines(window,  BLACK, False, [(167,180), (187,180)], 1) # HELPER

    window.blit(myfont_small.render('INPUT', True, BLACK),(12,40)) # HELPER
    pygame.draw.lines(window,  BLACK, False, [(18,35), (38,35)], 1) # HELPER

    pygame.draw.lines(window,  BLACK, False, [(25,339), (320,339)], 2) # HELPER FOR PLOTTING WEIGHTS
    window.blit(myfont.render("weight distribution", True, BLACK),(330,330)) # HELPER FOR PLOTTING WEIGHTS
    
    window.blit(myfont.render("Commands: 1, 0, [n]ew statistics, [e]nd", True, BLACK),(330,400)) # HELPER

initialize_screen(window)
pygame.display.update()


import random

# Number of input neurons 
N = 10
# Initialize variables
runs = 0
corrects = 0
neuron = []
neuron_last_21 = []
weights = [0 for _ in range(N)]
lastNpredictionStatus = []
y = 0

while True:
    # User input controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # n for new statistics
            if event.key == pygame.K_n: 
                neuron = []
                neuron_last_21 = []
                weights = [0 for _ in range(N)]
                initialize_screen(window)
                pygame.display.update()
                continue
            # e for exit
            elif event.key == pygame.K_e:
                sys.exit()
            # 1 for  1
            elif event.key == pygame.K_1:
                y = 1
                break
            # 0 for -1
            elif event.key == pygame.K_0:
                y = -1
                break
    else:
        continue

    # Increment number of runs
    runs += 1

    # Predict the y
    h = 0
    for each_neuron, each_weight in zip(neuron, weights):
        h += each_weight * each_neuron
    
    if h * y > 0:
        # The prediction is correct.
        corrects += 1
    # If a wrong prediction happened, update the weights
    if h * y <= 0:
        for i in range(len(neuron)):
            weights[i] += y * neuron[i] / len(neuron) 
    
    # This is for the sake of calculating the accuracy of the predictions 
    lastNpredictionStatus.append(h * y > 0)
    if len(lastNpredictionStatus) > N:
        lastNpredictionStatus = lastNpredictionStatus[-N:]


    # Append the user input to the input neurons
    neuron.append(y)
    if len(neuron) > N:
        neuron = neuron[-N:]

    # Save last 21 user input for further calculation
    neuron_last_21.append(y)
    if len(neuron_last_21) > 21:
        neuron_last_21 = neuron_last_21[-21:]

    # Calculate hit frequency
    hit_frequency = round(corrects/runs * 100, 2)
    # Calculate hit frequency for the last N user inputs
    hit_frequency_N = round(sum(lastNpredictionStatus)/len(lastNpredictionStatus) * 100, 2)

    prediction = 1 if h > 0 else -1

    # Draw colored circles for the last 21 user inputs
    for i in range(len(neuron_last_21)):
        length_of_neuron_last_21 = len(neuron_last_21)
        color = RED if neuron_last_21[length_of_neuron_last_21-1-i] == -1 else GREEN
        pygame.draw.circle(window,color,(28*(i+1),20),radius) # DRAW CIRCLE
    
    # Draw the prediction circle
    color = RED if prediction == -1 else GREEN
    pygame.draw.circle(window,color,(177, 165),radius) # DRAW CIRCLE

    window.blit(myfont.render('The prediction is correct' if h * y > 0 else \
        'The prediction is incorrect', True, BLACK),(300,200))
    window.blit(myfont.render(f"hit percentage: {hit_frequency}%"\
         , True, BLACK),(300,220))
    window.blit(myfont.render(f"hit percentage for the last {N} steps: {hit_frequency_N}%"\
         , True, BLACK),(300,240))

    # Draw weights
    for i in range(N):
        bar = -int(weights[i]*100//1)
        top = 340
        if bar > 0:                                   # left, top, width, height
            pygame.draw.rect(window, BLACK, pygame.Rect(30*(i+1), top, 15, bar), 1)
        else:
            pygame.draw.rect(window, BLACK, pygame.Rect(30*(i+1), top+bar, 15, abs(bar)), 1)
    
    
    pygame.display.update()
    initialize_screen(window)

