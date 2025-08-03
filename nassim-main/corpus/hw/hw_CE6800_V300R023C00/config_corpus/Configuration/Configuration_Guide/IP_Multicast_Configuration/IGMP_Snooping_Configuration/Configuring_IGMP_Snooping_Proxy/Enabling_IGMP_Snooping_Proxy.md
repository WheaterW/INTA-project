Enabling IGMP Snooping Proxy
============================

Enabling IGMP Snooping Proxy

#### Context

When IGMP is disabled on Layer 3 devices (for example, when only a static multicast group is configured), no IGMP querier is available on the network to maintain multicast group memberships. You can configure IGMP snooping proxy so that the Layer 2 device can function as an IGMP querier and sends IGMP Query messages.

When IGMP is enabled on the network, IGMP snooping proxy can be deployed on a Layer 2 device so that the device can send IGMP Report/Leave messages to its upstream Layer 3 device on behalf of user hosts. This helps minimize the number of such messages sent to the Layer 3 device.

A device configured with IGMP snooping proxy acts as a host for its upstream devices and as a querier for its downstream hosts.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Enable IGMP snooping proxy.
   
   
   ```
   [igmp snooping proxy](cmdqueryname=igmp+snooping+proxy)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   IGMP snooping proxy cannot be enabled in a VLAN if the corresponding VLANIF interface has Layer 3 multicast functions (such as IGMP or PIM) enabled.
   
   The IGMP snooping querier and IGMP message suppression functions can be enabled in a VLAN to implement the same function as IGMP snooping proxy. If the IGMP snooping proxy function is configured in a VLAN, neither the IGMP snooping querier function nor the IGMP message suppression function can be configured in the VLAN.
4. (Optional) Configure the device to transparently transmit protocol messages in a VLAN.
   
   
   ```
   [igmp snooping proxy router-protocol-pass](cmdqueryname=igmp+snooping+proxy+router-protocol-pass)
   ```
   
   By default, an IGMP snooping proxy device terminates received protocol messages and learns multicast forwarding entries from these messages. If IGMP snooping proxy is enabled on both the upstream and downstream devices, you can run this command so that the device transparently forwards the protocol messages it receives on a router port to other router ports, without learning the entries of the messages. In this way, the upstream and downstream devices do not learn entries from each other, preventing issues with entries being aged out.
5. (Optional) Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. (Optional) Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
7. (Optional) Disable the device from forwarding IGMP Query messages to the upstream router.
   
   
   ```
   [igmp snooping proxy-uplink-port](cmdqueryname=igmp+snooping+proxy-uplink-port) vlan vlan-id
   ```
   
   After IGMP snooping proxy is enabled on a device, it periodically broadcasts IGMP Query messages to all the interfaces (including the router ports) in a VLAN. This may result in reelection of the IGMP querier. To prevent such reelection if IGMP is enabled on the upstream device, run this command to disable forwarding of IGMP Query messages to router ports.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```