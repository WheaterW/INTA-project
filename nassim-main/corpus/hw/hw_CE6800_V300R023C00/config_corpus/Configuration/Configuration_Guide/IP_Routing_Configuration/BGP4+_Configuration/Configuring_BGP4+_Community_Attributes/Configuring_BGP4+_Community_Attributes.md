Configuring BGP4+ Community Attributes
======================================

Configuring BGP4+ Community Attributes

#### Prerequisites

Before configuring BGP4+ community attributes, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

Community attributes are transmitted between BGP4+ peers, regardless of ASs. With a community attribute configured, a group of routes share a route-policy. Before sending a route with the community attribute to peers, BGP4+ allows the modification of the original community attribute carried in the route.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a route-policy node and enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy+deny+permit+node) route-policy-name { deny | permit } node node
   ```
3. (Optional) Configure an if-match clause for the route-policy. The community attribute of routes can be added or modified only if the routes match the if-match clause.
   
   
   
   For detailed configurations, see [(Optional) Configuring an if-match Clause](vrp_bgp6_cfg_0024.html#EN-US_TASK_0000001130782194__table1881514486311).
4. Configure community attributes for BGP4+ routes.
   
   
   ```
   [apply community](cmdqueryname=apply+community+internet+no-advertise+no-export) { { community-number | aa:nn } &<1-32> | internet | no-advertise | no-export | no-export-subconfed } * [ additive ]
   ```
5. Exit the route-policy view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
7. Enter the BGP-IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
8. Configure an export route-policy.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [route-policy](cmdqueryname=route-policy+export) route-policy-name export
   ```
9. Enable the device to send standard community attributes to the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [advertise-community](cmdqueryname=advertise-community)
   ```
   
   By default, a device does not advertise community attributes to any peer or peer group.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```