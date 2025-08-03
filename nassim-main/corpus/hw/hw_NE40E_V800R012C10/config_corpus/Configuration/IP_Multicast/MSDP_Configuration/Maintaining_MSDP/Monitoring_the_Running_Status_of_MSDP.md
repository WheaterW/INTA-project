Monitoring the Running Status of MSDP
=====================================

You can monitor the MSDP running status by checking brief and detailed information about MSDP peers, (S, G) information in the source active (SA) cache, and the number of (S, G) entries in the SA cache.

#### Context

You can run the following commands in any view to check the MSDP running status.


#### Procedure

* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **brief** [ **state** { **connect** | **down** | **listen** | **shutdown** | **up** } ] command in any view to check brief information about MSDP peers.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **peer-status** [ *peer-address* ] command in any view to check detailed information about MSDP peers.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **rpf-peer** **original-rp** *original-rp-address* command in any view to check information about all reverse path forwarding (RPF) peers of a specific source's rendezvous point (RP) address, including RPF peer selection rules and RPF route types.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **sa-cache** [ *group-address* | *source-address* | { *as-number-plain* | *as-number-dot* } ] \* command in any view to check (S, G) information in the SA cache.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **sa-count** [ *as-number-plain* | *as-number-dot* ] command in any view to check the number of (S, G) entries in the SA cache.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** [ **peer** *peer-address* | **message-type** { **source-active** | **sa-request** | **sa-response**  | **keepalive** | **notification** | **traceroute-request** | **traceroute-reply** | **data-packets** | **unknown-type** } ] \* command in any view to check statistics about the received, sent, and discarded MSDP messages.