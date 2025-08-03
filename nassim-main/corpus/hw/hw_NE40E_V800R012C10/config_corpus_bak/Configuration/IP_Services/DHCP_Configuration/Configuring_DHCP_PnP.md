Configuring DHCP PnP
====================

This section describes how to configure Dynamic Host Configuration Protocol (DHCP) plug-and-play (PnP). DHCP PnP enables the network management system (NMS) to remotely configure and commission devices. This feature improves the working process and reduces operation and maintenance (O&M) costs.

#### Usage Scenario

Mobile networks have lots of access devices. Software commissioning engineers need to configure and commission these devices on site. This network construction method requires significant human and material resources, causing high capital expenditure (CAPEX) and operational expenditure (OPEX). DHCP PnP has been developed to resolve the problem.

DHCP PnP enables the NMS to use DHCP to automatically configure and commission devices remotely. This solution reduces the time required to commission devices on site and frees personnel from working in unfavorable outdoor environments. It improves the working process and reduces costs. [Figure 1](#EN-US_TASK_0172364708__en-us_task_0172364709_fig_dc_vrp_dhcp-pnp_cfg_001901) shows the DHCP PnP networking.

In VS mode, this feature is supported only by the admin VS.

**Figure 1** DHCP PnP networking  
![](images/fig_dc_vrp_dhcp-pnp_cfg_001901.png)


#### Pre-configuration Tasks

Before configuring DHCP PnP, complete the following tasks:

* Configure a DHCP server.
* Configure a DHCP relay agent if the DHCP client and DHCP server are not on the same network segment.


#### Procedure

* If PnP is required and the DHCP client and server are on different network segments, perform the following operations on the DHCP relay agent:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp select relay**](cmdqueryname=dhcp+select+relay)
     
     
     
     The DHCP relay function is enabled.
  4. Run [**ip relay address**](cmdqueryname=ip+relay+address) *ip-address*
     
     
     
     The IP address of the DHCP server to which the DHCP relay agent relays messages is configured on the DHCP relay agent.
  5. (Optional) Run [**ip relay source-ip-address**](cmdqueryname=ip+relay+source-ip-address) *ip-address*
     
     
     
     An IP address is configured for the DHCP relay agent.
     
     
     
     This step is performed only when DHCP relay agent and DHCP server routes are isolated and DHCP PnP is required.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* If PnP is not required, use serial interfaces to connect to the DHCP client. To disable PnP, run the [**undo pnp enable**](cmdqueryname=undo+pnp+enable) command in the system view.

#### Result

After the configuration is complete, run the following commands on the DHCP client to check the result:

Run the [**display pnp state**](cmdqueryname=display+pnp+state) command to check whether the device is in the DHCP PnP state.

```
<HUAWEI> display pnp state
```
```
PNP State!!!PLEASE UNDO PNP enable for manual Setup! 
You can undo PNP in system view with "undo pnp enable
```

Run the [**display nms-vpn-instance**](cmdqueryname=display+nms-vpn-instance) **ip-address** *ip-address* command to view VPN instances to which the specified IP address is bound.

```
<HUAWEI> display nms-vpn-instance ip-address 3.3.3.3
```
```
IP Address           Interface                                VPN-Instance  
--------------------------------------------------------------------------------
3.3.3.3              gigabitethernet0/3/2                     vpna  

```

#### Follow-up Procedure

After DHCP PnP is performed, the PnP default route is no longer required. Run the [**undo pnp default route**](cmdqueryname=undo+pnp+default+route) command on the DHCP client to delete route information and free up routing table space.