(Optional) Configuring TE Attributes for a Link
===============================================

TE link attributes, including the link bandwidth, administrative group, affinity, and SRLG, can be configured for you to select links for CR-LSP establishment.

#### Context

TE link attributes are as follows:

* Link bandwidth
  
  The link bandwidth attribute can be set to limit the CR-LSP bandwidth.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If no bandwidth is set for a link, the CR-LSP bandwidth may be higher than the maximum reservable link bandwidth. As a result, the CR-LSP cannot be established.
* TE metric of the link
  
  The IGP metric or TE metric of a link can be used for path calculation of a TE tunnel. In this manner, the path calculation of the TE tunnel is more independent of the IGP, and the path of the TE tunnel can be controlled more flexibly.
* Administrative group and affinity
  
  An affinity determines attributes for links to be used by an MPLS TE tunnel. The affinity property, together with the link administrative group attribute, is used to determine which links a tunnel uses.
  
  An affinity can be set using either a hexadecimal number or a name.
  + Hexadecimal number: A 32-bit hexadecimal number is set for each affinity and link administrative group attribute, which causes plan and computation difficulties. This is the traditional configuration mode of the NE40E.
  + Name: This mode is newly supported by the NE40E. Each bit of the 32-bit administrative group and affinity attribute is named, which simplifies configuration and maintenance. This mode is recommended.
* SRLG
  
  A shared risk link group (SRLG) is a set of links which are likely to fail concurrently because they share a physical resource (for example, an optical fiber). In an SRLG, if one link fails, the other links in the SRLG also fail.
  
  An SRLG enhances CR-LSP reliability on an MPLS TE network with CR-LSP hot standby or TE FRR enabled. Two or more links are at the same risk if they share physical resources. For example, links on an interface and its sub-interfaces are in an SRLG. Sub-interfaces share risks with their interface. These sub-interfaces will go down if the interface goes down. If the links of a primary tunnel and a backup or bypass tunnel are in the same SRLG, the links of the backup or bypass tunnel share risks with the links of the primary tunnel. The backup or bypass tunnel will go down if the primary tunnel goes down.

#### Procedure

* Configure link bandwidth.
  
  
  
  The bandwidth value is set on outbound interfaces along links of a TE tunnel that requires sufficient bandwidth.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of an MPLS TE-enabled interface is displayed.
  3. Run [**mpls te bandwidth max-reservable-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth) *max-bw-value*
     
     
     
     The maximum reservable link bandwidth is set.
  4. Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **bc0** *bc0-bw-value*
     
     
     
     The BC bandwidth is set for the link.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The maximum reservable bandwidth of a link cannot be higher than the actual bandwidth of the link. A maximum of 80% of the link bandwidth is recommended for the maximum reservable link bandwidth.
     + The BC0 bandwidth cannot be higher than the maximum reservable link bandwidth.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the TE metric value of a link.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of an MPLS TE-enabled interface is displayed.
  3. Run [**mpls te metric**](cmdqueryname=mpls+te+metric) *metric-value*
     
     
     
     The TE metric of a link is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an affinity and a link administrative group attribute in hexadecimal format.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + The modified administrative group takes effect only on LSPs that will be established, not on LSPs that have been established.
  + After the modified affinity is committed, the system will recalculate a path for the TE tunnel, and the established LSPs in this TE tunnel are affected.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view of an MPLS TE link is displayed.
  3. Run [**mpls te link administrative group**](cmdqueryname=mpls+te+link+administrative+group) *group-value*
     
     
     
     An administrative group is configured for the link.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The view of the MPLS TE tunnel interface is displayed.
  6. Run [**mpls te affinity property**](cmdqueryname=mpls+te+affinity+property) *properties* [ **mask** *mask-value* ] [ **secondary** | **best-effort** ]
     
     
     
     An affinity is set for the MPLS TE tunnel.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Name hexadecimal bits of an affinity and a link administrative group attribute.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + The modified administrative group takes effect only on LSPs that will be established, not on LSPs that have been established.
  + After the modified affinity is committed, the system will recalculate a path for the TE tunnel, and the established LSPs in this TE tunnel are affected.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping)
     
     
     
     An affinity name template is configured, and the affinity mapping view is displayed.
     
     
     
     This template must be configured on each node involved in MPLS TE path computation, and the global mappings between the names and values of affinity bits must be the same on all the involved nodes.
  3. Run [**attribute**](cmdqueryname=attribute) *bit-name* **bit-sequence** *bit-number*
     
     
     
     A mapping between an affinity bit and name is configured.
     
     
     
     There are 32 affinity bits in total. You can repeat this step to configure some or all affinity bits.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of an MPLS TE link is displayed.
  6. Run [**mpls te link administrative group name**](cmdqueryname=mpls+te+link+administrative+group+name) { *name-string* } &<1-32>
     
     
     
     Bit names are set for a link administrative group.
     
     
     
     The *name-string* value must be in the range specified in the affinity name mapping template.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The view of the MPLS TE tunnel interface is displayed.
  9. Run [**mpls te affinity**](cmdqueryname=mpls+te+affinity) { **primary** | **secondary** | **best-effort** } { **include-all** | **include-any** | **exclude** } *bit-name* &<1-32>
     
     
     
     An affinity is set for the MPLS TE tunnel.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure an SRLG.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  On the ingress of a hot-standby CR-LSP or a TE FRR tunnel, perform Steps 1 to 3. On the interface of each SRLG member, perform Step 5 and Step 6.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te srlg path-calculation**](cmdqueryname=mpls+te+srlg+path-calculation) [ **preferred** | **strict** ]
     
     
     
     An SRLG path calculation mode is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If **strict** is configured, CSPF uses an SRLG as a constraint when calculating a path for a bypass or backup CR-LSP.
     + If **preferred** is configured, CSPF uses an SRLG as a constraint when calculating a path for a bypass or backup CR-LSP for the first time; if calculation fails, CSPF no longer uses the SRLG as a constraint.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  6. Run [**mpls te srlg**](cmdqueryname=mpls+te+srlg) *srlg-number*
     
     
     
     The link on which the interface resides joins the SRLG.
     
     
     
     On a network with hot standby or TE FRR, the SRLG attribute needs to be configured for the outbound interface of the ingress on a tunnel and other members of the SRLG. A link joins an SRLG after the SRLG attribute is configured on an outbound interface of the link.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To delete the SRLG attribute from all interfaces on a device, run the [**undo mpls te srlg all-config**](cmdqueryname=undo+mpls+te+srlg+all-config) command in the MPLS view.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.