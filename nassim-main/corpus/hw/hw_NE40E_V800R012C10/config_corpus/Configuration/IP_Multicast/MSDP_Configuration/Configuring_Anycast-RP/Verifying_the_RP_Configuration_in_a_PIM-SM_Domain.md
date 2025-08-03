Verifying the RP Configuration in a PIM-SM Domain
=================================================

After configuring Anycast-Rendezvous Point (RP) in a PIM-SM domain, verify information about MSDP peers and RP information of PIM routing entries.

#### Prerequisites

Anycast-RP has been configured in a PIM-SM domain.


#### Procedure

* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **brief** command to check brief information about MSDP peers.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **peer-status** [ *peer-address* ] command to check detailed information about MSDP peers.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **routing-table** command to check information about the RP of PIM routing entries.