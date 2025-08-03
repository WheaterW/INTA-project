Clearing DHCP Server Statistics
===============================

This section describes how to use **reset** commands to clear DHCP server statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Cleared DHCP server statistics cannot be restored. Therefore, exercise caution when running **reset** commands.



#### Procedure

* Run the [**reset dhcp server statistics**](cmdqueryname=reset+dhcp+server+statistics) command in the user view to clear DHCP server statistics.
* Run the [**reset conflict-ip-address**](cmdqueryname=reset+conflict-ip-address) command in the IP address pool view to identify a conflicting address.
* Run the [**reset ip-pool max-usage**](cmdqueryname=reset+ip-pool+max-usage) command in the user view to display the historical maximum usage of IPv4 addresses.