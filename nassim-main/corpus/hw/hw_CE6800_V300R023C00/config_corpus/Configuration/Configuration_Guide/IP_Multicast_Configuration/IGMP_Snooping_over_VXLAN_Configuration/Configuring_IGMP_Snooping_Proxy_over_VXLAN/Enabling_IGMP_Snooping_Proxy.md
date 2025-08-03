Enabling IGMP Snooping Proxy
============================

Enabling IGMP Snooping Proxy

#### Context

When IGMP is disabled on Layer 3 devices (for example, when only a static multicast group is configured), no IGMP querier is available on the network to maintain multicast group memberships. In this case, you can configure IGMP snooping proxy on the Layer 2 device so that it functions as an IGMP querier and sends IGMP Query messages. Conversely, when IGMP is enabled on the network, you can also configure IGMP snooping proxy on a Layer 2 device. In this case, the device sends IGMP Report/Leave messages to its upstream Layer 3 device on behalf of user hosts. This helps reduce the number of such messages sent to the Layer 3 device.

A device configured with IGMP snooping proxy acts as a host for its upstream devices and as a querier for its downstream hosts.

![](public_sys-resources/note_3.0-en-us.png) 

IGMP snooping proxy involves two functions: querier and message suppression. The two functions can be both enabled in a BD to implement the same functionality as IGMP snooping proxy. In other words, if IGMP snooping proxy has been configured, you do not need to configure the querier or message suppression function. For details about how to configure the querier and message suppression functions, see [Configuring IGMP Snooping Querier](vrp_l2mc_over_vxlan_cfg_0024.html) and [(Optional) Configuring Report/Leave Message Suppression](vrp_l2mc_over_vxlan_cfg_0011.html), respectively.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Enable IGMP snooping proxy.
   
   
   ```
   [igmp snooping proxy](cmdqueryname=igmp+snooping+proxy)
   ```
4. (Optional) Configure the device to transparently transmit protocol messages in the BD.
   
   
   ```
   [igmp snooping proxy router-protocol-pass](cmdqueryname=igmp+snooping+proxy+router-protocol-pass)
   ```
   
   
   
   By default, an IGMP snooping proxy device does not transparently transmit received protocol messages upstream. Instead, it learns multicast forwarding entries from these messages. If IGMP snooping proxy is enabled on both the upstream and downstream devices, you can run this command so that the device transparently forwards the protocol messages it receives on a router port to other router ports, without learning the entries from the messages. In this way, the upstream and downstream devices do not learn entries from each other, which would otherwise cause entry aging problems.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```