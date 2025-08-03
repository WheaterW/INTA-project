Configuring Poison Reverse
==========================

Configuring Poison Reverse

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
4. Enable poison reverse.
   
   
   ```
   [ripng poison-reverse](cmdqueryname=ripng+poison-reverse)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If both split horizon and poison reverse are configured, only poison reverse takes effect.
   
   On non-broadcast multiple access (NBMA) networks, poison reverse is enabled on interfaces by default. On other types of networks, poison reverse is disabled on interfaces by default.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```