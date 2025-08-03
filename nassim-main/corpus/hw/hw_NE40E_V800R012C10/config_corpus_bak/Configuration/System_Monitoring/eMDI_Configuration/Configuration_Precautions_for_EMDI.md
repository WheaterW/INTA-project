Configuration Precautions for EMDI
==================================

Configuration_Precautions_for_EMDI

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| eMDI detection does not take effect on Ps in Layer 3 Rosen MVPN and L2VPN multicast scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In an NG MVPN scenario, Ps cannot identify VPN instances. If the SGs of multiple VPNs are the same, multiple copies of traffic are detected simultaneously, resulting in measurement errors. Avoid this scenario during network deployment. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In an NG MVPN dual-root protection scenario, when a device functions as both a transit node and a bud node, two copies of traffic are detected, resulting in measurement errors. During deployment, ensure that a device functions as both a transit node and a bud node. If a device functions as both a transit node and a bud node, run the emdi monitor-rate-only command to check only the rate. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Downstream eMDI detection is not supported in the following scenario:  1. Multicast PIM FRR.  2. Multicast source cloning-based PIM FRR.  3. ABR in an NG MVPN segment scenario.  4. Traffic is forwarded on the public network side of the root and bud nodes in an NG MVPN.  5. Layer 2 multicast is not supported.  EMDI detection does not take effect in unsupported scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After the eMDI detection period is changed, the counter detection result in the first period after the change is inaccurate. When the period is changed to a larger value, the detection data in the first period after the change is smaller than the actual detection data. When the period is changed to a smaller value, the detection data in the first period after the change is larger than the actual detection data. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the eMDI detection function is used in the following switching scenarios, errors occur in the detection period:  1. Inter-board trunk interface switching;  2. NG MVPN s and i tunnels are switched.  3. Dual-system hot backup switchback | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| To prevent misreporting of out-of-order packet statistics and alarms after traffic is interrupted and then restored, set the number of out-of-order packets to 0 if there are only out-of-order packet statistics but no packet loss statistics. When there is no packet loss count, the EMDI module cannot separately report the count of out-of-order packets. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In the BIER scenario, jitter measurement is not supported, and the channel configuration cannot carry the clock-rate parameter. As a result, transit and follow-up nodes cannot detect the clock rate of the channel and therefore cannot calculate the jitter. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| BIER eMDI detection is not supported in the upstream direction of the ingress PE and in the downstream direction of the egress PE. Common eMDI detection can be performed. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |