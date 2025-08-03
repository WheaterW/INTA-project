Clearing ND Statistics
======================

This section describes how to use reset commands to clear ND statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

ND statistics cannot be restored after they are cleared. Exercise caution when running reset commands.



#### Procedure

* Run the [**reset ipv6 neighbors**](cmdqueryname=reset+ipv6+neighbors) { **dynamic** | *interface-type* *interface-number* | **dynamic** { *interface-name* | *interface-type* *interface-number* } *ipv6-address* } command in the user view to clear IPv6 neighbor configurations.
* Run the [**reset ipv6 nd security statistics**](cmdqueryname=reset+ipv6+nd+security+statistics) *interface-type* *interface-number* command in the user view to clear statistics on IPv6 SEND messages on a specified interface.
* Run the [**reset ipv6 nd security timestamp**](cmdqueryname=reset+ipv6+nd+security+timestamp) *interface-type* *interface-number* command in the user view to clear the timestamp of an IPv6 SEND message on a specified interface.
* Run the [**reset ipv6 nd security nonce**](cmdqueryname=reset+ipv6+nd+security+nonce) *interface-type* *interface-number* command in the user view to clear the Nonce value of an IPv6 SEND message on a specified interface.
* Run the [**reset ipv6 nd proxy packet statistics all**](cmdqueryname=reset+ipv6+nd+proxy+packet+statistics+all) command in the user view to clear all the statistics about proxy ND.
* Run the [**reset ipv6 nd packet statistics all**](cmdqueryname=reset+ipv6+nd+packet+statistics+all) command in the user view to clear all ND message statistics.
* Run the [**reset ipv6 nd anti-attack record**](cmdqueryname=reset+ipv6+nd+anti-attack+record) { **all** | { *interface-name* | *interface-type* *interface-num* } } command in the user view to clear ND message attack records.
* Run the [**reset ipv6 nd miss anti-attack record**](cmdqueryname=reset+ipv6+nd+miss+anti-attack+record) { **all** | { *interface-name* | *interface-type* *interface-num* } } command in the user view to clear attack records in scenarios where ND entries are missing.