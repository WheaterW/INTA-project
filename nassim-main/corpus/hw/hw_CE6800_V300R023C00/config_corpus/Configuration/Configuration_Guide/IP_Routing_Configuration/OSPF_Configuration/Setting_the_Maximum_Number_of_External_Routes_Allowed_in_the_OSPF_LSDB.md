Setting the Maximum Number of External Routes Allowed in the OSPF LSDB
======================================================================

Setting the Maximum Number of External Routes Allowed in the OSPF LSDB

#### Prerequisites

Before setting the maximum number of external routes allowed in the LSDB, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

OSPF devices in the same area are considered to have converged once they have the same LSDB. However, achieving such a state can be difficult as the number of routes on a network continuously increases, causing some devices to be unable to carry excess routing information due to limited system resources. This is called an OSPF database overflow.

One way to solve such an issue is to configure stub areas or NSSAs, which reduces the amount of routing information on devices. However, such an approach cannot prevent an OSPF database overflow caused by a sharp increase in dynamic routes. To resolve this issue, set the maximum number of external routes allowed in the LSDB to dynamically limit the size of the LSDB.

![](../public_sys-resources/note_3.0-en-us.png) 

The maximum numbers set for all devices in the OSPF AS must be the same.

If the number of external routes in the LSDB exceeds the maximum number on a device, the device enters the overflow state and starts the overflow timer. For details, see [Table 1](#EN-US_TASK_0000001176742911__tab_dc_vrp_feature_new_00630701).

**Table 1** Operations performed by the device after it enters or exits the overflow state
| Phase | OSPF Processing |
| --- | --- |
| Staying in the overflow state | Removes self-generated non-default external routes and stops advertising non-default external routes.  Discards newly received non-default external routes and does not reply with an LSAck packet.  Checks whether the number of external routes is still greater than the preset maximum number when the overflow timer expires.   * Restarts the timer if the number of external routes is greater than the preset maximum number. * Exits the overflow state if the number of external routes is less than or equal to the preset maximum number. |
| Exiting the overflow state | Disables the overflow timer.  Advertises non-default external routes.  Accepts newly received non-default external routes and replies with LSAck packets. |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Set the maximum number of external routes allowed in the LSDB.
   
   
   ```
   [lsdb-overflow-limit](cmdqueryname=lsdb-overflow-limit) number
   ```
   
   If the number of external routes imported by OSPF exceeds the preset maximum number, the device deletes self-generated non-default external routes to ensure proper forwarding of the other external routes.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** command to check the OSPF LSDB information on each device.