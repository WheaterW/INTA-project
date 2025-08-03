Configuring the Entropy Label Capability for a BGP LSP
======================================================

Configuring the entropy label capability for a BGP LSP helps equalize and improve the performance of load balancing.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0201537302__fig14980124412302), an end-to-end BGP LSP is established between PE1 and PE2. In addition, an end-to-end VPNv4 IPv4 peer relationship is established between PE1 and PE2, an LDP LSP is established between PE1 and ASBR1, and an LDP LSP is established between ASBR2 and PE2. With the expansion of user networks, the load balancing technology is used to obtain higher bandwidth between nodes. However, load imbalance becomes increasingly severe on transit nodes. To improve load balancing performance, configure the entropy label capability for the BGP LSP on both PE1 and PE2.

**Figure 1** Load balancing performed on transit nodes  
![](figure/en-us_image_0201839367.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+elc+padding) { *peerIpv4Addr* | *peerGroupName* } **advertise-entropy-label** **elc** [ **padding** *paddingValue* ]
   
   
   
   The device is enabled to add the entropy label of the entropy label capability (ELC) type to BGP routes to be advertised to a specified peer or peer group.
5. Run [**peer**](cmdqueryname=peer) { *peerIpv4Addr* | *peerGroupName* } **entropy-label**
   
   
   
   The device is enabled to add the entropy label information to traffic to be forwarded to the specified peer or peer group.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check the entropy label in BGP routes.