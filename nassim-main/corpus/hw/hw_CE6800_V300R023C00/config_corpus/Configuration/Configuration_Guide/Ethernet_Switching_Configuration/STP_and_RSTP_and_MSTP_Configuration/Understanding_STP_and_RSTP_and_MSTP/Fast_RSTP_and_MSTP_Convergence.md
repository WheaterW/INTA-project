Fast RSTP and MSTP Convergence
==============================

The key to RSTP and MSTP fast convergence is the introduction of the [Proposal/Agreement Mechanism](#EN-US_CONCEPT_0000001345318749__section8346742194216), [Fast Switchover of the Root Port](#EN-US_CONCEPT_0000001345318749__section475992312432), and [Edge Port](#EN-US_CONCEPT_0000001345318749__section92892052115).

#### Proposal/Agreement Mechanism

The Proposal/Agreement (P/A for short) mechanism enables a designated port to quickly transition to Forwarding state. The P/A mechanism is classified into the common P/A mechanism and the enhanced P/A mechanism.

**Common P/A mechanism**

In [Figure 1](#EN-US_CONCEPT_0000001345318749__fig1649671517299), a new link is added between DeviceB and the root bridge DeviceA. On DeviceB, p2 is an alternate port, p3 is a designated port in Forwarding state, and p4 is an edge port.

**Figure 1** Common P/A negotiation process  
![](figure/en-us_image_0000001345238533.png)
The common P/A mechanism works as follows:

1. p0 and p1 become designated ports and send RST BPDUs to each other.
2. The RST BPDU sent from p0 is superior to that of p1. Therefore, p1 becomes a root port and stops sending RST BPDUs.
3. p0 enters the Discarding state and sets the Proposal and Agreement fields in its RST BPDU to 1.
4. After receiving an RST BPDU with the Proposal field set to 1, DeviceB sets the sync variable to 1 for all its ports.
5. As p2 has been blocked, its state remains unchanged. p4 is an edge port and does not participate in spanning tree calculation. Therefore, only the non-edge designated port p3 needs to be blocked.
6. When the sync variable of each port is set to 1, p2 and p3 enter the Discarding state. p1 enters the Forwarding state and sends an RST BPDU with the Agreement field set to 1 to DeviceA.
7. Upon receipt of this RST BPDU, DeviceA identifies that the RST BPDU is a response to the RST BPDU sent with the Proposal field. p0 then immediately enters the Forwarding state.

The P/A process can proceed to downstream devices.

Although STP can select designated ports quickly, to prevent loops, all ports must wait at least one interval of the Forward Delay timer before forwarding traffic. To overcome this bottleneck, RSTP blocks non-root ports to prevent loops, and uses the P/A mechanism to shorten the time that an upstream port waits before transitioning to Forwarding state.

![](public_sys-resources/note_3.0-en-us.png) 

The P/A mechanism requires a P2P full-duplex link between two devices. If P/A fails, a designated port is elected after two intervals of the Forward Delay timer. This is the same as designated port election in STP.

**Enhanced P/A mechanism**

In [Figure 2](#EN-US_CONCEPT_0000001345318749__fig2655133419412), the enhanced P/A mechanism works as follows:

1. At the beginning of negotiation, all devices consider themselves as the root bridge, on which all ports are designated ports in Discarding state. When the synced variable is set to 1, the Proposal and Agreement fields are also set to 1. The upstream device sends a proposal BPDU to the downstream device, requesting that the port connected to the downstream device rapidly enters the Forwarding state. After receiving this BPDU, the downstream device sets its port connected to the upstream device as the root port and blocks all non-edge ports.
2. The upstream device sends an agreement BPDU. After receiving this BPDU, the root port on the downstream enters the Forwarding state.
3. The downstream device replies with an agreement BPDU. After receiving this BPDU, the upstream device sets its port connected to the downstream device as the designated port, and the port then enters the Forwarding state.

By default, Huawei devices use the enhanced P/A mechanism for fast convergence. In order to enable a Huawei device to communicate with a third-party device that uses the common P/A mechanism, you can configure Huawei devices to use the common P/A mechanism.

**Figure 2** Enhanced P/A negotiation process  
![](figure/en-us_image_0000001345478677.png)

#### Fast Switchover of the Root Port

If a root port fails on an RSTP or MSTP network, the best alternate port becomes the root port and enters the Forwarding state. This is because the network segment connected to this alternate port has a designated port connected to the root bridge.

In [Figure 3](#EN-US_CONCEPT_0000001345318749__fig169043585126), DeviceA is the root bridge, DeviceB is the secondary root bridge, and interface 2 on DeviceC is the alternate port. If interface 1 (root port) on DeviceC fails: In STP mode, interface 2 on DeviceC becomes the root port and enters the Discarding state. It then waits for an interval of the Forward Delay timer (15 seconds by default), enters the Learning state, then waits for another interval of the Forward Delay timer before entering the Forwarding state. However, in RSTP/MSTP mode, interface 2 on DeviceC becomes the root port and immediately enters the Forwarding state.

Compared with STP, RSTP/MSTP reduces service traffic loss because the new root port can immediately enter the Forwarding state without waiting for two intervals of the Forward Delay timer.

**Figure 3** Fast switchover of the root port  
![](figure/en-us_image_0000001292398396.png)

#### Edge Port

An edge port is located at the edge of an RSTP or MSTP network and directly connected to a terminal.

This port does not participate in spanning tree calculation and can transition from the Disabled state to the Forwarding state immediately. It becomes a common port once it receives a BPDU. The spanning tree then needs to be recalculated, leading to network flapping, which can be addressed by [BPDU protection](vrp_stp_cfg_1110.html#EN-US_CONCEPT_0000001291918968__section8356190195615).