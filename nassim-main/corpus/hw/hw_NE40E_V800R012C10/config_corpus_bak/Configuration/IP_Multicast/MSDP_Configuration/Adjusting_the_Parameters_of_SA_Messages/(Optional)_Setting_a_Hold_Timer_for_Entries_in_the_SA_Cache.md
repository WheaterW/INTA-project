(Optional) Setting a Hold Timer for Entries in the SA Cache
===========================================================

The NE40E supports hold timer adjustment for the (S, G) entries in the SA cache.

#### Context

You can adjust the hold timer for the (S, G) entries in the SA cache on the NE40E. After the hold timer is adjusted, the device applies the new timer to the (S, G) entries corresponding to newly received SA messages.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**multicast routing-enable**](cmdqueryname=multicast+routing-enable) command to enable multicast routing.
3. Run the [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ] command to enter the MSDP view.
4. Run the [**sa-cache-holdtime**](cmdqueryname=sa-cache-holdtime) *holdtime* command to set a hold timer for the entries in the SA cache.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.