Verifying the Layer 2 Multicast Entry Limit Configuration
=========================================================

After configuring Layer 2 multicast entry limit, verify information such as the limit on the number of multicast groups.

#### Prerequisites

The Layer 2 multicast entry limit has been configured.
#### Procedure

* Run the [**display l2-multicast limit**](cmdqueryname=display+l2-multicast+limit) **vlan** [ *vlan-id1* [ to *vlan-id2* ] [ **interface** *interface-type* *interface-number* ] ] command to check Layer 2 multicast entry limit configurations and statistics in a specified VLAN.
* Run the [**display l2-multicast limit**](cmdqueryname=display+l2-multicast+limit) **vsi** [ *vsi-name* [ **interface** *interface-type* *interface-number* ] ] command to check Layer 2 multicast entry limit configurations and statistics in a specified VSI.
* Run the [**display l2-multicast limit**](cmdqueryname=display+l2-multicast+limit) **interface** *interface-type* *interface-number* command to check Layer 2 multicast entry limit configurations and statistics on a specified interface or sub-interface.
* Run the [**display l2-multicast limit**](cmdqueryname=display+l2-multicast+limit) **vsi** [ *vsi-name* [ **remote-peer** *ip-address* [ **negotiation-vc-id** *vc-id* ] ] ] command to check Layer 2 multicast entry limit configurations and statistics on a remote peer.
* Run the [**display l2-multicast limit**](cmdqueryname=display+l2-multicast+limit) [ **configuration** | **statistics** ] command to check all Layer 2 multicast entry limit configurations and statistics.