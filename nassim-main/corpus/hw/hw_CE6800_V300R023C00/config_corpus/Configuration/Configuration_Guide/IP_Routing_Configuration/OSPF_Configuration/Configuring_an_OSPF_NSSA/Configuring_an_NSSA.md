Configuring an NSSA
===================

Configuring an NSSA

#### Prerequisites

Before configuring an NSSA, you have completed the following task:

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
4. Configure the area as an NSSA.
   
   
   ```
   [nssa](cmdqueryname=nssa) [ default-route-advertise [ backbone-peer-ignore ] | no-import-route | no-summary | set-n-bit | suppress-forwarding-address | translator-always | translator-interval interval-value | zero-address-forwarding ] *
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * All devices in an NSSA must have the [**nssa**](cmdqueryname=nssa) command configuration.
   * Running the [**nssa**](cmdqueryname=nssa) command or canceling the configuration may cause the NSSA to be updated and neighbor relationships to be disconnected. The [**nssa**](cmdqueryname=nssa) command configuration on a device can be canceled or the configuration can be performed on new devices in the NSSA only after the last area update is complete.
5. (Optional) Set the cost of the default route information carried in Type 3 LSAs that are transmitted by the ABR to the NSSA.
   
   
   ```
   [default-cost](cmdqueryname=default-cost) cost
   ```
   
   
   
   To ensure the reachability of AS external routes, the ABR in the NSSA generates a default route and advertises it to the other devices in the NSSA. Setting a cost for the default route advertised to an NSSA adjusts the route selection result.
   
   By default, the cost of the default route that is sent by the ABR to the NSSA is 1.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```