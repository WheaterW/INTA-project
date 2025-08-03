Deleting Statistics About MSDP Peers
====================================

When you delete statistics about MSDP peers, you can choose whether to reset TCP connections between MSDP peers. Resetting TCP connections affects the MSDP running.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Deleted statistics about MSDP peers cannot be restored. Therefore, exercise caution when running the [**reset msdp**](cmdqueryname=reset+msdp) command.



#### Procedure

* To reset the TCP connection with the specified MSDP peer and delete the statistics about the specified MSDP peer, run the [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **peer** [ *peer-address* ] command in the user view.
* To delete the statistics about one or more MSDP peers without resetting TCP connections with MSDP peers, run the [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **statistics** [ *peer-address* ] command in the user view.
* To delete the statistics about the received, sent, and discarded MSDP messages, run the [**reset msdp**](cmdqueryname=reset+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **control-message** **counters** [ **peer** *peer-address* ] command in the user view.