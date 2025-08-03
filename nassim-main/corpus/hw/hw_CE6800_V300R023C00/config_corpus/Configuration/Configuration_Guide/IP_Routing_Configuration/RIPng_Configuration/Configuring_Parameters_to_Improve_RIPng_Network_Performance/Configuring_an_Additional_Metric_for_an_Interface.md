Configuring an Additional Metric for an Interface
=================================================

Configuring an Additional Metric for an Interface

#### Context

The additional metric is the metric (hop count) to be added to the original metric of a RIPng route. You can set additional metrics for incoming and outgoing RIPng routes using commands.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface mode.
4. Configure a metric to be added to the routes received by the interface.
   
   
   ```
   [ripng metricin](cmdqueryname=ripng+metricin) value
   ```
5. Configure a metric to be added to the routes advertised by the interface. Select either of the following methods based on actual conditions:
   
   
   * Configure an additional metric for the interface to advertise routes based on a basic ACL.
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Create an ACL and enter the ACL view.
        ```
        [acl ipv6](cmdqueryname=acl+ipv6) { name basic-acl6-name basic | [ number ] basic-acl6-number }
        ```
     3. Configure an ACL rule.
        ```
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name ]
        ```
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        The following table lists the strategies that can be taken when an ACL is used for filtering.
        
        **Table 1** ACL policies
        | Policy | Filter Result |
        | --- | --- |
        | The action in an ACL rule is **permit**. | A route that matches the rule is accepted or advertised normally by the system. |
        | The action in an ACL rule is **deny**. | A route that matches the rule is not accepted or advertised by the system. |
        | The network segment of a route is beyond the range specified in an ACL rule. | By default, a route that matches the rule is not accepted or advertised by the system. |
        | The ACL does not contain rules. | Any routes matched against the routing policy based on this ACL will not be advertised. |
        | If ACL rules are used for matching in the configuration order, a routing device matches routes against rules that are numbered in ascending order. | In this case, routes can be filtered using a blacklist or whitelist.  Filtering using a blacklist: Configure a rule with a smaller number and specify the **deny** action to filter out unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the **permit** action to advertise or accept the other routes.  Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be advertised or accepted. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes. |
     4. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     5. Enter the interface view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        ```
     6. Implement filtering based on the ACL.
        ```
        [ripng metricout](cmdqueryname=ripng+metricout) value
        [ripng metricout](cmdqueryname=ripng+metricout) { { acl6-number | acl6-name acl6-name } value }
        ```
   * Configure an additional metric for the interface to advertise routes based on an IP prefix list.
     ```
     [ripng metricout](cmdqueryname=ripng+metricout) value
     [ripng metricout](cmdqueryname=ripng+metricout) { ipv6-prefix ipv6-prefix-name value }
     ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

After the [**ripng metricin**](cmdqueryname=ripng+metricin) command is run, RIPng adds a metric to the received route and then adds the corresponding route entry to the routing table. As a result, increasing the metric of an interface also increases the metric of a RIP route received by the interface.

After the [**ripng metricout**](cmdqueryname=ripng+metricout) command is run, RIPng adds a metric to the route to be advertised. As a result, increasing the metric of an interface also increases the metric of a RIP route sent by the interface. However, the metric of a route in the routing table remains unchanged.

If the metric of a route exceeds 16, it is considered to be 16.