Verifying the Configuration
===========================

After configuring IPv6 neighbor discovery, verify the configuration.

#### Prerequisites

IPv6 neighbor discovery has been configured.


#### Procedure

* Run the [**display ipv6 neighbors**](cmdqueryname=display+ipv6+neighbors) [ *interface-type* *interface-number* | *ipv6-address* | **vid** *vlan-id* *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* ] command to check IPv6 neighbor entries.
* Run the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface) [ *interface-type* *interface-number* | **brief** ] command to check IPv6 configurations on an interface.
* Run the [**display ipv6 nd packet statistics**](cmdqueryname=display+ipv6+nd+packet+statistics) [ **slot** *slot-id* | **[**interface**](cmdqueryname=interface)** **interface-type** **interface-number** ] command to check statistics about ND messages.