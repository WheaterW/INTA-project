Clearing DCB Statistics
=======================

Clearing DCB Statistics

#### Context

When diagnosing and locating DCB faults, collect DCB statistics on interfaces in a specified period. Before re-collecting DCB statistics on all interfaces or a specified interface, clear existing DCB statistics.

![](public_sys-resources/notice_3.0-en-us.png) 

After the following reset commands are executed on an interface, DCB statistics on the interface are cleared and cannot be restored. Exercise caution when you perform this operation.



#### Procedure

* Run the [**reset dcb pfc**](cmdqueryname=reset+dcb+pfc) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command in the user view to clear statistics on PFC frames on an interface.
* Run the [**reset dcb fail-record**](cmdqueryname=reset+dcb+fail-record) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command in the user view to clear DCB negotiation failure records on an interface. (Not supported by the CE6885-LL (low latency mode).)
* Run the [**reset qos headroom-usage**](cmdqueryname=reset+qos+headroom-usage) [ **slot** *slot-id* | **interface** { **interface-name** | *interface-type* **interface-num** } ] command in the user view to clear the headroom buffer usage statistics. (Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)