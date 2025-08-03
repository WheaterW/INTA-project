(Optional) Configuring a Filter
===============================

(Optional) Configuring a Filter

#### Context

Filters can be flexibly defined using ACLs. Note the following during the filter configuration:

When a filter references an ACL, the device takes the relevant actions configured in the ACL rules on packets that match those rules.

The ACL referenced by a filter does not support the following parameters. If these parameters are configured, the filter is invalid.

* Basic ACL: **vpn-instance**
* Advanced ACL: **vpn-instance**, **icmp-type**, **igmp-type**, **source-pool**, **source-port-pool**, **destination-pool**, and **destination-port-pool**
* Layer 2 ACL: **802.3**
* Basic ACL6: **vpn-instance**
* Advanced ACL6: **destination**, **vpn-instance**, and **icmpv6-type**

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an attack defense policy and enter the attack defense policy view.
   
   
   ```
   [cpu-defend policy](cmdqueryname=cpu-defend+policy) policy-name
   ```
3. Configure a filter.
   
   
   ```
   [filter](cmdqueryname=filter) filter-id acl { acl-number | ipv6 ipv6-acl-number } [ interface { interface-type interface-number1 [ to interface-type interface-number2 ] } &<1-8> ] [ vlan { vlan-id1 [ to vlan-id2 ] } &<1-8> ]
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support **ipv6** *ipv6-acl-number*.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Apply the attack defense policy.
   
   
   * Configure attack defense policies in batches.
     ```
     [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name batch slot { start-slot [ to end-slot ] } &<1-12>
     ```
   * Configure an attack defense policy separately.
     ```
     [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name [ slot slot-id ]
     ```
   
   After an attack defense policy is created, you must apply the policy in the system view. Otherwise, the policy does not take effect.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```