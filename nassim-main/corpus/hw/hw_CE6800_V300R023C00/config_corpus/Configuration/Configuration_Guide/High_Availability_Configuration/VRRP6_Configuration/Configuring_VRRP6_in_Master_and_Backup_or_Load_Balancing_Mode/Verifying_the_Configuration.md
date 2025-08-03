Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display vrrp6**](cmdqueryname=display+vrrp6) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-id* ] command to check VRRP6 group information.
* Run the [**display vrrp6**](cmdqueryname=display+vrrp6) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-id* ] **verbose** command to check detailed information about the VRRP6 group.
* Run the [**display vrrp6 load-balance**](cmdqueryname=display+vrrp6+load-balance) [ **interface** *interface-type* *interface-number* **vrid** *virtual-router-id* ] [ **member-vrrp** [ **vrid** *member-vrrp-virtual-router-id* ] ] command to check information about all LBRGs and their member groups or a specific one.
* Run the **[**display vrrp6 state-change interface**](cmdqueryname=display+vrrp6+state-change+interface)** { **interface-name** | *interface-type* *interface-number* } ****vrid**** **virtual-router-id** command to check the status change of a specified VRRP6 group.