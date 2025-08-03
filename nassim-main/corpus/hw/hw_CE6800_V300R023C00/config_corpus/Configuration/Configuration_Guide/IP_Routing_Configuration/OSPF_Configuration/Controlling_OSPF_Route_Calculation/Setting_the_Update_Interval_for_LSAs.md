Setting the Update Interval for LSAs
====================================

Setting the Update Interval for LSAs

#### Prerequisites

Before setting the update interval for LSAs, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

OSPF sets a 5-second update interval for LSAs. This prevents network connections or frequent route flapping from consuming excessive network bandwidth or device resources. On a stable network that requires fast route convergence, you can alter the interval to 0 seconds. In this manner, LSAs indicating topology or route changes can be advertised immediately, which speeds up route convergence.

On an unstable network, routes are calculated frequently, consuming excessive CPU resources. Additionally, LSAs that describe the unstable topology are generated and transmitted, which, when frequently processed will compromise the rapid and stable operation of the entire network.

To speed up route convergence on the entire network, the OSPF intelligent timer controls LSA generation, LSA reception, and route calculation.

The OSPF intelligent timer works as follows:

* On a network where routes are calculated frequently, the OSPF intelligent timer dynamically adjusts the interval between route calculations based on user configuration and exponential backoff technology. This reduces the route calculation count and CPU resource consumption. Routes are calculated after the network topology becomes stable.
* On an unstable network, if frequent topology changes occur, the OSPF intelligent timer dynamically adjusts the interval for generating or receiving LSAs. In this way, no LSAs are generated and received LSAs are not processed within the interval, reducing the generation and flooding of invalid LSAs on the entire network.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Set the update interval for LSAs.
   
   
   ```
   [lsa-originate-interval](cmdqueryname=lsa-originate-interval) { 0 | intelligent-timer max-interval start-interval hold-interval [ other-type interval ] | other-type interval [ intelligent-timer max-interval start-interval hold-interval ] }
   ```
   
   Parameters in this command are described as follows:
   
   * **intelligent-timer**: uses the intelligent timer to set the update interval for Type 1 LSAs (router LSAs) and Type 2 LSAs (network LSAs).
   * *max-interval*: specifies the maximum interval at which OSPF LSAs are updated, in milliseconds.
   * *start-interval*: specifies the initial interval at which OSPF LSAs are updated, in milliseconds.
   * *hold-interval*: specifies the hold interval at which OSPF LSAs are updated, in milliseconds.
   * **other-type**: sets the update interval for Type 3 LSAs (Network-Summary-LSAs), Type 4 LSAs (ASBR-Summary-LSAs), and Type 10 LSAs (opaque LSAs).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```