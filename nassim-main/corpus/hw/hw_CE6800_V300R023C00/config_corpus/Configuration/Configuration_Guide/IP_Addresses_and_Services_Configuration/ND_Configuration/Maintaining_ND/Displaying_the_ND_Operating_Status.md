Displaying the ND Operating Status
==================================

Displaying the ND Operating Status

#### Procedure

* To display the ND operating status, run the following display commands in any view.

**Table 1** Displaying the ND operating status
| Operation | Command |
| --- | --- |
| Display ND message statistics. | [**display ipv6 nd packet statistics**](cmdqueryname=display+ipv6+nd+packet+statistics) [ **slot** *slot-id* | **[**interface**](cmdqueryname=interface)** *interface-type* **i***nterface-number* ] |
| Display statistics about sent and received ND messages in a BD. | [**display ipv6 nd packet statistics bridge-domain**](cmdqueryname=display+ipv6+nd+packet+statistics+bridge-domain) [ *bd-id* ] |
| Display ND entry statistics. | [**display ipv6 neighbors statistics**](cmdqueryname=display+ipv6+neighbors+statistics) { **all** | **static** | [**slot**](cmdqueryname=slot) { **all** | **slot-num** } |**interface** *interface-type**interface-number*} |
| Display information about ND entries. | [**display ipv6 neighbors**](cmdqueryname=display+ipv6+neighbors) [ **brief** | *interface-type* *interface-number* | *ipv6-address* | **vlan** *vlan-id* *interface-type* *interface-number* ] |
| Display attack records in scenarios where ND entries are missing. | [**display ipv6 nd miss anti-attack record**](cmdqueryname=display+ipv6+nd+miss+anti-attack+record) [ **all** | *interface-name* | *interface-type* *interface-num* ] |
| Display ND message attack records. | [**display ipv6 nd anti-attack record**](cmdqueryname=display+ipv6+nd+anti-attack+record) [ **all** | *interface-name* | *interface-type* *interface-num* ] |