Configuring an Aging Time for Dynamic PMTU Entries
==================================================

Configuring an Aging Time for Dynamic PMTU Entries

#### Context

When a device functions as a source node and sends packets to a destination node, the device dynamically negotiates the PMTU with the destination node based on the interface IPv6 MTUs. Packets are then fragmented based on the PMTU. After the aging time is reached, the dynamically obtained PMTU is deleted and then the source node dynamically renegotiates the PMTU with the destination node.

The interface MTU, interface IPv6 MTU, and PMTU are valid only for packets generated on the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an aging time for dynamic PMTU entries.
   
   
   ```
   [ipv6 pathmtu age](cmdqueryname=ipv6+pathmtu+age) age-time
   ```
   
   The aging time is the lifetime of dynamic PMTU entries in the buffer. Static PMTU entries do not age.
   
   When both static and dynamic PMTUs are configured, only the static PMTU takes effect.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```