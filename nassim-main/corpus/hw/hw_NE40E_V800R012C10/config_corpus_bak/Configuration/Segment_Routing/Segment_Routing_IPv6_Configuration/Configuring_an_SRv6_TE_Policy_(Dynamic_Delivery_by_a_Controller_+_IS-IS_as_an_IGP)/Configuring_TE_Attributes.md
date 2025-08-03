Configuring TE Attributes
=========================

After receiving TE attributes configured for links, an IGP (IS-IS/OSPFv3) advertises them to a controller through BGP-LS. This enables the controller to adjust links based on the TE attributes during SRv6 TE Policy computation.

#### Context

TE link attributes are as follows:

* Link bandwidth
  
  This attribute is mandatory if you want to limit the bandwidth of a path of an SRv6 TE Policy.
* Dynamic link bandwidth
  
  Dynamic bandwidth can be configured if you want TE to be aware of physical bandwidth changes on interfaces.
* Link-specific TE metric
  
  Either the IGP metric or link-specific TE metric can be used for SRv6 TE Policy computation by a controller. If the link-specific TE metric is used, SRv6 TE Policy path computation is more independent of IGP, implementing flexible tunnel path control.
* Administrative group and affinity attribute
  
  An SRv6 TE Policy's affinity attribute determines its link attribute. The administrative group and affinity attribute are used together to determine the links that can be used by the policy.
* SRLG
  
  A shared risk link group (SRLG) is a group of links that share a public physical resource, such as an optical fiber. Links in an SRLG are at the same risk of faults. If one of the links fails, other links in the SRLG also fail.
  
  An SRLG enhances SRv6 TE Policy reliability on a network with CR-LSP hot standby or TE FRR enabled. Links that share the same physical resource have the same risk. For example, links on an interface and its sub-interfaces are in an SRLG. The interface and its sub-interfaces have the same risk. If the interface goes down, its sub-interfaces will also go down. Similarly, if the link of the primary path of an SRv6 TE Policy and the links of the backup paths of the SRv6 TE Policy are in an SRLG and the primary path goes down, the backup paths will most likely go down.

To support SRv6 TE Policy over GRE, you can configure TE attributes on the desired GRE tunnel interface.


#### Procedure

* Enable TE attributes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**te attribute enable**](cmdqueryname=te+attribute+enable)
     
     
     
     TE is enabled.
     
     
     
     If MPLS TE has been enabled, the device automatically converts existing MPLS TE attribute configurations to TE attribute configurations when this command is run. You can also configure new TE features. The converted TE attribute configurations can be used for both MPLS TE tunnels and SRv6 TE Policies.
* (Optional) Configure link bandwidth.
  
  
  
  In real-world applications, link bandwidth only needs to be configured for outbound interfaces along the links of an SRv6 TE Policy that requires sufficient bandwidth.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**te bandwidth max-reservable-bandwidth**](cmdqueryname=te+bandwidth+max-reservable-bandwidth) *max-bw-value*
     
     
     
     The maximum reservable link bandwidth is configured.
  4. Run [**te bandwidth bc0**](cmdqueryname=te+bandwidth+bc0) *bc0Bw*
     
     
     
     The BC0 bandwidth is configured for the link.
     
     
     
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
  3. Run [**te bandwidth max-reservable-bandwidth dynamic**](cmdqueryname=te+bandwidth+max-reservable-bandwidth+dynamic) *max-dynamic-bw-value*
     
     
     
     The maximum reservable dynamic link bandwidth is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If this command is run in the same interface view as the [**te bandwidth max-reservable-bandwidth**](cmdqueryname=te+bandwidth+max-reservable-bandwidth) command, the later configuration overrides the previous one.
  4. (Optional) Run [**te bandwidth max-reservable-bandwidth dynamic baseline remain-bandwidth**](cmdqueryname=te+bandwidth+max-reservable-bandwidth+dynamic+baseline+remain-bandwidth)
     
     
     
     The device is configured to use the remaining bandwidth of the interface when calculating the maximum dynamic reservable bandwidth for TE.
     
     
     
     In scenarios such as channelized sub-interface and bandwidth lease, the remaining bandwidth of an interface changes, but the physical bandwidth does not. In this case, the actual forwarding capability of the interface decreases; however, the dynamic maximum reservable bandwidth of the TE tunnel is still calculated based on the physical bandwidth. As a result, the calculated TE bandwidth is greater than the actual bandwidth, and the actual forwarding capability of the interface does not meet the bandwidth requirement of the tunnel.
  5. Run [**te bandwidth dynamic**](cmdqueryname=te+bandwidth+dynamic) **bc0** *bc0-bw-percentage*
     
     
     
     The BC0 dynamic bandwidth is configured for the link.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If this command is run in the same interface view as the [**te bandwidth**](cmdqueryname=te+bandwidth) **bc0** command, the later configuration overrides the previous one.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure a link-specific TE metric value.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**te metric**](cmdqueryname=te+metric) *metric-value*
     
     
     
     A TE metric value is configured for the link.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the administrative group and affinity attribute in hexadecimal format.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**te link administrative group**](cmdqueryname=te+link+administrative+group) *group-value*
     
     
     
     A TE link administrative group is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the link administrative group and affinity attributes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping)
     
     
     
     An affinity name template is configured, and the affinity mapping view is displayed.
     
     
     
     This template must be configured on each node involved in SRv6 TE Policy path computation, and the global mappings between the names and values of affinity bits must be the same on all the involved nodes.
  3. Run [**attribute**](cmdqueryname=attribute) *bit-name* **bit-sequence** *bit-number*
     
     
     
     Mappings between affinity bit values and names are configured.
     
     
     
     This step configures only one bit of an affinity attribute, which has a total of 32 bits. Repeat this step as needed to configure some or all of the bits.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  6. Run [**te link administrative group name**](cmdqueryname=te+link+administrative+group+name) { *bit-name* } &<1-32>
     
     
     
     A link administrative group is configured.
     
     
     
     The *name-string* value must be in the range specified for the affinity attribute in the template.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure an SRLG.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view of a TE link is displayed.
  3. Run [**te srlg**](cmdqueryname=te+srlg) *srlg-number*
     
     
     
     The interface is added to an SRLG.
     
     On a network with hot standby or TE FRR protection, you need to configure the SRLG attribute for the outbound interface of the ingress on an SRv6 TE Policy as well as other members in the SRLG. A link joins an SRLG after the SRLG attribute is configured on an outbound interface of the link.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To delete the SRLG configuration from all interfaces on a device, run the [**undo te srlg all-config**](cmdqueryname=undo+te+srlg+all-config) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.