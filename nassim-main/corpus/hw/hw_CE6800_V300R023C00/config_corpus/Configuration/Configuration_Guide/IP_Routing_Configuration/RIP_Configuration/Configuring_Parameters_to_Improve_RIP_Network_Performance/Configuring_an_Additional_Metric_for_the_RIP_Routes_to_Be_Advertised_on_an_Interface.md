Configuring an Additional Metric for the RIP Routes to Be Advertised on an Interface
====================================================================================

Configuring an Additional Metric for the RIP Routes to Be Advertised on an Interface

#### Context

The additional metric (hop count) is added to the original RIP route metric. You can run different commands to configure an additional metric for the RIP routes to be advertised.


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
4. Configure a metric to be added to the routes advertised by the interface. Perform either of the following operations based on actual conditions:
   
   
   * Configure an additional metric for routes that match a specified ACL.
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Create an ACL and enter the ACL view.
        ```
        [acl](cmdqueryname=acl) { name basic-acl-name [ basic ] | [ number ] basic-acl-number }
        ```
     3. Configure an ACL rule.
        ```
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment-type fragment | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
        ```
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        The following table lists the strategies that can be taken when an ACL is used for filtering.
        
        **Table 1** ACL policies
        | Policy | Filter Result |
        | --- | --- |
        | The ACL rule action is set to **permit**. | A route that matches the rule can be advertised. |
        | The ACL rule action is set to **deny**. | A route that matches the rule will not be advertised. |
        | The network segment of a route is beyond the range specified in the ACL rule. | A route that matches the rule is not advertised by default. |
        | The ACL does not contain rules. | The routes matching against the filter-policy based on this ACL will not be advertised. |
        | If ACL rules are used for matching in the configuration order, a routing device matches routes against rules that are numbered in ascending order. | In this case, routes can be filtered using a blacklist or whitelist.  Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** to filter out unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** to allow other routes to be advertised.  Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** to allow the routes to be advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** to filter out unwanted routes. |
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
        [rip metricout](cmdqueryname=rip+metricout) { value | { acl-number | acl-name acl-name } value1 }
        ```
   * Configure an additional metric for routes that match a specified IP prefix list.
     
     ```
     [rip metricout](cmdqueryname=rip+metricout) { value | ip-prefix ip-prefix-name value1 }
     ```![](public_sys-resources/note_3.0-en-us.png) 
   
   When the [**rip metricout**](cmdqueryname=rip+metricout) command is used with an ACL or IP prefix list to configure an additional metric for the RIP routes to be advertised on an interface, the additional metric is added to the original metric of the RIP routes that match the ACL or IP prefix list specified in a route-policy. The metrics of RIP routes that do not pass the route-policy are increased by 1. Therefore, when the [**rip metricout**](cmdqueryname=rip+metricout) command is used with an ACL or IP prefix list, the additional metric ranges from 2 to 15.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```