TRAIN_GT_ANN = {
        "button-press-v2": "Press the button from side",
        "button-press-topdown-wall-v2": "Press the button from top",
        "coffee-pull-v2": "Pull the coffee cup",
        "dial-turn-v2": "Turn the dial",
        "door-open-v2": "Open the door",
        "door-unlock-v2": "Turn door lock clockwise",
        "drawer-close-v2": "Close the drawer",
        "faucet-open-v2": "Open the faucet",
        "handle-press-v2": "Press the handle",
        "handle-pull-side-v2": "Pull the handle up from the side",
        "peg-insert-side-v2": "Insert the peg from the side",
        "pick-place-v2": "Pick up the block and placing it to the goal position",
        "plate-slide-v2": "Slide the plate into the gate",
        "plate-slide-back-side-v2": "Slide the plate out of the gate from the side",
        "push-v2": "Push the block to the goal",
        "reach-v2": "Reach the goal",
        "stick-push-v2": "Push the stick",
        "stick-pull-v2": "Pull the stick",
        "window-open-v2": "Open the window",
        "hand-insert-v2": "Pick up the block and insert it into the hole",
}

EVAL_GT_ANN = {
        "button-press-wall-v2": "Press the button from side",
        "button-press-topdown-v2": "Press the button from top",
        "coffee-push-v2": "Push the coffee cup",
        "coffee-button-v2": "Press the coffee button",
        "door-close-v2": "Close the door",
        "door-lock-v2": "Turn door lock counter-clockwise",
        "faucet-close-v2": "Close the faucet",
        "handle-press-side-v2": "Press the handle from side",
        "handle-pull-v2": "Pull the handle",
        "pick-place-wall-v2": "Pick up the block and place it to the goal position",
        "plate-slide-back-v2": "Slide the plate out of the gate",
        "plate-slide-side-v2": "Slide the plate into the gate from the side",
        "push-back-v2": "Push the block back to the goal",
        "reach-wall-v2": "Reach the goal",
        "soccer-v2": "Slide the ball into the gate",
        "window-close-v2": "Close the window",
        "sweep-into-v2": "Sweep the block into the hole",
}

GENERATE_TRAIN_ANN = {
    "button-press-v2":[
        "Pressing the button from the side",
        "Pressing the red button",
        "Pressing the button on the yellow box",
        "Pushing the button inside"
    ],
    "button-press-topdown-wall-v2":[
        "Press the button from top",
        "Press the red button",
        "Press the red button on the yellow box",
        "Push the button downward",
    ],
    "coffee-pull-v2":[
        "Pull the coffee cup from the coffee machine",
        "Extract the coffee cup",
        "Remove the coffee cup from the coffee machine",
        "Drag the coffee cup",
    ],
    "dial-turn-v2":[
        "Turn the dial counterclockwise",
        "Rotate the dial to the left",
        "Twist the dial",
        "Adjust the dial counterclockwise"
    ],
    "door-open-v2":[
        "Rotate the door counterclockwise",
        "Swing the door open",
        "Draw the door open",
        "Draw the door counterclockwise"
    ],
    "door-unlock-v2":[
        "Turn door lock clockwise",
        "Rotate the door lock",
        "Twist the door lock",
        "Adjust the door lock"
    ],
    "drawer-close-v2":[
        "Push the drawer closed",
        "Shut the drawer",
        "Slide the drawer shut",
        "Close the green drawer"
    ],
    "faucet-open-v2":[
        "Rotate the faucet clockwise",
        "Twist the faucet in a clockwise direction",
        "Turn the faucet handle to the left",
        "Adjust the faucet clockwise"
    ],
    "handle-press-v2":[
        "Press the handle downward",
        "Depress the handle",
        "Lower the handle",
        "Apply downward pressure on the handle"
        ],
    "handle-pull-side-v2":[
        "Pull the handle upward",
        "Lift the handle",
        "Raise the handle",
        "Apply upward force to the handle"
    ],
    "peg-insert-side-v2":[
        "Push the peg into the hole from the side",
        "Move the peg into the box",
        "Insert the peg into the hole",
        "Guide the peg into the hole"
    ],
    "pick-place-v2":[
        "Lift the block to the goal position",
        "Pick up the block and setting it at the goal position",
        "Grab the block and positioning it at the goal",
        "Move the box to the goal position"
    ],
    "plate-slide-v2":[
        "Push the plate into the gate",
        "Slide the plate into the gate",
        "Move the plate into the gate",
        "Shift the plate into the gate"
    ],
    "plate-slide-back-side-v2":[
        "Pull the plate out of the gate",
        "Slide the plate out of the gate",
        "Move the plate out of the gate",
        "Shift the plate out of the gate"
    ],
    "push-v2":[
        "Move the block to the goal",
        "Slide the block toward the goal",
        "Propel the block to the goal",
        "Drive the block toward the goal"
    ],
    "reach-v2":[
        "Extend to the goal",
        "Stretch toward the goal",
        "Move to the goal",
        "Direct toward the goal"
    ],
    "stick-push-v2":[
        "Move the stick",
        "Slide the stick",
        "Shift the stick",
        "Propel the stick"
    ],
    "stick-pull-v2":[
        "Pull the stick",
        "Extract the stick",
        "Move the stick to the bottle",
        "Drag the stick"
    ],
    "window-open-v2":[
        "Pull the window open",
        "Slide the window open",
        "Move the window open",
        "Shift the window open"
    ],
    "hand-insert-v2":[
        "Move up the block and put it into the hole",
        "Insert the block into the hole",
        "Place the block into the hole",
        "Guide the block into the hole"
    ]
}

EVAL_ANN_1 = {
   "button-press-wall-v2": "Press the button near the wall",
   "button-press-topdown-v2": "Press the button down from above",
   "coffee-push-v2": "Slide the coffee cup forward",
   "coffee-button-v2": "Press the coffee button to activate",
   "door-close-v2": "Shut the door",
   "door-lock-v2": "Turn the door lock to the left",
   "faucet-close-v2": "Turn the faucet off",
   "handle-press-side-v2": "Press the handle down from side",
   "handle-pull-v2": "Pull the handle up",
   "pick-place-wall-v2": "Pick up the block and set it in the target spot bypassing the wall",
   "plate-slide-back-v2": "Pull the plate backward from the gate",
   "plate-slide-side-v2": "Guid the plate into the gate from the side",
   "push-back-v2": "Push the block backward into place",
   "reach-wall-v2": "Get to the goal position",
   "soccer-v2": "Put the ball into the goal",
   "window-close-v2": "Slide the window to close",
   "sweep-into-v2": "Sweep the item into the hole",
}

EVAL_ANN_2 = {
   "button-press-wall-v2": "Press the button behind the wall",
   "button-press-topdown-v2": "Press the button downward",
   "coffee-push-v2": "Move the coffee cup forward",
   "coffee-button-v2": "Activate the coffee button by pressing",
   "door-close-v2": "Bring the door to close",
   "door-lock-v2": "Rotate the door lock counter-clockwise",
   "faucet-close-v2": "Shut off the faucet",
   "handle-press-side-v2": "Engage the handle with a press",
   "handle-pull-v2": "Activate the handle by pulling",
   "pick-place-wall-v2": "Lift the block and depositing it at the goal location over the wall",
   "plate-slide-back-v2": "Slide the plate away from the gate",
   "plate-slide-side-v2": "Slide the plate into the gate from a sideways approach",
   "push-back-v2": "Take the block back to goal place",
   "reach-wall-v2": "Move towards the goal position",
   "soccer-v2": "Direct the ball into the gate",
   "window-close-v2": "Move the window to closed position",
   "sweep-into-v2": "Shovel the block into the opening",
}

EVAL_ANN_3 = {
   "button-press-wall-v2": "Press the side-mounted button on the wall",
   "button-press-topdown-v2": "Press the button firmly from above",
   "coffee-push-v2": "Push the coffee cup along the table",
   "coffee-button-v2": "Press the coffee maker's button to start",
   "door-close-v2": "Close the door until it latches",
   "door-lock-v2": "Turn the door lock left to secure",
   "faucet-close-v2": "Rotate the faucet off to stop the flow",
   "handle-press-side-v2": "Press the handle from a side angle",
   "handle-pull-v2": "Pull the handle outward to engage",
   "pick-place-wall-v2": "Pick up the block and placing it over the wall at the goal",
   "plate-slide-back-v2": "Move the plate backward from the gate",
   "plate-slide-side-v2": "Move the plate sideways into the gate",
   "push-back-v2": "Push the block back to its final position",
   "reach-wall-v2": "Reach the designated location near the wall",
   "soccer-v2": "Slide the ball into the goal area",
   "window-close-v2": "Draw the window shut",
   "sweep-into-v2": "Sweep the block into the hole",
}



