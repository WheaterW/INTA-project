Configuring Basic BIERv6 Functions
==================================

Configuring basic BIERv6 functions involves configuring sub-domains, BFR-prefixes, End.BIER SIDs, and BSLs for bit forwarding routers (BFRs). In addition, a BFR-ID needs to be configured for each bit forwarding egress router (BFER).

#### Context

A BIERv6 network consists of one or more sub-domains. [Figure 1](#EN-US_TASK_0318574770__fig7375201444012) shows a BIERv6 network. All nodes that support BIERv6 forwarding are called BFRs. The ingress node of multicast traffic is called a bit forwarding ingress router (BFIR), and the egress node is called a BFER.

**Figure 1** BIERv6 networking  
![](figure/en-us_image_0318574774.png "Click to enlarge")

A BFR can belong to one or more sub-domains. When planning sub-domains, ensure that the BFIR and all the BFERs to which the multicast traffic received by the BFIR is to be sent reside in the same sub-domain. This is necessary because sub-domain stitching is currently not supported. To facilitate management and improve the forwarding efficiency on a multicast network, you are advised to plan sub-domains based on the suggestions provided in [Table 1](#EN-US_TASK_0318574770__table1511911521618). A domain consists of one or more sub-domains and does not need to be configured.

**Table 1** Sub-domain planning suggestions
| Network Type | Planning Suggestion |
| --- | --- |
| Single-AS small- and medium-sized network | Plan only one sub-domain, with all IGP areas in it. |
| Single-AS large-scale network | The solutions are as follows:  Plan only one sub-domain, with all IGP areas in it. In addition, set BFR-IDs and BSLs to let the BFERs in the same IGP area have the same set ID. This helps improve forwarding efficiency. The concept and calculation formula of a set ID are described in the following section. |
| Single-AS multi-topology network | Plan sub-domains in one domain based on the number of topologies, with each topology corresponding to one sub-domain. |
| Multi-AS large-scale network | Inter-AS static traversal must be deployed. The sub-domain planning solutions are as follows:  Plan only one sub-domain, with all ASs in it. In addition, set BFR-IDs and BSLs to let the BFERs in the same AS have the same set ID. This helps improve forwarding efficiency. The concept and calculation formula of a set ID are described in the following section. |

One BFR can be configured with one or more BSLs. The BFR-ID of a BFER in a sub-domain must be unique. Planning BSLs and BFR-IDs properly can reduce the number of multicast packet copies and improve the forwarding efficiency on the multicast network. When planning BSLs and BFR-IDs, you are advised to adhere to the following guidelines:

* Denseness: Set the maximum BFR-ID as the number of BFERs in a sub-domain to deploy as few sets as possible. For example, if a sub-domain contains up to 256 BFERs, allocate BFR-IDs to the BFERs within the range of 1 to 256. Similarly, if the sub-domain contains up to 512 BFERs, allocate BFR-IDs to the BFERs within the range of 1 to 512.
* Uniqueness: Ensure that each BFR-ID is unique in a sub-domain.
* Region: Allocate the BFERs in the same region to the same set.
* Necessity: Allocate BFR-IDs only for BFERs. If a BFIR also needs to function as a BFER, you also need to configure a BFR-ID for it. For a BFIR-only node (functioning as a BFIR but not a BFER), it does not need to be configured with a BFR-ID.
* Evolvability: Reserve some BFR-IDs in each set for future network expansion.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Enable SRv6 and configure a locator address.
   
   
   
   If SRv6 has been enabled and an SRv6 locator has been configured for the local device, skip this step. Otherwise, perform the following operations:
   
   
   
   1. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter the SRv6 view.
   2. Run the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ [ **static** *static-length* ] | [ **args** *args-length* ] | [ **flex-algo** *flexAlgoId* ] ] \* ] command to configure an SRv6 locator.
      
      
      
      You can specify more attributes when creating an SRv6 locator. For details about locator attributes and configuration commands, see the corresponding Command Reference.
   3. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 locator view.
   4. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 view.
3. Configure an IPv6 address (to be used as the BFR-prefix) for an interface.
   
   
   
   A BFR-prefix is a loopback interface IPv6 address of the BFR in a sub-domain. If an IPv6 address has been configured for the interface on the local device, skip this step; otherwise, perform the following operations:
   
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   2. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } command to configure an IPv6 address for the interface.
      
      
      
      The IPv6 address must be a global unicast address with the prefix length of 128 bits. It cannot be an address of the subnet to which the locator belongs. If you are prompted that IPv6 has not been enabled on the interface, run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command. Similar details will be omitted in the rest of the document.
   3. Run the [**quit**](cmdqueryname=quit) command to exit the interface view.
4. Run the [**bier**](cmdqueryname=bier) command to enable BIER and enter the BIER view.
5. Run the [**sub-domain**](cmdqueryname=sub-domain) *sub-domain-val* **ipv6** command to specify a sub-domain for the BFR and enter the sub-domain view.
6. Configure BIERv6-related attributes.
   
   
   
   [Table 2](#EN-US_TASK_0318574770__table13897184015814) describes these attributes.
   
   **Table 2** BIERv6-related attributes
   | Operation | Command | Remarks |
   | --- | --- | --- |
   | Configure a BFR-ID for the BFER. | [**bfr-id**](cmdqueryname=bfr-id) *bfr-id-val* | This operation is not required for non-BFER nodes. If a BFIR also needs to function as a BFER, you also need to configure a BFR-ID for it.  On an MVPN over BIERv6 network, all receiver PEs are BFERs. |
   | Set the BSL and Max-SI. | [**encapsulation-type**](cmdqueryname=encapsulation-type) **ipv6** **bsl** { **64** | **128** | **256** } **max-si** *max-si-val* | Max-SI is the maximum set ID in a sub-domain. The formula for calculating the set ID is as follows:  **Set ID = int [ (BFR-ID â 1)/BSL ]**  In the preceding formula, **int** rounds down to the nearest integer. |
   | Specify the interface whose IP address is to be used as the BFR-prefix. | [**bfr-prefix**](cmdqueryname=bfr-prefix) **interface** { *interface-name* | *interface-type* *interface-number* } [ *ipv6-address-value* ] | A loopback interface must be specified, and IS-IS IPv6 must be enabled on the interface. |
   | Configure an End.BIER SID. | [**end-bier**](cmdqueryname=end-bier) **locator** *locator-name* **sid** *ipv6-sid* | The End.BIER SID must be an IPv6 address of the subnet to which the locator belongs. |
   | Configure the underlay protocol to be used to advertise BIERv6 information. | [**protocol**](cmdqueryname=protocol) *isis* | Currently, IS-IS or a static BIFT can be used to advertise BIERv6 information. The latter is used in inter-AS static traversal scenarios. |
   | (Optional) Configure the maximum number of links for load balancing. | [**max-load-balance**](cmdqueryname=max-load-balance) *max-load-balance-num* | Perform this operation only when BIERv6 link load balancing is required.  ForNE40E-M2E, the maximum value of *max-load-balance-num* is affected by the load balancing enhancement factor configured using the [**load-balance enhance-factor**](cmdqueryname=load-balance+enhance-factor) command. |
   | (Optional) Configure the BIERv6 load balancing enhancement factor. | [**load-balance enhance-factor**](cmdqueryname=load-balance+enhance-factor) *factor-value* | The maximum value of *factor-value* is equal to the maximum BIERv6 load balancing number (64) divided by the value configured using the [**max-load-balance**](cmdqueryname=max-load-balance) command.  NOTE:  Only NE40E-M2 supports the configuration. |
7. Run the [**quit**](cmdqueryname=quit) command to exit the sub-domain view.
8. Run the [**quit**](cmdqueryname=quit) command to exit the BIER view.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
10. Repeat [1](#EN-US_TASK_0318574770__step127334244280) to [9](#EN-US_TASK_0318574770__step56492106710) to configure all other BFRs on the BIERv6 network.