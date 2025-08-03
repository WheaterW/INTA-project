(Optional) Configuring IPv6 IS-IS to Discard a Specified LSP
============================================================

(Optional) Configuring IPv6 IS-IS to Discard a Specified LSP

#### Context

IPv6 IS-IS can be configured to discard a specified LSP in the following scenarios:

1. When devices on the entire network restart repeatedly due to abnormal LSPs and you have located the LSP that causes protocol restarts, you can configure this function as a last resort to prevent the device from restarting continuously. However, if this function is incorrectly configured, routing loops may occur.

2. If an LSP is identified as an attack packet, which is not supposed to appear in the local area, and the LSP has caused serious problems, such as device restarts, you can configure this function to filter out the LSP under the condition that the attack source cannot be located temporarily and that the LSP does not affect topology path computation.

3. If an LSP is identified as an attack packet, which is not supposed to appear in the local area, and it affects topology path computation and has caused serious problems, such as network-wide device restarts, you can configure this function on each device to discard the LSP to prevent it from participating in network-wide calculation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure the device to discard a specified LSP.
   
   
   ```
   [ignore-receive-lsp](cmdqueryname=ignore-receive-lsp) { system-id sysid | lsp-id  lspid }
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If this command is incorrectly configured, services cannot be restored even if the [**undo ignore-receive-lsp**](cmdqueryname=undo+ignore-receive-lsp) { **system-id** *sysid* | **lsp-id** *lspid* } command is run. In this case, you may need to reset the process to restore services.
   
   To filter out the LSP that affects topology path computation, you must ensure that it is removed from all the LSDBs on the entire network. Otherwise, routing loops may occur.
   
   You are advised not to run this command to filter out the LSPs that exist on the network as running this command may filter out normal service LSPs.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```