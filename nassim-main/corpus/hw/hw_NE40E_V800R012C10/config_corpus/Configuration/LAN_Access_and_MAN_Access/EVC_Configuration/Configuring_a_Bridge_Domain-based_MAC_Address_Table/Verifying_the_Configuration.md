Verifying the Configuration
===========================

After configuring a bridge domain-based MAC address table, you can check the configurations, including the aging time for dynamic MAC addresses in the bridge domain and the limit on the number of MAC addresses that a device can learn.

#### Prerequisites

The bridge domain-based MAC address table has been configured.


#### Procedure

* Run the [**display mac-address**](cmdqueryname=display+mac-address) [ *mac-address* ] **bridge-domain** *bd-id* [ **verbose** ] command to check all MAC address entries in a specified BD.
* Run the [**display mac-address**](cmdqueryname=display+mac-address) **static** { **bridge-domain** *bd-id* | *interface-type interface-number* | *interface-name* }\* [ **verbose** ] command to check all static MAC address entries in a specified BD.
* Run the [**display mac-address**](cmdqueryname=display+mac-address) **blackhole** **bridge-domain** *bd-id* [ **verbose** ] command to check all static blackhole MAC address entries in a specified BD.
* Run the [**display mac-address**](cmdqueryname=display+mac-address) **dynamic** [ **slot** *slot-id* ] **bridge-domain** *bd-id* [ **verbose** | **last-change** ] command to check all dynamically learned MAC address entries in a specified BD.
* Run the [**display mac-address**](cmdqueryname=display+mac-address) **dynamic-blackhole** [ **evpn** *evpn-name* | **bridge-domain** *bd-id* ] [ **verbose** | **last-change** ] command to check all dynamic blackhole MAC address entries in a specified BD.
* Run the [**display mac-address aging-time bridge-domain**](cmdqueryname=display+mac-address+aging-time+bridge-domain) command to check the aging time for dynamic MAC address entries in a specified BD.
* Run the [**display mac-limit**](cmdqueryname=display+mac-limit) [ **bridge-domain** *bd-id* ] command to check rules for dynamically learned MAC addresses in a BD.