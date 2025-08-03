Applying a Policy to BGP Route Advertisement
============================================

After a route advertisement policy is configured on a device, the device advertises only the routes that match the policy to its BGP peers.

#### Procedure

* Configure BGP to filter the routes to be advertised globally.
  
  
  
  You can configure the device to filter the routes to be advertised. Perform the following steps on a BGP Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Configure BGP to filter the routes to be advertised globally.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     BGP advertisement policies take effect in the following sequence:
     
     1. Globally advertised routes:
        
        Basic ACL-based advertisement policy configured using the [**filter-policy**](cmdqueryname=filter-policy+acl-name+export+direct+isis+ospf+rip+static) { *acl-number* | **acl-name** *acl-name* } **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] command
        
        IP prefix list-based advertisement policy configured using the [**filter-policy**](cmdqueryname=filter-policy+ip-prefix+export+direct+isis+ospf+rip+static) **ip-prefix** *ip-prefix-name* **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] command
     2. Basic ACL-based policy for advertising routes to a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+filter-policy+acl-name+export) { *ipv4-address* | *group-name* } **filter-policy** { *acl-number* | **acl-name** *acl-name* } **export** command
     3. AS\_Path filter-based policy for advertising routes to a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+as-path-filter+export) { *ipv4-address* | *group-name* } **as-path-filter** { *number* | *name* } **export** command
     4. IP prefix list-based policy for advertising routes to a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+ip-prefix+export) { *ipv4-address* | *group-name* } **ip-prefix** *ip-prefix-name* **export** command
     5. IP address list-based policy for advertising routes to a specific peer or peer group, configured using the [**peer**](cmdqueryname=peer+advertise+dependent-filter+condition-filter) { *ipv4-address* | *group-name* } **advertise dependent-filter** *dependent-filter-list* *outDependType* [ **condition-filter** *condition-filter-list* | **condition-ip-filter** *ip-prefix-name* ] command
     6. Route-policy-based policy for advertising routes to a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export** command
     
     
     + To filter routes based on a basic ACL, perform the following steps:
       1. Run the [**filter-policy**](cmdqueryname=filter-policy+acl-name+export+direct+isis+ospf+rip+static) { *acl-number* | **acl-name** *acl-name* } **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] command to filter the routes to be advertised.
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
     + To filter routes based on an IP prefix list, run the [**filter-policy**](cmdqueryname=filter-policy+ip-prefix+export+direct+isis+ospf+rip+static) **ip-prefix** *ip-prefix-name* **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] command.
     
     
     
     If a protocol type is specified, only the routes discovered by the specified routing protocol match the filtering condition. If no protocol type is specified, all BGP routes to be advertised match the filtering condition, including those imported using the [**import-route**](cmdqueryname=import-route) **(BGP)** command and local routes imported using the [**network**](cmdqueryname=network) **(BGP)** command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If an ACL is specified in the [**filter-policy**](cmdqueryname=filter-policy) command and no VPN instance is specified in ACL rules, BGP filters both public network and VPN routes in all address families. If a VPN instance is specified in an ACL rule, only data traffic from the VPN instance matches the filtering condition, and no routes are filtered.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP to filter the routes to be advertised to a specified peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Perform any of the following operations to filter the routes to be advertised to a specified peer or peer group:
     
     
     + To filter routes based on a basic ACL, perform the following steps:
       1. Run the [**peer**](cmdqueryname=peer+filter-policy+acl-name+export) { *ipv4-address* | *group-name* } **filter-policy** { *acl-number* | **acl-name** *acl-name* } **export** command to configure the device to filter the routes to be advertised to a specified peer or peer group.
       2. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
       3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
       4. Run the [**acl**](cmdqueryname=acl+name+basic+basic+number+number+match-order+config+auto) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
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
     + To filter routes based on an AS\_Path filter, run the [**peer**](cmdqueryname=peer+as-path-filter+export) { *ipv4-address* | *group-name* } **as-path-filter** { *number* | *name* } **export** command.
     + To filter routes based on an IP prefix list, run the [**peer**](cmdqueryname=peer+ip-prefix+export) { *ipv4-address* | *group-name* } **ip-prefix** *ip-prefix-name* **export** command.
     + To filter routes based on an IP address list, run the [**peer**](cmdqueryname=peer+advertise+dependent-filter+condition-filter) { *ipv4-address* | *group-name* } **advertise dependent-filter** *dependent-filter-list* *outDependType* [ **condition-filter** *condition-filter-list* | **condition-ip-filter** *ip-prefix-name* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If BGP route status changes after a filtering policy that is based on an IP address list is enabled, the routes are re-advertised based on the conditional advertisement policy 10 seconds later by default. To set the delay in advertising the routes, run the [**timer dependent-advertise-delay**](cmdqueryname=timer+dependent-advertise-delay) *delay-time* command.
     + To filter routes based on a route-policy, run the [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export** command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       A route-policy specified in the [**peer route-policy**](cmdqueryname=peer+route-policy) [**export**](cmdqueryname=export) command does not support interface-based matching rules (configured using the [**if-match interface**](cmdqueryname=if-match+interface) command).
     
     The export routing policy applied to a peer in a peer group can be different from that applied to the peer group. Specifically, a unique policy can be used to filter the routes to be advertised to each peer in the peer group.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.