Enabling IS-IS Auto FRR
=======================

Enabling IS-IS Auto FRR

#### Prerequisites

Before enabling IS-IS auto FRR, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0012.html).

#### Context

With the development of networks, voice over IP (VoIP) and on-line video services pose higher requirements for real-time transmission. If an IS-IS fault occurs, multiple processes must be performed before traffic is switched to a new link. Such processes include fault detection, LSP update, LSP flooding, route calculation, and FIB entry generation. As a result, the fault recovery time is much longer than 50 ms and cannot meet the requirement for real-time transmission.

With IS-IS auto FRR, devices can rapidly switch traffic from a faulty link to a backup link, which prevents traffic interruptions and in turn significantly improves IS-IS network reliability.

IS-IS auto FRR is suitable for IP services that are sensitive to delay and packet loss.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   ```
3. Enter the IS-IS FRR view.
   
   
   ```
   [frr](cmdqueryname=frr)
   ```
   
   By default, FRR is not enabled.
4. Enable IS-IS auto FRR to generate loop-free backup links.
   
   
   ```
   [loop-free-alternate](cmdqueryname=loop-free-alternate) [ level-1 | level-2 | level-1-2 ]
   ```
   
   
   
   If no IS-IS level is specified, IS-IS auto FRR is enabled for both Level-1 and Level-2.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   IS-IS can generate loop-free backup links only if the traffic protection inequality of IS-IS auto FRR is met.
5. (Optional) Use a route-policy to filter backup routes so that only the matching backup routes are added to the routing table.
   
   
   ```
   [frr-policy route](cmdqueryname=frr-policy+route) route-policy route-policy-name
   ```
   
   By default, all computed IS-IS backup routes are added to the routing table, consuming a large number of memory resources and complicating network optimization. To address this problem, use a route-policy so that the device adds only the matching backup routes to the routing table.
6. (Optional) Configure a solution for selecting a backup path for IS-IS auto FRR.
   
   
   ```
   [tiebreaker](cmdqueryname=tiebreaker) { node-protecting | lowest-cost | hold-max-cost | non-ecmp } preference preference [ level-1 | level-2 | level-1-2 ]
   ```
   
   By default, the solution of selecting a backup path for IS-IS auto FRR is node-protection path first.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis**](cmdqueryname=display+isis) *process-id* **route** [ **level-1** | **level-2** ] command to check information about the primary and backup links after IS-IS auto FRR is enabled.
* Run the [**display isis spf-tree**](cmdqueryname=display+isis+spf-tree) [ [ **level-1** | **level-2** ] | **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check the traffic protection type of IS-IS auto FRR.
* Run the [**display isis frr summary**](cmdqueryname=display+isis+frr+summary) command to check the FRR coverages of routes with different convergence priorities in an IS-IS process.