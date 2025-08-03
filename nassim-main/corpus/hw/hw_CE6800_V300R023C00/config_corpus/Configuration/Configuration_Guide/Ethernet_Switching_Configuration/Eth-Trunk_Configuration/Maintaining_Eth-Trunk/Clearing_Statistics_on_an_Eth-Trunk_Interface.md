Clearing Statistics on an Eth-Trunk Interface
=============================================

Clearing Statistics on an Eth-Trunk Interface

#### Context

Before collecting traffic statistics within a specified period of time on an Eth-Trunk interface, you need to clear existing statistics on the interface.

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when running the following commands.



#### Procedure

[Table 1](#EN-US_TASK_0000001176741133__table193611022104820) lists the commands for clearing statistics on an Eth-Trunk interface. Run the following commands in the user view to clear statistics.

**Table 1** Clearing statistics on an Eth-Trunk interface
| Operation | Command |
| --- | --- |
| Clear packet statistics on an Eth-Trunk interface. | [**reset interface counters**](cmdqueryname=reset+interface+counters) **eth-trunk** *trunk-id* |
| Clear LACPDU statistics on an Eth-Trunk interface in LACP mode. | [**reset lacp statistics eth-trunk**](cmdqueryname=reset+lacp+statistics+eth-trunk) [ *trunk-id* [ **interface** *interface-type* *interface-number* ] ] |