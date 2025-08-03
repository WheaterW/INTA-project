Creating a RIPng Process
========================

Creating a RIPng Process

#### Context

Before running RIPng on a routing device, you must create a RIPng process.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIPng process and enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
   
   
   
   RIPng supports multi-instance. To bind a RIPng process to a VPN instance, you can run the [**ripng**](cmdqueryname=ripng) [ *process-id* ] **vpn-instance** *vpn-instance-name* command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If you have run RIPng-related commands in the interface view before RIPng is enabled, the command configurations will take effect only after RIPng is enabled.
3. (Optional) Configure a description for the RIPng process.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```