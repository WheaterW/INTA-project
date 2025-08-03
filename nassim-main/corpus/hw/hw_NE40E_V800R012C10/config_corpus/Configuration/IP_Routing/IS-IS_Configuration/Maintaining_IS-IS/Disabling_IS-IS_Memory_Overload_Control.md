Disabling IS-IS Memory Overload Control
=======================================

IS-IS memory overload control is enabled by default and can be disabled.

#### Context

If the system memory is overloaded, each module needs to take necessary measures to control the memory usage increase or even reduce the memory usage. In this case, the IS-IS module takes any of the following measures to improve IS-IS resilience: restrict the establishment of new neighbor relationships, set the Overload bit in LSP fragment zero to be sent and reject new LSPs from neighbors, restrict the installation of newly imported routes, or delete imported routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**isis memory-overload exception-threshold discard new-lsp**](cmdqueryname=isis+memory-overload+exception-threshold+discard+new-lsp)
   
   
   
   IS-IS is enabled to set the Overload bit in its LSP fragment zero (to be sent) to 1 and discard new LSPs (received) if the system memory is overloaded and the memory usage of the IS-IS LSDB component is not among the top 3.
   
   
   
   If the system memory is overloaded and the memory usage of the IS-IS LSDB component is among the top 3, IS-IS sets the Overload bit in its LSP fragment zero (to be sent) to 1 and discards new LSPs (received) by default to improve IS-IS resilience. However, if the memory usage of the IS-IS LSDB component is not among the top 3 and new IS-IS services are added, the IS-IS LSDB component will consume more memory resources, aggravating the system memory overload issue. To prevent this issue, run the [**isis memory-overload exception-threshold discard new-lsp**](cmdqueryname=isis+memory-overload+exception-threshold+discard+new-lsp) command, which enables IS-IS to set the Overload bit in its LSP fragment zero (to be sent) to 1 and discard new LSPs (received). To disable this function, run the [**undo isis memory-overload exception-threshold discard new-lsp**](cmdqueryname=undo+isis+memory-overload+exception-threshold+discard+new-lsp) command.
   
   IS-IS memory overload control is enabled by default. If you disable this function by performing the next step, the configuration in this step will become invalid.
3. Run [**isis memory-overload control disable**](cmdqueryname=isis+memory-overload+control+disable)
   
   
   
   IS-IS memory overload control is disabled.
   
   
   
   To minimize the impact of memory overload on services, you are advised to keep IS-IS memory overload control enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.