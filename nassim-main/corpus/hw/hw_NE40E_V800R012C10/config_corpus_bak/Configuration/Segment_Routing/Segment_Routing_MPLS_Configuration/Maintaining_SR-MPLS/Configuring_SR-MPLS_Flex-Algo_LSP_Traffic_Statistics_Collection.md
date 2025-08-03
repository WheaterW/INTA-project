Configuring SR-MPLS Flex-Algo LSP Traffic Statistics Collection
===============================================================

This section describes how to configure SR-MPLS Flex-Algo LSP traffic statistics collection.

#### Context

Traffic statistics collection for an SR-MPLS Flex-Algo LSP helps you collect statistics about the traffic forwarded through the SR-MPLS Flex-Algo LSP.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**segment-routing**](cmdqueryname=segment-routing) command to enter the Segment Routing view.
3. Run the [**traffic-statistics flex-algo exclude**](cmdqueryname=traffic-statistics+flex-algo+exclude) { *flex-algo-begin* [ **to** *flex-algo-end* ] } &<1-10> command to enable traffic statistics collection for a specified SR-MPLS Flex-Algo LSP.
   
   
   
   By default, traffic statistics collection is enabled for all SR-MPLS Flex-Algo LSPs. You can use *flex-algo-begin* [ **to** *flex-algo-end* ] to exclude some Flex-Algo LSPs that do not require traffic statistics collection.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring SR-MPLS Flex-Algo LSP traffic statistics collection, verify the configuration.

* Run the [**display segment-routing traffic-statistics**](cmdqueryname=display+segment-routing+traffic-statistics) [ *ip-address* *mask-length* ] [ **flex-algo** [ *flexAlgoId* ] ] [ **verbose** ] command to check SR-MPLS BE traffic statistics.


#### Follow-up Procedure

To clear SR-MPLS Flex-Algo LSP traffic statistics before re-collection, run the [**reset segment-routing traffic-statistics**](cmdqueryname=reset+segment-routing+traffic-statistics) [ *ip-address* *mask-length* ] **flex-algo** [ *flexAlgoId* ] command.