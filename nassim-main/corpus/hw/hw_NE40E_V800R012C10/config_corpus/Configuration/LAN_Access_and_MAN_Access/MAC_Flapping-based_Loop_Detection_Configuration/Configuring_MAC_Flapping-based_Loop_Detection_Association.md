Configuring MAC Flapping-based Loop Detection Association
=========================================================

To inform the network administrator of loops in a timely manner, enable MAC flapping-based loop detection association on the main interfaces for sub-interfaces bound to virtual switching instances (VSIs) or bridge domains (BDs). If a loop occurs in a VSI or a BD, the associated sub-interface is blocked. Then, the main interface where the sub-interface resides is also blocked, and an alarm is reported. After the main interface is blocked, all its sub-interfaces (except EVC Layer 2 sub-interfaces) bound to VSIs or BDs are blocked.

#### Usage Scenario

MAC flapping-based loop detection association is supported. If a loop occurs in the VSI or the BD bound to a sub-interface, the sub-interface is blocked. However, a loop may also exist in a VSI or a BD bound to another sub-interface. If the loop is not eliminated in time, it will cause traffic congestion or even a network breakdown. To inform the network administrator of loops, enable MAC flapping-based loop detection association on the interface of the sub-interfaces bound with VSIs or BDs. In this situation, if a sub-interface bound with a VSI or a BD is blocked due to a loop, its interface is also blocked and an alarm is generated. After that, all the other sub-interfaces bound with VSIs or BDs are blocked.


#### Pre-configuration Tasks

Before configuring MAC flapping-based loop detection association, configure MAC flapping-based loop detection for a VPLS network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The Ethernet interface view is displayed.
3. Run [**monitor mac-shift**](cmdqueryname=monitor+mac-shift)
   
   
   
   MAC flapping-based loop detection association is enabled on the interface.
   
   
   
   The [**monitor mac-shift**](cmdqueryname=monitor+mac-shift) command can be run on both Layer 2 and Layer 3 interfaces.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring MAC flapping-based loop detection association, check the configurations as follows:

Run the [**display loop-detect eth-loop**](cmdqueryname=display+loop-detect+eth-loop) [ **vsi** *vsi-name* | **bridge-domain** *bd-id* ] command to view the configuration information of MAC flapping-based loop detection in a VSI or a BD. **Link-Block Port** shows the associated interface.