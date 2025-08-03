Activating L3VPN Interface Licenses on a Board
==============================================

The device supports L3VPN service activation by device or interface. If L3VPN service resources have been purchased based on the number of interfaces in the current project, you must allocate these resources to specified interfaces.

#### Pre-configuration Tasks

Before activating L3VPN interface licenses on a specified board, complete the following tasks:

* Run the [**license active**](cmdqueryname=license+active) *file-name* command to activate the license file on the active main control board.
* Run the [**active port-basic**](cmdqueryname=active+port-basic) **slot** *slotid* **card** *cardid* **port** *port-list* command to activate interface-specific basic hardware licenses on a board in batches.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active port-l3vpn-evpn**](cmdqueryname=active+port-l3vpn-evpn) **slot** *slot-id* **card** *card-id* **port** *port-list*
   
   
   
   L3VPN interface licenses are activated on a board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display license resource usage port-l3vpn-evpn**](cmdqueryname=display+license+resource+usage+port-l3vpn-evpn) { **all** | **slot** *slot-id* } [ **active** | **deactive** ] command to check whether L3VPN interface licenses have been activated on a board.