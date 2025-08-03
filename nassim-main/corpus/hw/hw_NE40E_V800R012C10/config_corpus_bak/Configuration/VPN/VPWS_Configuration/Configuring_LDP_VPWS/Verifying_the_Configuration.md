Verifying the Configuration
===========================

Verifying_the_Configuration

#### Prerequisites

LDP VPWS has been configured.


#### Procedure

* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type interface-number* ] command on a PE to check local VPWS connection information.
* Run the [**display mpls l2vc remote-info**](cmdqueryname=display+mpls+l2vc+remote-info) [ *vc-id* | **unmatch** | **verbose** ] command on a PE to check remote VPWS connection information.
* Run the [**display pw-template**](cmdqueryname=display+pw-template) [ *pw-template-name* ] command to check PW template information.
* Run the [**display local-ce mac**](cmdqueryname=display+local-ce+mac) [ *interface-type* *interface-number* ] command to check the MAC address and VLAN ID of the Ethernet interface on the local CE.
* Run the [**display mpls label-stack vll interface**](cmdqueryname=display+mpls+label-stack+vll+interface) *interface-type* *interface-number* command to check label stack information.
* Run the [**display mpls l2vpn interface**](cmdqueryname=display+mpls+l2vpn+interface) *interface-type* *interface-number* **performance** command to check the PW performance statistics on a TDM interface.