(Optional) Enabling LSP Fragment Extension on an IS-IS Device (IPv6)
====================================================================

If the LSP capacity is insufficient, newly imported routes and new TLVs fail to be added to LSP fragments. In this case, you can use LSP fragment extension to increase the LSP capacity, restoring the LSP space. When the LSP capacity is restored, the system automatically attempts to re-add these routes and TLVs to LSP fragments.

#### Context

The [**lsp-fragments-extend**](cmdqueryname=lsp-fragments-extend) command enables LSP fragment extension on an IS-IS device in a specified mode and at a specified level. An LSP fragment number occupies only one byte and therefore a maximum of 256 fragments are supported. If there is a large amount of LSP content and the number of fragments exceeds 256, some information is lost. LSP fragment extension can address such a problem. You can run the [**virtual-system**](cmdqueryname=virtual-system) command to configure one or more virtual systems to support more than 256 LSP fragments.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and the IS-IS view is displayed.
3. Run [**lsp-fragments-extend**](cmdqueryname=lsp-fragments-extend) [ [ **level-1** | **level-2** | **level-1-2** ] | [ **mode-1** | **mode-2** ] ] \*
   
   
   
   LSP fragment extension is enabled on the IS-IS device in a specified mode and at a specified level.