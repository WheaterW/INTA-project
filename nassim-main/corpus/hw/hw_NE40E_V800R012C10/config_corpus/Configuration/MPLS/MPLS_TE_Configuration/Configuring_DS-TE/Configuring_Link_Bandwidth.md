Configuring Link Bandwidth
==========================

You can configure link bandwidth to limit the bandwidth for a DS-TE tunnel.

#### Context

Perform the following steps on each outbound interface on a DS-TE LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the link outbound interface is displayed.
3. Run [**mpls te bandwidth max-reservable-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth) *max-bw-value*
   
   
   
   The maximum reservable link bandwidth is set.
4. Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) { **bc0** *bc0Bw* | **bc1** *bc1Bw* | **bc2** *bc2Bw* | **bc3** *bc3Bw* | **bc4** *bc4Bw* | **bc5** *bc5Bw* | **bc6** *bc6Bw* | **bc7** *bc7Bw* }\*
   
   
   
   BC bandwidth is configured for the link.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

A distinct bandwidth constraints model determines a specific mapping between the maximum reservable link bandwidth and BC bandwidth:

* RDM model: *max-reservable-bandwidth* â¥ *bc0Bw* â¥ *bc1Bw* â¥ *bc2Bw* â¥ *bc3Bw* â¥ *bc4Bw* â¥ *bc5Bw* â¥ *bc6Bw* â¥ *bc7Bw*
* MAM model: *max-reservable-bandwidth* â¥ *bc0Bw* + *bc1Bw* + *bc2Bw* + *bc3Bw* + *bc4Bw* + *bc5Bw* + *bc6Bw* + *bc7Bw*

The Bandwidth Constraint (BC) bandwidth refers to the bandwidth constraints on a link, whereas the CT bandwidth refers to the bandwidth constraints of various types of service traffic on a DS-TE tunnel. The BCi bandwidth of a link must be greater than or equal to the sum (0 <= i <= 7) of all CTi bandwidth values of DS-TE tunnels passing through the link. For example, three LSPs with CT1 passing through a link has bandwidth values x, y, and z, respectively. The link interface BC1 bandwidth must be greater than or equal to the sum of x, y, and z.