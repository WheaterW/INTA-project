Activating an SRv6 Port License for a Board
===========================================

If only an SRv6 port license rather than a device-based license is purchased, you can configure SRv6 services only after activating the SRv6 port license.

#### Usage Scenario

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After you install a device-based SRv6 license, the SRv6 function can be enabled without requiring you to activate an SRv6 port license through the **active port-srv6** command.

SRv6 services can be configured only after you activate an SRv6 port license.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active port-srv6**](cmdqueryname=active+port-srv6) **slot** *slotid* **card** *cardid* **port** *port-list*
   
   
   
   The SRv6 port license is activated for a specified board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display license resource usage port-srv6**](cmdqueryname=display+license+resource+usage+port-srv6) { **all** | **slot** *slotid* } [ **active** | **deactive** ] command to check whether the SRv6 port license has been activated for the board.