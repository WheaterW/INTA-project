Understanding EVPN ORF
======================

Understanding EVPN ORF

#### Background

The growing number of services run over an EVPN has triggered a proliferation of new users. As a result, BGP-EVPN peers on an EVPN are sending vast quantities of EVPN routes to each other. Even if the remote peer does not have an RT-matching EVPN instance, the local PE still sends it EVPN routes. To reduce the pressure on the network, each PE needs to receive only desired routes. However, configuring a separate export route-policy for each user drives up O&M costs significantly. To address this issue, configure EVPN outbound route filtering (ORF) on the network.


#### Implementation

After EVPN ORF is configured, each PE on the EVPN sends the import VPN targets (IRTs) and original AS number of the local EVPN instances to the other PEs or BGP EVPN RRs. Upon receipt of such information, which is sent through ORF routes, the peers construct export route-policies based on these routes so that the local PE receives only the desired routes, thereby reducing the receiving pressure on this PE.

[Figure 1](#EN-US_CONCEPT_0000001550402001__fig_dc_vrp_evpn_feature_001801) shows a basic EVPN on which each device supports EVPN ORF. PE1, PE2, and PE3 establish BGP EVPN peer relationships with the RR and function as its clients. In addition, EVPN instances with specific RTs are configured on each PE.

Before EVPN ORF is enabled, the RR advertises all the routes it receives from PE1's EVPN instances to PE2 and PE3. However, PE2 only needs routes with an export VPN target (ERT) of 1:1, and PE3 only needs routes with an ERT of 2:2. As a result, PE2 and PE3 discard unwanted routes upon receipt, wasting device resources.

After EVPN ORF is enabled on all devices and BGP EVPN peer relationships are established between the PEs and RR in the BGP-VPN-target address family view, the BGP EVPN peers negotiate the EVPN ORF capability. Each device sends the IRTs of its local EVPN instances to the BGP EVPN peers through ORF routes, and then constructs export route policies based on the ORF routes it receives. After receiving the EVPN1, EVPN4, and EVPN5 routes from PE1, the RR advertises only those with the ERT of 1:1 to PE2 and only those with the ERT of 2:2 to PE3.

**Figure 1** Basic usage scenario of EVPN ORF  
![](images/fig_dc_vrp_evpn_feature_001801.png)

The BGP-VPN-target address family obtains the IRT configured on the local device regardless of the type of the instance that the IRT comes from. If EVPN ORF is enabled on a network where some devices do not support it, the EVPN service may not run properly. However, the BGP-VPN-target address family can resolve this problem.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001550402001__fig_dc_vrp_evpn_feature_001801), PE1, PE2, and PE3 establish BGP EVPN peer relationships with the RR and function as its clients. Suppose that PE1, PE2, and the RR all support EVPN ORF but that PE3 does not, as it runs an earlier version. If EVPN ORF is enabled on the network and the BGP-VPN-target peer relationships are established, PE3 does not send ORF routes to the RR, meaning that PE1 does not receive the ORF routes with an ERT of 2:2 from the RR. As a result, the RR does not advertise the route with the ERT being 2:2 to PE3, affecting services between EVPN4 and EVPN2. Because the BGP-VPN-target address family does not differentiate the type of instance the IRT belongs to, you can configure an L3VPN instance on PE3 and set both the IRT and ERT to 2:2. This configuration allows PE3 to advertise an ORF route with an IRT of 2:2 to the RR, which then advertises the route to PE1. Upon receipt, PE1 modifies its export route-policy so that the RR can advertise the route with the ERT being 2:2 to PE3.

![](../public_sys-resources/note_3.0-en-us.png) 

For the preceding scenario, instead of configuring an L3VPN instance, you can configure the RR to advertise default ORF routes to PE1 and PE3, and then you can delete the BGP-VPN-target peer relationship between the RR and PE3. After the configuration is complete, PE1, PE2, and PE3 advertise all routes to the RR. The RR then advertises routes with ERTs of 1:1 and 2:2 to PE1, routes with an ERT of 1:1 to PE2, and all routes to PE3.

If both EVPN and L3VPN services are deployed on the preceding network, the preceding two configuration approaches cannot be used because the L3VPN service will not run properly. On the network shown in [Figure 2](#EN-US_CONCEPT_0000001550402001__fig_dc_vrp_evpn_feature_001802), only PE3 does not support EVPN ORF. In this case, after EVPN ORF is enabled on the network, the EVPN service cannot run properly. If an L3VPN instance is created, this instance receives the other PEs' L3VPN routes from the RR, which compromises the L3VPN service. To resolve this issue, you can disable the RR from filtering routes based on the IRT for PE3, thereby ensuring that both EVPN and L3VPN services can run properly.

**Figure 2** An EVPN ORF network carrying both EVPN and L3VPN services  
![](images/fig_dc_vrp_evpn_feature_001802.png)