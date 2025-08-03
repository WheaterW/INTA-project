Verifying the Configuration of BSR RP Parameters
================================================

After adjusting BootStrap router (BSR) Rendezvous Point (RP) parameters, verify BSR and RP information.

#### Prerequisites

BSR RP parameters have been adjusted.


#### Procedure

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **bsr-info** command to check information about the BSR in the PIM-SM domain.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **rp-info** [ *group-address* ] command to check information about the RP in the PIM-SM domain.