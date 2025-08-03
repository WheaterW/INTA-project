Verifying the Configuration
===========================

After configuring basic functions for a VRRP6 group, you can check information about the VRRP6 group.

#### Prerequisites

The basic functions have been configured for a VRRP6 group.


#### Procedure

* Run the [**display vrrp6**](cmdqueryname=display+vrrp6) **interface** *interface-type* *interface-number* [ **vrid** *virtual-id* ] [**brief**](cmdqueryname=brief) command to check the brief information about the VRRP6 group.
* Run the [**display vrrp6**](cmdqueryname=display+vrrp6) **interface** *interface-type* *interface-number* [ **vrid** *virtual-id* ] **verbose** command to check the detailed information about the VRRP6 group.
* Run the **[**display vrrp6 state-change interface**](cmdqueryname=display+vrrp6+state-change+interface)** { **interface-name** | *interface-type* *interface-number* } ****vrid**** **virtual-router-id** command to check the status change of a specified VRRP6 group.