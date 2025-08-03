(Optional) Configuring an Aging Time for ND Entries in the Stale State
======================================================================

You can configure a shorter aging time for ND entries in the Stale state to speed up their aging.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 nd stale-timeout**](cmdqueryname=ipv6+nd+stale-timeout) *seconds*
   
   
   
   An aging time is configured for ND entries in the Stale state.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled.
5. Run [**ipv6 nd stale-timeout**](cmdqueryname=ipv6+nd+stale-timeout) *seconds*
   
   
   
   An aging time is configured for ND entries in the Stale state for the interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.