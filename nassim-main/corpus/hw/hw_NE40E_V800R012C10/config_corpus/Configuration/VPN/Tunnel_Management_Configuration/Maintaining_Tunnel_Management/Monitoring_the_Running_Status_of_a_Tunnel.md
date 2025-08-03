Monitoring the Running Status of a Tunnel
=========================================

To determine whether a VPN tunnel has been established and the configurations of an established tunnel, monitor the running status of the VPN tunnel.

#### Context

In routine maintenance, run the following commands in any view to learn tunnel running information.


#### Procedure

* Run the [**display interface**](cmdqueryname=display+interface) **tunnel** *interface-number* command to check tunnel interface information.
* Run the [**display tunnel-info**](cmdqueryname=display+tunnel-info) **all** command to check tunnel information.
* Run the [**display tunnel-info**](cmdqueryname=display+tunnel-info) *tunnel-id* command to check tunnel details.
* Run the [**display tunnel-policy**](cmdqueryname=display+tunnel-policy) *policy-name* command to check the configurations of a specified tunnel policy.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** [ *vpn-instance-name* ] command to check the tunnel policy applied to the specified VPN instance.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) [ *ip-address* ] **verbose** command or the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] **verbose** command to check the tunnel used by VPN routing.