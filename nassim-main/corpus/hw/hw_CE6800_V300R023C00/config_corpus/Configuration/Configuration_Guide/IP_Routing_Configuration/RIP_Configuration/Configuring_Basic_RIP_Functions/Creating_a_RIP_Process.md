Creating a RIP Process
======================

Creating a RIP Process

#### Context

To run RIP on a device, you must first create a RIP process.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   RIP supports multi-process and multi-instance. To bind a RIP process to a VPN instance, run the [**rip**](cmdqueryname=rip) [ *process-id* ] **vpn-instance** *vpn-instance-name* command.
3. (Optional) Configure a description for the RIP process.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If RIP-related commands have been run in the interface view before a RIP process is created, the command configurations take effect only after a RIP process is created.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```