Verifying the IP-Trunk Interface Configuration
==============================================

After configuring the IP-Trunk interface, you can view the status and forwarding table of the IP-Trunk interface and information about member interfaces.

#### Prerequisites

An IP-Trunk interface has been configured.


#### Procedure

* Run the [**display interface ip-trunk**](cmdqueryname=display+interface+ip-trunk) [ *trunk-id* ] command to check the IP-Trunk interface information, including the status.
* Run the [**display trunkmembership ip-trunk**](cmdqueryname=display+trunkmembership+ip-trunk) *trunk-id* command to check information about member interfaces.
* Run the [**display trunkfwdtbl ip-trunk**](cmdqueryname=display+trunkfwdtbl+ip-trunk) *trunk-id* [ **slot** *slot-id* ] command to check information about the forwarding table for a link aggregation group.