Configuring OSPFv3 to Filter Received Routes
============================================

After receiving Link State Advertisements (LSAs), OSPFv3 determines whether to add the calculated routes to the local routing table based on a filtering policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run any of the following commands as required:
   
   
   * Configure a basic ACL:
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
        
        A rule is configured for the ACL.
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        When a filter-policy of a routing protocol is used to filter routes:
        + If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
        + If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
        + If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
        + If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
        + Routes can be filtered using a blacklist or whitelist:
          
          If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
          
          Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
          
          Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
     4. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
        
        The OSPFv3 view is displayed.
     5. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl6-number* | **acl6-name** *acl6-name* } **import**
        
        An import policy that is based on the ACL is configured to filter received routes.
   * Based on an IPv6 prefix list:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **ipv6-prefix** *ipv6-prefix-name* **import**
     
     An import policy that is based on an IPv6 prefix list is configured to filter received routes.
   * Based on a route-policy:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name*  **import**
     
     An import policy that is based on a route-policy is configured to filter received routes.
   * Based on a route-filter:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **route-filter** *route-filter-name* **import**
     
     An import policy that is based on a route-filter is configured to filter received routes.
   
   The [**filter-policy**](cmdqueryname=filter-policy) **import** command is used to filter the routes calculated by OSPFv3. Only the routes that match the filtering rules are added to the routing table and can be advertised. Routes that do not match the filtering rules can be added to the OSPFv3 routing table but not to the routing information base (RIB) and cannot be advertised. Therefore, the LSDB is not affected regardless of whether the received routes match the filtering rules.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.