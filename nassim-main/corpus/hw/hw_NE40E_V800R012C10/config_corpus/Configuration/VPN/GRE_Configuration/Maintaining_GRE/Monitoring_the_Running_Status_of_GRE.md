Monitoring the Running Status of GRE
====================================

In routine maintenance, you can run the GRE related display commands to view the GRE running status.

#### Procedure

* Run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) [ *interface-number* ] command to check the tunnel interface running status.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VPN routing table on the PE.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the routing table on the CE.
* Run the [**ping**](cmdqueryname=ping) **-a** *source-ip-address* [ **-vpn-instance** *vpn-instance-name* ] *dest-ip-address* command to check whether the two ends of a tunnel can communicate with each other.
* Run the [**display keepalive packets count**](cmdqueryname=display+keepalive+packets+count) command to check the numbers of Keepalive messages and Keepalive response messages sent and received by a GRE tunnel interface.