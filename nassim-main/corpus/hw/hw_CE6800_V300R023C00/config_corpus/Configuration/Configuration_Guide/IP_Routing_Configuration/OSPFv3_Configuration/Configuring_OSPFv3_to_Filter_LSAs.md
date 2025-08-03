Configuring OSPFv3 to Filter LSAs
=================================

Configuring OSPFv3 to Filter LSAs

#### Prerequisites

Before configuring OSPFv3 to filter LSAs in an area, you have completed the following tasks:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).
* To use a route-policy to filter LSAs, create the route-policy first.
* To use an IP prefix list to filter LSAs, create the IP prefix list first.

#### Context

Filtering LSAs in an area can prevent unnecessary LSA transmission. This reduces the size of the LSDB on neighbors and speeds up network convergence.

You can set filtering conditions for the incoming or outgoing Type 3 LSAs (inter-area-prefix-LSAs) so that only those that meet the filtering conditions are accepted or advertised. This function is applicable only to ABRs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Enter the OSPFv3 area view.
   
   
   ```
   [area](cmdqueryname=area+%28OSPFv3+view%29) area-id
   ```
4. To configure OSPFv3 to filter incoming or outgoing Type 3 LSAs in the area, use any of the following methods as needed:
   
   
   * Based on an ACL:
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
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
        | Condition | Filtering Result |
        | --- | --- |
        | The action in an ACL rule is **permit**. | The matched LSAs will be advertised or accepted. |
        | The action in an ACL rule is **deny**. | The matched LSAs will not be advertised or accepted. |
        | The prefix of a route is beyond the range specified in an ACL rule. | By default, the matched LSAs will not be advertised or accepted. |
        | The ACL does not contain rules. | Any LSAs matched against the filtering policy based on this ACL will not be advertised or accepted. |
        | If the configuration order is used as the ACL rule matching order, LSAs are matched against the ACL rules based on the configuration order by default. If the ACL rules are numbered with IDs, LSAs are matched against the ACL rules in ascending order of rule IDs. | In this case, there are two filtering modes.  Filtering using a blacklist: Configure a rule with an ID and specify the action **deny** in this rule to filter out the LSAs that the device does not want to accept or advertise. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other LSAs.  Filtering using a whitelist: Configure a rule with an ID and specify the action **permit** in this rule to permit the LSAs that the device wants to accept or advertise. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the LSAs that the device does not want to accept or advertise. |
     4. Enter the OSPFv3 view.
        ```
        [ospfv3](cmdqueryname=ospfv3) [ process-id ]
        ```
     5. Enter the OSPFv3 area view.
        ```
        [area](cmdqueryname=area) area-id
        ```
     6. Implement filtering based on the ACL.
        ```
        [filter](cmdqueryname=filter) { acl6-number | acl6-name acl6-name } import
        [filter](cmdqueryname=filter) { acl6-number | acl6-name acl6-name } export
        ```
   * Based on an IP prefix list:
     ```
     [filter](cmdqueryname=filter) ipv6-prefix ipv6-prefix-name import
     [filter](cmdqueryname=filter) ipv6-prefix ipv6-prefix-name export
     ```
   * Based on a route-policy:
     ```
     [filter](cmdqueryname=filter) route-policy route-policy-name import
     [filter](cmdqueryname=filter) route-policy route-policy-name export
     ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** command to check the OSPFv3 LSDB information.


[Understanding OSPFv3 LSA Filtering](../vrp/vrp_ospfv3_cfg_0127.html)



[Configuring OSPFv3 to Filter LSAs in an Area](../vrp/vrp_ospfv3_cfg_0044.html)



[Configuring OSPFv3 to Filter the LSAs to Be Sent](../vrp/vrp_ospfv3_cfg_0128.html)



[(Optional) Configuring OSPFv3 to Discard Specified LSAs](../vrp/vrp_ospfv3_cfg_00144.html)