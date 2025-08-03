Clearing the Statistics of VLAN Packets
=======================================

Before collecting traffic statistics in a specified time period on an interface, you need to reset the original statistics on the interface.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics of VLAN packets cannot be restored after you clear it. So, confirm the action before you use the command.

To clear the statistics of VLAN packets, run the following [**reset**](cmdqueryname=reset) command in the user view:


#### Procedure

* Run the [**reset statistics**](cmdqueryname=reset+statistics) **interface** *interface type interface number* **vlan** *vlan-id* command to clear the VLAN packet statistics on a specified interface.