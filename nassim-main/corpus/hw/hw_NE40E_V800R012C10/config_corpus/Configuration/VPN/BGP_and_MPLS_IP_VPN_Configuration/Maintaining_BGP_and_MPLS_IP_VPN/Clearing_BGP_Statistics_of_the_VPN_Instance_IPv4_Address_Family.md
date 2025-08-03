Clearing BGP Statistics of the VPN Instance IPv4 Address Family
===============================================================

The BGP statistics of the VPN instance IPv4 address
family cannot be restored after being cleared. Exercise caution
when clearing the statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The BGP statistics of the VPN
instance IPv4 address family cannot be restored after being cleared.
Exercise caution when clearing the statistics.



#### Procedure

* To clear the statistics about BGP peer flapping from the
  specified VPN instance IPv4 address family, run the [**reset bgp**](cmdqueryname=reset+bgp) **vpn-instance** *vpn-instance-name* **ipv4-family** [ *peer-address* ] **flap-info** command in the user view.
* To clear the statistics about route dampening from the
  specified VPN instance IPv4 address family, run the [**reset bgp**](cmdqueryname=reset+bgp) **vpn-instance** *vpn-instance-name* **ipv4-family** **dampening** [ *ip-address* [ *mask* | *mask-length* ] ] command in the user view.