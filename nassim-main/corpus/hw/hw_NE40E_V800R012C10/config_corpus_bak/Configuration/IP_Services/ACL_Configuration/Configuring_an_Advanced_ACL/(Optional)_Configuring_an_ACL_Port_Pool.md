(Optional) Configuring an ACL Port Pool
=======================================

When multiple port numbers need to be matched to ACL rules, you can configure an ACL port pool to reduce the configuration workload.

#### Context

In typical ACL usage scenarios, such as QoS traffic policy, a user may need to match multiple port numbers. To implement policy-based routing using advanced ACL rules to match multiple source and destination port numbers, the user needs to specify all possible combinations of source and destination port numbers when configuring ACL rules. On large-scale networks, tens of millions of ACL rules may need to be manually configured to match the port numbers, which is not viable.

To reduce the configuration workload, configure an ACL port pool. After an ACL port pool is configured, you only need to configure an ACL rule with a specified port pool name (*pool-name*) to match multiple port numbers.![](../../../../public_sys-resources/note_3.0-en-us.png) 

When an ACL rule needs to match multiple source and destination port numbers, you need to run this command twice to create an ACL source port pool and an ACL destination port pool separately.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl port-pool**](cmdqueryname=acl+port-pool) *pool-name*
   
   
   
   An ACL port pool is created, and the ACL port pool view is displayed.
3. Run [**eq**](cmdqueryname=eq) *begin-port-number*, [**neq**](cmdqueryname=neq) *begin-port-number*, [**gt**](cmdqueryname=gt) *begin-port-number*, [**lt**](cmdqueryname=lt) *end-port-number*, or [**range**](cmdqueryname=range) *begin-port-number* *end-port-number*
   
   
   
   Port numbers are added to the ACL port pool.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.