Verifying the Configuration
===========================

After configuring VPN GR Helper, you can check status information about IGP GR Helper, MPLS GR Helper, and BGP GR Helper.

#### Prerequisites

VPN GR Helper configurations are complete.
#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] [**graceful-restart-information**](cmdqueryname=graceful-restart-information) command to check OSPFv3 GR information.
* Run the [**display mpls ldp**](cmdqueryname=display+mpls+ldp) [ **all** ] [ **verbose** ] command to check LDP information.
* Run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session) [ **all** ] [ **verbose** ] command to check LDP session information.
* Run the [**display mpls rsvp-te graceful-restart**](cmdqueryname=display+mpls+rsvp-te+graceful-restart) command to check RSVP GR status on the local end.
* Run the [**display mpls rsvp-te graceful-restart peer**](cmdqueryname=display+mpls+rsvp-te+graceful-restart+peer) [ { **interface** *interface-type* *interface-number* | **node-id** }[ *ip-address* ] ] command to check RSVP GR status on the peer end.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) **verbose** command to check BGP GR status.