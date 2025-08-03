Verifying the Configuration of DHCP Relay
=========================================

After configuring a DHCP relay agent to transmit DHCP broadcast messages between DHCP clients and the DHCP server that reside on different network segments, verify the configuration.

#### Prerequisites

DHCP relay has been configured.


#### Procedure

* Run the [**display dhcp relay statistics**](cmdqueryname=display+dhcp+relay+statistics) command to check DHCP relay statistics.
* Run the [**display dhcp relay address**](cmdqueryname=display+dhcp+relay+address) { **all** | **interface** *interface-type* *interface-number* } command to check DHCP configurations on DHCP relay interfaces.
* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **dhcp** **statistics** **slot** *slot-id* command to check whitelist session-CAR statistics about DHCP messages on a specified interface board.
* Run the [**display dhcp relay proxy user**](cmdqueryname=display+dhcp+relay+proxy+user) [ **mac-address** *mac-address-data* | **ip-address** *ip-address-data* [ **vpn-instance** *vpn-instance-name* ] | **server-address** *server-address-data* [ **vpn-instance** *vpn-instance-name* ] | **interface** { *interface-name* | *interface-type* *interface-number* }] [ **verbose** ] command to check DHCP proxy user entries saved on the DHCP relay agent.