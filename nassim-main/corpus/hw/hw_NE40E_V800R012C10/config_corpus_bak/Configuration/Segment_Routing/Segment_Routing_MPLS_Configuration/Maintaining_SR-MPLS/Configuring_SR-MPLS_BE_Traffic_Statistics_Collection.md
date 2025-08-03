Configuring SR-MPLS BE Traffic Statistics Collection
====================================================

This section describes how to configure SR LSP (that is, SR-MPLS BE tunnel) traffic statistics collection.

#### Context

The SR-MPLS BE traffic statistics collection function helps you collect statistics about traffic forwarded by an SR-MPLS BE tunnel.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**segment-routing**](cmdqueryname=segment-routing) command to enter the Segment Routing view.
3. Run the [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable) **host** [ **ip-prefix** *ip-prefix-name* ] command to enable SR-MPLS BE traffic statistics collection.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring SR-MPLS BE traffic statistics collection, verify the configuration.

* Run the [**display segment-routing traffic-statistics**](cmdqueryname=display+segment-routing+traffic-statistics) [ *ip-address* *mask-length* ] [ **verbose** ] command to check SR-MPLS BE traffic statistics.


#### Follow-up Procedure

To clear traffic statistics before re-collection, run the [**reset segment-routing traffic-statistics**](cmdqueryname=reset+segment-routing+traffic-statistics) [ *ip-address* *mask-length* ] command.