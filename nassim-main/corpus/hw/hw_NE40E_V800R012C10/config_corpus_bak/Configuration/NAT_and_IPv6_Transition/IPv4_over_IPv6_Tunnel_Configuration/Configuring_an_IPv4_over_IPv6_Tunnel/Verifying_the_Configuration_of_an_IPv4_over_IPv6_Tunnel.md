Verifying the Configuration of an IPv4 over IPv6 Tunnel
=======================================================

After configuring an IPv4 over IPv6 tunnel, you can check the status of the tunnel interfaces and routing information.

#### Prerequisites

All configurations of an IPv4 over IPv6 tunnel are complete.


#### Procedure

* Run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) [ *interface-number* ] command to check the status of tunnel interfaces.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check IPv6 routing table information.
* Run the [**ping**](cmdqueryname=ping) { **-a** *source-ip-address* *dest-ip-address* | **-vpn-instance** *vpn-instance-name* } command to check whether the two ends of the tunnel are reachable.