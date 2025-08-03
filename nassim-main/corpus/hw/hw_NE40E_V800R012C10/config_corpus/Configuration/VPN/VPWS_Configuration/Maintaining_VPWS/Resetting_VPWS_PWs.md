Resetting VPWS PWs
==================

Resetting VPWS PWs

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The following [**reset**](cmdqueryname=reset) commands reset VPWS configurations. Exercise caution when using the commands.




#### Procedure

* Run the [**reset pw**](cmdqueryname=reset+pw)  [ **peer-address** *peer-ip* ]  *pw-id* *vc-type* command to re-create a PW or PW template.
* Run the [**reset local-ce mac**](cmdqueryname=reset+local-ce+mac) [ *interface-type* *interface-number* ] command to clear information about the MAC address and VLAN ID of a local CE dynamically learned by the Ethernet interface of a PE, so that the PE can re-learn this information.
* Run the [**reset traffic-statistics l2vpn pw**](cmdqueryname=reset+traffic-statistics+l2vpn+pw) { **all** | **interface** *interface-type* *interface-number* [ **secondary** | **bypass** ] } command to clear VPWS PW traffic statistics.
* Run the [**reset mpls l2vpn nd-dual-sending packet**](cmdqueryname=reset+mpls+l2vpn+nd-dual-sending+packet) [ **interface** *interface-type* *interface-number* ] command to clear information about ND dual-fed packets.