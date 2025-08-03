Configuration Precautions for QPPB
==================================

Configuration_Precautions_for_QPPB

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| 1. If the traffic matches both the ACL for a traffic policy and QPPB ACL and the forwarding action in the traffic behavior is redirect/deny/permit, the redirect and deny actions in the QPPB action table do not take effect.  2. If outgoing traffic on an interface matches both a traffic policy and a QPPB policy and the traffic policy is implemented based on the qos-local-id, only the QPPB policy takes effect. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| Interface-based MF classification does not support the matching of both the source and destination QoS local IDs in the outbound direction. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| Global MF classification does not support the matching of both the source and destination QoS local IDs in the outbound direction. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |