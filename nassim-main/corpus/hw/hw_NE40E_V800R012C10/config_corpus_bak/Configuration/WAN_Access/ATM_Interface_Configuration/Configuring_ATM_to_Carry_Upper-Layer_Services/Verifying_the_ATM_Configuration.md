Verifying the ATM Configuration
===============================

After configuring ATM to carry upper-layer services, verify the configuration and status of ATM interfaces or sub-interfaces, and information about Permanent Virtual Circuit (PVCs) and PVC mapping.

#### Prerequisites

ATM links have been configured to transmit different protocol packets.


#### Procedure

* Run the [**display interface atm**](cmdqueryname=display+interface+atm) [ *interface-number* | **main** ] command to check the configurations and status of ATM interfaces or sub-interfaces.
* Run the [**display atm pvc-info**](cmdqueryname=display+atm+pvc-info) [ **interface** *interface-type* *interface-number* [ **pvc** *pvc-name* [ *vpi*/*vci* ] ] ] command to check information about PVCs.
* Run the [**display atm pvc-info statistics**](cmdqueryname=display+atm+pvc-info+statistics) [ **interface** *interface-type* *interface-number* ] command to check PVC traffic statistics.
* Run the [**display atm map-info**](cmdqueryname=display+atm+map-info) [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* | *vpi*/*vci* } \* ] ] command to check information about PVC mapping.