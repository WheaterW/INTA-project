Verifying the ERPSv2 Configuration
==================================

After configuring ERPSv2, verify the configuration of ports added to an ERPS ring, port roles, control VLAN ID, ERP instances, ERPS version, and timers.

#### Prerequisites

ERPSv2 has been configured.


#### Procedure

* Run the [**display erps**](cmdqueryname=display+erps) [ **ring** *ring-id* ] [ **verbose** ] command to check configurations of device ports added to an ERPS ring and ring configurations.
* Run the [**display erps interface**](cmdqueryname=display+erps+interface) *interface-type interface-number* [ **ring** *ring-id* ] command to check the physical configurations of an ERPS ring port.