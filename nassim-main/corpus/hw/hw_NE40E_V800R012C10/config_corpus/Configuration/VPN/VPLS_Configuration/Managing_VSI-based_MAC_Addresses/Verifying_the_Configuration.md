Verifying the Configuration
===========================

After configuring VSI-based MAC address management, check the set limits of MAC address learning and the aging time of MAC address entries.

#### Prerequisites

VSI-based MAC address management has been configured.


#### Procedure

* Run the [**display mac-address aging-time**](cmdqueryname=display+mac-address+aging-time) **vsi** [ *vsi-name* ] command to check the aging time of MAC address entries.
* Run the [**display mac-address**](cmdqueryname=display+mac-address) [ *mac-address* ] [ **vsi** *vsi-name* ] [ **verbose** ] command to check information about MAC address entries.
* Run the [**display mac-address static**](cmdqueryname=display+mac-address+static) [ **vsi** *vsi-name* ] command to check information about static MAC address entries.
* Run the [**display mac-address dynamic**](cmdqueryname=display+mac-address+dynamic) [ **vsi** *vsi-name* ] command to check information about dynamic MAC address entries.
* Run the [**display mac-address blackhole**](cmdqueryname=display+mac-address+blackhole) [ **vsi** *vsi-name* ] [ **verbose** ] command to check information about static blackhole MAC address entries.
* Run the [**display mac-limit**](cmdqueryname=display+mac-limit) [ **vsi** *vsi-name* ] command to check MAC address learning limit rules.
* Run the [**display vsi**](cmdqueryname=display+vsi) [ ****name**** *vsi-name* ] **verbose** command to check the MAC address learning mode.