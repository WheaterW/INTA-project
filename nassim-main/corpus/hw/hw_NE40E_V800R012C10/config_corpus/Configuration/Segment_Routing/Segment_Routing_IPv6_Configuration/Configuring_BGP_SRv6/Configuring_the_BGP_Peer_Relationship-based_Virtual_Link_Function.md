Configuring the BGP Peer Relationship-based Virtual Link Function
=================================================================

A virtual link across the Layer 3 network can be created for a controller to compute paths.

#### Context

A virtual link across the Layer 3 network can be created based on the BGP peer relationship, with the local and remote IPv6 addresses of the virtual link being the same as those used to establish the peer relationship. Based on this link, topology information is reported to the controller for path computation. On the controller, only a virtual link with a reachable route is displayed in the topology. You can configure TE metric, affinity attribute, and TWAMP latency measurement for the virtual link. When binding a TWAMP test session to the virtual link, ensure that the local and remote addresses of the test session are the same as those of the link.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
   
   
   
   BGP is enabled, and the BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv6-address* **virtual-link**
   
   
   
   The BGP peer relationship-based virtual link function is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   BGP EPE must be configured before you enable the BGP peer relationship-based virtual link function.
4. Configure TE attributes, including link latency, metric, affinity, and SRLG attributes. These TE attributes can be transmitted to a controller through BGP-LS, allowing the controller to adjust SRv6 TE Policies based on the attributes.
   
   
   * Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **virtual-link twamp-light test-session** *session-id* command to configure TWAMP Light detection for the specified virtual link.
     
     When binding a test session to a BGP virtual link, ensure that the local and remote addresses of the test session are the same as those of the virtual link.
     
     Before running this command, you need to configure a TWAMP Light IPv6 session.
   * Run the [**peer**](cmdqueryname=peer) *ipv6-address* **virtual-link te link administrative group** *group-value* or [**peer**](cmdqueryname=peer) *ipv6-address* **virtual-link te link administrative group name** { *name-string* } &<1-32> command to configure an affinity value or name for the specified virtual link.
     
     Before running this command, you need to run the [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping) command in the system view to create an affinity name template and run the [**attribute**](cmdqueryname=attribute) *affinity-name* **bit-sequence** *bit-number* command in the template view to configure the mapping between affinity names and bits.
   * Run the [**peer**](cmdqueryname=peer) *ipv6-address* **virtual-link te metric** *metric-value* command to configure a metric value for the specified virtual link.
   * Run the [**peer**](cmdqueryname=peer) *ipv6-address* **virtual-link te srlg** { *srlgValue* } &<1-64> command to add the specified virtual link to an SRLG.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.