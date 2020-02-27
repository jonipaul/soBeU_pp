#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on February 27, 2020, at 12:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'so_be_u_00'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='P:\\userdata\\jonasn84\\shared\\experiments\\soBeU_pp\\soBeU_02_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "wScr"
wScrClock = core.Clock()
textWelcomeText =(
'Dear Participant, \n'
'Welcome to our experiement! \n'
'Please carefully go over the instructions on the following pages. \n'
'If you have any questions please ask the experimenter for help. \n\n'
'Press any key to continue'
)

textInstructionsText= (
'You have been randomly assigned to condition B. \n\n'
'In the following task you will repeatedly interact with two other players.You will have to make choices on how to engage with the other players.\n'
'You will make investments and try to maximize your gains (credits).\n\n'
'Following a choice you will receive a short feedback on how the other player has acted.\n'
'At the end of all interactions one random interaction will be selected and payed-out the sum of credits gained.\n\n'
'see next page for more information.\n'
'Press c to continue.'
)

textInstructionsText2 = """
The goal is to maximize your gains.\n
Every round you will receive an endowment of 10 credits.
You will have the choice to invest part (or all) of these credits in another player.
The credits that you invest get triple when transfered to the other player.
The other player can then decide what to do with that investment. 
They will then have to decide how many credits they want to send back to you (0% - 200%).

For example:
You decide to invest 5 credits. That money gets tripled to 15 credits.
The other player decides to send back 150% of the investment.

The toal for this round is 12.5 credits.
5 credits that you did not invest, plus 7.5 from the investement that you received back.
The other player gains 7.5 credits.

Press c to continue.
"""

textProfileText = """
Please type your player-name: \n
Importantly, this is not supposed to be your real name, just a name that other players can identify you with.
Type a name, and press 'enter' when you are ready.
"""

textServerText= """
We will now connect you to the the other Players through the Server.\n
This might take a minute.\n
Please contact the Experimenter if your Computer is unabled to connect.\n
Press c to continue.
"""

textInstructionsSb = """
You are now ready to start with the experiment. \n
On the next screens you will make decisions on how to engage with other players.\n\n
Make a choice using your left or right keys and confirm with enter

Note, all decisions (yours and others) happen simultaneously, and not in response to each other.

Press c to begin.
"""

textSbText = 'How much do you want to invest?'

textSbFeed1 = ' has decided to return '
textSbFeed2 = ' percent of your investment. \n\n'
textSbFeed3 = 'Your return is '
textSbFeed4 = ' credits!\n\n'
textSbFeed5 = 'Your total gain for this round is '

textEndText = """Thank you for participating.

This part of the experiment is now completed.
"""

textEndText2 = 'We randomly selected one interaction. Your gain is: '
textEndText3 = '\nPlease wait for the experimenter before continuing'

bufText = """waiting for other player"""
cB_1 = visual.Rect(
    win=win, name='cB_1',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
keyWelcome = keyboard.Keyboard()
out_0 = keyboard.Keyboard()

# Initialize components for Routine "wIns"
wInsClock = core.Clock()
cB_2 = visual.Rect(
    win=win, name='cB_2',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textInstructions = visual.TextStim(win=win, name='textInstructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
keyInstructions = keyboard.Keyboard()
out_1 = keyboard.Keyboard()

# Initialize components for Routine "wIns2"
wIns2Clock = core.Clock()
cB_12 = visual.Rect(
    win=win, name='cB_12',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textInstructions_2 = visual.TextStim(win=win, name='textInstructions_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyInstructions_2 = keyboard.Keyboard()
out_3 = keyboard.Keyboard()

# Initialize components for Routine "wPfl"
wPflClock = core.Clock()
cB = visual.Rect(
    win=win, name='cB',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
import string
allLetters = list(string.ascii_lowercase)
displayText = visual.TextStim(win=win, name='displayText',
    text='default text',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
copyText = visual.TextStim(win=win, name='copyText',
    text=None,
    font='Arial',
    pos=(0, - 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
out = keyboard.Keyboard()

# Initialize components for Routine "wSer"
wSerClock = core.Clock()
cB_3 = visual.Rect(
    win=win, name='cB_3',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textServer = visual.TextStim(win=win, name='textServer',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
keyServer = keyboard.Keyboard()
out_2 = keyboard.Keyboard()

# Initialize components for Routine "bufRou_2"
bufRou_2Clock = core.Clock()
cB_4 = visual.Rect(
    win=win, name='cB_4',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_1 = visual.TextStim(win=win, name='text_1',
    text='connecting      ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='connecting .    ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='connecting . .  ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='connecting . . .',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "bufEnd"
bufEndClock = core.Clock()
cB_5 = visual.Rect(
    win=win, name='cB_5',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
idle = visual.TextStim(win=win, name='idle',
    text='found',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
idle_2 = visual.TextStim(win=win, name='idle_2',
    text='init proc     ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
idle_3 = visual.TextStim(win=win, name='idle_3',
    text='init proc 2141',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
idle_4 = visual.TextStim(win=win, name='idle_4',
    text='init proc 2215',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
idle_5 = visual.TextStim(win=win, name='idle_5',
    text='init proc 3229',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
idle_6 = visual.TextStim(win=win, name='idle_6',
    text='init proc 4325',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
idle_7 = visual.TextStim(win=win, name='idle_7',
    text='init proc 1337',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
ilde_8 = visual.TextStim(win=win, name='ilde_8',
    text='buffering      ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
idle_9 = visual.TextStim(win=win, name='idle_9',
    text='buffering .    ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
idle_10 = visual.TextStim(win=win, name='idle_10',
    text='buffering . .  ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
idle_11 = visual.TextStim(win=win, name='idle_11',
    text='buffering . . .',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
idle_12 = visual.TextStim(win=win, name='idle_12',
    text='run /serv/234_1/sd connect',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "sbIn"
sbInClock = core.Clock()
sbTotal = 0
sbTotalPaul= 0
sbTotalLukas =0
cB_6 = visual.Rect(
    win=win, name='cB_6',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
sBInstructions = visual.TextStim(win=win, name='sBInstructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
keySbInstructions = keyboard.Keyboard()
out_sb = keyboard.Keyboard()

# Initialize components for Routine "sbRnd"
sbRndClock = core.Clock()
cB_8 = visual.Rect(
    win=win, name='cB_8',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
imagesbRnd = visual.ImageStim(
    win=win,
    name='imagesbRnd', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sbChoice = visual.RatingScale(win=win, name='sbChoice', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], tickHeight=-1, markerStart='5')
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "bufWait"
bufWaitClock = core.Clock()
cB_9 = visual.Rect(
    win=win, name='cB_9',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "sbFb"
sbFbClock = core.Clock()
import random

roundGain = []
cbFb = visual.Rect(
    win=win, name='cbFb',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textFb = visual.TextStim(win=win, name='textFb',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
out_Fb = keyboard.Keyboard()

# Initialize components for Routine "bufFix"
bufFixClock = core.Clock()
cbBuf = visual.Rect(
    win=win, name='cbBuf',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "sbQu1"
sbQu1Clock = core.Clock()
cB_11 = visual.Rect(
    win=win, name='cB_11',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
rating_they = visual.RatingScale(win=win, name='rating_they', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')

# Initialize components for Routine "sbQu2"
sbQu2Clock = core.Clock()
cB_14 = visual.Rect(
    win=win, name='cB_14',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
rating_you = visual.RatingScale(win=win, name='rating_you', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')

# Initialize components for Routine "bufWait"
bufWaitClock = core.Clock()
cB_9 = visual.Rect(
    win=win, name='cB_9',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "bufFix"
bufFixClock = core.Clock()
cbBuf = visual.Rect(
    win=win, name='cbBuf',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "reset"
resetClock = core.Clock()
cB_13 = visual.Rect(
    win=win, name='cB_13',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "sbRnd"
sbRndClock = core.Clock()
cB_8 = visual.Rect(
    win=win, name='cB_8',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
imagesbRnd = visual.ImageStim(
    win=win,
    name='imagesbRnd', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sbChoice = visual.RatingScale(win=win, name='sbChoice', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], tickHeight=-1, markerStart='5')
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "bufWait"
bufWaitClock = core.Clock()
cB_9 = visual.Rect(
    win=win, name='cB_9',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "sbFb"
sbFbClock = core.Clock()
import random

roundGain = []
cbFb = visual.Rect(
    win=win, name='cbFb',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textFb = visual.TextStim(win=win, name='textFb',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
out_Fb = keyboard.Keyboard()

# Initialize components for Routine "bufFix"
bufFixClock = core.Clock()
cbBuf = visual.Rect(
    win=win, name='cbBuf',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "sbQu1"
sbQu1Clock = core.Clock()
cB_11 = visual.Rect(
    win=win, name='cB_11',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
rating_they = visual.RatingScale(win=win, name='rating_they', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')

# Initialize components for Routine "sbQu2"
sbQu2Clock = core.Clock()
cB_14 = visual.Rect(
    win=win, name='cB_14',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
rating_you = visual.RatingScale(win=win, name='rating_you', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')

# Initialize components for Routine "bufWait"
bufWaitClock = core.Clock()
cB_9 = visual.Rect(
    win=win, name='cB_9',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "bufFix"
bufFixClock = core.Clock()
cbBuf = visual.Rect(
    win=win, name='cbBuf',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "sbEnd"
sbEndClock = core.Clock()
cB_10 = visual.Rect(
    win=win, name='cB_10',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
sbEndText = visual.TextStim(win=win, name='sbEndText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sbEndKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wScr"-------
# update component parameters for each repeat
textWelcome.setText(textWelcomeText
)
keyWelcome.keys = []
keyWelcome.rt = []
out_0.keys = []
out_0.rt = []
# keep track of which components have finished
wScrComponents = [cB_1, textWelcome, keyWelcome, out_0]
for thisComponent in wScrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wScrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wScr"-------
while continueRoutine:
    # get current time
    t = wScrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wScrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_1* updates
    if cB_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_1.frameNStart = frameN  # exact frame index
        cB_1.tStart = t  # local t and not account for scr refresh
        cB_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_1, 'tStartRefresh')  # time at next scr refresh
        cB_1.setAutoDraw(True)
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyWelcome.keys = theseKeys.name  # just the last key pressed
            keyWelcome.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *out_0* updates
    waitOnFlip = False
    if out_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        out_0.frameNStart = frameN  # exact frame index
        out_0.tStart = t  # local t and not account for scr refresh
        out_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(out_0, 'tStartRefresh')  # time at next scr refresh
        out_0.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(out_0.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(out_0.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if out_0.status == STARTED and not waitOnFlip:
        theseKeys = out_0.getKeys(keyList=['1'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            out_0.keys = theseKeys.name  # just the last key pressed
            out_0.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wScrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wScr"-------
for thisComponent in wScrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_1.started', cB_1.tStartRefresh)
thisExp.addData('cB_1.stopped', cB_1.tStopRefresh)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.addData('keyWelcome.started', keyWelcome.tStartRefresh)
thisExp.addData('keyWelcome.stopped', keyWelcome.tStopRefresh)
thisExp.nextEntry()
# check responses
if out_0.keys in ['', [], None]:  # No response was made
    out_0.keys = None
thisExp.addData('out_0.keys',out_0.keys)
if out_0.keys != None:  # we had a response
    thisExp.addData('out_0.rt', out_0.rt)
thisExp.addData('out_0.started', out_0.tStartRefresh)
thisExp.addData('out_0.stopped', out_0.tStopRefresh)
thisExp.nextEntry()
# the Routine "wScr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wIns"-------
# update component parameters for each repeat
textInstructions.setText(textInstructionsText)
keyInstructions.keys = []
keyInstructions.rt = []
out_1.keys = []
out_1.rt = []
# keep track of which components have finished
wInsComponents = [cB_2, textInstructions, keyInstructions, out_1]
for thisComponent in wInsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wInsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wIns"-------
while continueRoutine:
    # get current time
    t = wInsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wInsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_2* updates
    if cB_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_2.frameNStart = frameN  # exact frame index
        cB_2.tStart = t  # local t and not account for scr refresh
        cB_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_2, 'tStartRefresh')  # time at next scr refresh
        cB_2.setAutoDraw(True)
    
    # *textInstructions* updates
    if textInstructions.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        textInstructions.frameNStart = frameN  # exact frame index
        textInstructions.tStart = t  # local t and not account for scr refresh
        textInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInstructions, 'tStartRefresh')  # time at next scr refresh
        textInstructions.setAutoDraw(True)
    
    # *keyInstructions* updates
    waitOnFlip = False
    if keyInstructions.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        keyInstructions.frameNStart = frameN  # exact frame index
        keyInstructions.tStart = t  # local t and not account for scr refresh
        keyInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstructions, 'tStartRefresh')  # time at next scr refresh
        keyInstructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstructions.status == STARTED and not waitOnFlip:
        theseKeys = keyInstructions.getKeys(keyList=['c'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyInstructions.keys = theseKeys.name  # just the last key pressed
            keyInstructions.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *out_1* updates
    waitOnFlip = False
    if out_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        out_1.frameNStart = frameN  # exact frame index
        out_1.tStart = t  # local t and not account for scr refresh
        out_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(out_1, 'tStartRefresh')  # time at next scr refresh
        out_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(out_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(out_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if out_1.status == STARTED and not waitOnFlip:
        theseKeys = out_1.getKeys(keyList=['1'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            out_1.keys = theseKeys.name  # just the last key pressed
            out_1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wInsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wIns"-------
for thisComponent in wInsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_2.started', cB_2.tStartRefresh)
thisExp.addData('cB_2.stopped', cB_2.tStopRefresh)
thisExp.addData('textInstructions.started', textInstructions.tStartRefresh)
thisExp.addData('textInstructions.stopped', textInstructions.tStopRefresh)
# check responses
if keyInstructions.keys in ['', [], None]:  # No response was made
    keyInstructions.keys = None
thisExp.addData('keyInstructions.keys',keyInstructions.keys)
if keyInstructions.keys != None:  # we had a response
    thisExp.addData('keyInstructions.rt', keyInstructions.rt)
thisExp.addData('keyInstructions.started', keyInstructions.tStartRefresh)
thisExp.addData('keyInstructions.stopped', keyInstructions.tStopRefresh)
thisExp.nextEntry()
# check responses
if out_1.keys in ['', [], None]:  # No response was made
    out_1.keys = None
thisExp.addData('out_1.keys',out_1.keys)
if out_1.keys != None:  # we had a response
    thisExp.addData('out_1.rt', out_1.rt)
thisExp.addData('out_1.started', out_1.tStartRefresh)
thisExp.addData('out_1.stopped', out_1.tStopRefresh)
thisExp.nextEntry()
# the Routine "wIns" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wIns2"-------
# update component parameters for each repeat
textInstructions_2.setText(textInstructionsText2)
keyInstructions_2.keys = []
keyInstructions_2.rt = []
out_3.keys = []
out_3.rt = []
# keep track of which components have finished
wIns2Components = [cB_12, textInstructions_2, keyInstructions_2, out_3]
for thisComponent in wIns2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wIns2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wIns2"-------
while continueRoutine:
    # get current time
    t = wIns2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wIns2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_12* updates
    if cB_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_12.frameNStart = frameN  # exact frame index
        cB_12.tStart = t  # local t and not account for scr refresh
        cB_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_12, 'tStartRefresh')  # time at next scr refresh
        cB_12.setAutoDraw(True)
    
    # *textInstructions_2* updates
    if textInstructions_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        textInstructions_2.frameNStart = frameN  # exact frame index
        textInstructions_2.tStart = t  # local t and not account for scr refresh
        textInstructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInstructions_2, 'tStartRefresh')  # time at next scr refresh
        textInstructions_2.setAutoDraw(True)
    
    # *keyInstructions_2* updates
    waitOnFlip = False
    if keyInstructions_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        keyInstructions_2.frameNStart = frameN  # exact frame index
        keyInstructions_2.tStart = t  # local t and not account for scr refresh
        keyInstructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstructions_2, 'tStartRefresh')  # time at next scr refresh
        keyInstructions_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstructions_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstructions_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstructions_2.status == STARTED and not waitOnFlip:
        theseKeys = keyInstructions_2.getKeys(keyList=['c'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyInstructions_2.keys = theseKeys.name  # just the last key pressed
            keyInstructions_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *out_3* updates
    waitOnFlip = False
    if out_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        out_3.frameNStart = frameN  # exact frame index
        out_3.tStart = t  # local t and not account for scr refresh
        out_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(out_3, 'tStartRefresh')  # time at next scr refresh
        out_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(out_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(out_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if out_3.status == STARTED and not waitOnFlip:
        theseKeys = out_3.getKeys(keyList=['1'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            out_3.keys = theseKeys.name  # just the last key pressed
            out_3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wIns2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wIns2"-------
for thisComponent in wIns2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_12.started', cB_12.tStartRefresh)
thisExp.addData('cB_12.stopped', cB_12.tStopRefresh)
thisExp.addData('textInstructions_2.started', textInstructions_2.tStartRefresh)
thisExp.addData('textInstructions_2.stopped', textInstructions_2.tStopRefresh)
# check responses
if keyInstructions_2.keys in ['', [], None]:  # No response was made
    keyInstructions_2.keys = None
thisExp.addData('keyInstructions_2.keys',keyInstructions_2.keys)
if keyInstructions_2.keys != None:  # we had a response
    thisExp.addData('keyInstructions_2.rt', keyInstructions_2.rt)
thisExp.addData('keyInstructions_2.started', keyInstructions_2.tStartRefresh)
thisExp.addData('keyInstructions_2.stopped', keyInstructions_2.tStopRefresh)
thisExp.nextEntry()
# check responses
if out_3.keys in ['', [], None]:  # No response was made
    out_3.keys = None
thisExp.addData('out_3.keys',out_3.keys)
if out_3.keys != None:  # we had a response
    thisExp.addData('out_3.rt', out_3.rt)
thisExp.addData('out_3.started', out_3.tStartRefresh)
thisExp.addData('out_3.stopped', out_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "wIns2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wPfl"-------
# update component parameters for each repeat
modify = False
text.text = ''
event.clearEvents('keyboard')
displayText.setText(textProfileText)
copyText.setText('')
out.keys = []
out.rt = []
# keep track of which components have finished
wPflComponents = [cB, displayText, copyText, out]
for thisComponent in wPflComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wPflClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wPfl"-------
while continueRoutine:
    # get current time
    t = wPflClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wPflClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB* updates
    if cB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB.frameNStart = frameN  # exact frame index
        cB.tStart = t  # local t and not account for scr refresh
        cB.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB, 'tStartRefresh')  # time at next scr refresh
        cB.setAutoDraw(True)
    keys = event.getKeys()
    
    if len(keys):
        if 'space' in keys:
            text.text = text.text + ' '
        elif 'backspace' in keys:
            text.text = text.text[:-1]
        elif 'lshift' in keys or 'rshift' in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                text.text = text.text + keys[0].upper()
                modify = False
            else:
                text.text = text.text + keys[0]
        copyText.setText(text.text)
    
    # *displayText* updates
    if displayText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        displayText.frameNStart = frameN  # exact frame index
        displayText.tStart = t  # local t and not account for scr refresh
        displayText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(displayText, 'tStartRefresh')  # time at next scr refresh
        displayText.setAutoDraw(True)
    
    # *copyText* updates
    if copyText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        copyText.frameNStart = frameN  # exact frame index
        copyText.tStart = t  # local t and not account for scr refresh
        copyText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText, 'tStartRefresh')  # time at next scr refresh
        copyText.setAutoDraw(True)
    
    # *out* updates
    waitOnFlip = False
    if out.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        out.frameNStart = frameN  # exact frame index
        out.tStart = t  # local t and not account for scr refresh
        out.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(out, 'tStartRefresh')  # time at next scr refresh
        out.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(out.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(out.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if out.status == STARTED and not waitOnFlip:
        theseKeys = out.getKeys(keyList=['1'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            out.keys = theseKeys.name  # just the last key pressed
            out.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wPflComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wPfl"-------
for thisComponent in wPflComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB.started', cB.tStartRefresh)
thisExp.addData('cB.stopped', cB.tStopRefresh)
textName = text.text
thisExp.addData("typedWord", text.text)
thisExp.addData('displayText.started', displayText.tStartRefresh)
thisExp.addData('displayText.stopped', displayText.tStopRefresh)
thisExp.addData('copyText.started', copyText.tStartRefresh)
thisExp.addData('copyText.stopped', copyText.tStopRefresh)
# check responses
if out.keys in ['', [], None]:  # No response was made
    out.keys = None
thisExp.addData('out.keys',out.keys)
if out.keys != None:  # we had a response
    thisExp.addData('out.rt', out.rt)
thisExp.addData('out.started', out.tStartRefresh)
thisExp.addData('out.stopped', out.tStopRefresh)
thisExp.nextEntry()
# the Routine "wPfl" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wSer"-------
# update component parameters for each repeat
textServer.setText(textServerText)
keyServer.keys = []
keyServer.rt = []
out_2.keys = []
out_2.rt = []
# keep track of which components have finished
wSerComponents = [cB_3, textServer, keyServer, out_2]
for thisComponent in wSerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wSerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wSer"-------
while continueRoutine:
    # get current time
    t = wSerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wSerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_3* updates
    if cB_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_3.frameNStart = frameN  # exact frame index
        cB_3.tStart = t  # local t and not account for scr refresh
        cB_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_3, 'tStartRefresh')  # time at next scr refresh
        cB_3.setAutoDraw(True)
    
    # *textServer* updates
    if textServer.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        textServer.frameNStart = frameN  # exact frame index
        textServer.tStart = t  # local t and not account for scr refresh
        textServer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textServer, 'tStartRefresh')  # time at next scr refresh
        textServer.setAutoDraw(True)
    
    # *keyServer* updates
    waitOnFlip = False
    if keyServer.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        keyServer.frameNStart = frameN  # exact frame index
        keyServer.tStart = t  # local t and not account for scr refresh
        keyServer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyServer, 'tStartRefresh')  # time at next scr refresh
        keyServer.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyServer.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyServer.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyServer.status == STARTED and not waitOnFlip:
        theseKeys = keyServer.getKeys(keyList=['c'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyServer.keys = theseKeys.name  # just the last key pressed
            keyServer.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *out_2* updates
    waitOnFlip = False
    if out_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        out_2.frameNStart = frameN  # exact frame index
        out_2.tStart = t  # local t and not account for scr refresh
        out_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(out_2, 'tStartRefresh')  # time at next scr refresh
        out_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(out_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(out_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if out_2.status == STARTED and not waitOnFlip:
        theseKeys = out_2.getKeys(keyList=['1'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            out_2.keys = theseKeys.name  # just the last key pressed
            out_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wSerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wSer"-------
for thisComponent in wSerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_3.started', cB_3.tStartRefresh)
thisExp.addData('cB_3.stopped', cB_3.tStopRefresh)
thisExp.addData('textServer.started', textServer.tStartRefresh)
thisExp.addData('textServer.stopped', textServer.tStopRefresh)
# check responses
if keyServer.keys in ['', [], None]:  # No response was made
    keyServer.keys = None
thisExp.addData('keyServer.keys',keyServer.keys)
if keyServer.keys != None:  # we had a response
    thisExp.addData('keyServer.rt', keyServer.rt)
thisExp.addData('keyServer.started', keyServer.tStartRefresh)
thisExp.addData('keyServer.stopped', keyServer.tStopRefresh)
thisExp.nextEntry()
# check responses
if out_2.keys in ['', [], None]:  # No response was made
    out_2.keys = None
thisExp.addData('out_2.keys',out_2.keys)
if out_2.keys != None:  # we had a response
    thisExp.addData('out_2.rt', out_2.rt)
thisExp.addData('out_2.started', out_2.tStartRefresh)
thisExp.addData('out_2.stopped', out_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "wSer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
bufferLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='bufferLoop')
thisExp.addLoop(bufferLoop)  # add the loop to the experiment
thisBufferLoop = bufferLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBufferLoop.rgb)
if thisBufferLoop != None:
    for paramName in thisBufferLoop:
        exec('{} = thisBufferLoop[paramName]'.format(paramName))

for thisBufferLoop in bufferLoop:
    currentLoop = bufferLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBufferLoop.rgb)
    if thisBufferLoop != None:
        for paramName in thisBufferLoop:
            exec('{} = thisBufferLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "bufRou_2"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    bufRou_2Components = [cB_4, text_1, text_2, text_3, text_4]
    for thisComponent in bufRou_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    bufRou_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "bufRou_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = bufRou_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bufRou_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cB_4* updates
        if cB_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cB_4.frameNStart = frameN  # exact frame index
            cB_4.tStart = t  # local t and not account for scr refresh
            cB_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cB_4, 'tStartRefresh')  # time at next scr refresh
            cB_4.setAutoDraw(True)
        if cB_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cB_4.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                cB_4.tStop = t  # not accounting for scr refresh
                cB_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cB_4, 'tStopRefresh')  # time at next scr refresh
                cB_4.setAutoDraw(False)
        
        # *text_1* updates
        if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_1.frameNStart = frameN  # exact frame index
            text_1.tStart = t  # local t and not account for scr refresh
            text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
            text_1.setAutoDraw(True)
        if text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1.tStop = t  # not accounting for scr refresh
                text_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_1, 'tStopRefresh')  # time at next scr refresh
                text_1.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bufRou_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bufRou_2"-------
    for thisComponent in bufRou_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bufferLoop.addData('cB_4.started', cB_4.tStartRefresh)
    bufferLoop.addData('cB_4.stopped', cB_4.tStopRefresh)
    bufferLoop.addData('text_1.started', text_1.tStartRefresh)
    bufferLoop.addData('text_1.stopped', text_1.tStopRefresh)
    bufferLoop.addData('text_2.started', text_2.tStartRefresh)
    bufferLoop.addData('text_2.stopped', text_2.tStopRefresh)
    bufferLoop.addData('text_3.started', text_3.tStartRefresh)
    bufferLoop.addData('text_3.stopped', text_3.tStopRefresh)
    bufferLoop.addData('text_4.started', text_4.tStartRefresh)
    bufferLoop.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'bufferLoop'


# ------Prepare to start Routine "bufEnd"-------
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
bufEndComponents = [cB_5, idle, idle_2, idle_3, idle_4, idle_5, idle_6, idle_7, ilde_8, idle_9, idle_10, idle_11, idle_12]
for thisComponent in bufEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
bufEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "bufEnd"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = bufEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=bufEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_5* updates
    if cB_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_5.frameNStart = frameN  # exact frame index
        cB_5.tStart = t  # local t and not account for scr refresh
        cB_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_5, 'tStartRefresh')  # time at next scr refresh
        cB_5.setAutoDraw(True)
    if cB_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cB_5.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            cB_5.tStop = t  # not accounting for scr refresh
            cB_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cB_5, 'tStopRefresh')  # time at next scr refresh
            cB_5.setAutoDraw(False)
    
    # *idle* updates
    if idle.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        idle.frameNStart = frameN  # exact frame index
        idle.tStart = t  # local t and not account for scr refresh
        idle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle, 'tStartRefresh')  # time at next scr refresh
        idle.setAutoDraw(True)
    if idle.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 0.5-frameTolerance:
            # keep track of stop time/frame for later
            idle.tStop = t  # not accounting for scr refresh
            idle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle, 'tStopRefresh')  # time at next scr refresh
            idle.setAutoDraw(False)
    
    # *idle_2* updates
    if idle_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        idle_2.frameNStart = frameN  # exact frame index
        idle_2.tStart = t  # local t and not account for scr refresh
        idle_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_2, 'tStartRefresh')  # time at next scr refresh
        idle_2.setAutoDraw(True)
    if idle_2.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 0.7-frameTolerance:
            # keep track of stop time/frame for later
            idle_2.tStop = t  # not accounting for scr refresh
            idle_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_2, 'tStopRefresh')  # time at next scr refresh
            idle_2.setAutoDraw(False)
    
    # *idle_3* updates
    if idle_3.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
        # keep track of start time/frame for later
        idle_3.frameNStart = frameN  # exact frame index
        idle_3.tStart = t  # local t and not account for scr refresh
        idle_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_3, 'tStartRefresh')  # time at next scr refresh
        idle_3.setAutoDraw(True)
    if idle_3.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 0.8-frameTolerance:
            # keep track of stop time/frame for later
            idle_3.tStop = t  # not accounting for scr refresh
            idle_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_3, 'tStopRefresh')  # time at next scr refresh
            idle_3.setAutoDraw(False)
    
    # *idle_4* updates
    if idle_4.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
        # keep track of start time/frame for later
        idle_4.frameNStart = frameN  # exact frame index
        idle_4.tStart = t  # local t and not account for scr refresh
        idle_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_4, 'tStartRefresh')  # time at next scr refresh
        idle_4.setAutoDraw(True)
    if idle_4.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 0.95-frameTolerance:
            # keep track of stop time/frame for later
            idle_4.tStop = t  # not accounting for scr refresh
            idle_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_4, 'tStopRefresh')  # time at next scr refresh
            idle_4.setAutoDraw(False)
    
    # *idle_5* updates
    if idle_5.status == NOT_STARTED and tThisFlip >= 0.95-frameTolerance:
        # keep track of start time/frame for later
        idle_5.frameNStart = frameN  # exact frame index
        idle_5.tStart = t  # local t and not account for scr refresh
        idle_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_5, 'tStartRefresh')  # time at next scr refresh
        idle_5.setAutoDraw(True)
    if idle_5.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 1.1-frameTolerance:
            # keep track of stop time/frame for later
            idle_5.tStop = t  # not accounting for scr refresh
            idle_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_5, 'tStopRefresh')  # time at next scr refresh
            idle_5.setAutoDraw(False)
    
    # *idle_6* updates
    if idle_6.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
        # keep track of start time/frame for later
        idle_6.frameNStart = frameN  # exact frame index
        idle_6.tStart = t  # local t and not account for scr refresh
        idle_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_6, 'tStartRefresh')  # time at next scr refresh
        idle_6.setAutoDraw(True)
    if idle_6.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 1.25-frameTolerance:
            # keep track of stop time/frame for later
            idle_6.tStop = t  # not accounting for scr refresh
            idle_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_6, 'tStopRefresh')  # time at next scr refresh
            idle_6.setAutoDraw(False)
    
    # *idle_7* updates
    if idle_7.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
        # keep track of start time/frame for later
        idle_7.frameNStart = frameN  # exact frame index
        idle_7.tStart = t  # local t and not account for scr refresh
        idle_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_7, 'tStartRefresh')  # time at next scr refresh
        idle_7.setAutoDraw(True)
    if idle_7.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 1.35-frameTolerance:
            # keep track of stop time/frame for later
            idle_7.tStop = t  # not accounting for scr refresh
            idle_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_7, 'tStopRefresh')  # time at next scr refresh
            idle_7.setAutoDraw(False)
    
    # *ilde_8* updates
    if ilde_8.status == NOT_STARTED and tThisFlip >= 1.35-frameTolerance:
        # keep track of start time/frame for later
        ilde_8.frameNStart = frameN  # exact frame index
        ilde_8.tStart = t  # local t and not account for scr refresh
        ilde_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ilde_8, 'tStartRefresh')  # time at next scr refresh
        ilde_8.setAutoDraw(True)
    if ilde_8.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 1.85-frameTolerance:
            # keep track of stop time/frame for later
            ilde_8.tStop = t  # not accounting for scr refresh
            ilde_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ilde_8, 'tStopRefresh')  # time at next scr refresh
            ilde_8.setAutoDraw(False)
    
    # *idle_9* updates
    if idle_9.status == NOT_STARTED and tThisFlip >= 1.85-frameTolerance:
        # keep track of start time/frame for later
        idle_9.frameNStart = frameN  # exact frame index
        idle_9.tStart = t  # local t and not account for scr refresh
        idle_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_9, 'tStartRefresh')  # time at next scr refresh
        idle_9.setAutoDraw(True)
    if idle_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > idle_9.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            idle_9.tStop = t  # not accounting for scr refresh
            idle_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_9, 'tStopRefresh')  # time at next scr refresh
            idle_9.setAutoDraw(False)
    
    # *idle_10* updates
    if idle_10.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
        # keep track of start time/frame for later
        idle_10.frameNStart = frameN  # exact frame index
        idle_10.tStart = t  # local t and not account for scr refresh
        idle_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_10, 'tStartRefresh')  # time at next scr refresh
        idle_10.setAutoDraw(True)
    if idle_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > idle_10.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            idle_10.tStop = t  # not accounting for scr refresh
            idle_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_10, 'tStopRefresh')  # time at next scr refresh
            idle_10.setAutoDraw(False)
    
    # *idle_11* updates
    if idle_11.status == NOT_STARTED and tThisFlip >= 2.85-frameTolerance:
        # keep track of start time/frame for later
        idle_11.frameNStart = frameN  # exact frame index
        idle_11.tStart = t  # local t and not account for scr refresh
        idle_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_11, 'tStartRefresh')  # time at next scr refresh
        idle_11.setAutoDraw(True)
    if idle_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > idle_11.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            idle_11.tStop = t  # not accounting for scr refresh
            idle_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_11, 'tStopRefresh')  # time at next scr refresh
            idle_11.setAutoDraw(False)
    
    # *idle_12* updates
    if idle_12.status == NOT_STARTED and tThisFlip >= 3.35-frameTolerance:
        # keep track of start time/frame for later
        idle_12.frameNStart = frameN  # exact frame index
        idle_12.tStart = t  # local t and not account for scr refresh
        idle_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(idle_12, 'tStartRefresh')  # time at next scr refresh
        idle_12.setAutoDraw(True)
    if idle_12.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 3.5-frameTolerance:
            # keep track of stop time/frame for later
            idle_12.tStop = t  # not accounting for scr refresh
            idle_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(idle_12, 'tStopRefresh')  # time at next scr refresh
            idle_12.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in bufEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bufEnd"-------
for thisComponent in bufEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_5.started', cB_5.tStartRefresh)
thisExp.addData('cB_5.stopped', cB_5.tStopRefresh)
thisExp.addData('idle.started', idle.tStartRefresh)
thisExp.addData('idle.stopped', idle.tStopRefresh)
thisExp.addData('idle_2.started', idle_2.tStartRefresh)
thisExp.addData('idle_2.stopped', idle_2.tStopRefresh)
thisExp.addData('idle_3.started', idle_3.tStartRefresh)
thisExp.addData('idle_3.stopped', idle_3.tStopRefresh)
thisExp.addData('idle_4.started', idle_4.tStartRefresh)
thisExp.addData('idle_4.stopped', idle_4.tStopRefresh)
thisExp.addData('idle_5.started', idle_5.tStartRefresh)
thisExp.addData('idle_5.stopped', idle_5.tStopRefresh)
thisExp.addData('idle_6.started', idle_6.tStartRefresh)
thisExp.addData('idle_6.stopped', idle_6.tStopRefresh)
thisExp.addData('idle_7.started', idle_7.tStartRefresh)
thisExp.addData('idle_7.stopped', idle_7.tStopRefresh)
thisExp.addData('ilde_8.started', ilde_8.tStartRefresh)
thisExp.addData('ilde_8.stopped', ilde_8.tStopRefresh)
thisExp.addData('idle_9.started', idle_9.tStartRefresh)
thisExp.addData('idle_9.stopped', idle_9.tStopRefresh)
thisExp.addData('idle_10.started', idle_10.tStartRefresh)
thisExp.addData('idle_10.stopped', idle_10.tStopRefresh)
thisExp.addData('idle_11.started', idle_11.tStartRefresh)
thisExp.addData('idle_11.stopped', idle_11.tStopRefresh)
thisExp.addData('idle_12.started', idle_12.tStartRefresh)
thisExp.addData('idle_12.stopped', idle_12.tStopRefresh)

# ------Prepare to start Routine "sbIn"-------
# update component parameters for each repeat
textInstructionsSb2 = 'Hi ' + textName + '!\n' + textInstructionsSb

sBInstructions.setText(textInstructionsSb2)
keySbInstructions.keys = []
keySbInstructions.rt = []
out_sb.keys = []
out_sb.rt = []
# keep track of which components have finished
sbInComponents = [cB_6, sBInstructions, keySbInstructions, out_sb]
for thisComponent in sbInComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sbInClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "sbIn"-------
while continueRoutine:
    # get current time
    t = sbInClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sbInClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_6* updates
    if cB_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_6.frameNStart = frameN  # exact frame index
        cB_6.tStart = t  # local t and not account for scr refresh
        cB_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_6, 'tStartRefresh')  # time at next scr refresh
        cB_6.setAutoDraw(True)
    
    # *sBInstructions* updates
    if sBInstructions.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        sBInstructions.frameNStart = frameN  # exact frame index
        sBInstructions.tStart = t  # local t and not account for scr refresh
        sBInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sBInstructions, 'tStartRefresh')  # time at next scr refresh
        sBInstructions.setAutoDraw(True)
    
    # *keySbInstructions* updates
    waitOnFlip = False
    if keySbInstructions.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        keySbInstructions.frameNStart = frameN  # exact frame index
        keySbInstructions.tStart = t  # local t and not account for scr refresh
        keySbInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keySbInstructions, 'tStartRefresh')  # time at next scr refresh
        keySbInstructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keySbInstructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keySbInstructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keySbInstructions.status == STARTED and not waitOnFlip:
        theseKeys = keySbInstructions.getKeys(keyList=['c'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keySbInstructions.keys = theseKeys.name  # just the last key pressed
            keySbInstructions.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *out_sb* updates
    waitOnFlip = False
    if out_sb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        out_sb.frameNStart = frameN  # exact frame index
        out_sb.tStart = t  # local t and not account for scr refresh
        out_sb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(out_sb, 'tStartRefresh')  # time at next scr refresh
        out_sb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(out_sb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(out_sb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if out_sb.status == STARTED and not waitOnFlip:
        theseKeys = out_sb.getKeys(keyList=['1'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            out_sb.keys = theseKeys.name  # just the last key pressed
            out_sb.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sbInComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sbIn"-------
for thisComponent in sbInComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_6.started', cB_6.tStartRefresh)
thisExp.addData('cB_6.stopped', cB_6.tStopRefresh)
thisExp.addData('sBInstructions.started', sBInstructions.tStartRefresh)
thisExp.addData('sBInstructions.stopped', sBInstructions.tStopRefresh)
# check responses
if keySbInstructions.keys in ['', [], None]:  # No response was made
    keySbInstructions.keys = None
thisExp.addData('keySbInstructions.keys',keySbInstructions.keys)
if keySbInstructions.keys != None:  # we had a response
    thisExp.addData('keySbInstructions.rt', keySbInstructions.rt)
thisExp.addData('keySbInstructions.started', keySbInstructions.tStartRefresh)
thisExp.addData('keySbInstructions.stopped', keySbInstructions.tStopRefresh)
thisExp.nextEntry()
# check responses
if out_sb.keys in ['', [], None]:  # No response was made
    out_sb.keys = None
thisExp.addData('out_sb.keys',out_sb.keys)
if out_sb.keys != None:  # we had a response
    thisExp.addData('out_sb.rt', out_sb.rt)
thisExp.addData('out_sb.started', out_sb.tStartRefresh)
thisExp.addData('out_sb.stopped', out_sb.tStopRefresh)
thisExp.nextEntry()
# the Routine "sbIn" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_0 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('contitions.xlsx', selection='0:4'),
    seed=None, name='trials_0')
thisExp.addLoop(trials_0)  # add the loop to the experiment
thisTrial_0 = trials_0.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_0.rgb)
if thisTrial_0 != None:
    for paramName in thisTrial_0:
        exec('{} = thisTrial_0[paramName]'.format(paramName))

for thisTrial_0 in trials_0:
    currentLoop = trials_0
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_0.rgb)
    if thisTrial_0 != None:
        for paramName in thisTrial_0:
            exec('{} = thisTrial_0[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    sbLoop_0 = data.TrialHandler(nReps=2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('contitions.xlsx', selection='0:4'),
        seed=None, name='sbLoop_0')
    thisExp.addLoop(sbLoop_0)  # add the loop to the experiment
    thisSbLoop_0 = sbLoop_0.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSbLoop_0.rgb)
    if thisSbLoop_0 != None:
        for paramName in thisSbLoop_0:
            exec('{} = thisSbLoop_0[paramName]'.format(paramName))
    
    for thisSbLoop_0 in sbLoop_0:
        currentLoop = sbLoop_0
        # abbreviate parameter names if possible (e.g. rgb = thisSbLoop_0.rgb)
        if thisSbLoop_0 != None:
            for paramName in thisSbLoop_0:
                exec('{} = thisSbLoop_0[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sbRnd"-------
        # update component parameters for each repeat
        text.setText('This round you are playing with ' + playerId + '!')
        imagesbRnd.setImage(avatarFile)
        sbChoice.reset()
        text_6.setText(textSbText)
        # keep track of which components have finished
        sbRndComponents = [cB_8, text, imagesbRnd, sbChoice, text_6]
        for thisComponent in sbRndComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbRndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbRnd"-------
        while continueRoutine:
            # get current time
            t = sbRndClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbRndClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_8* updates
            if cB_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_8.frameNStart = frameN  # exact frame index
                cB_8.tStart = t  # local t and not account for scr refresh
                cB_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_8, 'tStartRefresh')  # time at next scr refresh
                cB_8.setAutoDraw(True)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *imagesbRnd* updates
            if imagesbRnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imagesbRnd.frameNStart = frameN  # exact frame index
                imagesbRnd.tStart = t  # local t and not account for scr refresh
                imagesbRnd.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagesbRnd, 'tStartRefresh')  # time at next scr refresh
                imagesbRnd.setAutoDraw(True)
            # *sbChoice* updates
            if sbChoice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sbChoice.frameNStart = frameN  # exact frame index
                sbChoice.tStart = t  # local t and not account for scr refresh
                sbChoice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sbChoice, 'tStartRefresh')  # time at next scr refresh
                sbChoice.setAutoDraw(True)
            continueRoutine &= sbChoice.noResponse  # a response ends the trial
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbRndComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbRnd"-------
        for thisComponent in sbRndComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sbLoop_0.addData('cB_8.started', cB_8.tStartRefresh)
        sbLoop_0.addData('cB_8.stopped', cB_8.tStopRefresh)
        sbLoop_0.addData('text.started', text.tStartRefresh)
        sbLoop_0.addData('text.stopped', text.tStopRefresh)
        sbLoop_0.addData('imagesbRnd.started', imagesbRnd.tStartRefresh)
        sbLoop_0.addData('imagesbRnd.stopped', imagesbRnd.tStopRefresh)
        # store data for sbLoop_0 (TrialHandler)
        sbLoop_0.addData('sbChoice.response', sbChoice.getRating())
        sbLoop_0.addData('sbChoice.rt', sbChoice.getRT())
        sbLoop_0.addData('sbChoice.history', sbChoice.getHistory())
        sbLoop_0.addData('sbChoice.started', sbChoice.tStart)
        sbLoop_0.addData('sbChoice.stopped', sbChoice.tStop)
        sbResp = int(sbChoice.getRating())
        sbRT = sbChoice.getRT()
        
        print(sbRT)
        print(sbResp)
        sbLoop_0.addData('text_6.started', text_6.tStartRefresh)
        sbLoop_0.addData('text_6.stopped', text_6.tStopRefresh)
        # the Routine "sbRnd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "bufWait"-------
        # update component parameters for each repeat
        import random 
        
        timeR= [0,1,1,1,1,2,2,2,3,3,4,4,5]
        intTime= int(random.choice(timeR))
        
        
        text_7.setText(bufText)
        # keep track of which components have finished
        bufWaitComponents = [cB_9, text_7]
        for thisComponent in bufWaitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        bufWaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "bufWait"-------
        while continueRoutine:
            # get current time
            t = bufWaitClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=bufWaitClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_9* updates
            if cB_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_9.frameNStart = frameN  # exact frame index
                cB_9.tStart = t  # local t and not account for scr refresh
                cB_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_9, 'tStartRefresh')  # time at next scr refresh
                cB_9.setAutoDraw(True)
            if cB_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cB_9.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    cB_9.tStop = t  # not accounting for scr refresh
                    cB_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cB_9, 'tStopRefresh')  # time at next scr refresh
                    cB_9.setAutoDraw(False)
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bufWaitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "bufWait"-------
        for thisComponent in bufWaitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sbLoop_0.addData('cB_9.started', cB_9.tStartRefresh)
        sbLoop_0.addData('cB_9.stopped', cB_9.tStopRefresh)
        sbLoop_0.addData('text_7.started', text_7.tStartRefresh)
        sbLoop_0.addData('text_7.stopped', text_7.tStopRefresh)
        # the Routine "bufWait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "sbFb"-------
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        ResponseCoop = [1,1.5,2]
        ResponseUnco = [0.5,0.75,1]
        creditMultiPlier = 3
        
        if actionLabel == 0:
            multiPlier = random.choice(ResponseUnco)
        elif actionLabel == 1:
            multiPlier = random.choice(ResponseCoop)
        else:
            multiPlier= int(99)
        
        creditInvestment = sbResp
        creditLeft = 10 - sbResp
        
        creditGain = creditInvestment * multiPlier
        creditTotal = creditGain + creditLeft
        mpText = multiPlier*100
        
        textforThis1 = playerId + textSbFeed1 + str(mpText) + textSbFeed2
        textforThis2 = textSbFeed3 + str(creditGain) + textSbFeed4
        textforThis3 = textSbFeed5 + str(creditTotal) + textSbFeed4
        
        
        
        textFb.setText(textforThis1 + textforThis2 + textforThis3)
        out_Fb.keys = []
        out_Fb.rt = []
        # keep track of which components have finished
        sbFbComponents = [cbFb, textFb, out_Fb]
        for thisComponent in sbFbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbFbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbFb"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = sbFbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbFbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cbFb* updates
            if cbFb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cbFb.frameNStart = frameN  # exact frame index
                cbFb.tStart = t  # local t and not account for scr refresh
                cbFb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cbFb, 'tStartRefresh')  # time at next scr refresh
                cbFb.setAutoDraw(True)
            if cbFb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cbFb.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    cbFb.tStop = t  # not accounting for scr refresh
                    cbFb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cbFb, 'tStopRefresh')  # time at next scr refresh
                    cbFb.setAutoDraw(False)
            
            # *textFb* updates
            if textFb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFb.frameNStart = frameN  # exact frame index
                textFb.tStart = t  # local t and not account for scr refresh
                textFb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFb, 'tStartRefresh')  # time at next scr refresh
                textFb.setAutoDraw(True)
            if textFb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFb.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textFb.tStop = t  # not accounting for scr refresh
                    textFb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textFb, 'tStopRefresh')  # time at next scr refresh
                    textFb.setAutoDraw(False)
            
            # *out_Fb* updates
            waitOnFlip = False
            if out_Fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                out_Fb.frameNStart = frameN  # exact frame index
                out_Fb.tStart = t  # local t and not account for scr refresh
                out_Fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(out_Fb, 'tStartRefresh')  # time at next scr refresh
                out_Fb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(out_Fb.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(out_Fb.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if out_Fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > out_Fb.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    out_Fb.tStop = t  # not accounting for scr refresh
                    out_Fb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(out_Fb, 'tStopRefresh')  # time at next scr refresh
                    out_Fb.status = FINISHED
            if out_Fb.status == STARTED and not waitOnFlip:
                theseKeys = out_Fb.getKeys(keyList=['1'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    out_Fb.keys = theseKeys.name  # just the last key pressed
                    out_Fb.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbFbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbFb"-------
        for thisComponent in sbFbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        lastPlayer = playerId
        
        if actionLabel == 0:
            sbGain = 0
        elif actionLabel == 1:
            sbGain = sbResp
        else:
            pass
        
        sbTotal += sbGain
        
        if playerId == 'Paul':
            sbTotalPaul += sbGain
        elif playerId == 'Lukas':
            sbTotalLukas += sbGain
        else:
            pass
        
        roundGain.append(creditTotal)
        
        print(sbTotal)
        print(roundGain)
        
        thisExp.addData("totalMoney", sbTotal)
        thisExp.addData("paulMoney", sbTotalPaul)
        thisExp.addData("lukasMoney", sbTotalLukas)
        sbLoop_0.addData('cbFb.started', cbFb.tStartRefresh)
        sbLoop_0.addData('cbFb.stopped', cbFb.tStopRefresh)
        sbLoop_0.addData('textFb.started', textFb.tStartRefresh)
        sbLoop_0.addData('textFb.stopped', textFb.tStopRefresh)
        # check responses
        if out_Fb.keys in ['', [], None]:  # No response was made
            out_Fb.keys = None
        sbLoop_0.addData('out_Fb.keys',out_Fb.keys)
        if out_Fb.keys != None:  # we had a response
            sbLoop_0.addData('out_Fb.rt', out_Fb.rt)
        sbLoop_0.addData('out_Fb.started', out_Fb.tStartRefresh)
        sbLoop_0.addData('out_Fb.stopped', out_Fb.tStopRefresh)
        
        # ------Prepare to start Routine "bufFix"-------
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        bufFixComponents = [cbBuf, text_8]
        for thisComponent in bufFixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        bufFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "bufFix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = bufFixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=bufFixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cbBuf* updates
            if cbBuf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cbBuf.frameNStart = frameN  # exact frame index
                cbBuf.tStart = t  # local t and not account for scr refresh
                cbBuf.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cbBuf, 'tStartRefresh')  # time at next scr refresh
                cbBuf.setAutoDraw(True)
            if cbBuf.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cbBuf.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    cbBuf.tStop = t  # not accounting for scr refresh
                    cbBuf.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cbBuf, 'tStopRefresh')  # time at next scr refresh
                    cbBuf.setAutoDraw(False)
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bufFixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "bufFix"-------
        for thisComponent in bufFixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sbLoop_0.addData('cbBuf.started', cbBuf.tStartRefresh)
        sbLoop_0.addData('cbBuf.stopped', cbBuf.tStopRefresh)
        sbLoop_0.addData('text_8.started', text_8.tStartRefresh)
        sbLoop_0.addData('text_8.stopped', text_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2 repeats of 'sbLoop_0'
    
    
    # set up handler to look after randomisation of conditions etc
    sliders_01 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('sliders_they.xlsx'),
        seed=None, name='sliders_01')
    thisExp.addLoop(sliders_01)  # add the loop to the experiment
    thisSlider_01 = sliders_01.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSlider_01.rgb)
    if thisSlider_01 != None:
        for paramName in thisSlider_01:
            exec('{} = thisSlider_01[paramName]'.format(paramName))
    
    for thisSlider_01 in sliders_01:
        currentLoop = sliders_01
        # abbreviate parameter names if possible (e.g. rgb = thisSlider_01.rgb)
        if thisSlider_01 != None:
            for paramName in thisSlider_01:
                exec('{} = thisSlider_01[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sbQu1"-------
        # update component parameters for each repeat
        if lastPlayer == 'Paul':
            playerQ = 'Lukas' 
            if lastPlayer == 'Lukas':
                playerQ = 'Paul'
        if lastPlayer == 'Lukas':
            playerQ = 'Paul' 
            if lastPlayer == 'Paul':
                playerQ = 'Lukas'
        else:
            pass
        
        rating_they = visual.RatingScale(win=win, name='rating', size=1.0, pos=[0.0, -0.2], 
            scale=sliderText +' ' + playerQ + '?', labels = [sliderMin, sliderMax],
            tickHeight=-1,
            marker='triangle', markerStart=4, markerColor='DarkRed')
        
        
        
        rating_they.reset()
        # keep track of which components have finished
        sbQu1Components = [cB_11, rating_they]
        for thisComponent in sbQu1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbQu1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbQu1"-------
        while continueRoutine:
            # get current time
            t = sbQu1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbQu1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_11* updates
            if cB_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_11.frameNStart = frameN  # exact frame index
                cB_11.tStart = t  # local t and not account for scr refresh
                cB_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_11, 'tStartRefresh')  # time at next scr refresh
                cB_11.setAutoDraw(True)
            # *rating_they* updates
            if rating_they.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_they.frameNStart = frameN  # exact frame index
                rating_they.tStart = t  # local t and not account for scr refresh
                rating_they.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_they, 'tStartRefresh')  # time at next scr refresh
                rating_they.setAutoDraw(True)
            continueRoutine &= rating_they.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbQu1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbQu1"-------
        for thisComponent in sbQu1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sliders_01.addData('cB_11.started', cB_11.tStartRefresh)
        sliders_01.addData('cB_11.stopped', cB_11.tStopRefresh)
        lastPlayer = playerQ
        # store data for sliders_01 (TrialHandler)
        sliders_01.addData('rating_they.response', rating_they.getRating())
        sliders_01.addData('rating_they.rt', rating_they.getRT())
        sliders_01.addData('rating_they.started', rating_they.tStart)
        sliders_01.addData('rating_they.stopped', rating_they.tStop)
        # the Routine "sbQu1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'sliders_01'
    
    
    # set up handler to look after randomisation of conditions etc
    slider_02 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('sliders_you.xlsx'),
        seed=None, name='slider_02')
    thisExp.addLoop(slider_02)  # add the loop to the experiment
    thisSlider_02 = slider_02.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSlider_02.rgb)
    if thisSlider_02 != None:
        for paramName in thisSlider_02:
            exec('{} = thisSlider_02[paramName]'.format(paramName))
    
    for thisSlider_02 in slider_02:
        currentLoop = slider_02
        # abbreviate parameter names if possible (e.g. rgb = thisSlider_02.rgb)
        if thisSlider_02 != None:
            for paramName in thisSlider_02:
                exec('{} = thisSlider_02[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sbQu2"-------
        # update component parameters for each repeat
        rating_you = visual.RatingScale(win=win, name='rating', size=1.0, pos=[0.0, -0.2], 
            scale=sliderText + '?', labels = [sliderMin, sliderMax],
            tickHeight=-1,
            marker='triangle', markerStart=4, markerColor='DarkRed')
        
        
        
        rating_you.reset()
        # keep track of which components have finished
        sbQu2Components = [cB_14, rating_you]
        for thisComponent in sbQu2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbQu2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbQu2"-------
        while continueRoutine:
            # get current time
            t = sbQu2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbQu2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_14* updates
            if cB_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_14.frameNStart = frameN  # exact frame index
                cB_14.tStart = t  # local t and not account for scr refresh
                cB_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_14, 'tStartRefresh')  # time at next scr refresh
                cB_14.setAutoDraw(True)
            # *rating_you* updates
            if rating_you.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_you.frameNStart = frameN  # exact frame index
                rating_you.tStart = t  # local t and not account for scr refresh
                rating_you.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_you, 'tStartRefresh')  # time at next scr refresh
                rating_you.setAutoDraw(True)
            continueRoutine &= rating_you.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbQu2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbQu2"-------
        for thisComponent in sbQu2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('cB_14.started', cB_14.tStartRefresh)
        thisExp.addData('cB_14.stopped', cB_14.tStopRefresh)
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('rating_you.response', rating_you.getRating())
        thisExp.addData('rating_you.rt', rating_you.getRT())
        thisExp.nextEntry()
        thisExp.addData('rating_you.started', rating_you.tStart)
        thisExp.addData('rating_you.stopped', rating_you.tStop)
        # the Routine "sbQu2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'slider_02'
    
    
    # set up handler to look after randomisation of conditions etc
    buffer_0 = data.TrialHandler(nReps=4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='buffer_0')
    thisExp.addLoop(buffer_0)  # add the loop to the experiment
    thisBuffer_0 = buffer_0.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBuffer_0.rgb)
    if thisBuffer_0 != None:
        for paramName in thisBuffer_0:
            exec('{} = thisBuffer_0[paramName]'.format(paramName))
    
    for thisBuffer_0 in buffer_0:
        currentLoop = buffer_0
        # abbreviate parameter names if possible (e.g. rgb = thisBuffer_0.rgb)
        if thisBuffer_0 != None:
            for paramName in thisBuffer_0:
                exec('{} = thisBuffer_0[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "bufWait"-------
        # update component parameters for each repeat
        import random 
        
        timeR= [0,1,1,1,1,2,2,2,3,3,4,4,5]
        intTime= int(random.choice(timeR))
        
        
        text_7.setText(bufText)
        # keep track of which components have finished
        bufWaitComponents = [cB_9, text_7]
        for thisComponent in bufWaitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        bufWaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "bufWait"-------
        while continueRoutine:
            # get current time
            t = bufWaitClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=bufWaitClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_9* updates
            if cB_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_9.frameNStart = frameN  # exact frame index
                cB_9.tStart = t  # local t and not account for scr refresh
                cB_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_9, 'tStartRefresh')  # time at next scr refresh
                cB_9.setAutoDraw(True)
            if cB_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cB_9.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    cB_9.tStop = t  # not accounting for scr refresh
                    cB_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cB_9, 'tStopRefresh')  # time at next scr refresh
                    cB_9.setAutoDraw(False)
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bufWaitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "bufWait"-------
        for thisComponent in bufWaitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        buffer_0.addData('cB_9.started', cB_9.tStartRefresh)
        buffer_0.addData('cB_9.stopped', cB_9.tStopRefresh)
        buffer_0.addData('text_7.started', text_7.tStartRefresh)
        buffer_0.addData('text_7.stopped', text_7.tStopRefresh)
        # the Routine "bufWait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4 repeats of 'buffer_0'
    
    
    # ------Prepare to start Routine "bufFix"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    bufFixComponents = [cbBuf, text_8]
    for thisComponent in bufFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    bufFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "bufFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = bufFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bufFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cbBuf* updates
        if cbBuf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cbBuf.frameNStart = frameN  # exact frame index
            cbBuf.tStart = t  # local t and not account for scr refresh
            cbBuf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cbBuf, 'tStartRefresh')  # time at next scr refresh
            cbBuf.setAutoDraw(True)
        if cbBuf.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cbBuf.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                cbBuf.tStop = t  # not accounting for scr refresh
                cbBuf.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cbBuf, 'tStopRefresh')  # time at next scr refresh
                cbBuf.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bufFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bufFix"-------
    for thisComponent in bufFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_0.addData('cbBuf.started', cbBuf.tStartRefresh)
    trials_0.addData('cbBuf.stopped', cbBuf.tStopRefresh)
    trials_0.addData('text_8.started', text_8.tStartRefresh)
    trials_0.addData('text_8.stopped', text_8.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_0'


# ------Prepare to start Routine "reset"-------
routineTimer.add(0.010000)
# update component parameters for each repeat
roundGain = []
# keep track of which components have finished
resetComponents = [cB_13]
for thisComponent in resetComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
resetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "reset"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = resetClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=resetClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_13* updates
    if cB_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_13.frameNStart = frameN  # exact frame index
        cB_13.tStart = t  # local t and not account for scr refresh
        cB_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_13, 'tStartRefresh')  # time at next scr refresh
        cB_13.setAutoDraw(True)
    if cB_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cB_13.tStartRefresh + .01-frameTolerance:
            # keep track of stop time/frame for later
            cB_13.tStop = t  # not accounting for scr refresh
            cB_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cB_13, 'tStopRefresh')  # time at next scr refresh
            cB_13.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reset"-------
for thisComponent in resetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_13.started', cB_13.tStartRefresh)
thisExp.addData('cB_13.stopped', cB_13.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    sbLoop_1 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('contitions.xlsx', selection='5:25'),
        seed=None, name='sbLoop_1')
    thisExp.addLoop(sbLoop_1)  # add the loop to the experiment
    thisSbLoop_1 = sbLoop_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSbLoop_1.rgb)
    if thisSbLoop_1 != None:
        for paramName in thisSbLoop_1:
            exec('{} = thisSbLoop_1[paramName]'.format(paramName))
    
    for thisSbLoop_1 in sbLoop_1:
        currentLoop = sbLoop_1
        # abbreviate parameter names if possible (e.g. rgb = thisSbLoop_1.rgb)
        if thisSbLoop_1 != None:
            for paramName in thisSbLoop_1:
                exec('{} = thisSbLoop_1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sbRnd"-------
        # update component parameters for each repeat
        text.setText('This round you are playing with ' + playerId + '!')
        imagesbRnd.setImage(avatarFile)
        sbChoice.reset()
        text_6.setText(textSbText)
        # keep track of which components have finished
        sbRndComponents = [cB_8, text, imagesbRnd, sbChoice, text_6]
        for thisComponent in sbRndComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbRndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbRnd"-------
        while continueRoutine:
            # get current time
            t = sbRndClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbRndClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_8* updates
            if cB_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_8.frameNStart = frameN  # exact frame index
                cB_8.tStart = t  # local t and not account for scr refresh
                cB_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_8, 'tStartRefresh')  # time at next scr refresh
                cB_8.setAutoDraw(True)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *imagesbRnd* updates
            if imagesbRnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imagesbRnd.frameNStart = frameN  # exact frame index
                imagesbRnd.tStart = t  # local t and not account for scr refresh
                imagesbRnd.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagesbRnd, 'tStartRefresh')  # time at next scr refresh
                imagesbRnd.setAutoDraw(True)
            # *sbChoice* updates
            if sbChoice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sbChoice.frameNStart = frameN  # exact frame index
                sbChoice.tStart = t  # local t and not account for scr refresh
                sbChoice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sbChoice, 'tStartRefresh')  # time at next scr refresh
                sbChoice.setAutoDraw(True)
            continueRoutine &= sbChoice.noResponse  # a response ends the trial
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbRndComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbRnd"-------
        for thisComponent in sbRndComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sbLoop_1.addData('cB_8.started', cB_8.tStartRefresh)
        sbLoop_1.addData('cB_8.stopped', cB_8.tStopRefresh)
        sbLoop_1.addData('text.started', text.tStartRefresh)
        sbLoop_1.addData('text.stopped', text.tStopRefresh)
        sbLoop_1.addData('imagesbRnd.started', imagesbRnd.tStartRefresh)
        sbLoop_1.addData('imagesbRnd.stopped', imagesbRnd.tStopRefresh)
        # store data for sbLoop_1 (TrialHandler)
        sbLoop_1.addData('sbChoice.response', sbChoice.getRating())
        sbLoop_1.addData('sbChoice.rt', sbChoice.getRT())
        sbLoop_1.addData('sbChoice.history', sbChoice.getHistory())
        sbLoop_1.addData('sbChoice.started', sbChoice.tStart)
        sbLoop_1.addData('sbChoice.stopped', sbChoice.tStop)
        sbResp = int(sbChoice.getRating())
        sbRT = sbChoice.getRT()
        
        print(sbRT)
        print(sbResp)
        sbLoop_1.addData('text_6.started', text_6.tStartRefresh)
        sbLoop_1.addData('text_6.stopped', text_6.tStopRefresh)
        # the Routine "sbRnd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "bufWait"-------
        # update component parameters for each repeat
        import random 
        
        timeR= [0,1,1,1,1,2,2,2,3,3,4,4,5]
        intTime= int(random.choice(timeR))
        
        
        text_7.setText(bufText)
        # keep track of which components have finished
        bufWaitComponents = [cB_9, text_7]
        for thisComponent in bufWaitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        bufWaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "bufWait"-------
        while continueRoutine:
            # get current time
            t = bufWaitClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=bufWaitClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_9* updates
            if cB_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_9.frameNStart = frameN  # exact frame index
                cB_9.tStart = t  # local t and not account for scr refresh
                cB_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_9, 'tStartRefresh')  # time at next scr refresh
                cB_9.setAutoDraw(True)
            if cB_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cB_9.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    cB_9.tStop = t  # not accounting for scr refresh
                    cB_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cB_9, 'tStopRefresh')  # time at next scr refresh
                    cB_9.setAutoDraw(False)
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bufWaitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "bufWait"-------
        for thisComponent in bufWaitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sbLoop_1.addData('cB_9.started', cB_9.tStartRefresh)
        sbLoop_1.addData('cB_9.stopped', cB_9.tStopRefresh)
        sbLoop_1.addData('text_7.started', text_7.tStartRefresh)
        sbLoop_1.addData('text_7.stopped', text_7.tStopRefresh)
        # the Routine "bufWait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "sbFb"-------
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        ResponseCoop = [1,1.5,2]
        ResponseUnco = [0.5,0.75,1]
        creditMultiPlier = 3
        
        if actionLabel == 0:
            multiPlier = random.choice(ResponseUnco)
        elif actionLabel == 1:
            multiPlier = random.choice(ResponseCoop)
        else:
            multiPlier= int(99)
        
        creditInvestment = sbResp
        creditLeft = 10 - sbResp
        
        creditGain = creditInvestment * multiPlier
        creditTotal = creditGain + creditLeft
        mpText = multiPlier*100
        
        textforThis1 = playerId + textSbFeed1 + str(mpText) + textSbFeed2
        textforThis2 = textSbFeed3 + str(creditGain) + textSbFeed4
        textforThis3 = textSbFeed5 + str(creditTotal) + textSbFeed4
        
        
        
        textFb.setText(textforThis1 + textforThis2 + textforThis3)
        out_Fb.keys = []
        out_Fb.rt = []
        # keep track of which components have finished
        sbFbComponents = [cbFb, textFb, out_Fb]
        for thisComponent in sbFbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbFbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbFb"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = sbFbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbFbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cbFb* updates
            if cbFb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cbFb.frameNStart = frameN  # exact frame index
                cbFb.tStart = t  # local t and not account for scr refresh
                cbFb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cbFb, 'tStartRefresh')  # time at next scr refresh
                cbFb.setAutoDraw(True)
            if cbFb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cbFb.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    cbFb.tStop = t  # not accounting for scr refresh
                    cbFb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cbFb, 'tStopRefresh')  # time at next scr refresh
                    cbFb.setAutoDraw(False)
            
            # *textFb* updates
            if textFb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFb.frameNStart = frameN  # exact frame index
                textFb.tStart = t  # local t and not account for scr refresh
                textFb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFb, 'tStartRefresh')  # time at next scr refresh
                textFb.setAutoDraw(True)
            if textFb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFb.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textFb.tStop = t  # not accounting for scr refresh
                    textFb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textFb, 'tStopRefresh')  # time at next scr refresh
                    textFb.setAutoDraw(False)
            
            # *out_Fb* updates
            waitOnFlip = False
            if out_Fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                out_Fb.frameNStart = frameN  # exact frame index
                out_Fb.tStart = t  # local t and not account for scr refresh
                out_Fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(out_Fb, 'tStartRefresh')  # time at next scr refresh
                out_Fb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(out_Fb.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(out_Fb.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if out_Fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > out_Fb.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    out_Fb.tStop = t  # not accounting for scr refresh
                    out_Fb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(out_Fb, 'tStopRefresh')  # time at next scr refresh
                    out_Fb.status = FINISHED
            if out_Fb.status == STARTED and not waitOnFlip:
                theseKeys = out_Fb.getKeys(keyList=['1'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    out_Fb.keys = theseKeys.name  # just the last key pressed
                    out_Fb.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbFbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbFb"-------
        for thisComponent in sbFbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        lastPlayer = playerId
        
        if actionLabel == 0:
            sbGain = 0
        elif actionLabel == 1:
            sbGain = sbResp
        else:
            pass
        
        sbTotal += sbGain
        
        if playerId == 'Paul':
            sbTotalPaul += sbGain
        elif playerId == 'Lukas':
            sbTotalLukas += sbGain
        else:
            pass
        
        roundGain.append(creditTotal)
        
        print(sbTotal)
        print(roundGain)
        
        thisExp.addData("totalMoney", sbTotal)
        thisExp.addData("paulMoney", sbTotalPaul)
        thisExp.addData("lukasMoney", sbTotalLukas)
        sbLoop_1.addData('cbFb.started', cbFb.tStartRefresh)
        sbLoop_1.addData('cbFb.stopped', cbFb.tStopRefresh)
        sbLoop_1.addData('textFb.started', textFb.tStartRefresh)
        sbLoop_1.addData('textFb.stopped', textFb.tStopRefresh)
        # check responses
        if out_Fb.keys in ['', [], None]:  # No response was made
            out_Fb.keys = None
        sbLoop_1.addData('out_Fb.keys',out_Fb.keys)
        if out_Fb.keys != None:  # we had a response
            sbLoop_1.addData('out_Fb.rt', out_Fb.rt)
        sbLoop_1.addData('out_Fb.started', out_Fb.tStartRefresh)
        sbLoop_1.addData('out_Fb.stopped', out_Fb.tStopRefresh)
        
        # ------Prepare to start Routine "bufFix"-------
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        bufFixComponents = [cbBuf, text_8]
        for thisComponent in bufFixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        bufFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "bufFix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = bufFixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=bufFixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cbBuf* updates
            if cbBuf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cbBuf.frameNStart = frameN  # exact frame index
                cbBuf.tStart = t  # local t and not account for scr refresh
                cbBuf.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cbBuf, 'tStartRefresh')  # time at next scr refresh
                cbBuf.setAutoDraw(True)
            if cbBuf.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cbBuf.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    cbBuf.tStop = t  # not accounting for scr refresh
                    cbBuf.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cbBuf, 'tStopRefresh')  # time at next scr refresh
                    cbBuf.setAutoDraw(False)
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bufFixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "bufFix"-------
        for thisComponent in bufFixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sbLoop_1.addData('cbBuf.started', cbBuf.tStartRefresh)
        sbLoop_1.addData('cbBuf.stopped', cbBuf.tStopRefresh)
        sbLoop_1.addData('text_8.started', text_8.tStartRefresh)
        sbLoop_1.addData('text_8.stopped', text_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'sbLoop_1'
    
    
    # set up handler to look after randomisation of conditions etc
    sliders_11 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('sliders_they.xlsx'),
        seed=None, name='sliders_11')
    thisExp.addLoop(sliders_11)  # add the loop to the experiment
    thisSlider_11 = sliders_11.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSlider_11.rgb)
    if thisSlider_11 != None:
        for paramName in thisSlider_11:
            exec('{} = thisSlider_11[paramName]'.format(paramName))
    
    for thisSlider_11 in sliders_11:
        currentLoop = sliders_11
        # abbreviate parameter names if possible (e.g. rgb = thisSlider_11.rgb)
        if thisSlider_11 != None:
            for paramName in thisSlider_11:
                exec('{} = thisSlider_11[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sbQu1"-------
        # update component parameters for each repeat
        if lastPlayer == 'Paul':
            playerQ = 'Lukas' 
            if lastPlayer == 'Lukas':
                playerQ = 'Paul'
        if lastPlayer == 'Lukas':
            playerQ = 'Paul' 
            if lastPlayer == 'Paul':
                playerQ = 'Lukas'
        else:
            pass
        
        rating_they = visual.RatingScale(win=win, name='rating', size=1.0, pos=[0.0, -0.2], 
            scale=sliderText +' ' + playerQ + '?', labels = [sliderMin, sliderMax],
            tickHeight=-1,
            marker='triangle', markerStart=4, markerColor='DarkRed')
        
        
        
        rating_they.reset()
        # keep track of which components have finished
        sbQu1Components = [cB_11, rating_they]
        for thisComponent in sbQu1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbQu1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbQu1"-------
        while continueRoutine:
            # get current time
            t = sbQu1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbQu1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_11* updates
            if cB_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_11.frameNStart = frameN  # exact frame index
                cB_11.tStart = t  # local t and not account for scr refresh
                cB_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_11, 'tStartRefresh')  # time at next scr refresh
                cB_11.setAutoDraw(True)
            # *rating_they* updates
            if rating_they.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_they.frameNStart = frameN  # exact frame index
                rating_they.tStart = t  # local t and not account for scr refresh
                rating_they.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_they, 'tStartRefresh')  # time at next scr refresh
                rating_they.setAutoDraw(True)
            continueRoutine &= rating_they.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbQu1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbQu1"-------
        for thisComponent in sbQu1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sliders_11.addData('cB_11.started', cB_11.tStartRefresh)
        sliders_11.addData('cB_11.stopped', cB_11.tStopRefresh)
        lastPlayer = playerQ
        # store data for sliders_11 (TrialHandler)
        sliders_11.addData('rating_they.response', rating_they.getRating())
        sliders_11.addData('rating_they.rt', rating_they.getRT())
        sliders_11.addData('rating_they.started', rating_they.tStart)
        sliders_11.addData('rating_they.stopped', rating_they.tStop)
        # the Routine "sbQu1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'sliders_11'
    
    
    # set up handler to look after randomisation of conditions etc
    sliders_12 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('sliders_you.xlsx'),
        seed=None, name='sliders_12')
    thisExp.addLoop(sliders_12)  # add the loop to the experiment
    thisSlider_12 = sliders_12.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSlider_12.rgb)
    if thisSlider_12 != None:
        for paramName in thisSlider_12:
            exec('{} = thisSlider_12[paramName]'.format(paramName))
    
    for thisSlider_12 in sliders_12:
        currentLoop = sliders_12
        # abbreviate parameter names if possible (e.g. rgb = thisSlider_12.rgb)
        if thisSlider_12 != None:
            for paramName in thisSlider_12:
                exec('{} = thisSlider_12[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sbQu2"-------
        # update component parameters for each repeat
        rating_you = visual.RatingScale(win=win, name='rating', size=1.0, pos=[0.0, -0.2], 
            scale=sliderText + '?', labels = [sliderMin, sliderMax],
            tickHeight=-1,
            marker='triangle', markerStart=4, markerColor='DarkRed')
        
        
        
        rating_you.reset()
        # keep track of which components have finished
        sbQu2Components = [cB_14, rating_you]
        for thisComponent in sbQu2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sbQu2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sbQu2"-------
        while continueRoutine:
            # get current time
            t = sbQu2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sbQu2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_14* updates
            if cB_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_14.frameNStart = frameN  # exact frame index
                cB_14.tStart = t  # local t and not account for scr refresh
                cB_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_14, 'tStartRefresh')  # time at next scr refresh
                cB_14.setAutoDraw(True)
            # *rating_you* updates
            if rating_you.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_you.frameNStart = frameN  # exact frame index
                rating_you.tStart = t  # local t and not account for scr refresh
                rating_you.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_you, 'tStartRefresh')  # time at next scr refresh
                rating_you.setAutoDraw(True)
            continueRoutine &= rating_you.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sbQu2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sbQu2"-------
        for thisComponent in sbQu2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('cB_14.started', cB_14.tStartRefresh)
        thisExp.addData('cB_14.stopped', cB_14.tStopRefresh)
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('rating_you.response', rating_you.getRating())
        thisExp.addData('rating_you.rt', rating_you.getRT())
        thisExp.nextEntry()
        thisExp.addData('rating_you.started', rating_you.tStart)
        thisExp.addData('rating_you.stopped', rating_you.tStop)
        # the Routine "sbQu2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'sliders_12'
    
    
    # set up handler to look after randomisation of conditions etc
    buffer_1 = data.TrialHandler(nReps=4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='buffer_1')
    thisExp.addLoop(buffer_1)  # add the loop to the experiment
    thisBuffer_1 = buffer_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBuffer_1.rgb)
    if thisBuffer_1 != None:
        for paramName in thisBuffer_1:
            exec('{} = thisBuffer_1[paramName]'.format(paramName))
    
    for thisBuffer_1 in buffer_1:
        currentLoop = buffer_1
        # abbreviate parameter names if possible (e.g. rgb = thisBuffer_1.rgb)
        if thisBuffer_1 != None:
            for paramName in thisBuffer_1:
                exec('{} = thisBuffer_1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "bufWait"-------
        # update component parameters for each repeat
        import random 
        
        timeR= [0,1,1,1,1,2,2,2,3,3,4,4,5]
        intTime= int(random.choice(timeR))
        
        
        text_7.setText(bufText)
        # keep track of which components have finished
        bufWaitComponents = [cB_9, text_7]
        for thisComponent in bufWaitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        bufWaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "bufWait"-------
        while continueRoutine:
            # get current time
            t = bufWaitClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=bufWaitClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cB_9* updates
            if cB_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cB_9.frameNStart = frameN  # exact frame index
                cB_9.tStart = t  # local t and not account for scr refresh
                cB_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cB_9, 'tStartRefresh')  # time at next scr refresh
                cB_9.setAutoDraw(True)
            if cB_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cB_9.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    cB_9.tStop = t  # not accounting for scr refresh
                    cB_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cB_9, 'tStopRefresh')  # time at next scr refresh
                    cB_9.setAutoDraw(False)
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + intTime-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bufWaitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "bufWait"-------
        for thisComponent in bufWaitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        buffer_1.addData('cB_9.started', cB_9.tStartRefresh)
        buffer_1.addData('cB_9.stopped', cB_9.tStopRefresh)
        buffer_1.addData('text_7.started', text_7.tStartRefresh)
        buffer_1.addData('text_7.stopped', text_7.tStopRefresh)
        # the Routine "bufWait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4 repeats of 'buffer_1'
    
    
    # ------Prepare to start Routine "bufFix"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    bufFixComponents = [cbBuf, text_8]
    for thisComponent in bufFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    bufFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "bufFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = bufFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bufFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cbBuf* updates
        if cbBuf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cbBuf.frameNStart = frameN  # exact frame index
            cbBuf.tStart = t  # local t and not account for scr refresh
            cbBuf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cbBuf, 'tStartRefresh')  # time at next scr refresh
            cbBuf.setAutoDraw(True)
        if cbBuf.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cbBuf.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                cbBuf.tStop = t  # not accounting for scr refresh
                cbBuf.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cbBuf, 'tStopRefresh')  # time at next scr refresh
                cbBuf.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bufFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bufFix"-------
    for thisComponent in bufFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_1.addData('cbBuf.started', cbBuf.tStartRefresh)
    trials_1.addData('cbBuf.stopped', cbBuf.tStopRefresh)
    trials_1.addData('text_8.started', text_8.tStartRefresh)
    trials_1.addData('text_8.stopped', text_8.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_1'


# ------Prepare to start Routine "sbEnd"-------
routineTimer.add(30.000000)
# update component parameters for each repeat
drawRound = random.choice(roundGain)
print(drawRound)


textEndFinal = textEndText2 + str(drawRound) + ' credits!\n' + textEndText3



sbEndText.setText(textEndFinal)
sbEndKey.keys = []
sbEndKey.rt = []
# keep track of which components have finished
sbEndComponents = [cB_10, sbEndText, sbEndKey]
for thisComponent in sbEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sbEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "sbEnd"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sbEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sbEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cB_10* updates
    if cB_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cB_10.frameNStart = frameN  # exact frame index
        cB_10.tStart = t  # local t and not account for scr refresh
        cB_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cB_10, 'tStartRefresh')  # time at next scr refresh
        cB_10.setAutoDraw(True)
    if cB_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cB_10.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            cB_10.tStop = t  # not accounting for scr refresh
            cB_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cB_10, 'tStopRefresh')  # time at next scr refresh
            cB_10.setAutoDraw(False)
    
    # *sbEndText* updates
    if sbEndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sbEndText.frameNStart = frameN  # exact frame index
        sbEndText.tStart = t  # local t and not account for scr refresh
        sbEndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sbEndText, 'tStartRefresh')  # time at next scr refresh
        sbEndText.setAutoDraw(True)
    if sbEndText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sbEndText.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            sbEndText.tStop = t  # not accounting for scr refresh
            sbEndText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sbEndText, 'tStopRefresh')  # time at next scr refresh
            sbEndText.setAutoDraw(False)
    
    # *sbEndKey* updates
    waitOnFlip = False
    if sbEndKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sbEndKey.frameNStart = frameN  # exact frame index
        sbEndKey.tStart = t  # local t and not account for scr refresh
        sbEndKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sbEndKey, 'tStartRefresh')  # time at next scr refresh
        sbEndKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sbEndKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sbEndKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sbEndKey.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sbEndKey.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            sbEndKey.tStop = t  # not accounting for scr refresh
            sbEndKey.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sbEndKey, 'tStopRefresh')  # time at next scr refresh
            sbEndKey.status = FINISHED
    if sbEndKey.status == STARTED and not waitOnFlip:
        theseKeys = sbEndKey.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            sbEndKey.keys = theseKeys.name  # just the last key pressed
            sbEndKey.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sbEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sbEnd"-------
for thisComponent in sbEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cB_10.started', cB_10.tStartRefresh)
thisExp.addData('cB_10.stopped', cB_10.tStopRefresh)
thisExp.addData('sbEndText.started', sbEndText.tStartRefresh)
thisExp.addData('sbEndText.stopped', sbEndText.tStopRefresh)
# check responses
if sbEndKey.keys in ['', [], None]:  # No response was made
    sbEndKey.keys = None
thisExp.addData('sbEndKey.keys',sbEndKey.keys)
if sbEndKey.keys != None:  # we had a response
    thisExp.addData('sbEndKey.rt', sbEndKey.rt)
thisExp.addData('sbEndKey.started', sbEndKey.tStartRefresh)
thisExp.addData('sbEndKey.stopped', sbEndKey.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
