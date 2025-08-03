Configuring an OSPF Stub Area
=============================

Configuring a non-backbone area as a stub area can reduce routing entries in the area in an AS does not transmit routes learned from other areas in the AS or AS external routes. This reduces bandwidth and storage resource consumption.

#### Usage Scenario

The number of LSAs can be reduced by partitioning an OSPF network into different areas. To reduce the number of entries in the routing table and the number of LSAs to be transmitted in a non-backbone area, configure the non-backbone area on the border of the AS as a stub area.

Configuring a stub area is optional. A stub area generally resides on the border of an AS. For example, a non-backbone area with only one ABR can be configured as a stub area. In a stub area, the number of entries in the routing table and the amount of routing information to be transmitted greatly decrease.

Note the following points when configuring a stub area:

* The backbone area (Area 0) cannot be configured as a stub area.
* If an area needs to be configured as a stub area, all the Routers in this area must be configured with stub attributes using the [**stub**](cmdqueryname=stub) command.
* An ASBR cannot exist in a stub area. External routes are not transmitted in the stub area.
* Virtual links cannot exist in the stub area.

#### Pre-configuration Tasks

Before configuring an OSPF stub area, complete the following tasks:

* Configure an address for each involved interface to ensure that neighboring devices can communicate with each other at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPF area view is displayed.
4. Run [**stub**](cmdqueryname=stub)
   
   
   
   The specified area is configured as a stub area.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * All Routers in a stub area must have the [**stub**](cmdqueryname=stub) command configuration.
   * Running the [**stub**](cmdqueryname=stub) command or canceling the configuration may cause the stub area to be updated. The [**stub**](cmdqueryname=stub) command configuration on a device can be canceled or the configuration can be performed on new devices in the stub area only after the last area update is complete.
5. (Optional) Run [**stub**](cmdqueryname=stub) **no-summary**
   
   
   
   The ABR is prevented from sending Type 3 LSAs (Summary LSAs) to the stub area.
6. (Optional) Run [**stub**](cmdqueryname=stub) **default-route-advertise** **backbone-peer-ignore**
   
   
   
   The device is configured to advertise default routes without checking the neighbor status in the backbone area.
7. (Optional) Run [**default-cost**](cmdqueryname=default-cost) *cost*
   
   
   
   A cost is set for the default route advertised to the stub area.
   
   To ensure the reachability of AS external routes, the ABR in the stub area generates a default route and advertises it to non-ABR Routers in the stub area.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** command to check OSPF LSDB information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command to check information about OSPF neighbors.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table.