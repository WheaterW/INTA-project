Activating EVPN Interface Licenses on a Board
=============================================

The device supports EVPN service activation by device or interface. If EVPN service resources have been purchased based on the number of ports in the current project, you must allocate these resources to specified ports.

#### Pre-configuration Tasks

Before activating EVPN interface licenses on a board, complete the following tasks:

* Run the [**license active**](cmdqueryname=license+active) *file-name* command to activate a specified license file on the main control board.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active port-l3vpn-evpn**](cmdqueryname=active+port-l3vpn-evpn) **slot** *slot-id* **card** *card-id* **port** *port-list*
   
   
   
   EVPN interface licenses are activated on the board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display license resource usage port-l3vpn-evpn**](cmdqueryname=display+license+resource+usage+port-l3vpn-evpn) { **all** | **slot** *slot-id* } [ **active** | **deactive** ] command to check whether EVPN interface licenses have been activated on boards.