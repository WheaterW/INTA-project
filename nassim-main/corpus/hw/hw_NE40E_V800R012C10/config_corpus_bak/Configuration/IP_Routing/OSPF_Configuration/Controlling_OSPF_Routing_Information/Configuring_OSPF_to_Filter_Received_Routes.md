Configuring OSPF to Filter Received Routes
==========================================

After a filtering policy is configured for the OSPF routes that need to be delivered to the routing management module, only the routes that match the policy will be added to the routing table.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Perform any of the following operations as required:
   
   
   * Based on the basic ACL:
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        An ACL rule is configured.
        
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
     4. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
        
        The OSPF view is displayed.
     5. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **import**
        
        An import policy is configured to filter received routes.
   * Based on the IP prefix list:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **ip-prefix** *ip-prefix-name* **import**
     
     An import policy is configured to filter received routes.
   * Based on the route-policy:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* [ **secondary** ] **import**
     
     An import policy is configured to filter received routes.
   * Based on the route-filter:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **route-filter** *route-filter-name* [ **secondary** ] **import**
     
     An import policy is configured to filter received routes.
   
   OSPF is a link-state dynamic routing protocol, with routing information carried in the link status advertisement (LSA). Therefore, the [**filter-policy**](cmdqueryname=filter-policy) **import** command cannot be used to filter the advertised or received LSAs. This command is used to filter the routes calculated by OSPF. Only the routes that match the filtering rules are added to the routing information base (RIB).
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.