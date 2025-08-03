Resetting Statistics on the Number of DiscardedDHCP Packets
===========================================================

The clearing statistics on the number of discarded Dynamic Host Configuration Protocol (DHCP) packets function allows the device to clear statistics on the number of discarded DHCP packets.

#### Usage Scenario

After the alarm functions are enabled, the system collects statistics on the number of discarded DHCP packets. You can run the [**display dhcp snooping**](cmdqueryname=display+dhcp+snooping) command to view the statistics. To ensure accuracy, you can clear the existing statistics.![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics on discarded DHCP packets cannot be restored after you clear them. Therefore, exercise cautions before you clear the statistics.




#### Procedure

* Run the [**reset dhcp snooping statistics**](cmdqueryname=reset+dhcp+snooping+statistics) { **vlan** *vlan-id* [ **interface** *interface-type* *interface-number*] | **interface** *interface-type* *interface-number* | **bridge-domain** *bd-id* } command in the system view to clear statistics on the number of discarded DHCP packets.