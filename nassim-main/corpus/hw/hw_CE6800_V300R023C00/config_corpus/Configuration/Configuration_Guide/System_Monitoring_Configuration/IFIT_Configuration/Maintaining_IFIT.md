Maintaining IFIT
================

Maintaining IFIT

#### Context

During routine maintenance, you can view IFIT packet statistics to check whether packet statistics are correct.


#### Procedure

**Table 1** IFIT maintenance operations
| Operation | Command |
| --- | --- |
| Display detailed information about IFIT flow tables for IPv4 addresses. | [**display ifit flow-cache**](cmdqueryname=display+ifit+flow-cache) [ { **tcp** | **udp** } | **sip** *ipv4-sip-address* | **dip** *ipv4-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **status** { **active** | **aged** } | **flow-id** *flow-id-number* ] \* **slot** *slot-id* |
| Display detailed information about IFIT flow tables for IPv6 addresses. | [**display ifit flow-cache**](cmdqueryname=display+ifit+flow-cache) [ { **tcp** | **udp** } | **sip** *ipv6-sip-address* | **dip** *ipv6-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **status** { **active** | **aged** } | **flow-id** *flow-id-number* ] \* **slot** *slot-id*  NOTE:  This command is not supported on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM. |
| Display statistics in IFIT flow tables. | [**display ifit**](cmdqueryname=display+ifit) [ **forward** ] **flow-cache statistics slot** *slot-id* |
| Clear IFIT flow table information on a device. | [**reset ifit**](cmdqueryname=reset+ifit) [ **forward** ] **flow-cache slot** *slot-id*  NOTE:  You can clear IFIT flow table information only after running the [**undo ifit**](cmdqueryname=undo+ifit) command to disable IFIT measurement. |


![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after they are cleared. Exercise caution when clearing the statistics.