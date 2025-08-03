Enabling URPF on an Interface
=============================

Enabling URPF on an Interface

#### Prerequisites

Before configuring URPF, you have completed the following tasks:

Configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

When configuring URPF, you need to enable the URPF function on an interface.


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
4. Enable URPF on the interface.
   
   
   ```
   [ip urpf enable](cmdqueryname=ip+urpf+enable)
   ```
   
   By default, URPF is disabled on an interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```