Powering Off a Board
====================

When a board fails or needs maintenance or a hardware upgrade, you need to power off the board. Then, you can remove the board.

#### Usage Scenario

Determine the board to be powered off according to the actual situation.

In VS mode, this configuration process is supported only by the admin VS.

* Power off a main control board.
  
  You need to remove a main control board in any of the following situations:
  
  + The main control board needs maintenance, for example, dust cleaning.
  + The hardware of the main control board needs an upgrade, for example, memory capacity expansion.
  + The main control board fails.
* Power off an interface board.
  
  Power off the interface board in any of the following situations:
  
  + The interface board needs maintenance, for example, dust cleaning.
  + The interface board fails and needs to be repaired or replaced.

#### Pre-configuration Tasks

Before powering off a board, complete the following tasks:

* Check the slot of the board to be powered off.
* Prepare a spare board if the board needs to be replaced.

#### Procedure

* Power off a main control board.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**quit**](cmdqueryname=quit) command to return to the user view.
  3. Run the [**power**](cmdqueryname=power) **off** **slot** *slot-id* command to power off the main control board.
* Power off an interface board.
  
  
  
  After preparing a spare interface board, you can power off the interface board.
  
  Run the [**power**](cmdqueryname=power) **off** **slot** *slot-id* command to power off the interface board.
  
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If there is no terminal on the deployment site, you can power off the interface board by pressing the OFL button. The OFL button is on the upper part of the panel of the interface board. Press and hold the button for six seconds till the OFL indicator lights. This indicates that the interface board is powered off.

#### Verifying the Configuration

After the power-off operation, run the [**display device**](cmdqueryname=display+device) command. If the status of the board is displayed as Abnormal, the board is successfully powered off.