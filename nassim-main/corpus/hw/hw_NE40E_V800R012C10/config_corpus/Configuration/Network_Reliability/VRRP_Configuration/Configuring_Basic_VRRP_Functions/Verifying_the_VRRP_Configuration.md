Verifying the VRRP Configuration
================================

After the configurations of a Virtual Router Redundancy Protocol (VRRP) backup group are complete, you can view the status of the VRRP group.

#### Prerequisites

A VRRP group has been configured.


#### Procedure

* Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** *interface-type* *interface-number* [ *virtual-router-id* ] ] [ **brief** ] command to check information about the VRRP group.
* Run the **[**display vrrp state-change interface**](cmdqueryname=display+vrrp+state-change+interface)** { **interface-nam*e* | **interface-type** **interface-number** } ****vrid**** **virtual-router-id** command to check the status change of a specified VRRP group.
* Run the **[**display vrrp**](cmdqueryname=display+vrrp)** [ **interface** { **interface-name** | *interface-type* *interface-number* } ] [ **virtual-router-id** ] ****statistics**** command to check the status, configurations, and statistics about sent and received packets of the VRRP group.