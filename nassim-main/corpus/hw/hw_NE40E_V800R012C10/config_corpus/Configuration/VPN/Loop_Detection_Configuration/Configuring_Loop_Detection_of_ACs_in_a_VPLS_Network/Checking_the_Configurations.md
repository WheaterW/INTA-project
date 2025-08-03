Checking the Configurations
===========================

After configuring successfully, you can check information about the loop detect status and loop detect blocking of each interface.

#### Procedure

* Run the [**display loop-detect interface**](cmdqueryname=display+loop-detect+interface) { **ethernet** | **gigabitethernet** | **eth-trunk** } *interface-number* [ .*subinterface-number* ] command to check whether the interface is enabled with the loop detect function.
* Run the [**display loop-detect block**](cmdqueryname=display+loop-detect+block) { **all** | **interface** { **ethernet** | **gigabitethernet** | **eth-trunk** } *interface-number* [ .*subinterface-number* ] } command to check whether the interface is blocked.