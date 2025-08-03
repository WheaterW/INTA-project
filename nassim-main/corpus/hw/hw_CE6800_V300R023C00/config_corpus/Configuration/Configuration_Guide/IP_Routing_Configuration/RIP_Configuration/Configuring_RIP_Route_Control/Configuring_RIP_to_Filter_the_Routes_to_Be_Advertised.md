Configuring RIP to Filter the Routes to Be Advertised
=====================================================

Configuring RIP to Filter the Routes to Be Advertised

#### Context

By specifying an ACL or IP prefix list, you can configure a routing policy to filter the routes to be advertised.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Set the conditions to filter routes to be advertised. Perform any of the following operations as required:
   
   
   * Based on an ACL
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
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment-type { fragment } | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name ] *
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
     4. Enter the RIP view.
        ```
        [rip](cmdqueryname=rip) [ process-id ]
        ```
     5. Implement filtering based on the ACL.
        ```
        [filter-policy](cmdqueryname=filter-policy) { acl-number | acl-name acl-name } export [ bgp | direct | static | { isis | ospf | rip } [ process-id ] | interface-type interface-number ]
        ```
   * Based on an IP prefix list
     ```
     [filter-policy](cmdqueryname=filter-policy) ip-prefix ip-prefix-name export [ bgp | direct | static | { isis | ospf | rip } [ process-id ] | interface-type interface-number ]
     ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```