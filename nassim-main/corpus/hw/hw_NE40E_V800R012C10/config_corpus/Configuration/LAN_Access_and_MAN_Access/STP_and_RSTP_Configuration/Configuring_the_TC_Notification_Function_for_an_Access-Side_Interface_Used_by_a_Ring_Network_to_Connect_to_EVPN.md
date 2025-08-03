Configuring the TC Notification Function for an Access-Side Interface Used by a Ring Network to Connect to EVPN
===============================================================================================================

Configuring the TC Notification Function for an Access-Side Interface Used by a Ring Network to Connect to EVPN

#### Context

In a scenario where an Ethernet ring network is connected to an EVPN, if an access-side interface on the ring network is configured with a sub-interface bound to a BD and is also enabled to snoop STP TC BPDUs, you need to enable the TC notification function on the interface. In this way, after the interface receives a TC BPDU from the ring network, it can instruct the sub-interface to update ARP and MAC entries in a timely manner.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view.
3. Run the [**stp tc-snooping enable**](cmdqueryname=stp+tc-snooping+enable) command to enable the interface to snoop STP TC BPDUs.
4. Run the [**stp tc-snooping notify bridge-domain**](cmdqueryname=stp+tc-snooping+notify+bridge-domain) [ [**process**](cmdqueryname=process) *process-Id* ] command to enable the TC notification function on the interface.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.