Configuring a Policy for Receiving BGP4+ Routes
===============================================

BGP4+ filters received routes using a policy. Only the routes that match the policy can be added to a routing table.

#### Context

BGP4+ can apply a routing policy to all received routes or only routes received from a specific peer (group). If multiple filter policies are configured, BGP accepts only routes that match all the filter policies.

If a BGP4+ Router is maliciously attacked or network configuration errors occur, the device will receive a large number of routes from its peers. As a result, a large number of resources are consumed on the device. To prevent this issue, the administrator must limit the resources to be consumed during device operation based on the network planning and Router capacity. BGP4+ provides peer-specific route control to limit the number of routes sent from a peer or peer group.


#### Procedure

* Configure BGP4+ to filter all received routes.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  BGP4+ acceptance policies take effect in the following sequence:
  
  1. Globally received routes:
     
     To configure a basic ACL-based acceptance policy, run the [**filter-policy**](cmdqueryname=filter-policy+acl6-name+import) { *acl6-number* | **acl6-name** *acl6-name*} **import** command.
     
     To configure an IP prefix list-based acceptance policy, run the [**filter-policy**](cmdqueryname=filter-policy+ipv6-prefix+import) **ipv6-prefix** *ipv6-prefix-name* **import** command.
  2. To configure a basic ACL-based policy for accepting routes from a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**filter-policy**](cmdqueryname=filter-policy+acl6-name+import) { *acl6-number* | **acl6-name** *acl6-name* } **import** command.
  3. To configure an AS\_Path filter-based policy for accepting routes from a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**as-path-filter**](cmdqueryname=as-path-filter+import) { *number* | *name* } **import** command.
  4. To configure an IP prefix list-based policy for accepting routes from a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**ipv6-prefix**](cmdqueryname=ipv6-prefix+import) *ipv6-prefix-name* **import** command.
  5. To configure a route-policy-based policy for accepting routes from a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy+import) *route-policy-name* **import** command.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**filter-policy**](cmdqueryname=filter-policy+acl6-name+ipv6-prefix) { *acl6-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } [**import**](cmdqueryname=import)
     
     
     
     A policy is configured to filter all received BGP4+ routes.
     
     Only the routes that match the policy are accepted by BGP4+ and added to the routing table.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a routing policy to the routes received from a specified peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Filter the routes received from peers based on different filters:
     
     
     + Based on a basic ACL:
       1. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**filter-policy**](cmdqueryname=filter-policy+acl6-name+import) { *acl6-number* | **acl6-name** *acl6-name* } **import**
          
          The routes to be received from the specified peer or peer group are filtered.
       2. Run [**quit**](cmdqueryname=quit)
          
          Return to the BGP view.
       3. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       4. Run [**acl ipv6**](cmdqueryname=acl+ipv6+name+basic+number+match-order+config+auto) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
          
          The ACL view is displayed.
       5. Run [**rule**](cmdqueryname=rule+name+deny+permit) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** }
          
          An ACL rule is configured.
          
          When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
          - If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
          - If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
          - If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
          - Routes can be filtered using a blacklist or whitelist:
            
            If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
            
            Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
            
            Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
     + To use the AS\_Path filter for route filtering, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**as-path-filter**](cmdqueryname=as-path-filter+import) { *number* | *name* } **import** command.
     + To use an IP prefix list for route filtering, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**ipv6-prefix**](cmdqueryname=ipv6-prefix+import) *ipv6-prefix-name* **import** command.
     + To use a route-policy for route filtering, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy+import) *route-policy-name* **import** command.
     
     The import routing policy applied to a peer in a peer group can be different from that applied to the peer group. Specifically, a unique policy can be used to filter the routes to be received from each peer in the peer group.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limit the number of routes received from peers.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* | *ipv6-address* } [**route-limit**](cmdqueryname=route-limit+alert-only+idle-forever+idle-timeout) *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
     
     
     
     The maximum number of routes that the device is allowed to accept from the specified peer or peer group is set.
     
     
     
     This command provides route control based on peers. You can specify parameters as needed to control the processing if the number of the routes accepted from a peer exceeds the limit specified.
     
     + If **alert-only** is set, the peer relationship is not interrupted and no more routes are accepted after the route limit is reached. In this case, an alarm is generated, and a log is recorded.
     + If **idle-forever** is set, the peer relationship is interrupted and the system does not automatically attempt to re-establish the connection. In this case, an alarm is generated, and a log is recorded. In this case, the peer status is Idle in the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ **verbose** ] command output. To restore the BGP connection, run the [**reset bgp**](cmdqueryname=reset+bgp) command. Configuring this parameter is not recommended.
     + If **idle-timeout** is set, the peer relationship is interrupted. The device retries setting up a connection after the timer expires. An alarm is generated, and a log is recorded. In this case, the peer status is Idle in the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ **verbose** ] command output. To restore the BGP connection before the timer expires, run the [**reset bgp**](cmdqueryname=reset+bgp) command.
     + If none of the preceding parameters is set, the peer relationship is disconnected. The device retries setting up a connection in 30 seconds. An alarm is generated, and a log is recorded.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the number of routes received by the local Router exceeds the upper limit and the [**peer route-limit**](cmdqueryname=peer+route-limit+alert-only) command is used for the first time, the local Router and its peer reestablish the peer relationship, regardless of whether **alert-only** is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.