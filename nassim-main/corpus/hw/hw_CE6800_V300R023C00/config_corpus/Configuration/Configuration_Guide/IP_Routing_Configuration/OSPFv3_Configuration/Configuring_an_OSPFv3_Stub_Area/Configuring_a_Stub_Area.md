Configuring a Stub Area
=======================

Configuring a Stub Area

#### Prerequisites

Before configuring a stub area, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Enter the OSPFv3 area view.
   
   
   ```
   [area](cmdqueryname=area+%28OSPFv3+view%29) area-id
   ```
4. Configure the area as a stub area.
   
   
   ```
   [stub](cmdqueryname=stub+%28OSPFv3%29)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * All devices in a stub area must have the [**stub**](cmdqueryname=stub+%28OSPFv3%29) command configuration.
   * Running the [**stub**](cmdqueryname=stub+%28OSPFv3%29) command or canceling the configuration may cause the stub area to be updated. The [**stub**](cmdqueryname=stub+%28OSPFv3%29) command configuration on a device can be canceled or the configuration can be performed on new devices in the stub area only after the last area update is complete.
5. (Optional) Stop the ABR from sending Type 3 LSAs to the stub area.
   
   
   ```
   [stub](cmdqueryname=stub+%28OSPFv3%29) no-summary
   ```
6. (Optional) Stop the ABR from checking the neighbor status in the backbone area when it generates a default route and advertises it to the stub area.
   
   
   ```
   [stub](cmdqueryname=stub+%28OSPFv3%29) default-route-advertise backbone-peer-ignore
   ```
7. (Optional) Set a cost for the default route advertised to the stub area.
   
   
   ```
   [default-cost](cmdqueryname=default-cost+%28OSPFv3+area+view%29) cost
   ```
   
   By default, the cost of the default route advertised to the stub area is 1.
   
   To ensure the reachability of AS external routes, the ABR in the stub area generates a default route and advertises it to non-ABR devices in the stub area.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```