Controlling the Acceptance of BGP Routes
========================================

Controlling the Acceptance of BGP Routes

#### Prerequisites

Before controlling the acceptance of BGP routes, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

After an import policy is configured, only the routes that match the import policy can be accepted.


#### Procedure

* Configure a BGP device to accept routes from all its peers or peer groups.
  
  
  
  You can configure the BGP device to filter the received routes before acceptance.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure BGP to filter the routes to be received globally.
     
     
     + Configure the BGP device to filter the received routes against a basic ACL.
       1. Enter the ACL view.
          ```
          [acl](cmdqueryname=acl+name+basic+basic+number+number) { name basic-acl-name { basic | [ basic ] number basic-acl-number } | [ number ] basic-acl-number }
          ```
       2. Configure an ACL rule.
          
          ```
          [rule](cmdqueryname=rule+name+deny+permit+fragment-type+fragment+non-fragment) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment-type { fragment | non-fragment | non-subseq | fragment-subseq | fragment-spe-first } | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name ] *
          ```
          
          When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is permit, a route matching the rule will be accepted or advertised by the device.
          - If the action specified in an ACL rule is deny, a route matching the rule will not be accepted or advertised by the device.
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
       5. Enter the IPv4 unicast address family view.
          ```
          [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
          ```
       6. Configure the device to filter received routes.
          ```
          [filter-policy](cmdqueryname=filter-policy+acl-name+import) { acl-number | acl-name acl-name } import
          ```
     + Configure BGP to filter the routes received from all peers based on an IP prefix list.
       1. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       2. Enter the IPv4 unicast address family view.
          ```
          [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
          ```
       3. Configure the device to filter received routes.
          ```
          [filter-policy](cmdqueryname=filter-policy+ip-prefix+import) ip-prefix ip-prefix-name import
          ```
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If an ACL is specified in the [**filter-policy**](cmdqueryname=filter-policy) command and no VPN instance is specified in ACL rules, BGP filters both public network and VPN routes in all address families. If a VPN instance is specified in an ACL rule, only data traffic from the VPN instance matches the filtering condition, and no routes are filtered.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the BGP device to accept routes from a specified peer or peer group.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Perform any of the following operations to filter the routes to be received from a specified peer or peer group:
     
     
     + Configure the device to filter the received routes against a basic ACL.
       1. Enter the ACL view.
          ```
          [acl](cmdqueryname=acl+name+basic+basic+number+number) { name basic-acl-name { basic | [ basic ] number basic-acl-number } | [ number ] basic-acl-number }
          ```
       2. Configure an ACL rule.
          
          ```
          [rule](cmdqueryname=rule+name+deny+permit+fragment-type+fragment+non-fragment) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment-type { fragment | non-fragment | non-subseq | fragment-subseq | fragment-spe-first } | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name ] *
          ```
          
          When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is permit, a route matching the rule will be accepted or advertised by the device.
          - If the action specified in an ACL rule is deny, a route matching the rule will not be accepted or advertised by the device.
          - If a route has not matched any ACL rules, the route will not be accepted or advertised by the device.
          - If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the device.
          - Routes can be filtered using a blacklist or whitelist:
            
            If **match-order** is set to **config** for the ACL, the ACL rules are matched based on their configuration order by default. If the ACL rules are numbered with IDs, the rules are matched in ascending order of their IDs.
            
            Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to advertise or accept the other routes.
            
            Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be advertised or accepted. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
       3. Return to the system view.
          ```
          [quit](cmdqueryname=quit)
          ```
       4. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       5. Enter the IPv4 unicast address family view.
          ```
          [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
          ```
       6. Configure the device to filter the routes to be received from a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer+filter-policy+acl-name+import) { ipv4-address | group-name | peerIpv6Addr } filter-policy { acl-number | acl-name acl-name } import
          ```
     + Configure the device to filter the routes received from a specified peer or peer group based on an IP prefix list.
       
       1. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       2. Enter the IPv4 unicast address family view.
          ```
          [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
          ```
       3. Configure the device to filter the routes to be received from a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer+ip-prefix+import) { ipv4-address | group-name | peerIpv6Addr } ip-prefix ip-prefix-name import
          ```
     + Configure the device to filter the routes received from a specified peer or peer group based on an AS\_Path filter.
       
       1. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       2. Enter the IPv4 unicast address family view.
          ```
          [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
          ```
       3. Configure the device to filter the routes to be received from a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer+as-path-filter+import) { ipv4-address | group-name | peerIpv6Addr } as-path-filter { number | name } import
          ```
     + Configure the device to filter the routes to be received from a specified peer or peer group based on a route-policy.
       
       1. Enter the BGP view.
          ```
          [bgp](cmdqueryname=bgp) as-number
          ```
       2. Enter the IPv4 unicast address family view.
          ```
          [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
          ```
       3. Configure the device to filter the routes received from a specified peer or peer group.
          ```
          [peer](cmdqueryname=peer+route-policy+import) { ipv4-address | group-name | peerIpv6Addr } route-policy route-policy-name import
          ```
          ![](public_sys-resources/note_3.0-en-us.png) 
          
          A route-policy specified in the [**peer route-policy**](cmdqueryname=peer+route-policy) [**import**](cmdqueryname=import) command does not support interface-based matching rules (configured using the [**if-match interface**](cmdqueryname=if-match+interface) command).
     
     The import routing policy applied to a peer in a peer group can be different from that applied to the peer group. Specifically, a unique policy can be used to filter the routes to be received from each peer in the peer group.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```