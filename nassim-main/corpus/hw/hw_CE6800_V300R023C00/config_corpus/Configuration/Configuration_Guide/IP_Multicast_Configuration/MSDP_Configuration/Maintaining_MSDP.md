Maintaining MSDP
================

Maintaining MSDP

#### Clearing Statistics About MSDP Peers

When clearing statistics about MSDP peers, you can also choose to reset the TCP connections between them. Resetting TCP connections affects the running status of MSDP.

![](public_sys-resources/notice_3.0-en-us.png) 

MSDP peer statistics cannot be restored after they are cleared. Exercise caution when clearing statistics.


**Table 1** Clearing statistics about MSDP peers
| Operation | Command |
| --- | --- |
| Reset TCP connections of MSDP peers, and clear all statistics about the MSDP peers. | [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **peer** [ *peer-address* ] |
| Clear the statistics about one or more MSDP peers without resetting a specified peer's TCP connection. | [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **statistics** [ *peer-address* ] |
| Clear statistics about the received, sent, and discarded MSDP messages. | [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** [ **peer** *peer-address* ] |



#### Clearing (S, G) Information in the SA Cache

![](public_sys-resources/notice_3.0-en-us.png) 

(S, G) information in the SA cache cannot be restored after you clear it. Exercise caution when clearing (S, G) information in the SA cache.

To delete the (S, G) information from an SA cache, run the [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **sa-cache** [ *group-address* ] command in the user view.