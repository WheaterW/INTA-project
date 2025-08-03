Clearing DHCPv6 Server Message Statistics
=========================================

Clearing_DHCPv6_Server_Message_Statistics

#### Context

During routine maintenance, if you need to collect DHCPv6 server message statistics in an upcoming period, you can clear the existing statistics so that the device starts collection afresh for this period.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Once cleared, DHCPv6 server message statistics cannot be restored. Exercise caution when clearing the statistics.



#### Procedure

* Run the [**reset dhcpv6 server statistics**](cmdqueryname=reset+dhcpv6+server+statistics) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] command to clear DHCPv6 server message statistics.