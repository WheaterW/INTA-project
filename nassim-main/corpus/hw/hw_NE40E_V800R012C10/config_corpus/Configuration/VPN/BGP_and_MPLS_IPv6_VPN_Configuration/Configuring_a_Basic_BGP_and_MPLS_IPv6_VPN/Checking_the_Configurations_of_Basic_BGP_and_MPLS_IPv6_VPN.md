Checking the Configurations of Basic BGP/MPLS IPv6 VPN
======================================================

After configuring a basic BGP/MPLS IPv6 VPN, check information about the VPN instance IPv6 address family created on the PE, including the RD and other attributes and also information about the IPv6 VPN routes to the local and remote sites on the PE and CE.

#### Prerequisites

A basic BGP/MPLS IPv6 VPN has been configured.


#### Procedure

* Run the following commands on the PE to check information about the created VPN instance IPv6 address family, including the RD and other attributes.
  
  
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) *vpn-instance-name* command to check brief information about a specified VPN instance.
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** *vpn-instance-name* command to check detailed information about a specified VPN instance, including information in the IPv4 and IPv6 address families enabled for the VPN instance.
  + Run the [**display ip vpn-instance import-vt**](cmdqueryname=display+ip+vpn-instance+import-vt) *ivt-value* command to check information about the VPN instances with the specified import VPN target.
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) [ *vpn-instance-name* ] **interface** command to view information about the interface bound to a specified VPN instance.
  + Run the [**display bgp vpnv6 all peer**](cmdqueryname=display+bgp+vpnv6+peer) command to check information about all BGP VPNv6 peers.
* Run the following commands on the PE and CE to check information about the IPv6 VPN routes to the local and remote sites:
  
  
  + Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on the PE to check the routing information of a specified VPN instance IPv6 address family.
  + Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command on the CE to check routing information.