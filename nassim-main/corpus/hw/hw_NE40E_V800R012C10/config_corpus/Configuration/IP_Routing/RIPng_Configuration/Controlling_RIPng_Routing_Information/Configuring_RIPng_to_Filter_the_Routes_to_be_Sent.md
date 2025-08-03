Configuring RIPng to Filter the Routes to be Sent
=================================================

You can configure RIPng to filter the routes to be sent.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
   
   
   
   The RIPng view is displayed.
3. Run the following commands as required to filter the routes to be sent based on different policies.
   
   
   * To configure ACL-based filtering, run the [**filter-policy**](cmdqueryname=filter-policy) { *acl6-number* | **acl6-name** *acl6-name* } **export** [ *protocol* [ *process-id* ] ] command.
     
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* A rule is configured for the ACL.
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        When a filtering policy of a routing protocol is used to filter routes:
        + If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
        + If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
        + If a route has not matched any ACL rules, the route will not be received or advertised by the system.
        + If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
        + In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
          
          Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
          
          Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
   * To configure IP prefix list-based filtering, run the [**filter-policy**](cmdqueryname=filter-policy) **ipv6-prefix** *ipv6-prefix-name* **export** [ *protocol* [ *process-id* ] ] command.
   * To configure a route-policy-based filtering, run the [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* **export** [ *protocol* [ *process-id* ] ] command.
   
   RIPng can filter the routes to be sent based on an ACL6, route-policy, or an IPv6 prefix list. Only the routes that meet the match conditions are advertised to neighbors. If no protocol is specified in the command, all the routing information to be advertised will be filtered, including the imported routes and local RIPng routes (similar to direct routes).
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.