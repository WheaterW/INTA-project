Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **mvpn** **all** **peer** [ [ *ipv4-address* ] **verbose** ] command to check BGP MVPN peer relationship information.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) { **vpn-instance** *vpn-instance-name* | **all-instance** } **ipmsi** [ **verbose** [ *grpAddr* | **srcAddr** ] \* ] command to check I-PMSI tunnel information of a specified VPN instance, or those of all VPN instances.
* Run the [**display pim**](cmdqueryname=display+pim) { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** command to check the PIM routing entries of a specified VPN instance, or those of all VPN instances.