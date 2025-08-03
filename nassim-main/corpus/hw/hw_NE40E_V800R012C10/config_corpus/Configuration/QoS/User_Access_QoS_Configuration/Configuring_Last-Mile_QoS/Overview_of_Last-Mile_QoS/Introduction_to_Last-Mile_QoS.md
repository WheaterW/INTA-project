Introduction to Last-Mile QoS
=============================

Last-mile QoS adjusts downstream traffic based on the link layer protocol running between a user and DSLAM.

#### Shaped Rate Adjustment: Last-Mile QoS

Last mile indicates the link between the user and the access switch (such as the Ethernet DSLAM), as shown in [Figure 1](#EN-US_CONCEPT_0268652987__en-us_concept_0172356883_fig_qos_feature_03508). Residential and enterprise users generally access the Ethernet DSLAM using IPoE, PPPoE and the DSLAM is connected to the BRAS or SR, edge device on the backbone network, through a metropolitan area network (MAN).

**Figure 1** Last mile  
![](images/fig_feature_image_0021580504.png)

In a broadband service access scenario, an Ethernet link connects a BRAS or SR and a DSLAM. The BRAS or SR encapsulates Ethernet packets, and traffic shaping is implemented based on the Ethernet packets.

Even if the link connects the user and DSLAM is also an Ethernet link, the encapsulation cost of the packets sent between the user and DSLAM can possibly exceed that on the user side of the BRAS or SR. For example, the Ethernet packet encapsulated on the BRAS or SR does not carry a VLAN tag, but the packet sent between the user and DSLAM carries a single or double VLAN tags due to VLAN or QinQ encapsulation.

To resolve this problem, last-mile QoS can be configured on the BRAS or SR. Last-mile QoS allows a device to calculate the length of headers to be added to packets based on the bandwidth purchased by users and the bandwidth of the downstream interface on the DSLAM for traffic shaping.

Therefore, the BRAS or SR cannot automatically infer the sum length of the packets that has been encapsulated on the DSLAM and requires compensation bytes.

After compensation bytes are configured, if the DSLAM connects to the CPE through an Ethernet link, the BRAS or SR can automatically infer the sum length of the packet encapsulated on the DSLAM based on the length of the forwarded packet and the configured compensation bytes, and determine the shaped rate to be adjusted.

The following tables provide common encapsulation-costs and compensation bytes.

**Table 1** Packet encapsulation-cost
| Encapsulation Type | | Encapsulation-cost (Bytes) |
| --- | --- | --- |
| PPP header | | 2 |
| Eth header | | 14 |
| VLAN header | | 4 |
| QinQ header | | 8 |
| AAL5 encapsulation | VC | AAL5 Header + AAL5 tail = 0 + 8 = 8 |
| LLC Type1 (connection-less mode, such as IPoE, PPPoE) | AAL5 Header + AAL5 tail = 8 + 8 = 16 |


**Table 2** Common compensation bytes for last-mile QoS
| Scenario | Compensation Bytes |
| --- | --- |
|  | = VLAN header - QinQ header  = - 4 |
|  | = 0 - QinQ header  = - 8 |