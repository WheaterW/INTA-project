Verifying the Configuration
===========================

After configuring BGP4+ 6PE, check whether CEs can learn routes to each other.

#### Procedure

1. Run the [**display bgp**](cmdqueryname=display+bgp+ipv6+peer) **ipv6 peer** command on each PE to check the BGP peer relationship status.
2. Run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session+vpn-instance+verbose) **vpn-instance** *vpn-instance-name* [ *peer-id* | **verbose** ] command on PEs to check the status of the LDP session between the PEs.
3. Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* *prefix-length* command on each PE or the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table+longer-match+verbose) *ipv6-address* *prefix-length* [ **longer-match** ] [ **verbose** ] command on each CE to check the routes destined for the remote IPv6 network.