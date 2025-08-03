Setting the Aging Time of Dynamic PMTU Entries
==============================================

The PMTU aging time changes the lifetime of dynamic PMTU entries in the buffer. Static PMTU entries do not age.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pathmtu age**](cmdqueryname=ipv6+pathmtu+age) *age-time*
   
   
   
   The aging time of dynamic PMTU entries is set.
   
   
   
   The PMTU aging time changes the lifetime of the dynamic PMTU entries in the buffer and does not function static PMTU entries, because static PMTU entries do not age.
   
   When both static and dynamic PMTUs are configured, only static PMTUs take effect.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.