Resetting the DLDP Status
=========================

Resetting the DLDP Status

#### Context

When DLDP detects a unidirectional link on an interface, the interface enters the Disable state. DLDP prompts you to shut down the interface or automatically sets the interface state to Down based on the configured DLDP shutdown mode (manual or automatic). To enable the interface to detect unidirectional links again, you can reset the DLDP status of the interface as follows:

* If the interface is manually shut down using the **shutdown** command, run the **undo shutdown** command to enable the interface to detect unidirectional links again. After running the **undo shutdown** command, you do not need to run the commands in the following procedure.
* If the system automatically sets the interface state to Down, wait for the interface to recover using the auto recovery mechanism after the link state becomes bidirectional. You can also run the run the commands in the following procedure to reset the DLDP status of the interface.

After a reset is performed, the DLDP status of the interface depends on the physical status of the interface. If the physical status is Down, the DLDP status of the interface changes to Inactive. If the physical status is Up, the DLDP status changes to Active.

When you reset the DLDP status globally on a device, the DLDP status is reset for all the disabled interfaces on the device. When you reset the DLDP status on a disabled interface, the DLDP status is reset only for this interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Reset the DLDP status globally.
   
   
   ```
   [dldp reset](cmdqueryname=dldp+reset)
   ```
3. Enter the interface or interface group view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   [port-group](cmdqueryname=port-group) port-group-name
   ```
4. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch) 
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Reset the DLDP status of the interface.
   
   
   ```
   [dldp reset](cmdqueryname=dldp+reset)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```