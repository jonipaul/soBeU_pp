﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on February 21, 2020, at 14:03
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
    originPath='P:\\userdata\\jonasn84\\shared\\experiments\\sbtg_pp\\soBeU_00.py',
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
cB_1 = visual.Rect(
    win=win, name='cB_1',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Dear Participant,\n\nwelcome to our experiement!\n\nPlease have a seat and go over the instructions on the following page.\n\nPress any key to continue',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyWelcome = keyboard.Keyboard()

# Initialize components for Routine "wIns"
wInsClock = core.Clock()
cB_2 = visual.Rect(
    win=win, name='cB_2',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textInstructions = visual.TextStim(win=win, name='textInstructions',
    text='You have been assigned to condition B\n\n\nIn the following task you will repeatedly interact with two other players.\n\nYou will have to make choices on how to engage with the other players.\n\nFollowing a choice you will receive a short feedback on how the other player has acted.\n\n\nAt the end of all interactions we will select one-interaction at random and pay-out the sum of money gained.\n\nPress the c-key on your keyboard to continue.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyInstructions = keyboard.Keyboard()

# Initialize components for Routine "wSer"
wSerClock = core.Clock()
cB_3 = visual.Rect(
    win=win, name='cB_3',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textServer = visual.TextStim(win=win, name='textServer',
    text="We will now connect you to the the other Players through the Server.\n\nThis might take a minute.\n\n\nPlease contact the Experimenter if your Computer is unabled to connect.\n\nPress 'c' to continue",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyServer = keyboard.Keyboard()

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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='connecting .    ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='connecting . .  ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='connecting . . .',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
idle_2 = visual.TextStim(win=win, name='idle_2',
    text='init proc     ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
idle_3 = visual.TextStim(win=win, name='idle_3',
    text='init proc 2141',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
idle_4 = visual.TextStim(win=win, name='idle_4',
    text='init proc 2215',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
idle_5 = visual.TextStim(win=win, name='idle_5',
    text='init proc 3229',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
idle_6 = visual.TextStim(win=win, name='idle_6',
    text='init proc 4325',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
idle_7 = visual.TextStim(win=win, name='idle_7',
    text='init proc 1337',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
ilde_8 = visual.TextStim(win=win, name='ilde_8',
    text='buffering      ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
idle_9 = visual.TextStim(win=win, name='idle_9',
    text='buffering .    ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
idle_10 = visual.TextStim(win=win, name='idle_10',
    text='buffering . .  ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
idle_11 = visual.TextStim(win=win, name='idle_11',
    text='buffering . . .',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
idle_12 = visual.TextStim(win=win, name='idle_12',
    text='run /serv/234_1/sd connect',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "sbIn"
sbInClock = core.Clock()
cB_6 = visual.Rect(
    win=win, name='cB_6',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
sBInstructions = visual.TextStim(win=win, name='sBInstructions',
    text="You are now ready to start with the experiment.\n\nOn the next screens you will make decisions on how to engage with other players.\n\nMake a choice using your 'left' or 'right' keys\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keySbInstructions = keyboard.Keyboard()

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
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
imagesbRnd = visual.ImageStim(
    win=win,
    name='imagesbRnd', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=0, high=4, labels=['0', '4'], scale='', markerStart='2')

# Initialize components for Routine "buf500"
buf500Clock = core.Clock()
cB_9 = visual.Rect(
    win=win, name='cB_9',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "sbFb"
sbFbClock = core.Clock()
cbFb = visual.Rect(
    win=win, name='cbFb',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textFb = visual.TextStim(win=win, name='textFb',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

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
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
imagesbRnd = visual.ImageStim(
    win=win,
    name='imagesbRnd', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=0, high=4, labels=['0', '4'], scale='', markerStart='2')

# Initialize components for Routine "buf500"
buf500Clock = core.Clock()
cB_9 = visual.Rect(
    win=win, name='cB_9',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "sbFb"
sbFbClock = core.Clock()
cbFb = visual.Rect(
    win=win, name='cbFb',
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textFb = visual.TextStim(win=win, name='textFb',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
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
    opacity=1, depth=0.0, interpolate=True)
sbEndText = visual.TextStim(win=win, name='sbEndText',
    text='Thank you for participating.\n\nThis part of the experiment is now completed.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sbEndKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wScr"-------
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
# keep track of which components have finished
wScrComponents = [cB_1, textWelcome, keyWelcome]
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
# the Routine "wScr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wIns"-------
# update component parameters for each repeat
keyInstructions.keys = []
keyInstructions.rt = []
# keep track of which components have finished
wInsComponents = [cB_2, textInstructions, keyInstructions]
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
# the Routine "wIns" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wSer"-------
# update component parameters for each repeat
keyServer.keys = []
keyServer.rt = []
# keep track of which components have finished
wSerComponents = [cB_3, textServer, keyServer]
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
# the Routine "wSer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
bufferLoop = data.TrialHandler(nReps=5, method='random', 
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
    
# completed 5 repeats of 'bufferLoop'


# ------Prepare to start Routine "bufEnd"-------
routineTimer.add(3.500000)
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
        if tThisFlipGlobal > cB_5.tStartRefresh + 3.5-frameTolerance:
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
keySbInstructions.keys = []
keySbInstructions.rt = []
# keep track of which components have finished
sbInComponents = [cB_6, sBInstructions, keySbInstructions]
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
# the Routine "sbIn" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sbLoop = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('contitions.xlsx'),
    seed=None, name='sbLoop')
thisExp.addLoop(sbLoop)  # add the loop to the experiment
thisSbLoop = sbLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSbLoop.rgb)
if thisSbLoop != None:
    for paramName in thisSbLoop:
        exec('{} = thisSbLoop[paramName]'.format(paramName))

for thisSbLoop in sbLoop:
    currentLoop = sbLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSbLoop.rgb)
    if thisSbLoop != None:
        for paramName in thisSbLoop:
            exec('{} = thisSbLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sbRnd"-------
    # update component parameters for each repeat
    text.setText('This round you are playing with ' + playerId + '!')
    imagesbRnd.setImage(avatarFile)
    rating.reset()
    # keep track of which components have finished
    sbRndComponents = [cB_8, text, imagesbRnd, rating]
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
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
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
    sbLoop.addData('cB_8.started', cB_8.tStartRefresh)
    sbLoop.addData('cB_8.stopped', cB_8.tStopRefresh)
    sbLoop.addData('text.started', text.tStartRefresh)
    sbLoop.addData('text.stopped', text.tStopRefresh)
    sbLoop.addData('imagesbRnd.started', imagesbRnd.tStartRefresh)
    sbLoop.addData('imagesbRnd.stopped', imagesbRnd.tStopRefresh)
    # store data for sbLoop (TrialHandler)
    sbLoop.addData('rating.response', rating.getRating())
    sbLoop.addData('rating.rt', rating.getRT())
    sbLoop.addData('rating.history', rating.getHistory())
    sbLoop.addData('rating.started', rating.tStart)
    sbLoop.addData('rating.stopped', rating.tStop)
    # the Routine "sbRnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "buf500"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    buf500Components = [cB_9]
    for thisComponent in buf500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    buf500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "buf500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = buf500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=buf500Clock)
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
            if tThisFlipGlobal > cB_9.tStartRefresh + .500-frameTolerance:
                # keep track of stop time/frame for later
                cB_9.tStop = t  # not accounting for scr refresh
                cB_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cB_9, 'tStopRefresh')  # time at next scr refresh
                cB_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in buf500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "buf500"-------
    for thisComponent in buf500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sbLoop.addData('cB_9.started', cB_9.tStartRefresh)
    sbLoop.addData('cB_9.stopped', cB_9.tStopRefresh)
    
    # ------Prepare to start Routine "sbFb"-------
    # update component parameters for each repeat
    textFb.setText(+ playerId + 'has decided to' + choiceLabel + 'you receive' + amount)
    # keep track of which components have finished
    sbFbComponents = [cbFb, textFb]
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
    while continueRoutine:
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
            if tThisFlipGlobal > cbFb.tStartRefresh + .500-frameTolerance:
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
    thisExp.addData('cbFb.started', cbFb.tStartRefresh)
    thisExp.addData('cbFb.stopped', cbFb.tStopRefresh)
    thisExp.addData('textFb.started', textFb.tStartRefresh)
    thisExp.addData('textFb.stopped', textFb.tStopRefresh)
    # the Routine "sbFb" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'sbLoop'


# set up handler to look after randomisation of conditions etc
sbLoop_rev = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('contitions.xlsx'),
    seed=None, name='sbLoop_rev')
thisExp.addLoop(sbLoop_rev)  # add the loop to the experiment
thisSbLoop_rev = sbLoop_rev.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSbLoop_rev.rgb)
if thisSbLoop_rev != None:
    for paramName in thisSbLoop_rev:
        exec('{} = thisSbLoop_rev[paramName]'.format(paramName))

for thisSbLoop_rev in sbLoop_rev:
    currentLoop = sbLoop_rev
    # abbreviate parameter names if possible (e.g. rgb = thisSbLoop_rev.rgb)
    if thisSbLoop_rev != None:
        for paramName in thisSbLoop_rev:
            exec('{} = thisSbLoop_rev[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sbRnd"-------
    # update component parameters for each repeat
    text.setText('This round you are playing with ' + playerId + '!')
    imagesbRnd.setImage(avatarFile)
    rating.reset()
    # keep track of which components have finished
    sbRndComponents = [cB_8, text, imagesbRnd, rating]
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
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
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
    sbLoop_rev.addData('cB_8.started', cB_8.tStartRefresh)
    sbLoop_rev.addData('cB_8.stopped', cB_8.tStopRefresh)
    sbLoop_rev.addData('text.started', text.tStartRefresh)
    sbLoop_rev.addData('text.stopped', text.tStopRefresh)
    sbLoop_rev.addData('imagesbRnd.started', imagesbRnd.tStartRefresh)
    sbLoop_rev.addData('imagesbRnd.stopped', imagesbRnd.tStopRefresh)
    # store data for sbLoop_rev (TrialHandler)
    sbLoop_rev.addData('rating.response', rating.getRating())
    sbLoop_rev.addData('rating.rt', rating.getRT())
    sbLoop_rev.addData('rating.history', rating.getHistory())
    sbLoop_rev.addData('rating.started', rating.tStart)
    sbLoop_rev.addData('rating.stopped', rating.tStop)
    # the Routine "sbRnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "buf500"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    buf500Components = [cB_9]
    for thisComponent in buf500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    buf500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "buf500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = buf500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=buf500Clock)
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
            if tThisFlipGlobal > cB_9.tStartRefresh + .500-frameTolerance:
                # keep track of stop time/frame for later
                cB_9.tStop = t  # not accounting for scr refresh
                cB_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cB_9, 'tStopRefresh')  # time at next scr refresh
                cB_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in buf500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "buf500"-------
    for thisComponent in buf500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sbLoop_rev.addData('cB_9.started', cB_9.tStartRefresh)
    sbLoop_rev.addData('cB_9.stopped', cB_9.tStopRefresh)
    
    # ------Prepare to start Routine "sbFb"-------
    # update component parameters for each repeat
    textFb.setText(+ playerId + 'has decided to' + choiceLabel + 'you receive' + amount)
    # keep track of which components have finished
    sbFbComponents = [cbFb, textFb]
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
    while continueRoutine:
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
            if tThisFlipGlobal > cbFb.tStartRefresh + .500-frameTolerance:
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
    thisExp.addData('cbFb.started', cbFb.tStartRefresh)
    thisExp.addData('cbFb.stopped', cbFb.tStopRefresh)
    thisExp.addData('textFb.started', textFb.tStartRefresh)
    thisExp.addData('textFb.stopped', textFb.tStopRefresh)
    # the Routine "sbFb" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'sbLoop_rev'


# ------Prepare to start Routine "sbEnd"-------
routineTimer.add(30.000000)
# update component parameters for each repeat
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