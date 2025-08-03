Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-id* ] [ **verbose** ] command to check the VRRP group status.
* Run the [**display vrrp load-balance**](cmdqueryname=display+vrrp+load-balance) [ **interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id* ] [ **member-vrrp** [ **vrid** *member-vrrp-virtual-router-id* ] ] command to check information about all LBRGs and their member groups or a specific one.
* Run the **[**display vrrp state-change interface**](cmdqueryname=display+vrrp+state-change+interface)** { **interface-nam*e* | **interface-type** **interface-number** } ****vrid**** **virtual-router-id** command to check the status change of a specified VRRP group.
* Run the **[**display vrrp**](cmdqueryname=display+vrrp)** [ **interface** { **interface-name** | *interface-type* *interface-number* } ] [ **virtual-router-id** ] ****statistics**** command to check the status, configurations, and statistics about sent and received packets of the VRRP group.