Enabling IPv6 IS-IS Auto FRR
============================

Enabling IPv6 IS-IS Auto FRR

#### Prerequisites

Before configuring IPv6 IS-IS auto FRR, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0012.html).

#### Context

With IPv6 IS-IS auto FRR, devices can rapidly switch traffic from a faulty link to a backup link, which prevents traffic interruptions and in turn significantly improves IPv6 IS-IS network reliability.

IPv6 IS-IS auto FRR is suitable for services that are sensitive to delay and packet loss.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   ```
3. Enable IPv6 FRR and enter the IPv6 IS-IS FRR view.
   
   
   ```
   [ipv6 frr](cmdqueryname=ipv6+frr)
   ```
   
   By default, IPv6 FRR is not enabled.
4. Enable IPv6 IS-IS auto FRR to generate loop-free backup links.
   
   
   ```
   [loop-free-alternate](cmdqueryname=loop-free-alternate) [ level-1 | level-2 | level-1-2 ]
   ```
   
   
   
   If no IS-IS level is specified, IPv6 IS-IS auto FRR is enabled for both Level-1 and Level-2.
5. (Optional) Use a route-policy to filter backup routes so that only the matching backup routes are added to the routing table.
   
   
   ```
   [frr-policy route](cmdqueryname=frr-policy+route) route-policy route-policy-name
   ```
   
   By default, all computed IS-IS backup routes are added to the routing table, consuming a large number of memory resources and complicating network optimization. To address this problem, use a route-policy so that the device adds only the matching backup routes to the routing table.
6. (Optional) Configure a solution for selecting a backup path for IPv6 IS-IS auto FRR.
   
   
   ```
   [tiebreaker](cmdqueryname=tiebreaker) { node-protecting | lowest-cost | hold-max-cost | non-ecmp } preference preference [ level-1 | level-2 | level-1-2 ]
   ```
   
   By default, the solution of selecting a backup path for IPv6 IS-IS auto FRR is node-protection path first.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display isis route**](cmdqueryname=display+isis+route) [ **level-1** | **level-2** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] **ipv6** [ *ipv6-address* [ *prefix-length* ] ] [ **verbose** ] command to check information about the primary and backup links after IPv6 IS-IS auto FRR is enabled.

Run the [**display isis frr summary**](cmdqueryname=display+isis+frr+summary) command to check the FRR coverages of routes with different convergence priorities in an IS-IS process.