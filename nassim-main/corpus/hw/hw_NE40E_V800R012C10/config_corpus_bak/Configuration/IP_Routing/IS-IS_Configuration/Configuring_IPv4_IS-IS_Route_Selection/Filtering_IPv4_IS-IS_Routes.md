Filtering IPv4 IS-IS Routes
===========================

If some IS-IS routes are not preferred, configure conditions to filter IS-IS routes. Only IS-IS routes meeting the specified conditions can be added to an IP routing table.

#### Context

Only routes in an IP routing table can be used to forward IP packets. An IS-IS route can take effect only after it has been added to an IP routing table.

You can configure a basic ACL, an IP prefix list, or a route-policy to filter routes so that only the matched IS-IS routes can be delivered to the IP routing table. IS-IS routes that do not meet the specified conditions cannot be added to the IP routing table nor selected to forward IP packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Configure IS-IS to deliver specified IS-IS routes to the IP routing table.
   
   
   
   Run any of the following commands as required:
   
   * Based on the basic ACL:
     1. Run the [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **import** command.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
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
   * Based on an IP prefix list:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **ip-prefix** *ip-prefix-name* **import**
   * Based on a route-policy:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* **import**
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.