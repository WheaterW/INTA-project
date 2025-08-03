Verifying the Configuration
===========================

After EVPN in ring network access mode is configured, you can check the spanning tree status of ports in the MSTP process on ring network devices and check EVPN route information on PEs.

#### Prerequisites

EVPN in ring network access mode has been configured.


#### Procedure

* Run the [**display stp process**](cmdqueryname=display+stp+process) [ *process-id* ] **brief** command to check the spanning tree status of ports in a specified MSTP process.
* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) **ad-route** *prefix* command to check whether the extended community attribute of a specified Ethernet A-D route carries the ring ID attribute.