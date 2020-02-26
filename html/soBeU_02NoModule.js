<<<<<<< HEAD
﻿/***************** 
 * Sobeu_02 Test *
 *****************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'soBeU_02';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(wScrRoutineBegin);
flowScheduler.add(wScrRoutineEachFrame);
flowScheduler.add(wScrRoutineEnd);
flowScheduler.add(wInsRoutineBegin);
flowScheduler.add(wInsRoutineEachFrame);
flowScheduler.add(wInsRoutineEnd);
flowScheduler.add(wIns2RoutineBegin);
flowScheduler.add(wIns2RoutineEachFrame);
flowScheduler.add(wIns2RoutineEnd);
flowScheduler.add(wPflRoutineBegin);
flowScheduler.add(wPflRoutineEachFrame);
flowScheduler.add(wPflRoutineEnd);
flowScheduler.add(wSerRoutineBegin);
flowScheduler.add(wSerRoutineEachFrame);
flowScheduler.add(wSerRoutineEnd);
const bufferLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(bufferLoopLoopBegin, bufferLoopLoopScheduler);
flowScheduler.add(bufferLoopLoopScheduler);
flowScheduler.add(bufferLoopLoopEnd);
flowScheduler.add(bufEndRoutineBegin);
flowScheduler.add(bufEndRoutineEachFrame);
flowScheduler.add(bufEndRoutineEnd);
flowScheduler.add(sbInRoutineBegin);
flowScheduler.add(sbInRoutineEachFrame);
flowScheduler.add(sbInRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(sbEndRoutineBegin);
flowScheduler.add(sbEndRoutineEachFrame);
flowScheduler.add(sbEndRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "wScr"
  wScrClock = new util.Clock();
  textWelcomeText ="""
  Dear Participant, \n
  Welcome to our experiement! \n
  Please carefully go over the instructions on the following pages. \n
  If you have any questions please ask the experimenter for help. \n\n
  Press any key to continue
  """
  textWelcomeText = str(textWelcomeText)
  
  textInstructionsText= """
  You have been randomly assigned to condition B. \n\n
  In the following task you will repeatedly interact with two other players.You will have to make choices on how to engage with the other players.\n
  You will make investments and try to maximize your gains (credits).\n\n
  Following a choice you will receive a short feedback on how the other player has acted.\n
  At the end of all interactions one random interaction will be selected and payed-out the sum of credits gained.\n\n
  see next page for more information.\n
  Press \'c\' to continue.
  """
  
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
  
  Press \'c\' to continue.
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
  Press \'c\' to continue.
  """
  
  textInstructionsSb = """
  You are now ready to start with the experiment. \n
  On the next screens you will make decisions on how to engage with other players.\n\n
  Make a choice using your \'left\' or \'right\' keys and confirm with \'enter\'
  
  Note, all decisions (yours and others) happen simultaneously, and not in response to each other.
  
  Press \'c\' to begin.
  """
  
  textSbText = """ How much do you want to invest?"""
  
  textSbFeed1 = ' has decided to return '
  textSbFeed2 = ' percent of your investment. \n\n'
  textSbFeed3 = 'Your return is '
  textSbFeed4 = ' credits!\n\n'
  textSbFeed5 = 'Your total gain for this round is '
  
  textEndText = """Thank you for participating.
  
  This part of the experiment is now completed.
  """
  
  bufText = """waiting for other player"""
  cB_1 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_1', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyWelcome = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_0 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wIns"
  wInsClock = new util.Clock();
  cB_2 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_2', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstructions',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyInstructions = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_1 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wIns2"
  wIns2Clock = new util.Clock();
  cB_12 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_12', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textInstructions_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstructions_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  keyInstructions_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_3 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wPfl"
  wPflClock = new util.Clock();
  cB = new visual.Rect ({
    win: psychoJS.window, name: 'cB', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  displayText = new visual.TextStim({
    win: psychoJS.window,
    name: 'displayText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  copyText = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  out = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wSer"
  wSerClock = new util.Clock();
  cB_3 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_3', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textServer = new visual.TextStim({
    win: psychoJS.window,
    name: 'textServer',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyServer = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "bufRou_2"
  bufRou_2Clock = new util.Clock();
  cB_4 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_4', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_1',
    text: 'connecting      ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'connecting .    ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'connecting . .  ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'connecting . . .',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "bufEnd"
  bufEndClock = new util.Clock();
  cB_5 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_5', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  idle = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle',
    text: 'found',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  idle_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_2',
    text: 'init proc     ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  idle_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_3',
    text: 'init proc 2141',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  idle_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_4',
    text: 'init proc 2215',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  idle_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_5',
    text: 'init proc 3229',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  idle_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_6',
    text: 'init proc 4325',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  idle_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_7',
    text: 'init proc 1337',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  ilde_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ilde_8',
    text: 'buffering      ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  idle_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_9',
    text: 'buffering .    ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  idle_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_10',
    text: 'buffering . .  ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  idle_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_11',
    text: 'buffering . . .',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  idle_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_12',
    text: 'run /serv/234_1/sd connect',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  // Initialize components for Routine "sbIn"
  sbInClock = new util.Clock();
  cB_6 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_6', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  sBInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'sBInstructions',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keySbInstructions = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_sb = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sbRnd"
  sbRndClock = new util.Clock();
  cB_8 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_8', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  imagesbRnd = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagesbRnd', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.2], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "bufRand"
  bufRandClock = new util.Clock();
  cB_9 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_9', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "sbFb"
  sbFbClock = new util.Clock();
  cbFb = new visual.Rect ({
    win: psychoJS.window, name: 'cbFb', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textFb = new visual.TextStim({
    win: psychoJS.window,
    name: 'textFb',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  out_Fb = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "bufFix"
  bufFixClock = new util.Clock();
  cbBuf = new visual.Rect ({
    win: psychoJS.window, name: 'cbBuf', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.4,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "sbQu"
  sbQuClock = new util.Clock();
  cB_11 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_11', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "bufRand"
  bufRandClock = new util.Clock();
  cB_9 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_9', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "bufFix"
  bufFixClock = new util.Clock();
  cbBuf = new visual.Rect ({
    win: psychoJS.window, name: 'cbBuf', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.4,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "sbEnd"
  sbEndClock = new util.Clock();
  cB_10 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_10', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  sbEndText = new visual.TextStim({
    win: psychoJS.window,
    name: 'sbEndText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  sbEndKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function wScrRoutineBegin() {
  //------Prepare to start Routine 'wScr'-------
  t = 0;
  wScrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textWelcome.setText(textWelcomeText);
  keyWelcome.keys = undefined;
  keyWelcome.rt = undefined;
  out_0.keys = undefined;
  out_0.rt = undefined;
  // keep track of which components have finished
  wScrComponents = [];
  wScrComponents.push(cB_1);
  wScrComponents.push(textWelcome);
  wScrComponents.push(keyWelcome);
  wScrComponents.push(out_0);
  
  wScrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wScrRoutineEachFrame() {
  //------Loop for each frame of Routine 'wScr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wScrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_1* updates
  if (t >= 0.0 && cB_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_1.tStart = t;  // (not accounting for frame time here)
    cB_1.frameNStart = frameN;  // exact frame index
    cB_1.setAutoDraw(true);
  }

  
  // *textWelcome* updates
  if (t >= 0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textWelcome.tStart = t;  // (not accounting for frame time here)
    textWelcome.frameNStart = frameN;  // exact frame index
    textWelcome.setAutoDraw(true);
  }

  
  // *keyWelcome* updates
  if (t >= 2 && keyWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyWelcome.tStart = t;  // (not accounting for frame time here)
    keyWelcome.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyWelcome.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyWelcome.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyWelcome.clearEvents(); });
  }

  if (keyWelcome.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyWelcome.getKeys({keyList: [], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyWelcome.keys = theseKeys[0].name;  // just the last key pressed
      keyWelcome.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_0* updates
  if (t >= 0.0 && out_0.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_0.tStart = t;  // (not accounting for frame time here)
    out_0.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_0.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_0.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_0.clearEvents(); });
  }

  if (out_0.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_0.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_0.keys = theseKeys[0].name;  // just the last key pressed
      out_0.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wScrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wScrRoutineEnd() {
  //------Ending Routine 'wScr'-------
  wScrComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyWelcome.keys', keyWelcome.keys);
  if (typeof keyWelcome.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyWelcome.rt', keyWelcome.rt);
      routineTimer.reset();
      }
  
  keyWelcome.stop();
  psychoJS.experiment.addData('out_0.keys', out_0.keys);
  if (typeof out_0.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_0.rt', out_0.rt);
      routineTimer.reset();
      }
  
  out_0.stop();
  // the Routine "wScr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wInsRoutineBegin() {
  //------Prepare to start Routine 'wIns'-------
  t = 0;
  wInsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textInstructions.setText(textInstructionsText);
  keyInstructions.keys = undefined;
  keyInstructions.rt = undefined;
  out_1.keys = undefined;
  out_1.rt = undefined;
  // keep track of which components have finished
  wInsComponents = [];
  wInsComponents.push(cB_2);
  wInsComponents.push(textInstructions);
  wInsComponents.push(keyInstructions);
  wInsComponents.push(out_1);
  
  wInsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wInsRoutineEachFrame() {
  //------Loop for each frame of Routine 'wIns'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wInsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_2* updates
  if (t >= 0.0 && cB_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_2.tStart = t;  // (not accounting for frame time here)
    cB_2.frameNStart = frameN;  // exact frame index
    cB_2.setAutoDraw(true);
  }

  
  // *textInstructions* updates
  if (t >= 0 && textInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textInstructions.tStart = t;  // (not accounting for frame time here)
    textInstructions.frameNStart = frameN;  // exact frame index
    textInstructions.setAutoDraw(true);
  }

  
  // *keyInstructions* updates
  if (t >= 2 && keyInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyInstructions.tStart = t;  // (not accounting for frame time here)
    keyInstructions.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyInstructions.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions.clearEvents(); });
  }

  if (keyInstructions.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyInstructions.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyInstructions.keys = theseKeys[0].name;  // just the last key pressed
      keyInstructions.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_1* updates
  if (t >= 0.0 && out_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_1.tStart = t;  // (not accounting for frame time here)
    out_1.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_1.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_1.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_1.clearEvents(); });
  }

  if (out_1.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_1.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_1.keys = theseKeys[0].name;  // just the last key pressed
      out_1.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wInsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wInsRoutineEnd() {
  //------Ending Routine 'wIns'-------
  wInsComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyInstructions.keys', keyInstructions.keys);
  if (typeof keyInstructions.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyInstructions.rt', keyInstructions.rt);
      routineTimer.reset();
      }
  
  keyInstructions.stop();
  psychoJS.experiment.addData('out_1.keys', out_1.keys);
  if (typeof out_1.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_1.rt', out_1.rt);
      routineTimer.reset();
      }
  
  out_1.stop();
  // the Routine "wIns" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wIns2RoutineBegin() {
  //------Prepare to start Routine 'wIns2'-------
  t = 0;
  wIns2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textInstructions_2.setText(textInstructionsText2);
  keyInstructions_2.keys = undefined;
  keyInstructions_2.rt = undefined;
  out_3.keys = undefined;
  out_3.rt = undefined;
  // keep track of which components have finished
  wIns2Components = [];
  wIns2Components.push(cB_12);
  wIns2Components.push(textInstructions_2);
  wIns2Components.push(keyInstructions_2);
  wIns2Components.push(out_3);
  
  wIns2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wIns2RoutineEachFrame() {
  //------Loop for each frame of Routine 'wIns2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wIns2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_12* updates
  if (t >= 0.0 && cB_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_12.tStart = t;  // (not accounting for frame time here)
    cB_12.frameNStart = frameN;  // exact frame index
    cB_12.setAutoDraw(true);
  }

  
  // *textInstructions_2* updates
  if (t >= 0 && textInstructions_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textInstructions_2.tStart = t;  // (not accounting for frame time here)
    textInstructions_2.frameNStart = frameN;  // exact frame index
    textInstructions_2.setAutoDraw(true);
  }

  
  // *keyInstructions_2* updates
  if (t >= 2 && keyInstructions_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyInstructions_2.tStart = t;  // (not accounting for frame time here)
    keyInstructions_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyInstructions_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions_2.clearEvents(); });
  }

  if (keyInstructions_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyInstructions_2.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyInstructions_2.keys = theseKeys[0].name;  // just the last key pressed
      keyInstructions_2.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_3* updates
  if (t >= 0.0 && out_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_3.tStart = t;  // (not accounting for frame time here)
    out_3.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_3.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_3.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_3.clearEvents(); });
  }

  if (out_3.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_3.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_3.keys = theseKeys[0].name;  // just the last key pressed
      out_3.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wIns2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wIns2RoutineEnd() {
  //------Ending Routine 'wIns2'-------
  wIns2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyInstructions_2.keys', keyInstructions_2.keys);
  if (typeof keyInstructions_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyInstructions_2.rt', keyInstructions_2.rt);
      routineTimer.reset();
      }
  
  keyInstructions_2.stop();
  psychoJS.experiment.addData('out_3.keys', out_3.keys);
  if (typeof out_3.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_3.rt', out_3.rt);
      routineTimer.reset();
      }
  
  out_3.stop();
  // the Routine "wIns2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wPflRoutineBegin() {
  //------Prepare to start Routine 'wPfl'-------
  t = 0;
  wPflClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  modify = false;
  text.text = '';
  displayText.setText(textProfileText);
  copyText.setText('');
  out.keys = undefined;
  out.rt = undefined;
  // keep track of which components have finished
  wPflComponents = [];
  wPflComponents.push(cB);
  wPflComponents.push(displayText);
  wPflComponents.push(copyText);
  wPflComponents.push(out);
  
  wPflComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wPflRoutineEachFrame() {
  //------Loop for each frame of Routine 'wPfl'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wPflClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB* updates
  if (t >= 0.0 && cB.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB.tStart = t;  // (not accounting for frame time here)
    cB.frameNStart = frameN;  // exact frame index
    cB.setAutoDraw(true);
  }

  let theseKeys = psychoJS.eventManager.getKeys();
  if (theseKeys.length > 0) {  // at least one key was pressed
    textAdd = theseKeys[theseKeys.length-1]; 
    }
  
  
  if (textAdd === 'return') {
      textAdd = '';  // Add nothing
      continueRoutine = false;  // End routine (if that is what you want)
  } else if (textAdd === 'space') {
      textAdd = ' ';  // Add a space
  } else if (textAdd === 'backspace') {
      text.text = text.text.slice(0, -1);
      textAdd = undefined;
  } else if (['lshift', 'rshift'].includes(textAdd)) {
      modify = true;
  } else if (textAdd !== undefined) {
      if (modify) {
          text.text = text.text + textAdd.toUpperCase();
          modify = false;
      } else {
          text.text = text.text + textAdd
      }
      textAdd = undefined;
  }
  
  // *displayText* updates
  if (t >= 0.0 && displayText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    displayText.tStart = t;  // (not accounting for frame time here)
    displayText.frameNStart = frameN;  // exact frame index
    displayText.setAutoDraw(true);
  }

  
  // *copyText* updates
  if (t >= 0.0 && copyText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    copyText.tStart = t;  // (not accounting for frame time here)
    copyText.frameNStart = frameN;  // exact frame index
    copyText.setAutoDraw(true);
  }

  
  // *out* updates
  if (t >= 0.0 && out.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out.tStart = t;  // (not accounting for frame time here)
    out.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out.clearEvents(); });
  }

  if (out.status === PsychoJS.Status.STARTED) {
    let theseKeys = out.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out.keys = theseKeys[0].name;  // just the last key pressed
      out.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wPflComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wPflRoutineEnd() {
  //------Ending Routine 'wPfl'-------
  wPflComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData("typedWord", text.text)
  text.setText('')  // empty the onscreen text ready for next input
  psychoJS.experiment.addData('out.keys', out.keys);
  if (typeof out.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out.rt', out.rt);
      routineTimer.reset();
      }
  
  out.stop();
  // the Routine "wPfl" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wSerRoutineBegin() {
  //------Prepare to start Routine 'wSer'-------
  t = 0;
  wSerClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textServer.setText(textServerText);
  keyServer.keys = undefined;
  keyServer.rt = undefined;
  out_2.keys = undefined;
  out_2.rt = undefined;
  // keep track of which components have finished
  wSerComponents = [];
  wSerComponents.push(cB_3);
  wSerComponents.push(textServer);
  wSerComponents.push(keyServer);
  wSerComponents.push(out_2);
  
  wSerComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wSerRoutineEachFrame() {
  //------Loop for each frame of Routine 'wSer'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wSerClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_3* updates
  if (t >= 0.0 && cB_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_3.tStart = t;  // (not accounting for frame time here)
    cB_3.frameNStart = frameN;  // exact frame index
    cB_3.setAutoDraw(true);
  }

  
  // *textServer* updates
  if (t >= 0 && textServer.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textServer.tStart = t;  // (not accounting for frame time here)
    textServer.frameNStart = frameN;  // exact frame index
    textServer.setAutoDraw(true);
  }

  
  // *keyServer* updates
  if (t >= 2 && keyServer.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyServer.tStart = t;  // (not accounting for frame time here)
    keyServer.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyServer.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyServer.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyServer.clearEvents(); });
  }

  if (keyServer.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyServer.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyServer.keys = theseKeys[0].name;  // just the last key pressed
      keyServer.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_2* updates
  if (t >= 0.0 && out_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_2.tStart = t;  // (not accounting for frame time here)
    out_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_2.clearEvents(); });
  }

  if (out_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_2.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_2.keys = theseKeys[0].name;  // just the last key pressed
      out_2.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wSerComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wSerRoutineEnd() {
  //------Ending Routine 'wSer'-------
  wSerComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyServer.keys', keyServer.keys);
  if (typeof keyServer.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyServer.rt', keyServer.rt);
      routineTimer.reset();
      }
  
  keyServer.stop();
  psychoJS.experiment.addData('out_2.keys', out_2.keys);
  if (typeof out_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_2.rt', out_2.rt);
      routineTimer.reset();
      }
  
  out_2.stop();
  // the Routine "wSer" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function bufferLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  bufferLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'bufferLoop'});
  psychoJS.experiment.addLoop(bufferLoop); // add the loop to the experiment
  currentLoop = bufferLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = bufferLoop[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisBufferLoop = result.value;
    thisScheduler.add(importConditions(bufferLoop));
    thisScheduler.add(bufRou_2RoutineBegin);
    thisScheduler.add(bufRou_2RoutineEachFrame);
    thisScheduler.add(bufRou_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function bufferLoopLoopEnd() {
  psychoJS.experiment.removeLoop(bufferLoop);

  return Scheduler.Event.NEXT;
}

function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'contitions.xlsx', '1:20'),
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    const sbLoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(sbLoopLoopBegin, sbLoopLoopScheduler);
    thisScheduler.add(sbLoopLoopScheduler);
    thisScheduler.add(sbLoopLoopEnd);
    const sliders_1LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(sliders_1LoopBegin, sliders_1LoopScheduler);
    thisScheduler.add(sliders_1LoopScheduler);
    thisScheduler.add(sliders_1LoopEnd);
    const trials_2LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
    thisScheduler.add(trials_2LoopScheduler);
    thisScheduler.add(trials_2LoopEnd);
    thisScheduler.add(bufFixRoutineBegin);
    thisScheduler.add(bufFixRoutineEachFrame);
    thisScheduler.add(bufFixRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function sbLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  sbLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'contitions.xlsx', '1:20'),
    seed: undefined, name: 'sbLoop'});
  psychoJS.experiment.addLoop(sbLoop); // add the loop to the experiment
  currentLoop = sbLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = sbLoop[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisSbLoop = result.value;
    thisScheduler.add(importConditions(sbLoop));
    thisScheduler.add(sbRndRoutineBegin);
    thisScheduler.add(sbRndRoutineEachFrame);
    thisScheduler.add(sbRndRoutineEnd);
    thisScheduler.add(bufRandRoutineBegin);
    thisScheduler.add(bufRandRoutineEachFrame);
    thisScheduler.add(bufRandRoutineEnd);
    thisScheduler.add(sbFbRoutineBegin);
    thisScheduler.add(sbFbRoutineEachFrame);
    thisScheduler.add(sbFbRoutineEnd);
    thisScheduler.add(bufFixRoutineBegin);
    thisScheduler.add(bufFixRoutineEachFrame);
    thisScheduler.add(bufFixRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function sbLoopLoopEnd() {
  psychoJS.experiment.removeLoop(sbLoop);

  return Scheduler.Event.NEXT;
}

function sliders_1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  sliders_1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'sliders.xlsx',
    seed: undefined, name: 'sliders_1'});
  psychoJS.experiment.addLoop(sliders_1); // add the loop to the experiment
  currentLoop = sliders_1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = sliders_1[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisSlider_1 = result.value;
    thisScheduler.add(importConditions(sliders_1));
    thisScheduler.add(sbQuRoutineBegin);
    thisScheduler.add(sbQuRoutineEachFrame);
    thisScheduler.add(sbQuRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function sliders_1LoopEnd() {
  psychoJS.experiment.removeLoop(sliders_1);

  return Scheduler.Event.NEXT;
}

function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_2'});
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_2[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_2 = result.value;
    thisScheduler.add(importConditions(trials_2));
    thisScheduler.add(bufRandRoutineBegin);
    thisScheduler.add(bufRandRoutineEachFrame);
    thisScheduler.add(bufRandRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

function bufRou_2RoutineBegin() {
  //------Prepare to start Routine 'bufRou_2'-------
  t = 0;
  bufRou_2Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  bufRou_2Components = [];
  bufRou_2Components.push(cB_4);
  bufRou_2Components.push(text_1);
  bufRou_2Components.push(text_2);
  bufRou_2Components.push(text_3);
  bufRou_2Components.push(text_4);
  
  bufRou_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufRou_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'bufRou_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufRou_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_4* updates
  if (t >= 0.0 && cB_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_4.tStart = t;  // (not accounting for frame time here)
    cB_4.frameNStart = frameN;  // exact frame index
    cB_4.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_4.setAutoDraw(false);
  }
  
  // *text_1* updates
  if (t >= 0.0 && text_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_1.tStart = t;  // (not accounting for frame time here)
    text_1.frameNStart = frameN;  // exact frame index
    text_1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_1.setAutoDraw(false);
  }
  
  // *text_2* updates
  if (t >= 1 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_2.setAutoDraw(false);
  }
  
  // *text_3* updates
  if (t >= 1.5 && text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_3.tStart = t;  // (not accounting for frame time here)
    text_3.frameNStart = frameN;  // exact frame index
    text_3.setAutoDraw(true);
  }

  frameRemains = 1.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_3.setAutoDraw(false);
  }
  
  // *text_4* updates
  if (t >= 2 && text_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_4.tStart = t;  // (not accounting for frame time here)
    text_4.frameNStart = frameN;  // exact frame index
    text_4.setAutoDraw(true);
  }

  frameRemains = 2 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_4.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufRou_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufRou_2RoutineEnd() {
  //------Ending Routine 'bufRou_2'-------
  bufRou_2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

function bufEndRoutineBegin() {
  //------Prepare to start Routine 'bufEnd'-------
  t = 0;
  bufEndClock.reset(); // clock
  frameN = -1;
  routineTimer.add(4.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  bufEndComponents = [];
  bufEndComponents.push(cB_5);
  bufEndComponents.push(idle);
  bufEndComponents.push(idle_2);
  bufEndComponents.push(idle_3);
  bufEndComponents.push(idle_4);
  bufEndComponents.push(idle_5);
  bufEndComponents.push(idle_6);
  bufEndComponents.push(idle_7);
  bufEndComponents.push(ilde_8);
  bufEndComponents.push(idle_9);
  bufEndComponents.push(idle_10);
  bufEndComponents.push(idle_11);
  bufEndComponents.push(idle_12);
  
  bufEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufEndRoutineEachFrame() {
  //------Loop for each frame of Routine 'bufEnd'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufEndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_5* updates
  if (t >= 0.0 && cB_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_5.tStart = t;  // (not accounting for frame time here)
    cB_5.frameNStart = frameN;  // exact frame index
    cB_5.setAutoDraw(true);
  }

  frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_5.setAutoDraw(false);
  }
  
  // *idle* updates
  if (t >= 0.2 && idle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle.tStart = t;  // (not accounting for frame time here)
    idle.frameNStart = frameN;  // exact frame index
    idle.setAutoDraw(true);
  }

  frameRemains = 0.5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle.setAutoDraw(false);
  }
  
  // *idle_2* updates
  if (t >= 0.5 && idle_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_2.tStart = t;  // (not accounting for frame time here)
    idle_2.frameNStart = frameN;  // exact frame index
    idle_2.setAutoDraw(true);
  }

  frameRemains = 0.7  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_2.setAutoDraw(false);
  }
  
  // *idle_3* updates
  if (t >= 0.7 && idle_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_3.tStart = t;  // (not accounting for frame time here)
    idle_3.frameNStart = frameN;  // exact frame index
    idle_3.setAutoDraw(true);
  }

  frameRemains = 0.8  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_3.setAutoDraw(false);
  }
  
  // *idle_4* updates
  if (t >= 0.8 && idle_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_4.tStart = t;  // (not accounting for frame time here)
    idle_4.frameNStart = frameN;  // exact frame index
    idle_4.setAutoDraw(true);
  }

  frameRemains = 0.95  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_4.setAutoDraw(false);
  }
  
  // *idle_5* updates
  if (t >= 0.95 && idle_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_5.tStart = t;  // (not accounting for frame time here)
    idle_5.frameNStart = frameN;  // exact frame index
    idle_5.setAutoDraw(true);
  }

  frameRemains = 1.1  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_5.setAutoDraw(false);
  }
  
  // *idle_6* updates
  if (t >= 1.1 && idle_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_6.tStart = t;  // (not accounting for frame time here)
    idle_6.frameNStart = frameN;  // exact frame index
    idle_6.setAutoDraw(true);
  }

  frameRemains = 1.25  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_6.setAutoDraw(false);
  }
  
  // *idle_7* updates
  if (t >= 1.25 && idle_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_7.tStart = t;  // (not accounting for frame time here)
    idle_7.frameNStart = frameN;  // exact frame index
    idle_7.setAutoDraw(true);
  }

  frameRemains = 1.35  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_7.setAutoDraw(false);
  }
  
  // *ilde_8* updates
  if (t >= 1.35 && ilde_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ilde_8.tStart = t;  // (not accounting for frame time here)
    ilde_8.frameNStart = frameN;  // exact frame index
    ilde_8.setAutoDraw(true);
  }

  frameRemains = 1.85  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (ilde_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    ilde_8.setAutoDraw(false);
  }
  
  // *idle_9* updates
  if (t >= 1.85 && idle_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_9.tStart = t;  // (not accounting for frame time here)
    idle_9.frameNStart = frameN;  // exact frame index
    idle_9.setAutoDraw(true);
  }

  frameRemains = 1.85 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_9.setAutoDraw(false);
  }
  
  // *idle_10* updates
  if (t >= 2.35 && idle_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_10.tStart = t;  // (not accounting for frame time here)
    idle_10.frameNStart = frameN;  // exact frame index
    idle_10.setAutoDraw(true);
  }

  frameRemains = 2.35 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_10.setAutoDraw(false);
  }
  
  // *idle_11* updates
  if (t >= 2.85 && idle_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_11.tStart = t;  // (not accounting for frame time here)
    idle_11.frameNStart = frameN;  // exact frame index
    idle_11.setAutoDraw(true);
  }

  frameRemains = 2.85 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_11.setAutoDraw(false);
  }
  
  // *idle_12* updates
  if (t >= 3.35 && idle_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_12.tStart = t;  // (not accounting for frame time here)
    idle_12.frameNStart = frameN;  // exact frame index
    idle_12.setAutoDraw(true);
  }

  frameRemains = 3.5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_12.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufEndRoutineEnd() {
  //------Ending Routine 'bufEnd'-------
  bufEndComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

function sbInRoutineBegin() {
  //------Prepare to start Routine 'sbIn'-------
  t = 0;
  sbInClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  sBInstructions.setText(textInstructionsSb2);
  keySbInstructions.keys = undefined;
  keySbInstructions.rt = undefined;
  out_sb.keys = undefined;
  out_sb.rt = undefined;
  // keep track of which components have finished
  sbInComponents = [];
  sbInComponents.push(cB_6);
  sbInComponents.push(sBInstructions);
  sbInComponents.push(keySbInstructions);
  sbInComponents.push(out_sb);
  
  sbInComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbInRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbIn'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbInClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_6* updates
  if (t >= 0.0 && cB_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_6.tStart = t;  // (not accounting for frame time here)
    cB_6.frameNStart = frameN;  // exact frame index
    cB_6.setAutoDraw(true);
  }

  
  // *sBInstructions* updates
  if (t >= 0.2 && sBInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sBInstructions.tStart = t;  // (not accounting for frame time here)
    sBInstructions.frameNStart = frameN;  // exact frame index
    sBInstructions.setAutoDraw(true);
  }

  
  // *keySbInstructions* updates
  if (t >= 2 && keySbInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keySbInstructions.tStart = t;  // (not accounting for frame time here)
    keySbInstructions.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keySbInstructions.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keySbInstructions.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keySbInstructions.clearEvents(); });
  }

  if (keySbInstructions.status === PsychoJS.Status.STARTED) {
    let theseKeys = keySbInstructions.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keySbInstructions.keys = theseKeys[0].name;  // just the last key pressed
      keySbInstructions.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_sb* updates
  if (t >= 0.0 && out_sb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_sb.tStart = t;  // (not accounting for frame time here)
    out_sb.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_sb.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_sb.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_sb.clearEvents(); });
  }

  if (out_sb.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_sb.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_sb.keys = theseKeys[0].name;  // just the last key pressed
      out_sb.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbInComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbInRoutineEnd() {
  //------Ending Routine 'sbIn'-------
  sbInComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keySbInstructions.keys', keySbInstructions.keys);
  if (typeof keySbInstructions.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keySbInstructions.rt', keySbInstructions.rt);
      routineTimer.reset();
      }
  
  keySbInstructions.stop();
  psychoJS.experiment.addData('out_sb.keys', out_sb.keys);
  if (typeof out_sb.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_sb.rt', out_sb.rt);
      routineTimer.reset();
      }
  
  out_sb.stop();
  // the Routine "sbIn" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function sbRndRoutineBegin() {
  //------Prepare to start Routine 'sbRnd'-------
  t = 0;
  sbRndClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text.setText((('This round you are playing with ' + playerId) + '!'));
  imagesbRnd.setImage(avatarFile);
  text_6.setText(textSbText);
  // keep track of which components have finished
  sbRndComponents = [];
  sbRndComponents.push(cB_8);
  sbRndComponents.push(text);
  sbRndComponents.push(imagesbRnd);
  sbRndComponents.push(text_6);
  
  sbRndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbRndRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbRnd'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbRndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_8* updates
  if (t >= 0.0 && cB_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_8.tStart = t;  // (not accounting for frame time here)
    cB_8.frameNStart = frameN;  // exact frame index
    cB_8.setAutoDraw(true);
  }

  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *imagesbRnd* updates
  if (t >= 0.0 && imagesbRnd.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    imagesbRnd.tStart = t;  // (not accounting for frame time here)
    imagesbRnd.frameNStart = frameN;  // exact frame index
    imagesbRnd.setAutoDraw(true);
  }

  
  // *text_6* updates
  if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_6.tStart = t;  // (not accounting for frame time here)
    text_6.frameNStart = frameN;  // exact frame index
    text_6.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbRndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbRndRoutineEnd() {
  //------Ending Routine 'sbRnd'-------
  sbRndComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "sbRnd" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function bufRandRoutineBegin() {
  //------Prepare to start Routine 'bufRand'-------
  t = 0;
  bufRandClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_7.setText(bufText);
  // keep track of which components have finished
  bufRandComponents = [];
  bufRandComponents.push(cB_9);
  bufRandComponents.push(text_7);
  
  bufRandComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufRandRoutineEachFrame() {
  //------Loop for each frame of Routine 'bufRand'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufRandClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_9* updates
  if (t >= 0.0 && cB_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_9.tStart = t;  // (not accounting for frame time here)
    cB_9.frameNStart = frameN;  // exact frame index
    cB_9.setAutoDraw(true);
  }

  frameRemains = 0.0 + intTime - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_9.setAutoDraw(false);
  }
  
  // *text_7* updates
  if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_7.tStart = t;  // (not accounting for frame time here)
    text_7.frameNStart = frameN;  // exact frame index
    text_7.setAutoDraw(true);
  }

  frameRemains = 0.0 + intTime - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_7.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufRandComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufRandRoutineEnd() {
  //------Ending Routine 'bufRand'-------
  bufRandComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "bufRand" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function sbFbRoutineBegin() {
  //------Prepare to start Routine 'sbFb'-------
  t = 0;
  sbFbClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.000000);
  // update component parameters for each repeat
  textFb.setText(((textforThis1 + textforThis2) + textforThis3));
  out_Fb.keys = undefined;
  out_Fb.rt = undefined;
  // keep track of which components have finished
  sbFbComponents = [];
  sbFbComponents.push(cbFb);
  sbFbComponents.push(textFb);
  sbFbComponents.push(out_Fb);
  
  sbFbComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbFbRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbFb'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbFbClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cbFb* updates
  if (t >= 0.0 && cbFb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cbFb.tStart = t;  // (not accounting for frame time here)
    cbFb.frameNStart = frameN;  // exact frame index
    cbFb.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cbFb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cbFb.setAutoDraw(false);
  }
  
  // *textFb* updates
  if (t >= 0.0 && textFb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textFb.tStart = t;  // (not accounting for frame time here)
    textFb.frameNStart = frameN;  // exact frame index
    textFb.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textFb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textFb.setAutoDraw(false);
  }
  
  // *out_Fb* updates
  if (t >= 0.0 && out_Fb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_Fb.tStart = t;  // (not accounting for frame time here)
    out_Fb.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_Fb.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_Fb.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_Fb.clearEvents(); });
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (out_Fb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    out_Fb.status = PsychoJS.Status.FINISHED;
  }

  if (out_Fb.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_Fb.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_Fb.keys = theseKeys[0].name;  // just the last key pressed
      out_Fb.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbFbComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbFbRoutineEnd() {
  //------Ending Routine 'sbFb'-------
  sbFbComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('out_Fb.keys', out_Fb.keys);
  if (typeof out_Fb.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_Fb.rt', out_Fb.rt);
      routineTimer.reset();
      }
  
  out_Fb.stop();
  return Scheduler.Event.NEXT;
}

function bufFixRoutineBegin() {
  //------Prepare to start Routine 'bufFix'-------
  t = 0;
  bufFixClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  bufFixComponents = [];
  bufFixComponents.push(cbBuf);
  bufFixComponents.push(text_8);
  
  bufFixComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufFixRoutineEachFrame() {
  //------Loop for each frame of Routine 'bufFix'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufFixClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cbBuf* updates
  if (t >= 0.0 && cbBuf.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cbBuf.tStart = t;  // (not accounting for frame time here)
    cbBuf.frameNStart = frameN;  // exact frame index
    cbBuf.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cbBuf.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cbBuf.setAutoDraw(false);
  }
  
  // *text_8* updates
  if (t >= 0.2 && text_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_8.tStart = t;  // (not accounting for frame time here)
    text_8.frameNStart = frameN;  // exact frame index
    text_8.setAutoDraw(true);
  }

  frameRemains = 0.2 + 0.6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_8.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufFixComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufFixRoutineEnd() {
  //------Ending Routine 'bufFix'-------
  bufFixComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

function sbQuRoutineBegin() {
  //------Prepare to start Routine 'sbQu'-------
  t = 0;
  sbQuClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  sbQuComponents = [];
  sbQuComponents.push(cB_11);
  
  sbQuComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbQuRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbQu'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbQuClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_11* updates
  if (t >= 0.0 && cB_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_11.tStart = t;  // (not accounting for frame time here)
    cB_11.frameNStart = frameN;  // exact frame index
    cB_11.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbQuComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbQuRoutineEnd() {
  //------Ending Routine 'sbQu'-------
  sbQuComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "sbQu" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function sbEndRoutineBegin() {
  //------Prepare to start Routine 'sbEnd'-------
  t = 0;
  sbEndClock.reset(); // clock
  frameN = -1;
  routineTimer.add(30.000000);
  // update component parameters for each repeat
  sbEndText.setText(textEndText);
  sbEndKey.keys = undefined;
  sbEndKey.rt = undefined;
  // keep track of which components have finished
  sbEndComponents = [];
  sbEndComponents.push(cB_10);
  sbEndComponents.push(sbEndText);
  sbEndComponents.push(sbEndKey);
  
  sbEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbEndRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbEnd'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbEndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_10* updates
  if (t >= 0.0 && cB_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_10.tStart = t;  // (not accounting for frame time here)
    cB_10.frameNStart = frameN;  // exact frame index
    cB_10.setAutoDraw(true);
  }

  frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_10.setAutoDraw(false);
  }
  
  // *sbEndText* updates
  if (t >= 0.0 && sbEndText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sbEndText.tStart = t;  // (not accounting for frame time here)
    sbEndText.frameNStart = frameN;  // exact frame index
    sbEndText.setAutoDraw(true);
  }

  frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (sbEndText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    sbEndText.setAutoDraw(false);
  }
  
  // *sbEndKey* updates
  if (t >= 0.0 && sbEndKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sbEndKey.tStart = t;  // (not accounting for frame time here)
    sbEndKey.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { sbEndKey.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { sbEndKey.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { sbEndKey.clearEvents(); });
  }

  frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (sbEndKey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    sbEndKey.status = PsychoJS.Status.FINISHED;
  }

  if (sbEndKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = sbEndKey.getKeys({keyList: [], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      sbEndKey.keys = theseKeys[0].name;  // just the last key pressed
      sbEndKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbEndRoutineEnd() {
  //------Ending Routine 'sbEnd'-------
  sbEndComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('sbEndKey.keys', sbEndKey.keys);
  if (typeof sbEndKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('sbEndKey.rt', sbEndKey.rt);
      routineTimer.reset();
      }
  
  sbEndKey.stop();
  return Scheduler.Event.NEXT;
}

function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}

function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
=======
﻿/***************** 
 * Sobeu_02 Test *
 *****************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'soBeU_02';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(wScrRoutineBegin);
flowScheduler.add(wScrRoutineEachFrame);
flowScheduler.add(wScrRoutineEnd);
flowScheduler.add(wInsRoutineBegin);
flowScheduler.add(wInsRoutineEachFrame);
flowScheduler.add(wInsRoutineEnd);
flowScheduler.add(wIns2RoutineBegin);
flowScheduler.add(wIns2RoutineEachFrame);
flowScheduler.add(wIns2RoutineEnd);
flowScheduler.add(wPflRoutineBegin);
flowScheduler.add(wPflRoutineEachFrame);
flowScheduler.add(wPflRoutineEnd);
flowScheduler.add(wSerRoutineBegin);
flowScheduler.add(wSerRoutineEachFrame);
flowScheduler.add(wSerRoutineEnd);
const bufferLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(bufferLoopLoopBegin, bufferLoopLoopScheduler);
flowScheduler.add(bufferLoopLoopScheduler);
flowScheduler.add(bufferLoopLoopEnd);
flowScheduler.add(bufEndRoutineBegin);
flowScheduler.add(bufEndRoutineEachFrame);
flowScheduler.add(bufEndRoutineEnd);
flowScheduler.add(sbInRoutineBegin);
flowScheduler.add(sbInRoutineEachFrame);
flowScheduler.add(sbInRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(sbEndRoutineBegin);
flowScheduler.add(sbEndRoutineEachFrame);
flowScheduler.add(sbEndRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "wScr"
  wScrClock = new util.Clock();
  textWelcomeText ="""
  Dear Participant, \n
  Welcome to our experiement! \n
  Please carefully go over the instructions on the following pages. \n
  If you have any questions please ask the experimenter for help. \n\n
  Press any key to continue
  """
  textWelcomeText = str(textWelcomeText)
  
  textInstructionsText= """
  You have been randomly assigned to condition B. \n\n
  In the following task you will repeatedly interact with two other players.You will have to make choices on how to engage with the other players.\n
  You will make investments and try to maximize your gains (credits).\n\n
  Following a choice you will receive a short feedback on how the other player has acted.\n
  At the end of all interactions one random interaction will be selected and payed-out the sum of credits gained.\n\n
  see next page for more information.\n
  Press \'c\' to continue.
  """
  
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
  
  Press \'c\' to continue.
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
  Press \'c\' to continue.
  """
  
  textInstructionsSb = """
  You are now ready to start with the experiment. \n
  On the next screens you will make decisions on how to engage with other players.\n\n
  Make a choice using your \'left\' or \'right\' keys and confirm with \'enter\'
  
  Note, all decisions (yours and others) happen simultaneously, and not in response to each other.
  
  Press \'c\' to begin.
  """
  
  textSbText = """ How much do you want to invest?"""
  
  textSbFeed1 = ' has decided to return '
  textSbFeed2 = ' percent of your investment. \n\n'
  textSbFeed3 = 'Your return is '
  textSbFeed4 = ' credits!\n\n'
  textSbFeed5 = 'Your total gain for this round is '
  
  textEndText = """Thank you for participating.
  
  This part of the experiment is now completed.
  """
  
  bufText = """waiting for other player"""
  cB_1 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_1', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyWelcome = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_0 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wIns"
  wInsClock = new util.Clock();
  cB_2 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_2', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstructions',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyInstructions = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_1 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wIns2"
  wIns2Clock = new util.Clock();
  cB_12 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_12', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textInstructions_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstructions_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  keyInstructions_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_3 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wPfl"
  wPflClock = new util.Clock();
  cB = new visual.Rect ({
    win: psychoJS.window, name: 'cB', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  displayText = new visual.TextStim({
    win: psychoJS.window,
    name: 'displayText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  copyText = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  out = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wSer"
  wSerClock = new util.Clock();
  cB_3 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_3', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textServer = new visual.TextStim({
    win: psychoJS.window,
    name: 'textServer',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyServer = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "bufRou_2"
  bufRou_2Clock = new util.Clock();
  cB_4 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_4', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_1',
    text: 'connecting      ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'connecting .    ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'connecting . .  ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'connecting . . .',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "bufEnd"
  bufEndClock = new util.Clock();
  cB_5 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_5', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  idle = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle',
    text: 'found',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  idle_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_2',
    text: 'init proc     ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  idle_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_3',
    text: 'init proc 2141',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  idle_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_4',
    text: 'init proc 2215',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  idle_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_5',
    text: 'init proc 3229',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  idle_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_6',
    text: 'init proc 4325',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  idle_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_7',
    text: 'init proc 1337',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  ilde_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ilde_8',
    text: 'buffering      ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  idle_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_9',
    text: 'buffering .    ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  idle_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_10',
    text: 'buffering . .  ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  idle_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_11',
    text: 'buffering . . .',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  idle_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'idle_12',
    text: 'run /serv/234_1/sd connect',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  // Initialize components for Routine "sbIn"
  sbInClock = new util.Clock();
  cB_6 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_6', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  sBInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'sBInstructions',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keySbInstructions = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  out_sb = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sbRnd"
  sbRndClock = new util.Clock();
  cB_8 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_8', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  imagesbRnd = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagesbRnd', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.2], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "bufRand"
  bufRandClock = new util.Clock();
  cB_9 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_9', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "sbFb"
  sbFbClock = new util.Clock();
  cbFb = new visual.Rect ({
    win: psychoJS.window, name: 'cbFb', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  textFb = new visual.TextStim({
    win: psychoJS.window,
    name: 'textFb',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  out_Fb = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "bufFix"
  bufFixClock = new util.Clock();
  cbBuf = new visual.Rect ({
    win: psychoJS.window, name: 'cbBuf', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.4,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "sbQu"
  sbQuClock = new util.Clock();
  cB_11 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_11', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "bufRand"
  bufRandClock = new util.Clock();
  cB_9 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_9', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "bufFix"
  bufFixClock = new util.Clock();
  cbBuf = new visual.Rect ({
    win: psychoJS.window, name: 'cbBuf', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.4,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "sbEnd"
  sbEndClock = new util.Clock();
  cB_10 = new visual.Rect ({
    win: psychoJS.window, name: 'cB_10', 
    width: [4, 4][0], height: [4, 4][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  sbEndText = new visual.TextStim({
    win: psychoJS.window,
    name: 'sbEndText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  sbEndKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function wScrRoutineBegin() {
  //------Prepare to start Routine 'wScr'-------
  t = 0;
  wScrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textWelcome.setText(textWelcomeText);
  keyWelcome.keys = undefined;
  keyWelcome.rt = undefined;
  out_0.keys = undefined;
  out_0.rt = undefined;
  // keep track of which components have finished
  wScrComponents = [];
  wScrComponents.push(cB_1);
  wScrComponents.push(textWelcome);
  wScrComponents.push(keyWelcome);
  wScrComponents.push(out_0);
  
  wScrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wScrRoutineEachFrame() {
  //------Loop for each frame of Routine 'wScr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wScrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_1* updates
  if (t >= 0.0 && cB_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_1.tStart = t;  // (not accounting for frame time here)
    cB_1.frameNStart = frameN;  // exact frame index
    cB_1.setAutoDraw(true);
  }

  
  // *textWelcome* updates
  if (t >= 0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textWelcome.tStart = t;  // (not accounting for frame time here)
    textWelcome.frameNStart = frameN;  // exact frame index
    textWelcome.setAutoDraw(true);
  }

  
  // *keyWelcome* updates
  if (t >= 2 && keyWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyWelcome.tStart = t;  // (not accounting for frame time here)
    keyWelcome.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyWelcome.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyWelcome.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyWelcome.clearEvents(); });
  }

  if (keyWelcome.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyWelcome.getKeys({keyList: [], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyWelcome.keys = theseKeys[0].name;  // just the last key pressed
      keyWelcome.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_0* updates
  if (t >= 0.0 && out_0.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_0.tStart = t;  // (not accounting for frame time here)
    out_0.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_0.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_0.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_0.clearEvents(); });
  }

  if (out_0.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_0.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_0.keys = theseKeys[0].name;  // just the last key pressed
      out_0.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wScrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wScrRoutineEnd() {
  //------Ending Routine 'wScr'-------
  wScrComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyWelcome.keys', keyWelcome.keys);
  if (typeof keyWelcome.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyWelcome.rt', keyWelcome.rt);
      routineTimer.reset();
      }
  
  keyWelcome.stop();
  psychoJS.experiment.addData('out_0.keys', out_0.keys);
  if (typeof out_0.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_0.rt', out_0.rt);
      routineTimer.reset();
      }
  
  out_0.stop();
  // the Routine "wScr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wInsRoutineBegin() {
  //------Prepare to start Routine 'wIns'-------
  t = 0;
  wInsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textInstructions.setText(textInstructionsText);
  keyInstructions.keys = undefined;
  keyInstructions.rt = undefined;
  out_1.keys = undefined;
  out_1.rt = undefined;
  // keep track of which components have finished
  wInsComponents = [];
  wInsComponents.push(cB_2);
  wInsComponents.push(textInstructions);
  wInsComponents.push(keyInstructions);
  wInsComponents.push(out_1);
  
  wInsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wInsRoutineEachFrame() {
  //------Loop for each frame of Routine 'wIns'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wInsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_2* updates
  if (t >= 0.0 && cB_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_2.tStart = t;  // (not accounting for frame time here)
    cB_2.frameNStart = frameN;  // exact frame index
    cB_2.setAutoDraw(true);
  }

  
  // *textInstructions* updates
  if (t >= 0 && textInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textInstructions.tStart = t;  // (not accounting for frame time here)
    textInstructions.frameNStart = frameN;  // exact frame index
    textInstructions.setAutoDraw(true);
  }

  
  // *keyInstructions* updates
  if (t >= 2 && keyInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyInstructions.tStart = t;  // (not accounting for frame time here)
    keyInstructions.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyInstructions.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions.clearEvents(); });
  }

  if (keyInstructions.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyInstructions.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyInstructions.keys = theseKeys[0].name;  // just the last key pressed
      keyInstructions.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_1* updates
  if (t >= 0.0 && out_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_1.tStart = t;  // (not accounting for frame time here)
    out_1.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_1.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_1.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_1.clearEvents(); });
  }

  if (out_1.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_1.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_1.keys = theseKeys[0].name;  // just the last key pressed
      out_1.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wInsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wInsRoutineEnd() {
  //------Ending Routine 'wIns'-------
  wInsComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyInstructions.keys', keyInstructions.keys);
  if (typeof keyInstructions.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyInstructions.rt', keyInstructions.rt);
      routineTimer.reset();
      }
  
  keyInstructions.stop();
  psychoJS.experiment.addData('out_1.keys', out_1.keys);
  if (typeof out_1.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_1.rt', out_1.rt);
      routineTimer.reset();
      }
  
  out_1.stop();
  // the Routine "wIns" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wIns2RoutineBegin() {
  //------Prepare to start Routine 'wIns2'-------
  t = 0;
  wIns2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textInstructions_2.setText(textInstructionsText2);
  keyInstructions_2.keys = undefined;
  keyInstructions_2.rt = undefined;
  out_3.keys = undefined;
  out_3.rt = undefined;
  // keep track of which components have finished
  wIns2Components = [];
  wIns2Components.push(cB_12);
  wIns2Components.push(textInstructions_2);
  wIns2Components.push(keyInstructions_2);
  wIns2Components.push(out_3);
  
  wIns2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wIns2RoutineEachFrame() {
  //------Loop for each frame of Routine 'wIns2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wIns2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_12* updates
  if (t >= 0.0 && cB_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_12.tStart = t;  // (not accounting for frame time here)
    cB_12.frameNStart = frameN;  // exact frame index
    cB_12.setAutoDraw(true);
  }

  
  // *textInstructions_2* updates
  if (t >= 0 && textInstructions_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textInstructions_2.tStart = t;  // (not accounting for frame time here)
    textInstructions_2.frameNStart = frameN;  // exact frame index
    textInstructions_2.setAutoDraw(true);
  }

  
  // *keyInstructions_2* updates
  if (t >= 2 && keyInstructions_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyInstructions_2.tStart = t;  // (not accounting for frame time here)
    keyInstructions_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyInstructions_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyInstructions_2.clearEvents(); });
  }

  if (keyInstructions_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyInstructions_2.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyInstructions_2.keys = theseKeys[0].name;  // just the last key pressed
      keyInstructions_2.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_3* updates
  if (t >= 0.0 && out_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_3.tStart = t;  // (not accounting for frame time here)
    out_3.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_3.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_3.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_3.clearEvents(); });
  }

  if (out_3.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_3.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_3.keys = theseKeys[0].name;  // just the last key pressed
      out_3.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wIns2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wIns2RoutineEnd() {
  //------Ending Routine 'wIns2'-------
  wIns2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyInstructions_2.keys', keyInstructions_2.keys);
  if (typeof keyInstructions_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyInstructions_2.rt', keyInstructions_2.rt);
      routineTimer.reset();
      }
  
  keyInstructions_2.stop();
  psychoJS.experiment.addData('out_3.keys', out_3.keys);
  if (typeof out_3.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_3.rt', out_3.rt);
      routineTimer.reset();
      }
  
  out_3.stop();
  // the Routine "wIns2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wPflRoutineBegin() {
  //------Prepare to start Routine 'wPfl'-------
  t = 0;
  wPflClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  modify = false;
  text.text = '';
  displayText.setText(textProfileText);
  copyText.setText('');
  out.keys = undefined;
  out.rt = undefined;
  // keep track of which components have finished
  wPflComponents = [];
  wPflComponents.push(cB);
  wPflComponents.push(displayText);
  wPflComponents.push(copyText);
  wPflComponents.push(out);
  
  wPflComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wPflRoutineEachFrame() {
  //------Loop for each frame of Routine 'wPfl'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wPflClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB* updates
  if (t >= 0.0 && cB.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB.tStart = t;  // (not accounting for frame time here)
    cB.frameNStart = frameN;  // exact frame index
    cB.setAutoDraw(true);
  }

  let theseKeys = psychoJS.eventManager.getKeys();
  if (theseKeys.length > 0) {  // at least one key was pressed
    textAdd = theseKeys[theseKeys.length-1]; 
    }
  
  
  if (textAdd === 'return') {
      textAdd = '';  // Add nothing
      continueRoutine = false;  // End routine (if that is what you want)
  } else if (textAdd === 'space') {
      textAdd = ' ';  // Add a space
  } else if (textAdd === 'backspace') {
      text.text = text.text.slice(0, -1);
      textAdd = undefined;
  } else if (['lshift', 'rshift'].includes(textAdd)) {
      modify = true;
  } else if (textAdd !== undefined) {
      if (modify) {
          text.text = text.text + textAdd.toUpperCase();
          modify = false;
      } else {
          text.text = text.text + textAdd
      }
      textAdd = undefined;
  }
  
  // *displayText* updates
  if (t >= 0.0 && displayText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    displayText.tStart = t;  // (not accounting for frame time here)
    displayText.frameNStart = frameN;  // exact frame index
    displayText.setAutoDraw(true);
  }

  
  // *copyText* updates
  if (t >= 0.0 && copyText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    copyText.tStart = t;  // (not accounting for frame time here)
    copyText.frameNStart = frameN;  // exact frame index
    copyText.setAutoDraw(true);
  }

  
  // *out* updates
  if (t >= 0.0 && out.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out.tStart = t;  // (not accounting for frame time here)
    out.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out.clearEvents(); });
  }

  if (out.status === PsychoJS.Status.STARTED) {
    let theseKeys = out.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out.keys = theseKeys[0].name;  // just the last key pressed
      out.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wPflComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wPflRoutineEnd() {
  //------Ending Routine 'wPfl'-------
  wPflComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData("typedWord", text.text)
  text.setText('')  // empty the onscreen text ready for next input
  psychoJS.experiment.addData('out.keys', out.keys);
  if (typeof out.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out.rt', out.rt);
      routineTimer.reset();
      }
  
  out.stop();
  // the Routine "wPfl" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function wSerRoutineBegin() {
  //------Prepare to start Routine 'wSer'-------
  t = 0;
  wSerClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textServer.setText(textServerText);
  keyServer.keys = undefined;
  keyServer.rt = undefined;
  out_2.keys = undefined;
  out_2.rt = undefined;
  // keep track of which components have finished
  wSerComponents = [];
  wSerComponents.push(cB_3);
  wSerComponents.push(textServer);
  wSerComponents.push(keyServer);
  wSerComponents.push(out_2);
  
  wSerComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function wSerRoutineEachFrame() {
  //------Loop for each frame of Routine 'wSer'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = wSerClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_3* updates
  if (t >= 0.0 && cB_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_3.tStart = t;  // (not accounting for frame time here)
    cB_3.frameNStart = frameN;  // exact frame index
    cB_3.setAutoDraw(true);
  }

  
  // *textServer* updates
  if (t >= 0 && textServer.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textServer.tStart = t;  // (not accounting for frame time here)
    textServer.frameNStart = frameN;  // exact frame index
    textServer.setAutoDraw(true);
  }

  
  // *keyServer* updates
  if (t >= 2 && keyServer.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyServer.tStart = t;  // (not accounting for frame time here)
    keyServer.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyServer.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyServer.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyServer.clearEvents(); });
  }

  if (keyServer.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyServer.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyServer.keys = theseKeys[0].name;  // just the last key pressed
      keyServer.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_2* updates
  if (t >= 0.0 && out_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_2.tStart = t;  // (not accounting for frame time here)
    out_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_2.clearEvents(); });
  }

  if (out_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_2.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_2.keys = theseKeys[0].name;  // just the last key pressed
      out_2.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  wSerComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function wSerRoutineEnd() {
  //------Ending Routine 'wSer'-------
  wSerComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keyServer.keys', keyServer.keys);
  if (typeof keyServer.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyServer.rt', keyServer.rt);
      routineTimer.reset();
      }
  
  keyServer.stop();
  psychoJS.experiment.addData('out_2.keys', out_2.keys);
  if (typeof out_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_2.rt', out_2.rt);
      routineTimer.reset();
      }
  
  out_2.stop();
  // the Routine "wSer" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function bufferLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  bufferLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'bufferLoop'});
  psychoJS.experiment.addLoop(bufferLoop); // add the loop to the experiment
  currentLoop = bufferLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = bufferLoop[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisBufferLoop = result.value;
    thisScheduler.add(importConditions(bufferLoop));
    thisScheduler.add(bufRou_2RoutineBegin);
    thisScheduler.add(bufRou_2RoutineEachFrame);
    thisScheduler.add(bufRou_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function bufferLoopLoopEnd() {
  psychoJS.experiment.removeLoop(bufferLoop);

  return Scheduler.Event.NEXT;
}

function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'contitions.xlsx', '1:20'),
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    const sbLoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(sbLoopLoopBegin, sbLoopLoopScheduler);
    thisScheduler.add(sbLoopLoopScheduler);
    thisScheduler.add(sbLoopLoopEnd);
    const sliders_1LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(sliders_1LoopBegin, sliders_1LoopScheduler);
    thisScheduler.add(sliders_1LoopScheduler);
    thisScheduler.add(sliders_1LoopEnd);
    const trials_2LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
    thisScheduler.add(trials_2LoopScheduler);
    thisScheduler.add(trials_2LoopEnd);
    thisScheduler.add(bufFixRoutineBegin);
    thisScheduler.add(bufFixRoutineEachFrame);
    thisScheduler.add(bufFixRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function sbLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  sbLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'contitions.xlsx', '1:20'),
    seed: undefined, name: 'sbLoop'});
  psychoJS.experiment.addLoop(sbLoop); // add the loop to the experiment
  currentLoop = sbLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = sbLoop[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisSbLoop = result.value;
    thisScheduler.add(importConditions(sbLoop));
    thisScheduler.add(sbRndRoutineBegin);
    thisScheduler.add(sbRndRoutineEachFrame);
    thisScheduler.add(sbRndRoutineEnd);
    thisScheduler.add(bufRandRoutineBegin);
    thisScheduler.add(bufRandRoutineEachFrame);
    thisScheduler.add(bufRandRoutineEnd);
    thisScheduler.add(sbFbRoutineBegin);
    thisScheduler.add(sbFbRoutineEachFrame);
    thisScheduler.add(sbFbRoutineEnd);
    thisScheduler.add(bufFixRoutineBegin);
    thisScheduler.add(bufFixRoutineEachFrame);
    thisScheduler.add(bufFixRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function sbLoopLoopEnd() {
  psychoJS.experiment.removeLoop(sbLoop);

  return Scheduler.Event.NEXT;
}

function sliders_1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  sliders_1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'sliders.xlsx',
    seed: undefined, name: 'sliders_1'});
  psychoJS.experiment.addLoop(sliders_1); // add the loop to the experiment
  currentLoop = sliders_1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = sliders_1[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisSlider_1 = result.value;
    thisScheduler.add(importConditions(sliders_1));
    thisScheduler.add(sbQuRoutineBegin);
    thisScheduler.add(sbQuRoutineEachFrame);
    thisScheduler.add(sbQuRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function sliders_1LoopEnd() {
  psychoJS.experiment.removeLoop(sliders_1);

  return Scheduler.Event.NEXT;
}

function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_2'});
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_2[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_2 = result.value;
    thisScheduler.add(importConditions(trials_2));
    thisScheduler.add(bufRandRoutineBegin);
    thisScheduler.add(bufRandRoutineEachFrame);
    thisScheduler.add(bufRandRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

function bufRou_2RoutineBegin() {
  //------Prepare to start Routine 'bufRou_2'-------
  t = 0;
  bufRou_2Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  bufRou_2Components = [];
  bufRou_2Components.push(cB_4);
  bufRou_2Components.push(text_1);
  bufRou_2Components.push(text_2);
  bufRou_2Components.push(text_3);
  bufRou_2Components.push(text_4);
  
  bufRou_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufRou_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'bufRou_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufRou_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_4* updates
  if (t >= 0.0 && cB_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_4.tStart = t;  // (not accounting for frame time here)
    cB_4.frameNStart = frameN;  // exact frame index
    cB_4.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_4.setAutoDraw(false);
  }
  
  // *text_1* updates
  if (t >= 0.0 && text_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_1.tStart = t;  // (not accounting for frame time here)
    text_1.frameNStart = frameN;  // exact frame index
    text_1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_1.setAutoDraw(false);
  }
  
  // *text_2* updates
  if (t >= 1 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_2.setAutoDraw(false);
  }
  
  // *text_3* updates
  if (t >= 1.5 && text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_3.tStart = t;  // (not accounting for frame time here)
    text_3.frameNStart = frameN;  // exact frame index
    text_3.setAutoDraw(true);
  }

  frameRemains = 1.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_3.setAutoDraw(false);
  }
  
  // *text_4* updates
  if (t >= 2 && text_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_4.tStart = t;  // (not accounting for frame time here)
    text_4.frameNStart = frameN;  // exact frame index
    text_4.setAutoDraw(true);
  }

  frameRemains = 2 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_4.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufRou_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufRou_2RoutineEnd() {
  //------Ending Routine 'bufRou_2'-------
  bufRou_2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

function bufEndRoutineBegin() {
  //------Prepare to start Routine 'bufEnd'-------
  t = 0;
  bufEndClock.reset(); // clock
  frameN = -1;
  routineTimer.add(4.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  bufEndComponents = [];
  bufEndComponents.push(cB_5);
  bufEndComponents.push(idle);
  bufEndComponents.push(idle_2);
  bufEndComponents.push(idle_3);
  bufEndComponents.push(idle_4);
  bufEndComponents.push(idle_5);
  bufEndComponents.push(idle_6);
  bufEndComponents.push(idle_7);
  bufEndComponents.push(ilde_8);
  bufEndComponents.push(idle_9);
  bufEndComponents.push(idle_10);
  bufEndComponents.push(idle_11);
  bufEndComponents.push(idle_12);
  
  bufEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufEndRoutineEachFrame() {
  //------Loop for each frame of Routine 'bufEnd'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufEndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_5* updates
  if (t >= 0.0 && cB_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_5.tStart = t;  // (not accounting for frame time here)
    cB_5.frameNStart = frameN;  // exact frame index
    cB_5.setAutoDraw(true);
  }

  frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_5.setAutoDraw(false);
  }
  
  // *idle* updates
  if (t >= 0.2 && idle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle.tStart = t;  // (not accounting for frame time here)
    idle.frameNStart = frameN;  // exact frame index
    idle.setAutoDraw(true);
  }

  frameRemains = 0.5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle.setAutoDraw(false);
  }
  
  // *idle_2* updates
  if (t >= 0.5 && idle_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_2.tStart = t;  // (not accounting for frame time here)
    idle_2.frameNStart = frameN;  // exact frame index
    idle_2.setAutoDraw(true);
  }

  frameRemains = 0.7  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_2.setAutoDraw(false);
  }
  
  // *idle_3* updates
  if (t >= 0.7 && idle_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_3.tStart = t;  // (not accounting for frame time here)
    idle_3.frameNStart = frameN;  // exact frame index
    idle_3.setAutoDraw(true);
  }

  frameRemains = 0.8  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_3.setAutoDraw(false);
  }
  
  // *idle_4* updates
  if (t >= 0.8 && idle_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_4.tStart = t;  // (not accounting for frame time here)
    idle_4.frameNStart = frameN;  // exact frame index
    idle_4.setAutoDraw(true);
  }

  frameRemains = 0.95  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_4.setAutoDraw(false);
  }
  
  // *idle_5* updates
  if (t >= 0.95 && idle_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_5.tStart = t;  // (not accounting for frame time here)
    idle_5.frameNStart = frameN;  // exact frame index
    idle_5.setAutoDraw(true);
  }

  frameRemains = 1.1  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_5.setAutoDraw(false);
  }
  
  // *idle_6* updates
  if (t >= 1.1 && idle_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_6.tStart = t;  // (not accounting for frame time here)
    idle_6.frameNStart = frameN;  // exact frame index
    idle_6.setAutoDraw(true);
  }

  frameRemains = 1.25  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_6.setAutoDraw(false);
  }
  
  // *idle_7* updates
  if (t >= 1.25 && idle_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_7.tStart = t;  // (not accounting for frame time here)
    idle_7.frameNStart = frameN;  // exact frame index
    idle_7.setAutoDraw(true);
  }

  frameRemains = 1.35  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_7.setAutoDraw(false);
  }
  
  // *ilde_8* updates
  if (t >= 1.35 && ilde_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ilde_8.tStart = t;  // (not accounting for frame time here)
    ilde_8.frameNStart = frameN;  // exact frame index
    ilde_8.setAutoDraw(true);
  }

  frameRemains = 1.85  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (ilde_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    ilde_8.setAutoDraw(false);
  }
  
  // *idle_9* updates
  if (t >= 1.85 && idle_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_9.tStart = t;  // (not accounting for frame time here)
    idle_9.frameNStart = frameN;  // exact frame index
    idle_9.setAutoDraw(true);
  }

  frameRemains = 1.85 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_9.setAutoDraw(false);
  }
  
  // *idle_10* updates
  if (t >= 2.35 && idle_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_10.tStart = t;  // (not accounting for frame time here)
    idle_10.frameNStart = frameN;  // exact frame index
    idle_10.setAutoDraw(true);
  }

  frameRemains = 2.35 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_10.setAutoDraw(false);
  }
  
  // *idle_11* updates
  if (t >= 2.85 && idle_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_11.tStart = t;  // (not accounting for frame time here)
    idle_11.frameNStart = frameN;  // exact frame index
    idle_11.setAutoDraw(true);
  }

  frameRemains = 2.85 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_11.setAutoDraw(false);
  }
  
  // *idle_12* updates
  if (t >= 3.35 && idle_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    idle_12.tStart = t;  // (not accounting for frame time here)
    idle_12.frameNStart = frameN;  // exact frame index
    idle_12.setAutoDraw(true);
  }

  frameRemains = 3.5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (idle_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    idle_12.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufEndRoutineEnd() {
  //------Ending Routine 'bufEnd'-------
  bufEndComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

function sbInRoutineBegin() {
  //------Prepare to start Routine 'sbIn'-------
  t = 0;
  sbInClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  sBInstructions.setText(textInstructionsSb2);
  keySbInstructions.keys = undefined;
  keySbInstructions.rt = undefined;
  out_sb.keys = undefined;
  out_sb.rt = undefined;
  // keep track of which components have finished
  sbInComponents = [];
  sbInComponents.push(cB_6);
  sbInComponents.push(sBInstructions);
  sbInComponents.push(keySbInstructions);
  sbInComponents.push(out_sb);
  
  sbInComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbInRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbIn'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbInClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_6* updates
  if (t >= 0.0 && cB_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_6.tStart = t;  // (not accounting for frame time here)
    cB_6.frameNStart = frameN;  // exact frame index
    cB_6.setAutoDraw(true);
  }

  
  // *sBInstructions* updates
  if (t >= 0.2 && sBInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sBInstructions.tStart = t;  // (not accounting for frame time here)
    sBInstructions.frameNStart = frameN;  // exact frame index
    sBInstructions.setAutoDraw(true);
  }

  
  // *keySbInstructions* updates
  if (t >= 2 && keySbInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keySbInstructions.tStart = t;  // (not accounting for frame time here)
    keySbInstructions.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keySbInstructions.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keySbInstructions.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keySbInstructions.clearEvents(); });
  }

  if (keySbInstructions.status === PsychoJS.Status.STARTED) {
    let theseKeys = keySbInstructions.getKeys({keyList: ['c'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keySbInstructions.keys = theseKeys[0].name;  // just the last key pressed
      keySbInstructions.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *out_sb* updates
  if (t >= 0.0 && out_sb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_sb.tStart = t;  // (not accounting for frame time here)
    out_sb.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_sb.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_sb.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_sb.clearEvents(); });
  }

  if (out_sb.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_sb.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_sb.keys = theseKeys[0].name;  // just the last key pressed
      out_sb.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbInComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbInRoutineEnd() {
  //------Ending Routine 'sbIn'-------
  sbInComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('keySbInstructions.keys', keySbInstructions.keys);
  if (typeof keySbInstructions.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keySbInstructions.rt', keySbInstructions.rt);
      routineTimer.reset();
      }
  
  keySbInstructions.stop();
  psychoJS.experiment.addData('out_sb.keys', out_sb.keys);
  if (typeof out_sb.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_sb.rt', out_sb.rt);
      routineTimer.reset();
      }
  
  out_sb.stop();
  // the Routine "sbIn" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function sbRndRoutineBegin() {
  //------Prepare to start Routine 'sbRnd'-------
  t = 0;
  sbRndClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text.setText((('This round you are playing with ' + playerId) + '!'));
  imagesbRnd.setImage(avatarFile);
  text_6.setText(textSbText);
  // keep track of which components have finished
  sbRndComponents = [];
  sbRndComponents.push(cB_8);
  sbRndComponents.push(text);
  sbRndComponents.push(imagesbRnd);
  sbRndComponents.push(text_6);
  
  sbRndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbRndRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbRnd'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbRndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_8* updates
  if (t >= 0.0 && cB_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_8.tStart = t;  // (not accounting for frame time here)
    cB_8.frameNStart = frameN;  // exact frame index
    cB_8.setAutoDraw(true);
  }

  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *imagesbRnd* updates
  if (t >= 0.0 && imagesbRnd.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    imagesbRnd.tStart = t;  // (not accounting for frame time here)
    imagesbRnd.frameNStart = frameN;  // exact frame index
    imagesbRnd.setAutoDraw(true);
  }

  
  // *text_6* updates
  if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_6.tStart = t;  // (not accounting for frame time here)
    text_6.frameNStart = frameN;  // exact frame index
    text_6.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbRndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbRndRoutineEnd() {
  //------Ending Routine 'sbRnd'-------
  sbRndComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "sbRnd" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function bufRandRoutineBegin() {
  //------Prepare to start Routine 'bufRand'-------
  t = 0;
  bufRandClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_7.setText(bufText);
  // keep track of which components have finished
  bufRandComponents = [];
  bufRandComponents.push(cB_9);
  bufRandComponents.push(text_7);
  
  bufRandComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufRandRoutineEachFrame() {
  //------Loop for each frame of Routine 'bufRand'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufRandClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_9* updates
  if (t >= 0.0 && cB_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_9.tStart = t;  // (not accounting for frame time here)
    cB_9.frameNStart = frameN;  // exact frame index
    cB_9.setAutoDraw(true);
  }

  frameRemains = 0.0 + intTime - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_9.setAutoDraw(false);
  }
  
  // *text_7* updates
  if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_7.tStart = t;  // (not accounting for frame time here)
    text_7.frameNStart = frameN;  // exact frame index
    text_7.setAutoDraw(true);
  }

  frameRemains = 0.0 + intTime - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_7.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufRandComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufRandRoutineEnd() {
  //------Ending Routine 'bufRand'-------
  bufRandComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "bufRand" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function sbFbRoutineBegin() {
  //------Prepare to start Routine 'sbFb'-------
  t = 0;
  sbFbClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.000000);
  // update component parameters for each repeat
  textFb.setText(((textforThis1 + textforThis2) + textforThis3));
  out_Fb.keys = undefined;
  out_Fb.rt = undefined;
  // keep track of which components have finished
  sbFbComponents = [];
  sbFbComponents.push(cbFb);
  sbFbComponents.push(textFb);
  sbFbComponents.push(out_Fb);
  
  sbFbComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbFbRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbFb'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbFbClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cbFb* updates
  if (t >= 0.0 && cbFb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cbFb.tStart = t;  // (not accounting for frame time here)
    cbFb.frameNStart = frameN;  // exact frame index
    cbFb.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cbFb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cbFb.setAutoDraw(false);
  }
  
  // *textFb* updates
  if (t >= 0.0 && textFb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textFb.tStart = t;  // (not accounting for frame time here)
    textFb.frameNStart = frameN;  // exact frame index
    textFb.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textFb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textFb.setAutoDraw(false);
  }
  
  // *out_Fb* updates
  if (t >= 0.0 && out_Fb.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    out_Fb.tStart = t;  // (not accounting for frame time here)
    out_Fb.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { out_Fb.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { out_Fb.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { out_Fb.clearEvents(); });
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (out_Fb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    out_Fb.status = PsychoJS.Status.FINISHED;
  }

  if (out_Fb.status === PsychoJS.Status.STARTED) {
    let theseKeys = out_Fb.getKeys({keyList: ['1'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      out_Fb.keys = theseKeys[0].name;  // just the last key pressed
      out_Fb.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbFbComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbFbRoutineEnd() {
  //------Ending Routine 'sbFb'-------
  sbFbComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('out_Fb.keys', out_Fb.keys);
  if (typeof out_Fb.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('out_Fb.rt', out_Fb.rt);
      routineTimer.reset();
      }
  
  out_Fb.stop();
  return Scheduler.Event.NEXT;
}

function bufFixRoutineBegin() {
  //------Prepare to start Routine 'bufFix'-------
  t = 0;
  bufFixClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  bufFixComponents = [];
  bufFixComponents.push(cbBuf);
  bufFixComponents.push(text_8);
  
  bufFixComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function bufFixRoutineEachFrame() {
  //------Loop for each frame of Routine 'bufFix'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = bufFixClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cbBuf* updates
  if (t >= 0.0 && cbBuf.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cbBuf.tStart = t;  // (not accounting for frame time here)
    cbBuf.frameNStart = frameN;  // exact frame index
    cbBuf.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cbBuf.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cbBuf.setAutoDraw(false);
  }
  
  // *text_8* updates
  if (t >= 0.2 && text_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_8.tStart = t;  // (not accounting for frame time here)
    text_8.frameNStart = frameN;  // exact frame index
    text_8.setAutoDraw(true);
  }

  frameRemains = 0.2 + 0.6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_8.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  bufFixComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function bufFixRoutineEnd() {
  //------Ending Routine 'bufFix'-------
  bufFixComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

function sbQuRoutineBegin() {
  //------Prepare to start Routine 'sbQu'-------
  t = 0;
  sbQuClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  sbQuComponents = [];
  sbQuComponents.push(cB_11);
  
  sbQuComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbQuRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbQu'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbQuClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_11* updates
  if (t >= 0.0 && cB_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_11.tStart = t;  // (not accounting for frame time here)
    cB_11.frameNStart = frameN;  // exact frame index
    cB_11.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbQuComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbQuRoutineEnd() {
  //------Ending Routine 'sbQu'-------
  sbQuComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "sbQu" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function sbEndRoutineBegin() {
  //------Prepare to start Routine 'sbEnd'-------
  t = 0;
  sbEndClock.reset(); // clock
  frameN = -1;
  routineTimer.add(30.000000);
  // update component parameters for each repeat
  sbEndText.setText(textEndText);
  sbEndKey.keys = undefined;
  sbEndKey.rt = undefined;
  // keep track of which components have finished
  sbEndComponents = [];
  sbEndComponents.push(cB_10);
  sbEndComponents.push(sbEndText);
  sbEndComponents.push(sbEndKey);
  
  sbEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

function sbEndRoutineEachFrame() {
  //------Loop for each frame of Routine 'sbEnd'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sbEndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cB_10* updates
  if (t >= 0.0 && cB_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cB_10.tStart = t;  // (not accounting for frame time here)
    cB_10.frameNStart = frameN;  // exact frame index
    cB_10.setAutoDraw(true);
  }

  frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cB_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cB_10.setAutoDraw(false);
  }
  
  // *sbEndText* updates
  if (t >= 0.0 && sbEndText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sbEndText.tStart = t;  // (not accounting for frame time here)
    sbEndText.frameNStart = frameN;  // exact frame index
    sbEndText.setAutoDraw(true);
  }

  frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (sbEndText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    sbEndText.setAutoDraw(false);
  }
  
  // *sbEndKey* updates
  if (t >= 0.0 && sbEndKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sbEndKey.tStart = t;  // (not accounting for frame time here)
    sbEndKey.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { sbEndKey.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { sbEndKey.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { sbEndKey.clearEvents(); });
  }

  frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (sbEndKey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    sbEndKey.status = PsychoJS.Status.FINISHED;
  }

  if (sbEndKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = sbEndKey.getKeys({keyList: [], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      sbEndKey.keys = theseKeys[0].name;  // just the last key pressed
      sbEndKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sbEndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function sbEndRoutineEnd() {
  //------Ending Routine 'sbEnd'-------
  sbEndComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('sbEndKey.keys', sbEndKey.keys);
  if (typeof sbEndKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('sbEndKey.rt', sbEndKey.rt);
      routineTimer.reset();
      }
  
  sbEndKey.stop();
  return Scheduler.Event.NEXT;
}

function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}

function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
>>>>>>> a2640077243630c143a5bec044958bb8c7a841b2
