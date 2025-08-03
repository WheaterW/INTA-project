Configuring Route Reflection for BGP VPNv4 Routes
=================================================

The prerequisite for enabling BGP VPNv4 route reflection is that the RR has established MP-IBGP peer relationships with all client PEs.

#### Context

For detailed configurations about an RR, see "BGP Configuration" in *NE40E Configuration Guide - IP Routing*.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** command to enter the BGP VPNv4 address family view.
4. Run the [**peer**](cmdqueryname=peer) { *peer-ipv4-address* | *group-name* } **reflect-client** command to configure the local device as an RR and the peer (or peer group) as a client of the RR.
5. (Optional) Run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable RR-based route reflection among clients if the clients are fully connected.
6. Run the [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target) command to disable VPN target-based VPNv4 route filtering.
7. (Optional) Run the [**rr-filter**](cmdqueryname=rr-filter) *extcomm-filter-name* command to configure a reflection policy for the RR, so that it reflects only IBGP routes with matching VPN targets. This configuration allows load balancing among RRs.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.