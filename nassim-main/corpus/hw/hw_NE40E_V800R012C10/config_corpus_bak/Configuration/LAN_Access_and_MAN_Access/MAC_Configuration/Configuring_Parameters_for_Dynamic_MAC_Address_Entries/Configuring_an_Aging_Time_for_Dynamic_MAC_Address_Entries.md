Configuring an Aging Time for Dynamic MAC Address Entries
=========================================================

Dynamic MAC address entries do not need to be created manually and they will be aged automatically. An aging time can be configured for dynamic MAC address entries to prevent the explosive growth of MAC address entries.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mac-address aging-time**](cmdqueryname=mac-address+aging-time) *seconds* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>The aging time of dynamic MAC address entries is set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.