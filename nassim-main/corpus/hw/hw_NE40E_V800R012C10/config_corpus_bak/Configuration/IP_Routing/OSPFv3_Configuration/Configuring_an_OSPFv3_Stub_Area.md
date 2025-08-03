Configuring an OSPFv3 Stub Area
===============================

A non-backbone area in the edge of an AS can be configured as a stub area so that routes from other areas on the OSPFv3 network or AS external routes are not transmitted. This reduces bandwidth and storage resource consumption on the Router, routing table size, and the amount of routing information to be transmitted.

#### Usage Scenario

The number of LSAs can be reduced by partitioning an AS into different areas. To reduce the number of entries in the routing table and the number of LSAs to be transmitted in a non-backbone area, configure the non-backbone area on the border of the AS as a stub area.

Configuring a stub area is optional. A stub area generally resides on the border of an AS. For example, a non-backbone area with only one ABR can be configured as a stub area. In a stub area, the number of entries in the routing table and the amount of routing information to be transmitted greatly decrease.

Note the following points when configuring a stub area:

* The backbone area (Area 0) cannot be configured as a stub area.
* If an area needs to be configured as a stub area, all the Routers in this area must be configured with stub attributes using the [**stub**](cmdqueryname=stub) command.
* An ASBR cannot exist in a stub area. External routes are not transmitted in the stub area.

#### Pre-configuration Tasks

Before configuring a stub area, complete the following tasks:

* Configuring IP addresses for interfaces to ensure that neighboring Routers are reachable at the network layer
* [Configuring Basic OSPFv3 Functions](dc_vrp_ospfv3_cfg_2003.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPFv3 area view is displayed.
4. Run [**stub**](cmdqueryname=stub)
   
   
   
   The specified area is configured as a stub area.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * All Routers in a stub area must be configured with stub attributes using the [**stub**](cmdqueryname=stub) command.
   * Configuring or deleting stub attributes will update routing information in the area. Stub attributes can be deleted or configured again only after the routing update is complete.
5. (Optional) Run [**stub**](cmdqueryname=stub) **no-summary**
   
   
   
   The ABR is prevented from sending Type 3 LSAs (Summary LSAs) to the stub area.
6. (Optional) Run [**stub**](cmdqueryname=stub) **default-route-advertise** **backbone-peer-ignore**
   
   
   
   The device is configured to advertise default routes and ignore the status of the neighbors in the backbone area.
7. (Optional) Run [**default-cost**](cmdqueryname=default-cost) *cost*
   
   
   
   The cost of the default route to the stub area is set.
   
   To ensure the reachability of AS external routes, the ABR in the stub area generates a default route and advertises the route to the other Routers in the stub area.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** command, and you can view LSDB information, including the types of LSAs and link state IDs.

When Router is in a common area, there are AS external routes in the routing table. After the area where Router resides is configured as a stub area, AS external routes are invisible.