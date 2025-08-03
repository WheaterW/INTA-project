Verifying the Configuration
===========================

After IS-IS SR-MPLS Flex-Algo is configured, you can view associated information.

#### Prerequisites

All IS-IS SR-MPLS Flex-Algo configurations are complete.


#### Procedure

1. Run the [**display isis**](cmdqueryname=display+isis+flex-algo) *process-id* **flex-algo** [ *flex-algo-id* ] [ **level-1** | **level-2** ] command to check the preferred FAD in the LSDB.
2. Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
3. Run the [**display isis**](cmdqueryname=display+isis)*process-id* **route****ipv4** **flex-algo** [ *flex-algo-id* ] [ [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* or [**display isis route**](cmdqueryname=display+isis+route)[ *process-id* ] **ipv4** **flex-algo** [ *flex-algo-id* ] [ [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check Flex-Algo-related IS-IS route information.
4. Run the [**display isis**](cmdqueryname=display+isis)[ *process-id* ] **spf-tree** [ **systemid** *systemid* ] **flex-algo** [ *flex-algo-id* ] [ [ **level-1** | **level-2** ] | **verbose** ] \* command to check the SPF tree topology information of a specified Flex-Algo.
5. Run the [**display segment-routing prefix mpls forwarding**](cmdqueryname=display+segment-routing+prefix+mpls+forwarding) **flex-algo** [ *flexAlgoId* ] [ **ip-prefix** *ip-prefix* *mask-length* | **label** *label* ] [ **verbose** ] command to check the Flex-Algo-based SR label forwarding table.
6. Run the [**display segment-routing state ip-prefix**](cmdqueryname=display+segment-routing+state+ip-prefix)*ip-prefix* *mask-length* **flex-algo** *flexAlgoId* command to check the SR status of a specified Flex-Algo based on a specified IP prefix.