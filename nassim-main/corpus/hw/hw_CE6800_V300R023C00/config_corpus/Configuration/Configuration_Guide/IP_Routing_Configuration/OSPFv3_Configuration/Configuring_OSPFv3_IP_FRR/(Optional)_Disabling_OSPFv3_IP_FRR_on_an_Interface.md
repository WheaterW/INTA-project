(Optional) Disabling OSPFv3 IP FRR on an Interface
==================================================

(Optional) Disabling OSPFv3 IP FRR on an Interface

#### Context

If an interface is connected to a device running key services, ensure that a backup path does not pass through this interface in order to prevent the services from being compromised after FRR calculation. To meet this requirement, disable OSPFv3 IP FRR on the interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Disable FRR on the OSPFv3 interface.
   
   
   ```
   [ospfv3 frr block](cmdqueryname=ospfv3+frr+block)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```