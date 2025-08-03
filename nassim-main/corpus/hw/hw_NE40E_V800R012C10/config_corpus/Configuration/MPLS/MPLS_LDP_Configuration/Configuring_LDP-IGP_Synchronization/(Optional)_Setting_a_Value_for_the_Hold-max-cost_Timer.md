(Optional) Setting a Value for the Hold-max-cost Timer
======================================================

If the LDP session or LDP adjacency on the primary link fails, LSP traffic is switched to the backup link within the specified hold-max-cost period before the reestablishment of the LDP session and LDP adjacency on the primary link.

#### Context

Select parameters based on networking requirements:

* If IGP routes carry only LDP services, specify the **infinite** parameter to ensure that the behavior for IGP routes is always consistent with that for an LDP LSP.
* If IGP routes carry multiple types of services, including LDP services, set a specific time value to ensure that an LDP session or adjacency teardown does not affect IGP route selection or other services.


#### Procedure

* If OSPF is used, perform the following configuration on the interfaces on both ends of the link between the node where the primary LSP and the backup LSP diverge from each other and its LDP peer on the primary LSP:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ospf timer ldp-sync hold-max-cost**](cmdqueryname=ospf+timer+ldp-sync+hold-max-cost+infinite) { *value* | **infinite** }
     
     
     
     The period during which the interface advertises the maximum link cost in local LSAs is set.
     
     
     
     The hold-max-cost timer value determines the period in which the local node advertises the maximum link cost in local LSAs.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To set a value for the hold-max-cost timer on an OSPF multi-area adjacency interface, run the [**ospf timer ldp-sync hold-max-cost**](cmdqueryname=ospf+timer+ldp-sync+hold-max-cost+infinite+multi-area) { *value* | **infinite** } **multi-area** *area-id* command.
  4. (Optional) Set the maximum cost for OSPF links.
     
     
     
     In an IGP-LDP synchronization scenario, when an LDP tunnel's next hop changes, a large number of entries need to be updated. If upstream and downstream forwarding entries reside on different boards, they may not be updated synchronously during traffic switchback. As a result, packet loss occurs if upstream forwarding entries are updated but downstream forwarding entries are not. To prevent packet loss, FRR forwarding entries can be created for the switchback path, and the link's primary/backup status can be updated during traffic switchback. As defined in standard protocols, in an IGP-LDP synchronization scenario, if LDP is not in the fully operational state, OSPF needs to set the link cost to LSInfinity (65535); however, a link cannot participate in FRR route computation if its cost is 65535. To resolve this conflict in an IGP-LDP synchronization scenario, run the [**maximum-link-cost**](cmdqueryname=maximum-link-cost) *cost* command to change the maximum cost for OSPF links.
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] command to enter the OSPF view.
     3. Run the [**maximum-link-cost**](cmdqueryname=maximum-link-cost) *cost* command to set the maximum cost for OSPF links.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* If IS-IS is used:
  
  
  
  Perform the following configuration on the node where the primary and backup links diverge from each other.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The specified IS-IS process is started, and the IS-IS view is displayed.
  3. Run [**timer ldp-sync hold-max-cost**](cmdqueryname=timer+ldp-sync+hold-max-cost+infinite) { **infinite** | *interval* }
     
     
     
     The period in which all interfaces in the IS-IS process advertise the maximum link cost in local LSPs is set.
  
  
  
  Perform the following configuration on the interfaces of both ends of the link between the cross node of primary and backup links and the LDP neighboring node on the primary link.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis timer ldp-sync hold-max-cost**](cmdqueryname=isis+timer+ldp-sync+hold-max-cost+infinite) { *value* | **infinite** }
     
     
     
     The period in which the IS-IS interface advertises the maximum link cost in local LSPs is set.
     
     
     
     The hold-max-cost timer value determines the period in which the local node advertises the maximum link cost in local LSPs.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.