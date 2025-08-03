Clearing the Traffic Statistics of BGP LSPs
===========================================

After BGP LSP traffic statistics collection is configured, you can query and monitor BGP LSP traffic in real time. Unneeded traffic statistics of BGP LSPs can be cleared.

#### Context

By default, the [**reset mpls traffic-statistics bgp**](cmdqueryname=reset+mpls+traffic-statistics+bgp) command clears the traffic statistics of all BGP LSPs. If an IPv4 address and a mask length are specified, the command clears only the traffic statistics of the BGP LSPs whose FEC matches the specified IPv4 address and mask length.


#### Procedure

* Run the [**reset mpls traffic-statistics bgp**](cmdqueryname=reset+mpls+traffic-statistics+bgp) [*ipv4-address* *mask-length*] command to clear the traffic statistics of BGP LSPs.