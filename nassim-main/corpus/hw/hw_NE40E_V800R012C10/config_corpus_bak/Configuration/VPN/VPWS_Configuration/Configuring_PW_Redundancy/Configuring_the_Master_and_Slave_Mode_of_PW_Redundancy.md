Configuring the Master/Slave Mode of PW Redundancy
==================================================

PW redundancy in master/slave mode implements fault isolation for public and AC links.

#### Context

When creating a PW on the local end, configure the PWs that are connected to the two remote PEs. The primary/secondary PW status is manually specified on a local PE and the remote master PE and is notified to the remote slave PE connected to the local PE. The combined usage of PW redundancy in master/slave mode and the bypass PW can prevent network-side faults from affecting the AC side and AC-side faults from affecting the network side.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is applicable only to the master/slave PW redundancy mode. If only the independent PW redundancy mode is used, skip this configuration.



#### Procedure

1. Create a primary PW. See [Configuring a VPWS Connection](dc_vrp_vpws_cfg_3006.html).
2. Create a secondary PW. For details, see [Configuring a Secondary PW](dc_vrp_vpws_cfg_5002.html).
3. Configure the master/slave PW redundancy mode.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the AC interface view.
   3. Run the [**mpls l2vpn redundancy**](cmdqueryname=mpls+l2vpn+redundancy) **master** command to configure the master/slave PW redundancy mode.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. (Optional) Configure VPWS switching. For details, see [Configuring VPWS Switching](dc_vrp_vpws_cfg_5001.html).
   
   
   
   If multi-segment PWs need to be set up, you must configure VPWS switching on each SPE. PW redundancy supports only dynamic VPWS switching.
5. Configure a bypass PW.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the AC interface view.
   2. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] | **access-port** | **ignore-standby-state** ] \* **bypass** command to configure a bypass PW.
6. (Optional) Run [**mpls l2vpn stream-dual-receiving**](cmdqueryname=mpls+l2vpn+stream-dual-receiving)
   
   
   
   A CSG is enabled to receive packets on both primary and secondary PWs, preventing packet loss during a primary/secondary PW switchback.
7. (Optional) Run [**mpls l2vpn switchover**](cmdqueryname=mpls+l2vpn+switchover)
   
   
   
   Traffic is switched from the primary PW to the secondary PW.
   
   In the scenario where PW redundancy in master/slave mode is configured, traffic is transmitted through the primary PW, and the secondary PW functions normally. To forcibly switch traffic from the primary PW to the secondary PW (for example, because of a device upgrade or service re-deployment), you can use this command. To switch traffic back to the primary PW (for example, after the device is upgraded), you can run the undo form of this command to forcibly switch traffic from the secondary PW to the primary PW.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.