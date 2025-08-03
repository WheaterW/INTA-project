Clearing ND Statistics
======================

Clearing ND Statistics

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

ND statistics cannot be restored after they are cleared. Exercise caution when running reset commands.



#### Procedure

* To clear ND statistics, run the following reset commands in the user view.

**Table 1** Clearing ND statistics
| Operation | Command |
| --- | --- |
| Clear dynamic ND entries on an interface. | [**reset ipv6 neighbors**](cmdqueryname=reset+ipv6+neighbors) { **dynamic** | *interface-type* *interface-number* | **dynamic** { *interface-name* | *interface-type* *interface-number* } *ipv6-address* } |
| Clear dynamic ND entries on a VLAN. | [**reset ipv6 neighbors**](cmdqueryname=reset+ipv6+neighbors) **vlan***vlan-id* [ *interface-type* *interface-number* ] |
| Clear statistics about SEND messages on an interface. | [**reset ipv6 nd security statistics**](cmdqueryname=reset+ipv6+nd+security+statistics) *interface-type* *interface-number* |
| Clear the timestamp of SEND messages on an interface. | [**reset ipv6 nd security timestamp**](cmdqueryname=reset+ipv6+nd+security+timestamp) *interface-type* *interface-number* |
| Clear the Nonce value of SEND messages on an interface. | [**reset ipv6 nd security nonce**](cmdqueryname=reset+ipv6+nd+security+nonce) *interface-type* *interface-number* |
| Clear statistics about dropped ND attack messages with fixed source MAC addresses. | [**reset ipv6 nd source-mac statistics**](cmdqueryname=reset+ipv6+nd+source-mac+statistics) { **interface** *interface-type* *interface-number* | **all** } |
| Clear all ND message statistics. | [**reset ipv6 nd packet statistics all**](cmdqueryname=reset+ipv6+nd+packet+statistics+all) |
| Clear ND message attack records. | [**reset ipv6 nd anti-attack record**](cmdqueryname=reset+ipv6+nd+anti-attack+record) { **all** | *interface-name* | *interface-type* *interface-num* } |
| Clear attack records in scenarios where ND entries are missing. | [**reset ipv6 nd miss anti-attack record**](cmdqueryname=reset+ipv6+nd+miss+anti-attack+record) { **all** | *interface-name* | *interface-type* *interface-num* } |