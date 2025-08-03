Configuring an NQA Test Group
=============================

This section describes how to configure an NQA test group to monitor the status of multiple links by binding it to multiple NQA test instances.

#### Prerequisites

NQA test instances have been configured. Currently, an NQA test group can be bound to only [ICMP](dc_vrp_nqa_cfg_0005.html) and [TCP](dc_vrp_nqa_cfg_0006.html) test instances.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa group**](cmdqueryname=nqa+group) *group-name*
   
   
   
   An NQA test group is created, and the NQA group view is displayed.
3. Run [**operator**](cmdqueryname=operator) { **and** | **or** }
   
   
   
   The operation type between test instances in the NQA test group is set to AND or OR.
4. (Optional) Run [**description**](cmdqueryname=description) *string*
   
   
   
   A description is configured for the NQA test group.
5. Run [**nqa test-instance**](cmdqueryname=nqa+test-instance) *admin-name* *test-name*
   
   
   
   The NQA test group is bound to a test instance.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

Run the [**display nqa group**](cmdqueryname=display+nqa+group) [ *group-name* ] command to check the test results of the NQA test group.


#### Follow-up Procedure

After the preceding configurations are complete, the test results of the NQA test group can be reported to the static route module to control the advertisement of static routes by [Configuring NQA Group for IPv4 Static Route](dc_vrp_static-route_disjoin_cfg_0075.html) or [Configuring NQA Group for IPv6 Static Route](dc_vrp_static-route_disjoin_cfg_0076.html).