Applying a Policy to BGP4+ Route Advertisement
==============================================

If BGP4+ is configured to filter received routes, only the routes that meet the matching rules are added to the local BGP4+ routing table and advertised to BGP4+ peers.

#### Context

BGP4+ can apply a routing policy to all the routes to be advertised or only to the routes to be advertised to a specified peer or peer group. If multiple filter policies are configured, BGP advertises only routes that match all the filter policies.


#### Procedure

* Configure BGP to filter all the routes to be advertised.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**filter-policy**](cmdqueryname=filter-policy+acl6-name+ipv6-prefix) { *acl6-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } [**export**](cmdqueryname=export+direct+isis+ospfv3+ripng+static) [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** | **unr** ]
     
     
     
     The device is configured to filter the routes to be advertised.
     
     
     
     After BGP4+ filters the routes imported using the [**import-route**](cmdqueryname=import-route) command, only those routes that match the filtering conditions are added to the local BGP4+ routing table and advertised to BGP4+ peers.
     
     If *protocol* is specified, only routes of the specified protocol are filtered. If *protocol* is not specified, all BGP routes to be advertised are filtered, including the routes imported using the [**import-route**](cmdqueryname=import-route) or [**network**](cmdqueryname=network) command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     BGP4+ advertisement policies take effect in the following sequence:
     
     1. Globally advertised routes:
        
        To configure a basic ACL-based advertisement policy, run the [**filter-policy**](cmdqueryname=filter-policy+acl6-name) { *acl6-number* | **acl6-name** *acl6-name* } [**export**](cmdqueryname=export+direct+isis+ospfv3+ripng+static) [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** | **unr** ] command.
        
        To configure an IP prefix list-based advertisement policy, run the [**filter-policy**](cmdqueryname=filter-policy+ipv6-prefix) **ipv6-prefix** *ipv6-prefix-name* [**export**](cmdqueryname=export+direct+isis+ospfv3+ripng+static) [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** | **unr** ] command.
     2. To configure a basic ACL-based policy for advertising routes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**filter-policy**](cmdqueryname=filter-policy+acl6-name+export) { *acl6-number* | **acl6-name** *acl6-name* } **export** command.
     3. To configure an AS\_Path filter-based policy for advertising routes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**as-path-filter**](cmdqueryname=as-path-filter+export) { *number* | *name* } **export** command.
     4. To configure an IP prefix list-based policy for advertising routes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**ipv6-prefix**](cmdqueryname=ipv6-prefix+export) *ipv6-prefix-name* **export** command.
     5. To configure an IPv6 address list-based policy for advertising routes to a specific peer or peer group, run the [**peer**](cmdqueryname=peer+advertise+dependent-filter+condition-filter) { *peerIpv4Addr* | *peerIpv6Addr* | *groupName* } **advertise dependent-filter** *dependent-filter-list* *outDependType* [ **condition-filter** *condition-filter-list* | **condition-ip-filter** *ip-prefix-name* ] command.
     6. To configure a route-policy-based policy for advertising routes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy+export) *route-policy-name* **export** command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a routing policy to the routes to be advertised to a certain peer (group).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run the following command as needed to configure the device to use a specified filter to filter the routes to be advertised to a specified peer.
     
     
     + Based on a basic ACL:
       1. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**filter-policy**](cmdqueryname=filter-policy+acl6-name+export) { *acl6-number* | **acl6-name** *acl6-name* } **export**
          
          The routes to be advertised to the specified peer or peer group are filtered.
       2. Run [**quit**](cmdqueryname=quit)
          
          Return to the BGP view.
       3. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       4. Run [**acl ipv6**](cmdqueryname=acl+ipv6+name+basic+number+match-order+config+auto) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
          
          The ACL view is displayed.
       5. Run [**rule**](cmdqueryname=rule+name+deny+permit) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** }\*
          
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
     + To use an AS\_Path filter to filter routes, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**as-path-filter**](cmdqueryname=as-path-filter+export) { *number* | *name* } **export** command.
     + To use an IP prefix list to filter routes, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**ipv6-prefix**](cmdqueryname=ipv6-prefix+export) *ipv6-prefix-name* **export** command.
     + To use an IPv6 address list to filter routes, run the [**peer**](cmdqueryname=peer+advertise+dependent-filter+condition-filter) { *peerIpv4Addr* | *peerIpv6Addr* | *groupName* } **advertise dependent-filter** *dependent-filter-list* *outDependType* [ **condition-filter** *condition-filter-list* | **condition-ip-filter** *ip-prefix-name* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If BGP route status changes after a filtering policy that is based on an IPv6 address list is enabled, the routes are re-advertised based on the conditional advertisement policy 10 seconds later by default. To set the delay in advertising the routes, run the [**timer dependent-advertise-delay**](cmdqueryname=timer+dependent-advertise-delay) *delay-time* command.
     + To use a route-policy for route filtering, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy+export) *route-policy-name* **export** command.
     
     The export routing policy applied to a peer in a peer group can be different from that applied to the peer group. Specifically, a unique policy can be used to filter the routes to be advertised to each peer in the peer group.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.