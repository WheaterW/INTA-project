Configuring RA Attributes
=========================

Configuring RA Attributes

#### Context

* An RA message can carry parameters, such as the maximum number of hops, prefix, neighbor reachable time, and lifetime of the RA message.
* If a host is connected to multiple devices, it must select a device to forward packets based on their destination addresses. In this case, the devices can advertise the default router preference and specified route information to the host, allowing the host to select a proper forwarding device based on the packets' destination addresses.
  
  After receiving the RA messages carrying the route information, the host updates its routing table. When sending packets to another device, the host queries the routing table and selects a proper route to send packets.
  
  When receiving the RA messages that carry the default router preference, the host updates its routing table. Then, when sending packets to another device, if there is no route to be selected, the host queries the routing table. After this, the host selects a device with the highest preference on the local link to send packets. If the device is faulty, the host selects another device according to a descending order of preference.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the maximum number of hops for RA messages.
   
   
   ```
   [ipv6 nd hop-limit](cmdqueryname=ipv6+nd+hop-limit) limit
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
5. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
6. Configure RA attributes.
   
   
   
   **Table 1** Configuring RA attributes
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the maximum number of hops for RA messages. | [**ipv6 nd ra hop-limit**](cmdqueryname=ipv6+nd+ra+hop-limit) *limit* | *limit* specifies the maximum number of hops that RA messages (IPv6 unicast packets sent by a host) pass through. |
   | Configure the device not to carry the default address prefix generated based on the interface IPv6 address in an RA message. | [**ipv6 nd ra prefix**](cmdqueryname=ipv6+nd+ra+prefix) **default** **no-advertise** | The prefix configured using the command cannot be fe80:: (prefix of a link-local address), ff00:: (prefix of a multicast address), or prefix of an unspecified address. It also cannot be the prefix that has been used by another interface (including the interface address prefix and prefix carried in RA messages). |
   | Configure a prefix to be carried in RA messages. | [**ipv6 nd ra prefix**](cmdqueryname=ipv6+nd+ra+prefix) *ipv6-address* *prefix-length* *valid-lifetime* *preferred-lifetime* [ **no-autoconfig** ] [ **off-link** ] | The address prefix configured using the [**ipv6 nd ra prefix**](cmdqueryname=ipv6+nd+ra+prefix) command has a higher priority than the default address prefix. Considering that an RA message carries a maximum of 17 address prefixes, the default address prefix will not be carried in an RA message to be advertised if 17 address prefixes have been configured.  If stateless address autoconfiguration is used, you must specify the prefix length as 64. If not specified, the address does not take effect, and RA messages will be discarded. |
   | Configure the managed address configuration flag of stateful address autoconfiguration in an RA message. | [**ipv6 nd autoconfig managed-address-flag**](cmdqueryname=ipv6+nd+autoconfig+managed-address-flag) | If the managed address configuration flag is configured, a host obtains an IPv6 address through stateful address autoconfiguration. |
   | Configure the other configuration flag of stateful address autoconfiguration in an RA message. | [**ipv6 nd autoconfig other-flag**](cmdqueryname=ipv6+nd+autoconfig+other-flag) | If the managed address configuration flag is set to 1 in an RA message, the other configuration flag must also be set to 1. |
   | Configure a neighbor reachable time. | [**ipv6 nd nud reachable-time**](cmdqueryname=ipv6+nd+nud+reachable-time) *value* | Each RA message sent by a router carries the neighbor reachable time so that all the nodes along the same link can use the same time. |
   | Configure a lifetime for RA messages. | [**ipv6 nd ra router-lifetime**](cmdqueryname=ipv6+nd+ra+router-lifetime) *ra-lifetime* | An RA message advertisement interval must be less than or equal to an RA message lifetime. |
   | Configure the device not to carry the MTU option in RA messages. | [**ipv6 nd ra advertised-mtu disable**](cmdqueryname=ipv6+nd+ra+advertised-mtu+disable) | By default, the MTU value contained in RA messages is the same as that configured using the [**ipv6 mtu**](cmdqueryname=ipv6+mtu) command. If the [**ipv6 mtu**](cmdqueryname=ipv6+mtu) command has not been run to configure the MTU option, the default interface MTU is used. To disable the device from carrying the MTU option in RA messages to be sent, run the [**ipv6 nd ra advertised-mtu disable**](cmdqueryname=ipv6+nd+ra+advertised-mtu+disable) command. |
   | Configure RA message advertisement intervals. | [**ipv6 nd ra**](cmdqueryname=ipv6+nd+ra) { **max-interval** *maximum-interval* | **min-interval** *minimum-interval* } | The maximum interval cannot be shorter than 4/3 of the minimum interval. |
   | Configure a default router preference for RA messages. | [**ipv6 nd ra preference**](cmdqueryname=ipv6+nd+ra+preference) { **high** | **medium** | **low** } | The default router preference of RA messages is medium. |
   | Configure route information for RA messages. | [**ipv6 nd ra route-information**](cmdqueryname=ipv6+nd+ra+route-information) *ipv6-address* *prefix-length* **lifetime** *route-lifetime* [ **preference** { **high** | **medium** | **low** } ] | An RA message includes route information. The device sends the specified routes to the hosts on the local network segment by using this information. The hosts can send packets by using these routes. |
   | Configure an address or lifetime for the RDNSS option carried in an RA message. | [**ipv6 nd ra dns-server**](cmdqueryname=ipv6+nd+ra+dns-server) *ipv6-address* [ *lifetime* ] | In ND address autoconfiguration scenarios, if a DNS server address changes, hosts cannot promptly detect the change. As a result, DNS resolution fails and services that rely on DNS cannot be used. To resolve this issue, configure a DNS server address on a routing device. After the configuration is complete, the device periodically advertises the DNS server address in RA messages. Upon receipt of such messages, hosts can obtain the latest available DNS server address and use the DNS service accurately. |
   | Configure a domain name suffix or lifetime for the DNSSL option carried in an RA message. | [**ipv6 nd ra dns-suffix**](cmdqueryname=ipv6+nd+ra+dns-suffix) *domain* [ *lifetime* ] | In ND address autoconfiguration scenarios, it is difficult to memorize a complete DNS domain name. To facilitate memorization and improve work efficiency, configure a DNS domain name suffix on a routing device. After the configuration is complete, the device periodically advertises the configured DNS domain name suffix in RA messages. Upon receipt of such messages, hosts obtain the DNS domain name suffix and append it to the hostname to form a complete domain name for DNS domain name resolution. |
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface) [ *interface-type* *interface-number* | **brief** ] command to check RA configurations.