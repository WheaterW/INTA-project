Activating the FlexE Interface License on a Board
=================================================

To configure FlexE services on a board, you must activate the FlexE interface license on the board first.

#### Pre-configuration Tasks

Before activating the FlexE interface license on a board, complete the following tasks:

1. Run the [**license active**](cmdqueryname=license+active) *file-name* command to activate a specified license file on the main control board.
2. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
3. Run the [**license**](cmdqueryname=license) command to enter the license view.
4. Run the [**active port-basic**](cmdqueryname=active+port-basic) **slot** *slotid* **card** *cardid* **port** *portlist* command to activate the interface-specific basic hardware license.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active port-flexe**](cmdqueryname=active+port-flexe) **slot** *slotid* **card** *cardid* **port** *portlist*
   
   
   
   The FlexE interface license is activated on a specified board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.