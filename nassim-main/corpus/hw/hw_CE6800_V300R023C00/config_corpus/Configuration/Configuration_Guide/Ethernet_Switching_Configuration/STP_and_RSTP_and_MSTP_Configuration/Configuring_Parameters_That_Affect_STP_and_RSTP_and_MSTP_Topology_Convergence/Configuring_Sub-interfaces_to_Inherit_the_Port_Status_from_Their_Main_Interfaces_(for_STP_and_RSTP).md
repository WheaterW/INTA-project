Configuring Sub-interfaces to Inherit the Port Status from Their Main Interfaces (for STP/RSTP)
===============================================================================================

Configuring Sub-interfaces to Inherit the Port Status from Their Main Interfaces (for STP/RSTP)

#### Prerequisites

The STP working mode has been set to STP or RSTP.


#### Context

If a loop occurs on the network where a Layer 2 sub-interface resides, you can configure the Layer 2 sub-interface to inherit the port status of its main interface to break the loop.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure Layer 2 sub-interfaces to inherit the port status of their main interface.
   
   
   ```
   [loop-protect l2-subinterface enable](cmdqueryname=loop-protect+l2-subinterface+enable)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the interface view to check whether Layer 2 sub-interfaces inherit the port status of their main interface.