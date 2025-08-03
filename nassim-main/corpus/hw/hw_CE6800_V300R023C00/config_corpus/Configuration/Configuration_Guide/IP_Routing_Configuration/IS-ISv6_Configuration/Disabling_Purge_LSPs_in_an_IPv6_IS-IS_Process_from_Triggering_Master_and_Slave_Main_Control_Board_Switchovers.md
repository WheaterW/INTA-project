Disabling Purge LSPs in an IPv6 IS-IS Process from Triggering Master/Slave Main Control Board Switchovers
=========================================================================================================

Disabling Purge LSPs in an IPv6 IS-IS Process from Triggering Master/Slave Main Control Board Switchovers

#### Context

When an IS-IS process on a device sends a purge LSP, the device deletes the corresponding LSP and floods it to the network. In normal cases, before the device sends a purge LSP, the end that generated the corresponding LSP sends an updated LSP. If the clock on the device runs fast, the device frequently floods purge LSPs to devices on the entire network, causing network flapping. If the device sends more than five purge LSPs for 80% or more non-pseudonode LSPs with a non-zero fragment number in the local LSDB within 6500s, a master/slave main control board switchover is performed if the device has two main control boards, or the device is restarted if it has only one main control board. The switchover or restart prevents network flapping.

By default, purge LSPs in an IPv6 IS-IS process trigger master/slave main control board switchovers. You can disable the function as required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable purge LSPs in an IPv6 IS-IS process from triggering master/slave main control board switchovers.
   
   
   ```
   [isis purge-lsp auto-protect disable](cmdqueryname=isis+purge-lsp+auto-protect+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```