Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display msdp**](cmdqueryname=display+msdp) { **vpn-instance** *vpn-instance-name* | **all-instance** }  **sa-cache** [ *group-address* | *source-address* | { *as-number* | *as-number\_string* } ] \* command to check the (S, G) information in the SA cache.
* Run the [**display msdp**](cmdqueryname=display+msdp) { **vpn-instance** *vpn-instance-name* | **all-instance** } **sa-count** [ *as-number* | *as-number*\_string ] command to check the number of (S, G) entries.
* Run the [**display msdp**](cmdqueryname=display+msdp) { **vpn-instance** *vpn-instance-name* | **all-instance** } **peer-status** [ *peer-address* ] command to check detailed information about MSDP peers.