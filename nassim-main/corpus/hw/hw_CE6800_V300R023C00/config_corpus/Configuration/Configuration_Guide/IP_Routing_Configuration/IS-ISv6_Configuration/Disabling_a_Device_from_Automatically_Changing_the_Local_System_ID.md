Disabling a Device from Automatically Changing the Local System ID
==================================================================

Disabling a Device from Automatically Changing the Local System ID

#### Context

By default, a device automatically changes the local system ID in the following situations:

* It detects a system ID conflict on the network.
* The sequence number of a local LSP reaches the maximum value.![](public_sys-resources/note_3.0-en-us.png) 
  
  The device automatically changes the local system ID up to three times.

You can disable a device from automatically changing the local system ID as required.


#### Procedure

* Disable the device from automatically changing the local system ID even if a system ID conflict is detected on the network.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Disable the device from automatically changing the local system ID even if a system ID conflict is detected on the network.
     
     
     ```
     [isis system-id auto-recover disable](cmdqueryname=isis+system-id+auto-recover+disable)
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Disable the device from automatically changing the local system ID even if the sequence number of a local LSP reaches the maximum value.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Disable the device from automatically changing the local system ID even if the sequence number of a local LSP reaches the maximum value.
     
     
     ```
     [isis lsp seq-overflow auto-recover disable](cmdqueryname=isis+lsp+seq-overflow+auto-recover+disable)
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display isis system-id conflict**](cmdqueryname=display+isis+system-id+conflict) command to check information about system ID conflicts.