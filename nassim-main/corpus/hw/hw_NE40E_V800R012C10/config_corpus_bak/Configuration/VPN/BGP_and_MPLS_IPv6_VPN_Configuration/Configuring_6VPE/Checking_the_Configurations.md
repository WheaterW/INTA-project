Checking the Configurations
===========================

After 6VPE is configured on a PE, check that the PE successfully establishes a BGP IPv4 peer relationship with the CE in the VPN instance IPv6 address family.

#### Prerequisites

All 6VPE configurations are complete.


#### Procedure

* Run the following commands on a PE to view information about the created BGP VPN instance IPv6 address family, including the RD and other attributes.
  
  
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) *vpn-instance-name* command to check brief information about a specified VPN instance.
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** *vpn-instance-name* command to check detailed information about a specified VPN instance, including information about the VPN instance IPv4 address family and IPv6 address family.
  + Run the [**display ip vpn-instance import-vt**](cmdqueryname=display+ip+vpn-instance+import-vt) *ivt-value* command to check information about VPN instances with a specified import VPN target.
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) [ *vpn-instance-name* ] **interface** command to check information about the interface bound to a specified VPN instance.
* Run the following command on a PE to check the BGP IPv4 peer relationship established with a CE in the VPN instance IPv6 address family.
  
  
  + Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **vpn-instance** *vpn-instance-name* **peer** *ipv4-address* **verbose** command on the PE to check the BGP IPv4 peer relationship between the PE and CE in the VPN instance IPv6 address family.