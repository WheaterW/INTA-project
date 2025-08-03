Setting the Convergence Priority for OSPF Routes
================================================

Setting the Convergence Priority for OSPF Routes

#### Prerequisites

Before setting the convergence priority for OSPF routes, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

LSA flooding, LSDB synchronization, and route calculation can be implemented based on a convergence priority set for OSPF routes to help adjust the route convergence speed. If an LSA has multiple convergence priorities, the highest priority takes effect.

OSPF calculates LSAs in the sequence of intra-area routes, inter-area routes, and AS external routes. If convergence priorities are set for these three types of routes, OSPF calculates the different types of routes separately. The convergence priorities in the descending order are as follows: Critical > High > Medium > Low. In addition, to ensure that LSAs with a higher convergence priority are processed first, OSPF places LSAs into the critical, high, medium, and low queues based on convergence priorities during LSA flooding.

By default, the convergence priorities of public OSPF host routes, direct routes, static routes, and other protocol (such as BGP and RIP) routes are **medium**, **high**, **medium**, and **low**, respectively. On the public network, the convergence priority of OSPF 32-bit host routes is **medium**.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IP prefix list.
   
   
   ```
   [ip ip-prefix](cmdqueryname=ip+ip-prefix) ip-prefix-name [ index index-number ] { permit | deny } ipv4-address mask-length [ match-network ] [ greater-equal greater-equal-value ] [ less-equal less-equal-value ]
   ```
3. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
4. Set a convergence priority for the OSPF routes that match the specified IP prefix list.
   
   
   ```
   [prefix-priority](cmdqueryname=prefix-priority) { critical | high | medium } ip-prefix ip-prefix-name
   ```
   
   This command sets a convergence priority for the OSPF routes matching the specified IP prefix list. The configuration takes effect on the public network only.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** *ip-address* [ *mask* | *mask-length* ] command to check information about a specified OSPF route. The command output shows the priority of the specified OSPF route.