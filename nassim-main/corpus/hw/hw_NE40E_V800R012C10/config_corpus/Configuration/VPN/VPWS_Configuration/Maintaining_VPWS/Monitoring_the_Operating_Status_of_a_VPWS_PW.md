Monitoring the Operating Status of a VPWS PW
============================================

Monitoring the Operating Status of a VPWS PW

#### Context

In routine maintenance, you can run the following commands in any view to check the operating status of a VPWS PW as needed.


#### Procedure

* Run the [**display vll ccc**](cmdqueryname=display+vll+ccc) [ *ccc-name* | **type** **local** ] command to check CCC information.
* Run the [**display l2vpn ccc-interface vc-type**](cmdqueryname=display+l2vpn+ccc-interface+vc-type) { **all** | *vc-type* } [ **up** | **down** ] command to check information about the interface used by an L2VPN connection.
* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type interface-number* ] command on a PE to check local VPWS connection information.
* Run the [**display mpls l2vc remote-info**](cmdqueryname=display+mpls+l2vc+remote-info) [ *vc-id* | **unmatch** | **verbose** ] command on a PE to check remote VPWS connection information.
* Run the [**display mpls static-l2vc**](cmdqueryname=display+mpls+static-l2vc) [ *vc-id* | **interface** *interface-type* *interface-number* | **state** { **down** | **up** } | **brief** ] command on a PE to check static VPWS connection information.
* Run the [**display mpls switch-l2vc**](cmdqueryname=display+mpls+switch-l2vc) [ *ip-address* *vc-id* **encapsulation** *encapsulation-type* | **state** { **down** | **up** } | **brief** ] command on a PE to check VPWS switching information.
* Run the [**display pw-template**](cmdqueryname=display+pw-template) [ *pw-template-name* ] command to check PW template information.
* Run the [**display local-ce mac**](cmdqueryname=display+local-ce+mac) [ *interface-type* *interface-number* ] command to check the MAC address and VLAN ID of the Ethernet interface on the local CE.
* Run the [**display l2vpn error discard**](cmdqueryname=display+l2vpn+error+discard) command to check information about messages discarded by the L2VPN component.
* Run the [**display mpls l2vpn nd-dual-sending packet interface**](cmdqueryname=display+mpls+l2vpn+nd-dual-sending+packet+interface) *interface-type* *interface-number* command to check information about ND dual-fed packets.