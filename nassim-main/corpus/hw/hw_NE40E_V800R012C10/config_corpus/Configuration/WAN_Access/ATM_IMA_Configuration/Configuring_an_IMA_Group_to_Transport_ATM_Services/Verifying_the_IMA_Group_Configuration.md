Verifying the IMA Group Configuration
=====================================

After completing configurations on an IMA group interface, verify the configuration.

#### Prerequisites

An IMA group has been configured to transport ATM services.


#### Procedure

* Run the [**display atm pvc-info**](cmdqueryname=display+atm+pvc-info) [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* [ *vpi*/*vci* ] | *vpi*/*vci* } ] ] command to check PVC information.
* Run the [**display atm service**](cmdqueryname=display+atm+service) [ *service-name* ] command to check information about the service type configured for a PVC.
* Run the [**display interface ima-group**](cmdqueryname=display+interface+ima-group) [ *group-number* ] command to check configurations and status of an IMA group interface.
* Run the [**display connectivity-test**](cmdqueryname=display+connectivity-test) **interface** *interface-type* *interface-number* { **pvc** *vpi/vci* | **pvp** *vpi* } command to check the result of continuity check on ATM services.
* Run the [**display atm llid**](cmdqueryname=display+atm+llid) command to check whether the LLID takes effect.