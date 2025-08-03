Verifying the Configuration
===========================

After configuring OSPFv3 authentication, you can check the configurations.

#### Prerequisites

OSPFv3 authentication has been configured.


#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] command to view the SA applied in a specified process.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3)  [ *process-id* ] **area** [ *area-id* ] command to view the SA applied in a specified area.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3)  [ *process-id* ] **interface** [ ****area**** { **area-id** | **area-idIpv4** }] [ **interfaceType** **interfaceNum** | **interfaceName** ] command to check the SA applied to the interface.