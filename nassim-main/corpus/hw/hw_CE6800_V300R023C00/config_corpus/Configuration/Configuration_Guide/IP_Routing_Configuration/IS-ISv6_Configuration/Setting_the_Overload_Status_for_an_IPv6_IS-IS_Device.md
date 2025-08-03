Setting the Overload Status for an IPv6 IS-IS Device
====================================================

Setting the Overload Status for an IPv6 IS-IS Device

#### Prerequisites

Before setting the overload status for an IPv6 IS-IS device, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

IPv6 IS-IS uses the OL field in LSPs to identify the overload status of an IPv6 IS-IS device. If a device sets the OL bit to 1, other devices ignore this device (except for direct routes to it) when performing SPF calculation. In [Figure 1](#EN-US_TASK_0000001176662177__fig_dc_feature_isis_000801), packets from DeviceA to network segment 2001:db8:1::/64 are forwarded through DeviceB. If DeviceA receives an LSP with the OL bit set to 1 from DeviceB, DeviceA considers that the LSDB of DeviceB is incomplete. Consequently, the packets to network segment 2001:db8:1::/64 are forwarded through DeviceD and DeviceE. However, the packets destined for the network segment directly connected to DeviceB are still forwarded through DeviceA.

**Figure 1** Network diagram with IPv6 IS-IS overload  
![](figure/en-us_image_0000001176742129.png)

If a device can neither store new LSPs nor perform LSDB synchronization normally, the routing information calculated by the device is incorrect. In this case, the device automatically enters the overload status. As a result, other devices ignore it (except for direct routes to it) when performing SPF calculation.

A device may enter the overload status due to a device exception or a manual configuration. If a device needs to be isolated from the network temporarily for upgrade or maintenance purposes, you can set the overload status for the device to prevent other devices from using it to forward traffic.![](public_sys-resources/note_3.0-en-us.png) 

* If a device enters the overload status due to a device exception, the device deletes all imported and leaked routing information.
* If a device enters the overload status due to a manual configuration, the device determines whether to delete all imported and leaked routing information based on the configuration.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Set the overload status for the device.
   
   
   ```
   [set-overload](cmdqueryname=set-overload) { on-startup [ timeout1 | start-from-nbr system-id [ timeout1 [ timeout2 ] ] | wait-for-bgp [ timeout1 ] ] [ route-delay-distribute timeout4 ] [ send-sa-bit [ timeout3 ] ] [ route-max-metric ] } [ allow { interlevel | external } * ]
   ```
   
   By default, the overload status is not set for the device.
   
   **on-startup**: If **on-startup** is specified, the device enters the overload status when it restarts or encounters an exception, and it stays in the status for a specified period. To delay route advertisement in this case, you must specify both the **on-startup** and **route-delay-distribute** parameters.
   
   **start-from-nbr**: This parameter configures the device to remain in the overload status for a specified period based on the status of the neighbor with a specified system ID.
   
   **wait-for-bgp**: IS-IS routes converge faster than BGP routes do. On a network where both IS-IS and BGP are configured, you can specify **wait-for-bgp** so that the device stays in the overload status for a specified period. This prevents routing black holes by ensuring the device waits until BGP convergence is complete. After the period elapses, the device exits the overload status.
   
   **send-sa-bit**: This parameter configures the device to set the OL bit to 1 in the IIHs it sends after a restart.
   
   **allow**: This parameter allows the device to advertise prefix routes even in the overload status. By default, a device in the overload status does not advertise prefix routes.
   
   **route-max-metric**: This parameter sets the metrics of locally originated routes to the maximum value.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ [ **level-1** | **level-2** ] | **verbose** [ **no-name** ] | [ **local** | *lsp-id* | **is-name** *symbolic-name* ] ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.