Verifying the Dynamic RP Parameter Configuration
================================================

After adjusting dynamic Rendezvous Point (RP) parameters, verify BootStrap router (BSR) and RP information.

#### Prerequisites

The adjustment of dynamic RP parameters on an IPv6 network is complete as needed.


#### Procedure

* Run the [**display pim ipv6 bsr-info**](cmdqueryname=display+pim+ipv6+bsr-info) command to check information about a BSR in an IPv6 PIM-SM domain.
* Run the [**display pim ipv6 rp-info**](cmdqueryname=display+pim+ipv6+rp-info) [ *ipv6-group-address* ] command to check information about an RP in an IPv6 PIM-SM domain.