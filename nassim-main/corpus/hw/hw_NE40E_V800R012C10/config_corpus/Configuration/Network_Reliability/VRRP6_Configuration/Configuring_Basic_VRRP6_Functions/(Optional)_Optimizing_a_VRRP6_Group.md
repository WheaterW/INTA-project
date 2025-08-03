(Optional) Optimizing a VRRP6 Group
===================================

To optimize a VRRP6 group, enable the ping to a virtual IPv6 address, set the interval at which the master device in the VRRP6 group sends NA packets, and disable a device from checking the hop count in VRRP6 Advertisement packets.

#### Context

[Table 1](#EN-US_TASK_0172361852__tab_dc_vrp_vrrp6_cfg_010601) describes VRRP6 group optimization functions.

**Table 1** VRRP6 group optimization functions
| Function Item | Description |
| --- | --- |
| [Enabling a device to respond to ping packets destined for a virtual IPv6 address](#EN-US_TASK_0172361852__step_01) | Hosts can ping the virtual IPv6 address of a VRRP6 group configured on Routers. This function can be used to monitor the connectivity of links between hosts and a gateway. |
| [Disabling a device from checking TTL values in VRRP6 Advertisement packets](#EN-US_TASK_0172361852__step_03) | A VRRP6-enabled device checks the TTL value in every received VRRP6 Advertisement packet, and discards packets if their TTL value is not 255. On a network where devices of different vendors are deployed, a device with TTL check enabled may incorrectly discard valid packets. In this case, disable TTL check so that devices of different vendors can communicate. |
| [Configuring a mode that the master device uses to send ND packets](#EN-US_TASK_0172361852__step_06) | A QinQ termination sub-interface sends ND packets with two tags and the inner tag is a range of VLAN IDs. To ensure that switches connected to users learn the correct MAC address of the VRRP6 group, the VRRP6 group on the QinQ termination sub-interface sends ND packets to all VLANs identified by inner VLAN IDs. This increases the burden on the VRRP6-enabled device. To release the burden, the VRRP6-enabled device can be configured to send ND packets carrying only the minimal inner VLAN ID. |
| [Configuring a device to calculate the checksum of a VRRP6 packet based on the content excluding the IPv6 pseudo header](#EN-US_TASK_0172361852__step_05) | After receiving a VRRP6 packet, a Huawei device calculates the packet's checksum based on the content including the IPv6 pseudo header. However, a non-Huawei device may calculate the packet's checksum based on the content excluding the IPv6 pseudo header. As a result, VRRP negotiation between the Huawei and non-Huawei devices may fail. To resolve this issue, configure the Huawei device to calculate the checksum of a VRRP6 packet based on the content excluding the IPv6 pseudo header. |



#### Procedure

* Enable a device to respond to ping packets destined for a virtual IPv6 address.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp virtual-ip ping enable**](cmdqueryname=vrrp+virtual-ip+ping+enable)
     
     
     
     The device is enabled to respond to ping packets destined for a virtual IPv6 address.
     
     After this function is enabled, hosts can ping a virtual IPv6 address, which may expose the device to ICMPv6 attacks. In this case, run the [**undo vrrp virtual-ip ping enable**](cmdqueryname=undo+vrrp+virtual-ip+ping+enable) command to disable the ping function.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Disable a device from checking TTL values in VRRP6 Advertisement packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface where a VRRP6 group resides is displayed.
  3. Run [**vrrp6 un-check hop-limit**](cmdqueryname=vrrp6+un-check+hop-limit)
     
     
     
     The device is disabled from checking TTL values in VRRP6 Advertisement packets.
     
     
     
     To enable a device to check TTL values in received VRRP6 Advertisement packets, run the [**undo **vrrp6 un-check hop-limit****](cmdqueryname=undo+vrrp6+un-check+hop-limit) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a mode that the master device uses to send ND packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp gratuitous-arp timeout**](cmdqueryname=vrrp+gratuitous-arp+timeout) *time*
     
     
     
     An interval at which the master device sends gratuitous ND packets is configured.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.sub-interface-number*
     
     
     
     The view of an Ethernet sub-interface or Eth-Trunk sub-interface where a VRRP6 group resides is displayed.
  4. Run [**vrrp6 nd send-mode simple**](cmdqueryname=vrrp6+nd+send-mode+simple)
     
     
     
     The sub-interface for QinQ VLAN tag termination on the master device is configured to send ND packets only with the first VLAN ID specified in the inner tag and each VLAN ID in the outer tag.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a device to calculate the checksum of a VRRP6 packet based on the content excluding the IPv6 pseudo header.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp6 checksum exclude pseudo-header**](cmdqueryname=vrrp6+checksum+exclude+pseudo-header)
     
     
     
     The device is configured to calculate the checksum of a VRRP6 packet based on the content excluding the IPv6 pseudo header.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.