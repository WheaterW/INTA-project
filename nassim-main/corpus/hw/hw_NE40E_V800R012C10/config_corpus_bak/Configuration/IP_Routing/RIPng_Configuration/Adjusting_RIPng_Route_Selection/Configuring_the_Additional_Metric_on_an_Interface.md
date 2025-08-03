Configuring the Additional Metric on an Interface
=================================================

The additional metric is the metric (hop count) to be added to the original metric of a RIPng route. You can set additional metrics for received RIPng routes and those to be sent.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ripng metricin**](cmdqueryname=ripng+metricin) *value*
   
   
   
   The metric to be added to received routes is set.
4. Set the metric to be added to routes to be sent.
   
   
   
   Run any of the following commands as required:
   
   * Configure a basic ACL:
     1. Run [**ripng metricout**](cmdqueryname=ripng+metricout) { *value* | { *acl6-number* | **acl6-name** *acl6-name* } *value1* } \*
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* A rule is configured for the ACL.
        
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
     
     Run [**ripng metricout**](cmdqueryname=ripng+metricout) { *value* | **ipv6-prefix** *ipv6-prefix-name* *value1* } \*
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.

#### Follow-up Procedure

Run the [**ripng metricin**](cmdqueryname=ripng+metricin) command to set an additional metric for received RIPng routes. This command affects the metric of each received route in the routing table.

Run the [**ripng metricout**](cmdqueryname=ripng+metricout) command to set an additional metric for advertised RIPng routes. However, the metric of the route in the routing table remains unchanged.

If the metric plus the additional metric exceeds 16, 16 is used as the metric.