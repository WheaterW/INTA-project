Understanding BGP ORF
=====================

Outbound route filtering (ORF) enables a BGP device to send local routing policies (outbound route filters) to a BGP peer, which can then use the received policies to filter out unwanted routes before route advertisement.

In most cases, users expect a carrier to send only the routes that they require, and the carrier does not want to maintain a separate export routing policy for each user. ORF meets the requirements of both users and the carrier. ORF supports on-demand route advertisement, which significantly reduces bandwidth consumption and the configuration workload.

Prefix-based ORF, defined in standard protocols, can be used to send prefix-based inbound policies configured by users to a carrier through Route-refresh messages. The carrier's device then filters out unwanted routes before route advertisement based on the received inbound policies. This prevents users from receiving a large number of unwanted routes and conserves resources.

#### Applications

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130624150__fig_dc_vrp_bgp_feature_200001), DeviceA and DeviceB are directly connected, and prefix-based ORF is enabled on them. After negotiating the prefix-based ORF capability with DeviceB, DeviceA adds its local prefix-based inbound policy to a Route-refresh message and then sends the message to DeviceB. DeviceB uses the information in the received message to construct a corresponding outbound policy, and then advertises only the routes that match the outbound policy to DeviceA.

**Figure 1** Applying ORF to directly connected BGP peers  
![](figure/en-us_image_0000001130784016.png)

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001130624150__fig_dc_vrp_bgp_feature_200002), DeviceA and DeviceB are clients of the RR in the AS, and each establishes a BGP peer relationship with the RR. Prefix-based ORF is enabled on all three devices. After negotiating the prefix-based ORF capability with the RR, DeviceA and DeviceB add their local prefix-based inbound policies to Route-refresh messages and then send the messages to the RR. Based on the prefix information in the received Route-refresh messages, the RR constructs corresponding outbound policies to filter the to-be-advertised routes and reflects only the matched routes to DeviceA and DeviceB.

**Figure 2** Applying ORF to an AS with an RR  
![](figure/en-us_image_0000001130624222.png)