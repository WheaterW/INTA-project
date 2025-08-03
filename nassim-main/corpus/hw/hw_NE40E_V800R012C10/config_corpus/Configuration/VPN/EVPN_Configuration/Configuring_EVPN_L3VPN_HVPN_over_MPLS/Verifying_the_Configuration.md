Verifying the Configuration
===========================

After configuring EVPN L3VPN HVPN over MPLS, verify the default or specific routes sent from the remote end on the UPE or NPE.

#### Prerequisites

EVPN L3VPN HVPN over MPLS has been configured.


#### Procedure

* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on the UPE or NPE to check the VRF table. The command output shows the default or specific routes sent by the remote end.
* Run the [**display bgp evpn routing-table**](cmdqueryname=display+bgp+evpn+routing-table) command on the EVPN-enabled UPE or NPE. The command output shows the EVPN routes sent by the remote end.