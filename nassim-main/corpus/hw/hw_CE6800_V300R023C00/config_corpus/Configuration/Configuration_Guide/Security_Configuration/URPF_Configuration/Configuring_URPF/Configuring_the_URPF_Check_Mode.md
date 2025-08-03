Configuring the URPF Check Mode
===============================

Configuring the URPF Check Mode

#### Context

URPF check can be performed in strict or loose mode. You can configure the **allow default-route** parameter to allow packets to match the default route.

![](public_sys-resources/note_3.0-en-us.png) 

It is recommended that URPF be enabled before services are configured. If you need to enable URPF after services are configured, configure URPF during off-peak hours and ensure that service requirements on the live network can be met even when the maximum number of FIB entries is reduced by half.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the URPF check mode.
   1. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Switch the interface working mode to Layer 3.
      
      
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
      
      Determine whether to perform this step based on the current interface working mode.
   3. Configure the URPF check mode on the interfaces.
      
      
      ```
      [ip urpf](cmdqueryname=ip+urpf) { loose | strict }
      ```
      
      By default, URPF is disabled on an interface. If URPF is enabled on an interface, the default URPF check mode is loose.
   4. Configure the default route to participate in URPF check.
      
      
      ```
      [ip urpf](cmdqueryname=ip+urpf) allow default-route
      ```
      
      By default, no default route is configured to participate in URPF check.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```