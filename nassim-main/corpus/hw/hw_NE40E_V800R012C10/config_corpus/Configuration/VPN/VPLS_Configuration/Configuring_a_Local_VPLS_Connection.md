Configuring a Local VPLS Connection
===================================

A local VPLS connection enables two CEs that connect to the same PE to communicate.

#### Usage Scenario

If two CEs connect to the same PE, you can establish a local VPLS connection between the two CEs for them to communicate. In this situation, the PE functions similarly to a Layer 2 switch to directly transmit packets without using any public network tunnel.


#### Pre-configuration Tasks

Before configuring a local VPLS connection, complete the following tasks:

* Configure the encapsulation types of PE interfaces (AC interfaces) connecting to CEs.
* Configure basic MPLS functions on the PE.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ]
   
   
   
   A VSI is configured, and its view is displayed.
5. Run [**pwsignal ldp**](cmdqueryname=pwsignal+ldp)
   
   
   
   LDP is configured as the signaling type of the VSI.
6. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   An ID is configured for the VSI.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the VSI view.
8. Run [**mac-learning disable**](cmdqueryname=mac-learning+disable)
   
   
   
   MAC address learning is disabled.
9. Run [**p2p-vsi enable**](cmdqueryname=p2p-vsi+enable)
   
   
   
   A local VPLS connection is configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verify the configuration.

After the configuration is complete, check the configuration as follows:

* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
* Run the [**display vsi services**](cmdqueryname=display+vsi+services) { *vsi-name* | **all** | **interface** *interface-type* *interface-number* | **vlan** *vlan-id* } command to check information about the AC interfaces associated with a specified VSI.