Configuring TE Attributes
=========================

Configure TE attributes for links so that SR-MPLS TE paths can be adjusted based on the TE attributes during path computation.

#### Context

TE link attributes are as follows:

* Link bandwidth
  
  This attribute must be configured if you want to limit the bandwidth of an SR-MPLS TE tunnel link.
* Dynamic link bandwidth
  
  Dynamic bandwidth can be configured if you want TE to be aware of physical bandwidth changes on interfaces.
* TE metric of a link
  
  Either the IGP metric or TE metric of a link can be used during SR-MPLS TE path computation. If the TE metric is used, SR-MPLS TE path computation is more independent of IGP, implementing flexible tunnel path control.
* Administrative group and affinity attribute
  
  An SR-MPLS TE tunnel's affinity attribute determines its link attribute. The affinity attribute and link administrative group are used together to determine the links that can be used by the SR-MPLS TE tunnel.
* SRLG
  
  A shared risk link group (SRLG) is a group of links that share a public physical resource, such as an optical fiber. Links in an SRLG are at the same risk of faults. If one of the links fails, other links in the SRLG also fail.
  
  An SRLG enhances SR-MPLS TE reliability on a network with CR-LSP hot standby or TE FRR enabled. Links that share the same physical resource have the same risk. For example, links on an interface and its sub-interfaces are in an SRLG. The interface and its sub-interfaces have the same risk. If the interface goes down, its sub-interfaces will also go down. Similarly, if the link of the primary path of an SR-MPLS TE tunnel and the links of the backup paths of the SR-MPLS TE tunnel are in an SRLG, the backup paths will most likely go down when the primary path goes down.

#### Procedure

* (Optional) Configure link bandwidth.
  
  
  
  Link bandwidth needs to be configured only on outbound interfaces of SR-MPLS TE tunnel links that have bandwidth requirements.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**mpls te bandwidth max-reservable-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth) *max-bw-value*
     
     
     
     The maximum reservable link bandwidth is configured.
  4. Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **bc0** *bc0-bw-value*
     
     
     
     The BC0 bandwidth is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The maximum reservable link bandwidth cannot be higher than the physical link bandwidth. You are advised to set the maximum reservable link bandwidth to be less than or equal to 80% of the physical link bandwidth.
     + The BC0 bandwidth cannot be higher than the maximum reservable link bandwidth.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure dynamic link bandwidth.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**mpls te bandwidth max-reservable-bandwidth dynamic**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth+dynamic) *max-dynamic-bw-value*
     
     
     
     The maximum reservable dynamic link bandwidth is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If this command is run in the same interface view as the [**mpls te bandwidth max-reservable-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth) command, the later configuration overrides the previous one.
  4. (Optional) Run [**mpls te bandwidth max-reservable-bandwidth dynamic baseline remain-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth+dynamic+baseline+remain-bandwidth)
     
     
     
     The device is configured to use the remaining bandwidth of the interface when calculating the maximum dynamic reservable bandwidth for TE.
     
     
     
     In scenarios such as channelized sub-interface and bandwidth lease, the remaining bandwidth of an interface changes, but the physical bandwidth does not. In this case, the actual forwarding capability of the interface decreases; however, the dynamic maximum reservable bandwidth of the TE tunnel is still calculated based on the physical bandwidth. As a result, the calculated TE bandwidth is greater than the actual bandwidth, and the actual forwarding capability of the interface does not meet the bandwidth requirement of the tunnel.
  5. Run [**mpls te bandwidth dynamic**](cmdqueryname=mpls+te+bandwidth+dynamic) **bc0** *bc0-bw-percentage*
     
     
     
     The BC0 dynamic bandwidth is configured for the link.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If this command is run in the same interface view as the [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **bc0** command, the later configuration overrides the previous one.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure a TE metric for a link.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**mpls te metric**](cmdqueryname=mpls+te+metric) *metric-value*
     
     
     
     A TE metric is configured for the link.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the administrative group and affinity attribute in hexadecimal format.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**mpls te link administrative group**](cmdqueryname=mpls+te+link+administrative+group) *group-value*
     
     
     
     A TE link administrative group is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the administrative group and affinity attribute based on the affinity and administrative group names.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping)
     
     
     
     An affinity name template is configured, and the affinity mapping view is displayed.
     
     
     
     This template must be configured on each node involved in SR-MPLS TE path computation, and the global mappings between the names and values of affinity bits must be the same on all the involved nodes.
  3. Run [**attribute**](cmdqueryname=attribute) *bit-name* **bit-sequence** *bit-number*
     
     
     
     Mappings between affinity bit values and names are configured.
     
     
     
     This step configures only one bit of an affinity attribute, which has a total of 32 bits. Repeat this step as needed to configure some or all of the bits.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  6. Run [**mpls te link administrative group name**](cmdqueryname=mpls+te+link+administrative+group+name) { *name-string* } &<1-32>
     
     
     
     A link administrative group is configured.
     
     
     
     The *name-string* value must be in the range specified for the affinity attribute in the template.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure an SRLG.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**mpls te srlg**](cmdqueryname=mpls+te+srlg) *srlg-number*
     
     
     
     The interface is added to an SRLG.
     
     
     
     In a hot-standby or TE FRR scenario, you need to configure SRLG attributes for the SR-MPLS TE outbound interface of the ingress and other member links in the SRLG to which the interface belongs. A link joins an SRLG only after SRLG attributes are configured for any outbound interface of the link.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To delete the SRLG attribute configurations of all interfaces on the local node, run the [**undo mpls te srlg all-config**](cmdqueryname=undo+mpls+te+srlg+all-config) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.