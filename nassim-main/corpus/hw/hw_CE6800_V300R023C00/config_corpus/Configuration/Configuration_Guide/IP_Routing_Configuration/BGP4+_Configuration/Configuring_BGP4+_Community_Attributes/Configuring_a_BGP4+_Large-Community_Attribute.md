Configuring a BGP4+ Large-Community Attribute
=============================================

Configuring a BGP4+ Large-Community Attribute

#### Prerequisites

Before configuring a BGP4+ large-community attribute, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

The large-community attribute can represent a 2-byte or 4-byte Autonomous System Number (ASN), and has two 4-byte LocalData IDs. The administrator can therefore apply route-policies more flexibly. The large-community attribute extends and can be used together with a community attribute.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a route-policy node and enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy+deny+permit+node) route-policy-name { deny | permit } node node
   ```
3. (Optional) Configure an if-match clause for the route-policy. The Large-Community attribute of routes can be added or modified only if the routes match the if-match clause.
   
   
   
   For details about the configuration, see [(Optional) Configuring an if-match Clause](vrp_bgp6_cfg_0024.html#EN-US_TASK_0000001130782194__table1881514486311).
4. Configure one or multiple large-community attributes for BGP4+ routes.
   
   
   ```
   [apply large-community](cmdqueryname=apply+large-community+additive+overwrite+delete) { aa:bb:cc } &<1-16> { additive | overwrite | delete }
   ```
   
   or
   
   ```
   [apply large-community-list](cmdqueryname=apply+large-community-list+additive+overwrite+delete) large-community-list-name { additive | overwrite | delete }
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
9. Enable the device to advertise Large-Community attributes to the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [advertise-large-community](cmdqueryname=advertise-large-community)
   ```
   
   
   
   By default, the device does not advertise Large-Community attributes to its peers or peer groups.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```