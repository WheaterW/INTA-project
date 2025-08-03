Monitoring the ND Operating Status
==================================

This section describes how to use display commands to monitor the ND operating status.

#### Context

You can run the following commands in any view to check the ND operating status in routine maintenance.


#### Procedure

* Run the [**display ipv6 neighbors**](cmdqueryname=display+ipv6+neighbors) [ *interface-type* *interface-number* | *ipv6-address* | **vpn-instance** *vpn-instance-name* ] command in any view to check IPv6 neighbor configurations.
* Run the [**display ipv6 nd security timestamp**](cmdqueryname=display+ipv6+nd+security+timestamp) *interface-type* *interface-number* command in any view to check the timestamp of an IPv6 SEND message.
* Run the [**display ipv6 nd security nonce**](cmdqueryname=display+ipv6+nd+security+nonce) *interface-type* *interface-number* command in any view to check the Nonce value of an IPv6 SEND message.
* Run the [**display ipv6 nd security statistics**](cmdqueryname=display+ipv6+nd+security+statistics) *interface-type* *interface-number* command in any view to check statistics about IPv6 SEND messages on a specified interface.
* Run the [**display ipv6 nd proxy packet statistics**](cmdqueryname=display+ipv6+nd+proxy+packet+statistics) [ **slot** *slot-id* | **interface** *interface-type* *interface-number* ] command in any view to check statistics about proxy ND.
* Run the [**display ipv6 nd miss anti-attack record**](cmdqueryname=display+ipv6+nd+miss+anti-attack+record) { **all** | { *interface-name* | *interface-type* *interface-num* } } command in any view to check attack records in scenarios where ND entries are missing.
* Run the [**display ipv6 nd anti-attack record**](cmdqueryname=display+ipv6+nd+anti-attack+record) { **all** | { *interface-name* | *interface-type* *interface-num* } } command in any view to check ND message attack records.