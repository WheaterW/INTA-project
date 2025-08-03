Configuration Precautions for Antilocking PFC
=============================================

Configuration Precautions for Antilocking PFC

#### Licensing Requirements

Antilocking PFC is under license control (CE-LIC-ABS).


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6860-SAN/CE6885-SAN-56F |
| CE8800 series | CE8850-SAN |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Antilocking PFC can continuously control sending and pausing of a small amount of traffic at a high frequency within a short period. Therefore, the Xoff threshold of traditional PFC is set to 30000 KB so that it does not take effect. | CE6800 series  CE8800 series | CE6860-SAN  CE8850-SAN |
| On an interface where antilocking PFC is enabled, when broadcast, unknown unicast, and multicast (BUM) traffic is congested, PFC is not triggered and no PFC frame is sent to the upstream device. For the unicast, multicast, and broadcast hybrid traffic of the same lossless queue, the multicast and broadcast traffic is directly discarded after the threshold for discarding packets is reached. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| When PFC frames are received, unicast, multicast, and broadcast services within the PFC-enabled priority queue respond and stop sending traffic. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| Antilocking PFC and traditional PFC cannot be both enabled on an interface. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| Antilocking PFC for priority queue 1 and differentiated flow scheduling in any queue on an interface cannot be both enabled.  For a priority queue on an interface, antilocking PFC and differentiated flow scheduling cannot be both enabled. | CE6800 series  CE8800 series | CE6860-SAN  CE8850-SAN |
| Antilocking PFC applies only to DCI long-distance scenarios (greater than 10 km) and does not apply within DCNs.  To meet the long-distance specifications, the DCI gateway needs to be deployed independently. If the DCI gateway is not deployed independently, the specifications need to be reduced. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| For the CE6885-SAN:  Antilocking PFC takes effect only after distance-based headroom buffer check is enabled.  For the CE6860-SAN and CE8850-SAN:  Antilocking PFC takes effect only after enhanced long-distance plane buffer optimization and distance-based headroom buffer check are enabled. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| When antilocking PFC is configured (including enabling antilocking PFC and modifying the buffer threshold for the queue where antilocking PFC takes effect) while traffic is being transmitted, transient packet loss may occur. You are advised to stop traffic before configuring antilocking PFC. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| When the RTT of a long-distance link changes in scenarios where distance-based headroom buffer check is enabled, transient packet loss may occur.  When the bandwidth of an interface enabled with antilocking PFC changes, for example, when the interface is split, aggregated, or has its optical module replaced, transient packet loss may occur. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| For the CE8800 Series:  Antilocking PFC and dragonfly antilocking PFC are mutually exclusive. | CE8800 series | CE8850-SAN |
| For the CE6800 Series:  Antilocking PFC and flow control are mutually exclusive on the same interface. | CE6800 series | CE6885-SAN-56F |