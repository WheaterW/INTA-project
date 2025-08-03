(Optional) Enabling IPsec
=========================

To enable the VSUP to process IPsec services, you need to enable IPsec.

#### Prerequisites

* The corresponding GTL license file has been loaded through the [**license active**](cmdqueryname=license+active) *file-name* command.
* Before configuring IPsec on the main control board, you do not need to enable IPsec. However, before configuring IPsec on the VSUP, you need to run the [**vsm on-board-mode disable**](cmdqueryname=vsm+on-board-mode+disable) command in the system view.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After you run the [**vsm on-board-mode disable**](cmdqueryname=vsm+on-board-mode+disable) command, IPsec cannot be configured on the main control board.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the following models support this configuration:

NE40E-M2K

NE40E-M2K-B



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active ipsec bandwidth-enhance**](cmdqueryname=active+ipsec+bandwidth-enhance+slot) *value* **slot** *slot-id*
   
   
   
   The bandwidth resource enhancement function is activated for the VSUP. The default IPsec bandwidth of a board is 0 Gbit/s. If this function is not activated, IPsec cannot be used on the board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display ipsec bandwidth**](cmdqueryname=display+ipsec+bandwidth+slot) [ **slot** *slot-id* ] command to check the bandwidth configured in the IPsec license.