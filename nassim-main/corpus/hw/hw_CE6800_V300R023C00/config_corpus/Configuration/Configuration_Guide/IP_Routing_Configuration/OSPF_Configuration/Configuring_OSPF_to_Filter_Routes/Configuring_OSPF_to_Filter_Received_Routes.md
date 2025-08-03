Configuring OSPF to Filter Received Routes
==========================================

Configuring OSPF to Filter Received Routes

#### Prerequisites

Before configuring OSPF to filter received routes, you have completed the following tasks:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).
* To use a route-policy to filter the routes, create the route-policy first.
* To use an IP prefix list to filter the routes, create the IP prefix list first.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Choose any of the following methods to filter the received routes:
   
   
   * Based on an ACL
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Create an ACL and enter the ACL view.
        ```
        [acl](cmdqueryname=acl) { name basic-acl-name { basic | [ number ] basic-acl-number } | [ number ] basic-acl-number }
        ```
     3. Configure an ACL rule.
        ```
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment-type fragment | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
        ```
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        The following table lists the strategies that can be taken when an ACL is used for filtering.
        
        **Table 1** ACL strategies
        | Condition | Result |
        | --- | --- |
        | The action in an ACL rule is **permit**. | The matched routes will be advertised or accepted. |
        | The action in an ACL rule is **deny**. | The matched routes will not be advertised or accepted. |
        | The network segment of a route is beyond the range specified in an ACL rule. | By default, the matched routes will not be advertised or accepted. |
        | The ACL does not contain rules. | Any routes matched against the filtering policy based on this ACL will not be advertised or accepted. |
        | If the configuration order is used as the ACL rule matching order, routes are matched against the ACL rules based on the configuration order by default. If the ACL rules are numbered with IDs, routes are matched against the ACL rules in ascending order of their IDs. | In this case, routes can be filtered using a blacklist or whitelist:  Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.  Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be advertised or accepted. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out unwanted routes. |
     4. Enter the OSPF view.
        ```
        [ospf](cmdqueryname=ospf) [ process-id ]
        ```
     5. Implement filtering based on the ACL.
        ```
        [filter-policy](cmdqueryname=filter-policy) { acl-number | acl-name acl-name [ secondary ] } import
        ```
   * Based on an IP prefix list
     ```
     [filter-policy](cmdqueryname=filter-policy) ip-prefix ip-prefix-name [ secondary ] import
     ```
   * Based on a route-policy
     ```
     [filter-policy](cmdqueryname=filter-policy) route-policy route-policy-name [ secondary ] import
     ```
   
   OSPF is a link-state dynamic routing protocol, with routing information stored in the LSAs. Therefore, received LSAs cannot be filtered using the [**filter-policy**](cmdqueryname=filter-policy) **import** command. Instead, the command is used to filter the routes calculated by OSPF, with only the routes that match the filtering rules being added to the routing information base (RIB).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```