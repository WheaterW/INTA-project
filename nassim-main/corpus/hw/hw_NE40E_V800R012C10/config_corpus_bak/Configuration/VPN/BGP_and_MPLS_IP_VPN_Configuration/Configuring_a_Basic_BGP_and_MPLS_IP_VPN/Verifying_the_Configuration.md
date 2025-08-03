Verifying the Configuration
===========================

After configuring a basic BGP/MPLS IP VPN, check information about the VPN instance IPv4 address family created on the PE, including the RD and other attributes. You can also check information about IPv4 VPN routes to the local and remote sites on the PE and CE.

#### Prerequisites

All configurations for the basic BGP/MPLS IP VPN are complete.


#### Procedure

* Run the following commands on the PE to check information about the created VPN instance IPv4 address family, including the RD and other attributes.
  
  
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) *vpn-instance-name* command to check brief information about the specified VPN instance.
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** *vpn-instance-name* command to check detailed information about the specified VPN instance, including information about the VPN instance IPv4 address family and IPv6 address family.
  + Run the [**display ip vpn-instance import-vt**](cmdqueryname=display+ip+vpn-instance+import-vt) *ivt-value* command to check information about VPN instances with the specified import VPN target.
  + Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) [ *vpn-instance-name* ] **interface** command to check information about the interface bound to the specified VPN instance.
  + Run the [**display mpls label-stack**](cmdqueryname=display+mpls+label-stack) **vpn-instance** *vpn-instance-name* *ip-address* command to check L3VPN label stack information.
  + Run the [**display mpls label-stack**](cmdqueryname=display+mpls+label-stack) **bgp-lsp** *ip-address* command to check BGP LSP label stack information.
* Run the following commands on the PE and CE to check information about IPv4 VPN routes to the local and remote sites.
  
  
  + Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command on the PE to check route information about the specified VPN instance IPv4 address family.
  + Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on the CE to check route information.