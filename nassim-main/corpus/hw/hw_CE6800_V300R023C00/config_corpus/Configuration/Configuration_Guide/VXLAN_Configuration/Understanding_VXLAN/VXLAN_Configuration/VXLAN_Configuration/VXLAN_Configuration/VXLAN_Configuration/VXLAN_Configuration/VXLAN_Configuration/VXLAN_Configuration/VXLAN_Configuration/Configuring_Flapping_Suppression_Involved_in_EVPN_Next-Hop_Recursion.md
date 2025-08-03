Configuring Flapping Suppression Involved in EVPN Next-Hop Recursion
====================================================================

Configuring Flapping Suppression Involved in EVPN Next-Hop Recursion

#### Prerequisites

Before configuring flapping suppression involved in EVPN next-hop recursion, complete either of the following tasks:

* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1066.html)

#### Context

If a large number of EVPN routes recurse to the same next hop that flaps frequently, the system's workload increases as it needs to process changes of these routes, consuming excessive system resources and leading to high CPU usage. To address this issue, configure flapping suppression involved in EVPN next-hop recursion.

Flapping suppression involved in EVPN next-hop recursion is enabled by default. After flapping suppression involved in EVPN next-hop recursion is enabled, an EVPN device determines whether to increase, retain, or reduce the penalty value by comparing the flapping interval with the configured threshold. When the penalty value exceeds 10, the EVPN device suppresses route recursion flapping. For example, if the intervals for increasing, retaining, and clearing the penalty value are T1, T2, and T3, respectively, the device calculates the penalty value as follows:

* Increases the penalty value by 1 if the flapping interval is less than T1.
* Retains the penalty value if the flapping interval is greater than or equal to T1, but less than T2.
* Reduces the penalty value by 1 if the flapping interval is greater than or equal to T2, but less than T3.
* Clears the penalty value if the flapping interval is greater than or equal to T3.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number 
   ```
3. Set the intervals for increasing, retaining, and clearing the penalty value for suppressing next-hop recursion flapping.
   
   
   ```
   [nexthop recursive-lookup restrain](cmdqueryname=nexthop+recursive-lookup+restrain) suppress-interval add-count-time hold-interval hold-count-time clear-interval clear-count-time
   ```
   
   By default, the intervals for increasing, retaining, and clearing the penalty value for suppressing next-hop recursion flapping are 60s, 120s, and 600s, respectively.
4. (Optional) Enter the BGP-EVPN address family view.
   
   
   ```
   [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
   ```
5. (Optional) Disable flapping suppression involved in EVPN next-hop recursion.
   
   
   ```
   [nexthop recursive-lookup restrain disable](cmdqueryname=nexthop+recursive-lookup+restrain+disable)
   ```
   
   If high CPU usage due to route recursion change processing is not a concern and you do not want to slow down route recursion processing, you can disable flapping suppression involved in EVPN next-hop recursion. After this step is performed, flapping suppression involved in next-hop recursion does not take effect for public routes in the BGP-EVPN address family.
6. (Optional) Return to the BGP view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. (Optional) Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. (Optional) Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
9. (Optional) Enter the BD EVPN instance view.
   
   
   ```
   [evpn](cmdqueryname=evpn)
   ```
10. (Optional) Disable flapping suppression involved in EVPN next-hop recursion.
    
    
    ```
    [nexthop recursive-lookup restrain disable](cmdqueryname=nexthop+recursive-lookup+restrain+disable)
    ```
    
    If high CPU usage due to route recursion change processing is not a concern and you do not want to slow down route recursion processing, you can disable flapping suppression involved in EVPN next-hop recursion. After this step is performed, flapping suppression involved in EVPN next-hop recursion does not take effect for the current BD EVPN instance route.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display bgp**](cmdqueryname=display+bgp) **evpn** **all** **routing-table** command to check EVPN route information.