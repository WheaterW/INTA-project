Configuring OSPFv3 to Filter Routes to Be Advertised
====================================================

Configuring OSPFv3 to Filter Routes to Be Advertised

#### Prerequisites

Before configuring OSPFv3 to filter routes to be advertised, you have completed the following tasks:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).
* To use an IP prefix list to filter the routes, create the IP prefix list first.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Configure OSPFv3 to filter the routes to be advertised by using either of the following methods:
   
   
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
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | [ vpn-instance vpn-instance-name | logging ] ] *
        ```
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        The following table lists the strategies that can be taken when an ACL is used for filtering.
        
        **Table 1** ACL strategies
        | Condition | Result |
        | --- | --- |
        | The action in an ACL rule is **permit**. | The matched routes will be advertised or accepted. |
        | The action in an ACL rule is **deny**. | The matched routes will not be advertised or accepted. |
        | The prefix of a route is beyond the range specified in an ACL rule. | By default, the matched routes will not be advertised or accepted. |
        | The ACL does not contain rules. | Any routes matched against the filtering policy based on this ACL will not be advertised or accepted. |
        | If the configuration order is used as the ACL rule matching order, routes are matched against the ACL rules based on the configuration order by default. If the ACL rules are numbered with IDs, routes are matched against the ACL rules in ascending order of their IDs. | In this case, routes can be filtered using a blacklist or whitelist:  Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.  Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be advertised or accepted. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out unwanted routes. |
     4. Enter the OSPFv3 view.
        ```
        [ospfv3](cmdqueryname=ospfv3) [ process-id ]
        ```
     5. Implement filtering based on the ACL.
        ```
        [filter-policy](cmdqueryname=filter-policy) { acl6-number | acl6-name acl6-name } export [ bgp | direct | static | { isis | ospfv3 | ripng } [ process-id ] ]
        ```
   * Based on an IP prefix list
     ```
     [filter-policy](cmdqueryname=filter-policy) ipv6-prefix ipv6-prefix-name export [ bgp | direct | static | { isis | ospfv3 | ripng } [ process-id ] ]
     ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```