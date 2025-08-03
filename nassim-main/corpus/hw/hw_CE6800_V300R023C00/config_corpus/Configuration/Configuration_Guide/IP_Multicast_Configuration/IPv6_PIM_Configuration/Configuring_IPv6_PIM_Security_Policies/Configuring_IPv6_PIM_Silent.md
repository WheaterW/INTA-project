Configuring IPv6 PIM Silent
===========================

Configuring IPv6 PIM Silent

#### Usage Scenario

On the access layer, IPv6 PIM needs to be enabled on a device's interface that is directly connected to a user host. With this configuration, the interface can establish an IPv6 PIM neighbor relationship to process various IPv6 PIM messages. This configuration, however, introduces security risks. When the host maliciously sends IPv6 PIM Hello messages, the device may break down.

To address this problem, configure PIM silent on the involved interface. After an interface enters the PIM silent state, the interface is disabled from accepting and forwarding IPv6 PIM messages, and all PIM neighbors and PIM states on the interface are deleted. The interface immediately becomes a DR. Multicast Listener Discovery (MLD) is not affected on the interface.

This function applies only to a device's interfaces that are directly connected to the subnet of user hosts and the subnet is connected only to this device. If this function is enabled on the interface connected to a device rather than a host, PIM neighbor relationships cannot be established, and multicast faults occur. If the subnet of user hosts is connected to multiple devices and PIM silent is enabled on these devices' interfaces, all these interfaces become static DRs, which means that there are multiple DRs on the subnet. This results in multicast faults.

![](public_sys-resources/note_3.0-en-us.png) 

After this function is configured on an interface, the interface no longer accepts or sends any IPv6 PIM messages, and other PIM functions on the interface become invalid. Therefore, exercise caution when using this function.



#### Prerequisites

Before configuring the PIM silent function, you have completed the following tasks:

* Configure a unicast routing protocol.
* [Configure IPv6 PIM-SM](vrp_ipv6pim_cfg_0001.html).
* Configure MLD.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable IPv6 PIM silent.
   
   
   ```
   [pim ipv6 silent](cmdqueryname=pim+ipv6+silent)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```