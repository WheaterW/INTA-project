Clearing DHCPv4 Statistics
==========================

You can clear DHCPv4 statistics by clearing the DHCPv4 relay statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

DHCPv4 statistics cannot be restored after they are cleared. Exercise caution when running reset commands.



#### Procedure

* Run the [**reset dhcp relay statistics**](cmdqueryname=reset+dhcp+relay+statistics) [ **interface** { *interface-type* *interface-number* | *interface-name*} ] command in the user view to clear the DHCPv4 relay statistics.
* Run the [**reset ip-pool max-usage**](cmdqueryname=reset+ip-pool+max-usage) [ **pool** [ *pool-name* ] | **domain** [ *domain-name* ] ] command in the user view to clear the historical maximum usage of addresses in an IPv4 address pool.
* Run the [**reset ip-pool max-ratio domain**](cmdqueryname=reset+ip-pool+max-ratio+domain) command in the user view to clear statistics about IP address pool usage in all domains on the device.
* After confirming statistics about the CAR for whitelisted DHCP sessions on a specified board, run the **reset cpu-defend whitelist session-car dhcp-server statistics slot** *slot-id* command in any view.