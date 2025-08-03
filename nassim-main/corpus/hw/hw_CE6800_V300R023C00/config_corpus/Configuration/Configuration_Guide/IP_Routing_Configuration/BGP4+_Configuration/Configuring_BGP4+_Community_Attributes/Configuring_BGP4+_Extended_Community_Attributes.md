Configuring BGP4+ Extended Community Attributes
===============================================

Configuring BGP4+ Extended Community Attributes

#### Prerequisites

Before configuring BGP4+ extended community attributes, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

At present, there are two types of BGP extended community attributes.

* VPN route-target (RT) extended community
* Source of Origin (SoO) extended community

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
4. Configure extended community attributes for BGP4+ routes.
   
   
   ```
   [apply extcommunity](cmdqueryname=apply+extcommunity+rt+additive) { rt { as-number:nn | ipv4-address:nn } } &<1-16> [ additive ]
   ```
   
   or
   
   ```
   [apply extcommunity soo](cmdqueryname=apply+extcommunity+soo+additive) { site-of-origin } &<1-16> additive
   ```
   
   or
   
   ```
   [apply extcommunity bandwidth](cmdqueryname=apply+extcommunity+bandwidth+none) { extCmntyString | none } or [apply extcommunity bandwidth](cmdqueryname=apply+extcommunity+bandwidth+aggregate+limit) aggregate [ limit bandwidth-value ]
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
9. Enable the device to advertise extended community attributes to the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [advertise-ext-community](cmdqueryname=advertise-ext-community)
   ```
   
   By default, a device does not advertise extended community attributes to any peer or peer group.
   
   After the [**peer advertise-ext-community**](cmdqueryname=peer+advertise-ext-community) command is run, BGP4+ advertises the routes with extended community attributes to the specified peer. If the peer only needs to accept the routes but not the extended community attributes, you can run the [**peer discard-ext-community**](cmdqueryname=peer+discard-ext-community) command on the peer to discard the extended community attributes in the received routing information.
10. (Optional) Configure the device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer.
    
    
    ```
    [peer](cmdqueryname=peer+advertise-ext-community) { peerIpv4Addr | peerIpv6Addr } advertise-ext-community
    ```
    
    Alternatively, configure the device to convert the Link Bandwidth extended community attribute (optional non-transitive) carried in BGP4+ routes into an optional transitive attribute before advertising the routes to a specified peer.
    
    ```
    [peer](cmdqueryname=peer+advertise+link-bandwidth+transitive) { peerIpv4Addr | peerIpv6Addr } advertise link-bandwidth transitive
    ```
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```