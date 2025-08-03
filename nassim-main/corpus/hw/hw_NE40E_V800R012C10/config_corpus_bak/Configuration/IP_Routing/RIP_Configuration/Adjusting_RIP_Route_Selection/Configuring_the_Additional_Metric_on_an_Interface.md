Configuring the Additional Metric on an Interface
=================================================

The additional metric is a metric (number of hops) that is added to the original metric of an RIP route. You set additional metrics for received RIP routes and those to be sent.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **interface** *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Set the metric to be added to received routes.
   
   
   
   Run any of the following commands as required:
   
   * Based on the basic ACL:
     1. Run [**rip metricin**](cmdqueryname=rip+metricin) { *value* | { *acl-number* | **acl-name** *acl-name* } *value1* }
        
        The metric to be added to the received routes that match the specified basic ACL is configured.
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
   * Based on an IP prefix list:
     
     Run [**rip metricin**](cmdqueryname=rip+metricin) { *value* | **ip-prefix** *ip-prefix-name* *value1* }
     
     The metric to be added to the received routes that match the specified basic ACL is configured.
4. Configure a metric to be added to the routes to be advertised by the interface.
   
   
   
   Run any of the following commands as required:
   
   * Based on the basic ACL:
     1. Run [**rip metricout**](cmdqueryname=rip+metricout) { *value* | { *acl-number* | **acl-name** *acl-name* } *value1* } \*
        
        The metric to be added to the routes that match the specified basic ACL and are to be advertised is configured.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        A rule is configured for the ACL.
        
        When the [**rule**](cmdqueryname=rule) command is run to configure rules for a named ACL, only the source address range specified by **source** and the time period specified by **time-range** are valid as the rules.
        
        When a filtering policy of a routing protocol is used to filter routes:
        + If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
        + If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
        + If a route has not matched any ACL rules, the route will not be received or advertised by the system.
        + If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
        + In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
          
          Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
          
          Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
   * Based on an IP prefix list:
     
     Run [**rip metricout**](cmdqueryname=rip+metricout) { *value* | **ip-prefix** *ip-prefix-name* *value1* } \*
     
     The metric to be added to the routes that match the specified IP prefix list and are to be advertised is configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an ACL or IP prefix list is specified in the [**rip metricout**](cmdqueryname=rip+metricout) command to filter the received RIP routes to be advertised, the configured metric is added only to the matched routes. If a RIP route does not match the ACL or the IP prefix list, its metric is increased by 1. When an ACL or an IP prefix list is used with the [**rip metricout**](cmdqueryname=rip+metricout) command, the additional metric ranges from 2 to 15.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.