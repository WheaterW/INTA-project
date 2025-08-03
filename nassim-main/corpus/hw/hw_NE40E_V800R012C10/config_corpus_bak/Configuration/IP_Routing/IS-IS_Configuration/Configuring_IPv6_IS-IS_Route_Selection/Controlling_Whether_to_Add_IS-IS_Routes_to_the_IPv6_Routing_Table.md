Controlling Whether to Add IS-IS Routes to the IPv6 Routing Table
=================================================================

If you do not want some IS-IS routes to be selected, you can configure a policy to prevent these routes from being added to the IP routing table.

#### Context

IP packets are forwarded based on the IP routing table. Routes in the IS-IS routing table take effect only after they are successfully added to the IP routing table.

Therefore, you can configure a basic ACL, IPv6 prefix list, or route-policy to allow only the matched IS-IS routes to be delivered to the IP routing table. Unmatched IS-IS routes are neither added to the IP routing table nor selected.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Configure a policy to add only some IS-IS routes to the IP routing table.
   
   
   
   Run any of the following commands as required:
   
   * Configure a basic ACL:
     1. Run the [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) { *acl6-number* | **acl6-name** *acl6-name* } **import** command.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
        
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
   * Based on an IP prefix list:
     
     Run the [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) **ipv6-prefix** *ipv6-prefix-name* **import** command.
   * Based on a route-policy:
     
     Run the [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) **route-policy** *route-policy-name* **import** command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.