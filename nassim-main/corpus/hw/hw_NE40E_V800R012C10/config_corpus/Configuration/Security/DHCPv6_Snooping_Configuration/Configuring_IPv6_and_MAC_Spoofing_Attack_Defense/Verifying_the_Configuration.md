Verifying the Configuration
===========================

After configuring IPv6/MAC spoofing attack defense, you can view statistics about discarded IPv6 and DHCPv6 packets and the binding relationships between interface names, MAC addresses, and IPv6 addresses in the DHCPv6 snooping binding table.

#### Prerequisites

IPv6/MAC spoofing attack defense has been configured.


#### Procedure

* Run the [**display dhcpv6 snooping bind-table**](cmdqueryname=display+dhcpv6+snooping+bind-table) { **interface** { *interface-type* *interface-num* | *interface-name* } | **ipv6-address** *ipv6-address* | **ipv6-prefix** *ipv6-prefix-mask* | **mac-address** *mac-address* | **vpn-instance** *vpn-name* | **static** | **dynamic** | **all** } command to check information about the DHCPv6 snooping binding table.
* Run the [**display dhcpv6 snooping interface**](cmdqueryname=display+dhcpv6+snooping+interface) { *interface-name* | *interface-type* *interface-num* } command to check the running information about the DHCPv6 snooping function.
* Run the **[**display dhcpv6 snooping statistics**](cmdqueryname=display+dhcpv6+snooping+statistics)** command to check statistics about the DHCPv6 packets sent and received after the DHCPv6 snooping function is enabled.