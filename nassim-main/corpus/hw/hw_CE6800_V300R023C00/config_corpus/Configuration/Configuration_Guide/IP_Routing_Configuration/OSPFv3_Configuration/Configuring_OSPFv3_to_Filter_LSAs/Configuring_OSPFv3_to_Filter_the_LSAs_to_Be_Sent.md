Configuring OSPFv3 to Filter the LSAs to Be Sent
================================================

Configuring OSPFv3 to Filter the LSAs to Be Sent

#### Prerequisites

Before configuring OSPFv3 to filter the LSAs to be sent, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

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
   
   Determine whether to perform this step based on the current interface working mode.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=area+%28OSPFv3+view%29)
   ```
5. Create an ACL and enter the ACL view.
   
   
   ```
   [acl ipv6](cmdqueryname=acl+ipv6) { name basic-acl6-name basic | [ number ] basic-acl6-number }
   ```
6. Configure an ACL rule.
   
   
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
7. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
9. Configure the interface to filter the LSAs to be sent.
   
   
   ```
   [ospfv3 filter-lsa-out](cmdqueryname=ospfv3+filter-lsa-out) { lsa-type type-value [ instance instanceId ] }
   ```
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** command to check the OSPFv3 LSDB information.