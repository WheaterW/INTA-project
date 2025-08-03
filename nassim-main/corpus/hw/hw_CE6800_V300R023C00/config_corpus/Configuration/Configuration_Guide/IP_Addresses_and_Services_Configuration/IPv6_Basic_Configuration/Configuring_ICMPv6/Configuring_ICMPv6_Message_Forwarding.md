Configuring ICMPv6 Message Forwarding
=====================================

Configuring ICMPv6 Message Forwarding

#### Prerequisites

Before configuring ICMPv6 message forwarding, you have completed the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is up.
* Configure IPv6 addresses for interfaces.

#### Context

Under normal circumstances, a device can send and receive ICMPv6 messages properly. However, when network traffic is heavy, host unreachable or port unreachable events frequently occur, leading to a surge in ICMPv6 messages, which burdens the network and degrades device performance. In addition, attackers usually use ICMPv6 error messages to probe the internal network topology.

To reduce a device's pressure in processing ICMPv6 messages and prevent ICMPv6 message attacks, configure the device to control the sending or receiving of ICMPv6 messages.

The device supports the configuration of ICMPv6 message forwarding based on an ICMPv6 name or specified type and code. [Table 1](#EN-US_TASK_0000001176741615__table109773913198) lists the supported ICMPv6 names. For details about the ICMPv6 messages corresponding to the types and codes, see [Understanding ICMPv6](vrp_ipv6_cfg_0020.html).

**Table 1** ICMPv6 names that can be configured in the system view
| Value of *icmpv6-name* | Type | Code | Description |
| --- | --- | --- | --- |
| echo | 128 | 0 | Echo Request |
| echo-reply | 129 | 0 | Echo Reply |
| err-header-field | 4 | 0 | Erroneous header field encountered |
| frag-time-exceeded | 3 | 1 | Fragment reassembly time exceeded |
| hop-limit-exceeded | 3 | 0 | Hop limit exceeded in transit |
| host-admin-prohib | 1 | 1 | Communication with destination administratively prohibited |
| host-unreachable | 1 | 3 | Address unreachable |
| multicast-listener-done | 132 | 0 | Multicast Listener Done |
| multicast-listener-query | 130 | 0 | Multicast Listener Query |
| multicast-listener-report | 131 | 0 | Multicast Listener Report |
| multicast-listener-report-v2 | 143 | 0 | Version 2 Multicast Listener Report |
| neighbor-advertisement | 136 | 0 | Neighbor Advertisement |
| neighbor-solicitation | 135 | 0 | Neighbor Solicitation |
| network-unreachable | 1 | 0 | No route to destination |
| packet-too-big | 2 | 0 | Packet Too Big |
| port-unreachable | 1 | 4 | Port unreachable |
| redirect | 137 | 0 | Redirect |
| router-advertisement | 134 | 0 | Router Advertisement |
| router-solicitation | 133 | 0 | Router Solicitation |
| unknown-ipv6-opt | 4 | 2 | Unrecognized IPv6 option encountered |
| unknown-next-hdr | 4 | 1 | Unrecognized Next Header type encountered |



#### Procedure

* Configure ICMPv6 message forwarding in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Disable the device from sending or receiving ICMPv6 messages as required.
     
     
     + Disable the device from sending ICMPv6 messages.
       ```
       [ipv6 icmp](cmdqueryname=ipv6+icmp+all-famous+send+disable) { icmpv6Type icmpv6Code | all-famous } send disable
       ```
     + Disable the device from receiving ICMPv6 messages.
       ```
       [ipv6 icmp](cmdqueryname=ipv6+icmp+all-famous+receive+disable) { icmpv6Type icmpv6Code | all-famous } receive disable
       ```
     + Disable the device from responding to received ICMPv6 multicast Echo messages.
       ```
       [ipv6 icmp multicast-address echo receive disable](cmdqueryname=ipv6+icmp+multicast-address+echo+receive+disable)
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure ICMPv6 message forwarding in the interface view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Enable IPv6.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  5. Disable the device from sending ICMPv6 messages on the interface.
     
     
     + Disable the device from sending ICMPv6 Hop Limit Exceeded messages on the interface.
       ```
       [ipv6 icmp hop-limit-exceeded send disable](cmdqueryname=ipv6+icmp+hop-limit-exceeded+send+disable)
       ```
     + Disable the device from sending ICMPv6 Host Unreachable messages on the interface.
       ```
       [ipv6 icmp host-unreachable send disable](cmdqueryname=ipv6+icmp+host-unreachable+send+disable)
       ```
     + Disable the device from sending ICMPv6 Port Unreachable messages on the interface.
       ```
       [ipv6 icmp port-unreachable send disable](cmdqueryname=ipv6+icmp+port-unreachable+send+disable)
       ```
     + Disable the device from responding to received ICMPv6 multicast Echo messages.
       ```
       [ipv6 icmp multicast-address echo receive disable](cmdqueryname=ipv6+icmp+multicast-address+echo+receive+disable)
       ```
  6. Exit the interface view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```