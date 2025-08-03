Configuring a Stub Area
=======================

Configuring a Stub Area

#### Prerequisites

Before configuring a stub area, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Enter the OSPF area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
4. Configure the area as a stub area.
   
   
   ```
   [stub](cmdqueryname=stub)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * All devices in a stub area must have the [**stub**](cmdqueryname=stub) command configuration.
   * Running the [**stub**](cmdqueryname=stub) command or canceling the configuration may cause the stub area to be updated. The [**stub**](cmdqueryname=stub) command configuration on a device can be canceled or the configuration can be performed on new devices in the stub area only after the last area update is complete.
5. (Optional) Stop the ABR from sending network-summary-LSAs (Type 3) to the stub area.
   
   
   ```
   [stub](cmdqueryname=stub) no-summary
   ```
6. (Optional) Stop the ABR from checking the neighbor status in the backbone area when it generates a default route and advertises it to the stub area.
   
   
   ```
   [stub](cmdqueryname=stub) default-route-advertise backbone-peer-ignore
   ```
7. (Optional) Set a cost for the default route advertised to the stub area.
   
   
   ```
   [default-cost](cmdqueryname=default-cost) cost
   ```
   
   By default, the cost of the default route advertised to the stub area is 1.
   
   To ensure the reachability of AS external routes, the ABR in the stub area generates a default route and advertises it to non-ABR devices in the stub area.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```