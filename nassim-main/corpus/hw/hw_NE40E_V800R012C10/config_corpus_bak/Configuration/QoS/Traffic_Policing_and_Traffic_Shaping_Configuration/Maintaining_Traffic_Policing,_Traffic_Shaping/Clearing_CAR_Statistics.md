Clearing CAR Statistics
=======================

This section describes how to clear CAR statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when performing this operation.

To clear CAR statistics in a specified direction on a specified interface, run the **reset** command in the user view.


#### Procedure

* Run the [**reset car statistics interface**](cmdqueryname=reset+car+statistics+interface) { *interface-type* *interface-number* | *interface-name* } [ **vlan** *vlan-id* | **vid** *vid* | **ce-vid** *ce-vid* | **vid** *vid* **ce-vid** *ce-vid* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* ] { **inbound** | **outbound** } command to clear CAR statistics in a specified direction on a specified interface.