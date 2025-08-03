Configuring the TC Notification Function for an Access-Side Interface Used by a Ring Network to Connect to VPLS
===============================================================================================================

Configuring the TC Notification Function for an Access-Side Interface Used by a Ring Network to Connect to VPLS

#### Context

In the scenario where an Ethernet ring network is connected to a BD VPLS network, if the access-side interface of the ring network is configured with a sub-interface bound to a BD and the BD is bound to the VSI, you need to enable the TC notification function on the interface. In this way, after the interface receives an STP TC-BPDU, it instructs the VSI to which the BD is bound to update ARP entries and MAC address entries in a timely manner.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view.
3. Run the [**stp enable**](cmdqueryname=stp+enable) command to enable STP/RSTP on the interface.
4. Run the [**stp tc-notify bridge-domain**](cmdqueryname=stp+tc-notify+bridge-domain) command to enable the TC notification function on the interface.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.