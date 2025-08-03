Clearing the Statistics on Eth-Trunk Interfaces
===============================================

Before collecting traffic statistics within a specified period of time on an Eth-Trunk interface, you need to clear existing statistics on the interface.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when running the following commands.



#### Procedure

* Run the [**reset counters interface eth-trunk**](cmdqueryname=reset+counters+interface+eth-trunk) [ *trunk-id* ] command in the user view to clear statistics on an Eth-Trunk interface.
* Run the [**reset lacp statistics eth-trunk**](cmdqueryname=reset+lacp+statistics+eth-trunk) [ *trunk-id* [ **interface** *interface-type* *interface-number* ] ] command in the user view to clear statistics on an Eth-Trunk interface in static LACP mode.
* Run the [**reset e-trunk packet-statistics**](cmdqueryname=reset+e-trunk+packet-statistics) [ **e-trunk-id** *e-trunk-id* ] command in the user view to clear statistics on an E-Trunk.