Checking Network Connectivity and Reachability
==============================================

Run the **ping** and **tracert** commands to check the connectivity and reachability of seamless MPLS networks.

#### Context

Run the following commands in any view of a BGP LSP endpoint node to check the connectivity and reachability of a BGP LSP.


#### Procedure

* Run the [**ping lsp**](cmdqueryname=ping+lsp+-a+-c+-exp+-h+-m+-r+-s+-t+-v+bgp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** ] \* **bgp** *destination-iphost* *mask-length* [ *ip-address* ] command to check BGP LSP connectivity.