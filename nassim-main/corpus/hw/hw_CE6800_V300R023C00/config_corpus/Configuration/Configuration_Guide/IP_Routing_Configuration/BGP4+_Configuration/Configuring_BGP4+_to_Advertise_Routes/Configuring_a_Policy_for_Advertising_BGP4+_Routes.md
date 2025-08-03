Configuring a Policy for Advertising BGP4+ Routes
=================================================

Configuring a Policy for Advertising BGP4+ Routes

#### Prerequisites

Before configuring a policy for advertising BGP4+ routes, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

BGP4+ can apply a routing policy to the routes to be advertised to all peers or to a specified peer or peer group. If multiple filtering policies are configured, BGP4+ advertises only those routes that match all the configured policies.


#### Procedure

* Configure BGP to filter the routes to be advertised to all peers.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  4. Configure the device to filter the routes to be advertised.
     
     
     ```
     [filter-policy](cmdqueryname=filter-policy+acl6-name+ipv6-prefix) { acl6-number | acl6-name acl6-name | ipv6-prefix ipv6-prefix-name } [export](cmdqueryname=export+direct+isis+ospfv3+ripng+static) [ direct | isis process-id | ospfv3 process-id | ripng process-id | static ]
     ```
     
     After BGP4+ filters the routes imported using the [**import-route**](cmdqueryname=import-route) command, only those routes that match the filtering conditions are added to the local BGP4+ routing table and advertised to BGP4+ peers.
     
     If *protocol* is specified, only the routes of the specified protocol are filtered. If *protocol* is not specified, the BGP4+ routes to be advertised are filtered, including those imported using the [**import-route**](cmdqueryname=import-route) or [**network**](cmdqueryname=network) command.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Apply a routing policy to the routes to be advertised to a specified peer or peer group.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the device to filter the routes to be advertised based on any of the following filters:
     
     
     + Based on a basic ACL:
       1. Enter the ACL view.
          ```
          [acl ipv6](cmdqueryname=acl+ipv6+name+basic+number) { name basic-acl6-name basic | [ number ] basic-acl6-number }
          ```
       2. Configure an ACL rule.
          
          ```
          [rule](cmdqueryname=rule+name+deny+permit+fragment+source+any+time-range) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name ] *
          ```
          
          When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the device.
          - If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the device.
          - If a route has not matched any ACL rules, the route will not be accepted or advertised by the device.
          - If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the device.
          - Routes can be filtered using a blacklist or whitelist:
            
            Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to advertise or accept the other routes.
            
            Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be advertised or accepted. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
            
            If **match-order** is set to **config** for the ACL, the ACL rules are matched based on their configuration order by default. If the ACL rules are numbered with IDs, the rules are matched in ascending order of their IDs.
       3. Return to the system view.
          ```
          [quit](cmdqueryname=quit)
          ```
       4. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       5. Enter the IPv6 unicast address family view.
          ```
          [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
          ```
       6. Configure the device to filter the routes to be advertised to a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [filter-policy](cmdqueryname=filter-policy+export) acl-number export
          ```
          ```
          [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [filter-policy](cmdqueryname=filter-policy+acl6-name+export) acl6-name acl6-name export
          ```
     + Based on an AS\_Path filter:
       
       1. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       2. Enter the IPv6 unicast address family view.
          ```
          [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
          ```
       3. Configure the device to filter the routes to be advertised to a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [as-path-filter](cmdqueryname=as-path-filter+export) { number | name } export
          ```
     + Based on an IP prefix list:
       
       1. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       2. Enter the IPv6 unicast address family view.
          ```
          [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
          ```
       3. Configure the device to filter the routes to be advertised to a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [ipv6-prefix](cmdqueryname=ipv6-prefix+export) ipv6-prefix-name export
          ```
     + Based on a route-policy:
       
       1. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       2. Enter the IPv6 unicast address family view.
          ```
          [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
          ```
       3. Configure the device to filter the routes to be advertised to a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [route-policy](cmdqueryname=route-policy+export) route-policy-name export
          ```
     
     The export routing policy applied to a peer in a peer group can be different from that applied to the peer group. Specifically, a unique policy can be used to filter the routes to be advertised to each peer in the peer group.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```