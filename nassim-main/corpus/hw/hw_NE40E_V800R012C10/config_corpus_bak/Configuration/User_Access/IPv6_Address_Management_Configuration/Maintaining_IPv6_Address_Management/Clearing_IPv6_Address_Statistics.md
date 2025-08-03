Clearing IPv6 Address Statistics
================================

Clearing_IPv6_Address_Statistics

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

IPv6 address statistics cannot be restored after they are cleared. Exercise caution when running the [**reset ipv6-pool max-ratio domain**](cmdqueryname=reset+ipv6-pool+max-ratio+domain) command.



#### Procedure

* Run the [**reset ipv6-pool max-ratio domain**](cmdqueryname=reset+ipv6-pool+max-ratio+domain) command in the user view to clear statistics about IPv6 address pool usage in all domains on the device.
* After confirming statistics about the CAR for whitelisted DHCPv6 sessions on a specified board, run the **reset cpu-defend whitelist-v6 session-car dhcpv6-server statistics slot** *slot-id* command in any view.