Configuration Precautions for SAID
==================================

Configuration_Precautions_for_SAID

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| SAID CFC detection is not supported on UNR routes, DCN routes, blackhole routes, inter-VPN access, SR, or FTNs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After confirming that the local device is faulty, SAID ping automatically resets the subcard or board. As a result, traffic on the board or subcard is interrupted. The reset reason is SAIDPING detected that the board was faulty and reset the board.(CPU Reset), and corresponding logs are recorded. The subcard or board is restarted, which affects packet forwarding. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| SEU-associated port loopback:  1. When a loopback is configured on a subcard's interface, there is a possibility that the peer interface goes Down.  2. When loopback is configured on a subcard's interface, the interface is blocked for 50 ms. As a result, traffic is interrupted for 50 ms (when the peer interface does not go Down).  3. Loopback can be set for a subcard interface at most once every 24 hours.  4. If a fault is detected, the subcard is reset. The subcard can be reset at most once within 24 hours.  After a fault is detected, traffic is interrupted for 50 ms and the subcard is reset.  Disable the corresponding function. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Service traffic is intermittently interrupted when SAID for ping detects a fault and interface loopback is enabled. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Only detection route forwarding is supported. The outbound interface of a route can only be a GE, Eth, 100GE, POS, IP-Trunk, Eth-Trunk, QinQ VLAN tag termination sub-interface, Dot1q VLAN tag termination sub-interface, or VLANIF interface. VLANIF interfaces can be configured in trunk or default VLAN mode, but cannot be configured in VLAN stacking or VLAN mapping mode. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |