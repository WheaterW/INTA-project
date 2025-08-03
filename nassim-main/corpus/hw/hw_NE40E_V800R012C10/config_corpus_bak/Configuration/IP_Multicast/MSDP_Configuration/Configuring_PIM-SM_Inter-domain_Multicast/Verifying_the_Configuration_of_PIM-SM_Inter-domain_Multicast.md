Verifying the Configuration of PIM-SM Inter-domain Multicast
============================================================

After configuring PIM-SM inter-domain multicast, verify information about MSDP peers.

#### Prerequisites

PIM-SM inter-domain multicast has been configured.


#### Procedure

* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **brief** command to check brief information about MSDP peers.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **peer-status** [ *peer-address* ] command to check detailed information about MSDP peers.