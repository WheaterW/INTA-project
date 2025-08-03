Verifying the Configuration of SA Message Parameters
====================================================

After configuring source active (SA) message parameters, verify information about and the number of (S, G) entries in the SA cache and check details about MSDP peers.

#### Prerequisites

SA message parameters have been configured.


#### Procedure

* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **sa-cache** [ *group-address* | *source-address* | { *as-number-plain* | *as-number-dot* } ] \* command to check information about (S, G) entries in the SA cache.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **sa-count** [ *as-number-plain* | *as-number-dot* ] command to check the number of (S, G) entries in the SA cache.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **peer-status** [ *peer-address* ] command to check detailed information about MSDP peers.