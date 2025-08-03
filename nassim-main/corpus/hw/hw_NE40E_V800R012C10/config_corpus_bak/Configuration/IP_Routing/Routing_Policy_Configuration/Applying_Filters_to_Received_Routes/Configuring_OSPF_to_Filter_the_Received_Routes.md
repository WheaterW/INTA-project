Configuring OSPF to Filter the Received Routes
==============================================

After a filtering policy is configured for the OSPF routes that need to be delivered to the routing management module, only the routes that match the policy will be added to the routing table.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   An OSPF process is started, and the OSPF view is displayed.
3. Set the conditions to filter the received routes.
   
   
   
   Run any of the following commands as required:
   
   * Based on the basic ACL:
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        A rule for the ACL is configured.
        
        When the [**rule**](cmdqueryname=rule) command is run to configure rules for a named ACL, only the source address range specified by **source** and the time period specified by **time-range** are valid as the rules.
        
        When a filtering policy of a routing protocol is used to filter routes:
        + If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
        + If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
        + If a route has not matched any ACL rules, the route will not be received or advertised by the system.
        + If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
        + In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
          
          Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
          
          Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
     4. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
        
        An OSPF process is started, and the OSPF view is displayed.
     5. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **import**
        
        An import policy that is based on the basic ACL is configured to filter routes received by OSPF.
   * Based on the IP prefix list:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **ip-prefix** *ip-prefix-name* **import**
     
     An import policy that is based on the IP prefix list is configured to filter routes received by OSPF.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.