Verifying the Configuration
===========================

After configuring the PPPoEv6 access service, check the PPPoEv6 access configurations.

#### Procedure

* Run the [**display access-user**](cmdqueryname=display+access-user) command to check information about online users.
* Run the [**display sub-interface**](cmdqueryname=display+sub-interface) *interface-type interface-number* **pevlan** *pe-vlan-id* [ **cevlan** *ce-vlan-id* ] command to check information about the sub-interface configured with a specified VLAN on the main interface.
* Run the [**display bas-interface**](cmdqueryname=display+bas-interface) command to check service information on the BAS interface.
* Run the [**display vlan-statistics**](cmdqueryname=display+vlan-statistics) **interface** *interface-type interface-number*.*subinterface-number* **pevlan** *pe-vlan-id* [ **cevlan** *ce-vlan-id* ] [ **verbose** ] command to check traffic and PPP protocol packet statistics of a specified VLAN on a BAS-enabled sub-interface.
* Run the [**display vlan-statistics**](cmdqueryname=display+vlan-statistics) **interface** *interface-type interface-number* **pevlan** *pe-vlan-id* command to check statistics about traffic in a specified VLAN on a BAS-enabled interface.
* Run the [**display ppp**](cmdqueryname=display+ppp) **slot** *slot-number* [**chasten-user**](cmdqueryname=chasten-user) [ **mac-address** *mac-address* ] command to check the information about the restricted users.
* Run the [**display ppp**](cmdqueryname=display+ppp) { **user-id** *user-id* | **username** *username* | **ip-address** *ipv4-address* [ **vpn-instance** *instance-name* ] | **ipv6-address** *ipv6-address* [ **vpn-instance** *instance-name* ] | **circuit-id** *circuit-id-text* | **remote-id** *circuit-id-text* } command to check the PPP protocol status.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Whether the [**ui-mode type1**](cmdqueryname=ui-mode+type1) command is configured in the system view affects the format of the command output.