Displaying the ARP Operating Status
===================================

Displaying the ARP Operating Status

#### Procedure

During routine maintenance, you can run the following commands to check the ARP operating status.

**Table 1** Displaying the ARP operating status
| Operation | Command |
| --- | --- |
| Display ARP entries of a specified device. | [**display arp**](cmdqueryname=display+arp) [ **network** *ip-address* [ *ip-mask* | *mask-length* ] ] [ **dynamic** | **static** ] |
| Display ARP entry statistics. | [**display arp statistics**](cmdqueryname=display+arp+statistics) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] |
| Display detailed information about the change of outbound interfaces in ARP entries learned by VLANIF/VBDIF interfaces. | [**display arp track**](cmdqueryname=display+arp+track) |
| Display ARP entries learned by a specified VLAN. | [**display arp vlan**](cmdqueryname=display+arp+vlan) *vlan-id* **interface** { *interface-name* | *interface-type* *interface-number* } |