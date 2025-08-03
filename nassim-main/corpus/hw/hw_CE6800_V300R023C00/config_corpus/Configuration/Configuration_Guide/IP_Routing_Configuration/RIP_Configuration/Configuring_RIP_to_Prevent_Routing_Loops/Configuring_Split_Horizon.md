Configuring Split Horizon
=========================

Configuring Split Horizon

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface mode.
4. Enable split horizon.
   
   
   ```
   [rip split-horizon](cmdqueryname=rip+split-horizon)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If both split horizon and poison reverse are configured, only poison reverse takes effect.
   
   On point-to-point (P2P) and broadcast networks, split horizon is enabled on interfaces by default. On non-broadcast multiple access (NBMA) and point-to-multipoint (P2MP) networks, split horizon is disabled on interfaces by default.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```