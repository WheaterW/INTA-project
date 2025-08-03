(Optional) Disabling the Multi-Process Mode of the FEI Component
================================================================

(Optional) Disabling the Multi-Process Mode of the FEI Component

#### Context

The multi-process mode of the FEI component is enabled by default, which helps improve the concurrent service processing capability of the device.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**undo set fei multi-thread enable**](cmdqueryname=undo+set+fei+multi-thread+enable) command to disable the multi-process mode of the FEI component.
   
   
   
   To re-enable the multi-process mode of the FEI component, run the [**set fei multi-thread enable**](cmdqueryname=set+fei+multi-thread+enable) command.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.