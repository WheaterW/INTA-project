Checking LSP Connectivity and Reachability
==========================================

A ping or tracert command enables a device to monitor LSP connectivity and reachability.

#### Context

Run either of the following commands to perform MPLS ping or MPLS tracert detection.


#### Procedure

* Run the [**ping lsp**](cmdqueryname=ping+lsp+-a+-c+-exp+-h+-m+-r+-s+-t+-v+ip) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] command in any view to execute an MPLS ping.
* Run the [**tracert lsp**](cmdqueryname=tracert+lsp+-a+-exp+-h+-r+-t+-s+ip+detail) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* | **-s** *size* ] \* **ip** *destination-iphost mask-length* [ *ip-address* ] [ **detail** ] command in any view to execute an MPLS tracert.