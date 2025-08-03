Understanding Parameters for Interoperation with Non-Huawei Devices
===================================================================

Understanding Parameters for Interoperation with Non-Huawei Devices

#### Proposal/Agreement Mechanism

The Proposal/Agreement mechanism implements rapid transition. Within this mechanism, there are two modes: enhanced mode and common mode. For details, see [Proposal/Agreement Mechanism](vrp_stp_cfg_1073.html#EN-US_CONCEPT_0000001345318749__section8346742194216). When Huawei devices are connected to non-Huawei devices on a network running a spanning tree protocol, select the same Proposal/Agreement mode as that used on non-Huawei devices. If they use different Proposal/Agreement modes, they may fail to communicate with each other.

* Enhanced mode: The port participates in calculation of the root port when calculating the synchronization flag bit.
  1. An upstream device sends a proposal BPDU to a downstream device, requesting rapid status transition. After receiving the message, the downstream device sets the port connected to the upstream device as a root port and blocks all non-edge ports.
  2. The upstream device then sends an agreement BPDU to the downstream device. After the downstream device receives the message, the root port transitions to the Forwarding state.
  3. The downstream device responds to the proposal BPDU with an agreement BPDU. After receiving the BPDU, the upstream device sets the port connected to the downstream device as a designated port, and the designated port transitions to the Forwarding state.
* Common mode: The current interface ignores the root port when calculating the synchronization flag bit.
  1. An upstream device sends a proposal BPDU to a downstream device, requesting rapid status transition. After receiving the BPDU, the downstream device sets the port connected to the upstream device as a root port and blocks all non-edge ports. The root port then transitions to the Forwarding state.
  2. The downstream device responds to the Proposal message with an agreement BPDU. After receiving the BPDU, the upstream device sets the port connected to the downstream device as a designated port, and the designated port transitions to the Forwarding state.

#### Formats of MST BPDUs Received and Sent by Ports (for MSTP)

Two MST BPDU formats are available: dot1s (defined in IEEE 802.1s) and legacy (proprietary BPDU format).

On an MSTP-enabled network where Huawei devices are connected to non-Huawei devices, you can designate the BPDU format or configure a port to automatically adjust the MST BPDU format. With this function, the port automatically adopts the BPDU format on the peer end.


#### Enabling Digest Snooping (for MSTP)

On an MSTP-enabled network, interconnected Huawei and non-Huawei devices cannot communicate with each other if they have the same region name, revision level, and VLAN-to-instance mappings but different keys carried in BPDUs. To address this problem, enable digest snooping on the Huawei device.

This function allows the Huawei device to keep its key carried in BPDUs consistent with that on the non-Huawei device.