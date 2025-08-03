Configuring RIP to Filter the Routes to Be Advertised
=====================================================

You can set conditions to filter the routes to be advertised. Only the routes that meet the conditions can be advertised.

#### Context

Devices can filter the routing information. To filter the routes to be advertised, you can configure an export filtering policy by specifying the ACL and IP prefix list.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Set the conditions to filter the advertised routes.
   
   
   
   Run any of the following commands as required:
   
   * Based on the basic ACL:
     1. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **export** [ **bgp** | **direct** | **static** | **unr** | { **isis** | **ospf** | **rip** } [ *process-id* ] | *interface-type* *interface-number* ]
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        A rule is configured for the ACL.
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        When a filtering policy of a routing protocol is used to filter routes:
        + If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
        + If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
        + If a route has not matched any ACL rules, the route will not be received or advertised by the system.
        + If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
        + In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
          
          Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
          
          Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
   * Based on the IP prefix:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **ip-prefix** *ip-prefix-name* **export** [ **bgp** | **direct** | **static** | **unr** | { **isis** | **ospf** | **rip** } [ *process-id* ] | *interface-type* *interface-number* ]
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.