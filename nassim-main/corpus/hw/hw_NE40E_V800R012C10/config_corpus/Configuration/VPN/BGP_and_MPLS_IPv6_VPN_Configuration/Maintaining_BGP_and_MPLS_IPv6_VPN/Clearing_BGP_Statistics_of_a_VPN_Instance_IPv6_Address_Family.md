Clearing BGP Statistics of a VPN Instance IPv6 Address Family
=============================================================

BGP statistics of the VPN instance IPv6 address family cannot be restored after being cleared. Exercise caution when clearing the statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

BGP statistics of the VPN instance IPv6 address family cannot be restored after being cleared. Exercise caution when clearing the statistics.



#### Procedure

* Run the [**reset bgp**](cmdqueryname=reset+bgp) **vpn-instance** *vpn-instance-name* **ipv6-family** [ *ipv6-address* ] **flap-info** command in the user view to clear the statistics about BGP peer flapping from the specified VPN instance IPv6 address family.
* Run the [**reset bgp**](cmdqueryname=reset+bgp) **vpn-instance** *vpn-instance-name* **ipv6-family** **dampening** [ *ipv6-address* *mask-length* ] command in the user view to clear the statistics about route dampening from the specified VPN instance IPv6 address family.