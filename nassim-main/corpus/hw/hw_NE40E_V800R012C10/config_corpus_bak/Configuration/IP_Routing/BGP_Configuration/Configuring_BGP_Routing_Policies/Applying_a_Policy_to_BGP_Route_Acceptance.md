Applying a Policy to BGP Route Acceptance
=========================================

After an import policy is configured, only the routes that match the import policy are accepted.

#### Procedure

* Configure BGP to filter the routes to be received globally.
  
  
  
  You can configure the device to filter the routes to be received.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Configure BGP to filter the routes to be received globally.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     BGP acceptance policies take effect in the following sequence:
     
     1. Globally received routes:
        
        Basic ACL-based acceptance policy configured using the [**filter-policy**](cmdqueryname=filter-policy+acl-name+import) { *acl-number* | **acl-name** *acl-name* } **import** command
        
        IP prefix list-based acceptance policy configured using the [**filter-policy**](cmdqueryname=filter-policy+ip-prefix+import) **ip-prefix** *ip-prefix-name* **import** command
     2. Basic ACL-based policy for accepting routes from a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+filter-policy+import) { *ipv4-address* | *group-name* } **filter-policy** { *acl-number* | **acl-name** *acl-name* } **import** command
     3. AS\_Path filter-based policy for accepting routes from a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+as-path-filter+import) { *ipv4-address* | *group-name* } **as-path-filter** { *number* | *name* } **import** command
     4. IP prefix list-based policy for accepting routes from a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+ip-prefix+import) { *ipv4-address* | *group-name* } **ip-prefix** *ip-prefix-name* **import** command
     5. Route-policy-based policy for accepting routes from a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+route-policy+import) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **import** command
     
     
     + To filter routes based on a basic ACL, perform the following steps:
       1. Run the [**filter-policy**](cmdqueryname=filter-policy+acl-name+import) { *acl-number* | **acl-name** *acl-name* } **import** command to filter the routes to be received.
       2. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
       3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
       4. Run the [**acl**](cmdqueryname=acl+name+basic+basic+number+match-order+config+auto) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
       5. Run the [**rule**](cmdqueryname=rule+name+deny+permit) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } command to configure a rule for the ACL.
          
          When the [**rule**](cmdqueryname=rule+source+time-range) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
          - If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
          - If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
          - If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
          - Routes can be filtered using a blacklist or whitelist:
            
            If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
            
            Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
            
            Filtering using a whitelist: Configure a rule with a small ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the routes that are not to be accepted or advertised.
     + To filter routes based on an IP prefix list, run the [**filter-policy**](cmdqueryname=filter-policy+ip-prefix+import) **ip-prefix** *ip-prefix-name* **import** command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If an ACL is specified in the [**filter-policy**](cmdqueryname=filter-policy) command and no VPN instance is specified in ACL rules, BGP filters both public network and VPN routes in all address families. If a VPN instance is specified in an ACL rule, only data traffic from the VPN instance matches the filtering condition, and no routes are filtered.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP to filter the routes to be received from a specified peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Perform any of the following operations to filter the routes to be received from a specified peer or peer group:
     
     
     + To filter routes based on a basic ACL, perform the following steps:
       1. Run the [**peer**](cmdqueryname=peer+filter-policy+import) { *ipv4-address* | *group-name* } **filter-policy** { *acl-number* | **acl-name** *acl-name* } **import** command to configure the device to filter the routes to be received from a specified peer or peer group.
       2. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
       3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
       4. Run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
       5. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \* command to configure a rule for the ACL.
          
          When the [**rule**](cmdqueryname=rule) command is run to configure rules for a named ACL, only the source address range specified by **source** and the time period specified by **time-range** are valid as the rules.
          
          When a filtering policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
          - If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
          - If a route has not matched any ACL rules, the route will not be received or advertised by the system.
          - If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
          - In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
            
            Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
            
            Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
     + To filter routes based on an AS\_Path filter, run the [**peer**](cmdqueryname=peer+as-path-filter+import) { *ipv4-address* | *group-name* } **as-path-filter** { *number* | *name* } **import** command.
     + To filter routes based on an IP prefix list, run the [**peer**](cmdqueryname=peer+ip-prefix+import) { *ipv4-address* | *group-name* } **ip-prefix** *ip-prefix-name* **import** command.
     + To filter routes based on a route-policy, run the [**peer**](cmdqueryname=peer+route-policy+import) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **import** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A route-policy specified in the [**peer route-policy**](cmdqueryname=peer+route-policy) [**import**](cmdqueryname=import) command does not support interface-based matching rules (configured using the [**if-match interface**](cmdqueryname=if-match+interface) command).
     
     The import policy applied to a peer in a peer group can be different from that applied to the peer group. Specifically, a unique policy can be used to filter the routes to be received from each peer in the peer group.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limit the number of routes received from peers.
  
  
  
  If a BGP Router is maliciously attacked or network configuration errors occur, the Router will receive a large number of routes from its peers. As a result, a large number of resources are consumed on the Router. To prevent this issue, the administrator must limit the resources to be consumed during device operation based on the network planning and Router capacity. BGP provides peer-specific route control to limit the number of routes received from a peer or peer group.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+route-limit) { *group-name* | *ipv4-address* } [**route-limit**](cmdqueryname=route-limit+alert-only+idle-forever+idle-timeout) *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *minutes* ]
     
     
     
     The maximum number of routes that the device is allowed to accept from the specified peer or peer group is set.
     
     
     
     This command provides route control based on peers. You can specify parameters as needed to control the processing if the number of the routes accepted from a peer exceeds the limit specified.
     
     + If **alert-only** is set, the peer relationship is not interrupted and no more routes are accepted after the route limit is reached. In this case, an alarm is generated, and a log is recorded.
     + If **idle-forever** is set, the peer relationship is interrupted and the system does not automatically attempt to re-establish the connection. In this case, an alarm is generated, and a log is recorded. In this case, the peer status is Idle in the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ **verbose** ] command output. To restore the BGP connection, run the [**reset bgp**](cmdqueryname=reset+bgp) command. Configuring this parameter is not recommended.
     + If **idle-timeout** is set, the peer relationship is interrupted. The device retries setting up a connection after the timer expires. An alarm is generated, and a log is recorded. In this case, the peer status is Idle in the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ **verbose** ] command output. To restore the BGP connection before the timer expires, run the [**reset bgp**](cmdqueryname=reset+bgp) command.
     + If none of the preceding parameters is set, the peer relationship is disconnected. The device retries setting up a connection in 30 seconds. An alarm is generated, and a log is recorded.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the number of routes received by the local Router exceeds the upper limit and the [**peer route-limit**](cmdqueryname=peer+route-limit+alert-only) command is used for the first time, the local Router and its peer reestablish the peer relationship, regardless of whether **alert-only** is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.