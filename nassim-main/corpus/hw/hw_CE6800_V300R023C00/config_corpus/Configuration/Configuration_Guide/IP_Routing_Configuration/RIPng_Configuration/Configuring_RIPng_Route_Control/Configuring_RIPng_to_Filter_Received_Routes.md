Configuring RIPng to Filter Received Routes
===========================================

Configuring RIPng to Filter Received Routes

#### Context

You can configure RIPng to filter received routes in order to selectively accept routes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
3. Perform any of the following operations to filter received routes:
   
   
   * Based on an ACL
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
     4. Enter the RIPng view.
        ```
        [ripng](cmdqueryname=ripng) [ process-id ]
        ```
     5. Implement filtering based on the ACL.
        ```
        [filter-policy](cmdqueryname=filter-policy) { acl6-number | acl6-name acl6-name } import
        ```
   * Based on an IP prefix list
     ```
     [filter-policy](cmdqueryname=filter-policy) ipv6-prefix ipv6-prefix-name import
     ```
   * Based on a route-policy
     ```
     [filter-policy](cmdqueryname=filter-policy) route-policy route-policy-name import
     ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```