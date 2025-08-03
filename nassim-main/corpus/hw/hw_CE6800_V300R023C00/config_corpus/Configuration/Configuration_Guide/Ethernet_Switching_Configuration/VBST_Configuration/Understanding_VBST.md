Understanding VBST
==================

Understanding VBST

#### VBST Fundamentals

VBST allows STP or RSTP to run in each VLAN so that the spanning tree in each VLAN is independent of each other. In this case, VBST implements load balancing of traffic from different VLANs. After the role of each device, the role of each port on each device, and the state of each port are determined, spanning tree calculation and convergence are complete, and the network is stabilized.

**Device role**

VBST calculates a spanning tree for each VLAN. Each spanning tree contains a root bridge (RB), and all devices except the root bridge are non-root bridge devices.

**Port role**

VBST inherits the port roles of RSTP: root port, designated port, alternate port, backup port, and edge port. For details, see "Device Roles, Port Roles, and Port States" in STP/RSTP/MSTP Configuration.

**Port state**

VBST inherits the port states of STP, RSTP, and MSTP: Forwarding, Learning, and Discarding. For details, see "Device Roles, Port Roles, and Port States" in STP/RSTP/MSTP Configuration.

**Timer**

VBST inherits the timers of STP, RSTP, and MSTP: Hello Time, Forward Delay, and Max Age timers. For details, see "STP/RSTP/MSTP Timers" in STP/RSTP/MSTP Configuration.

**VBST BPDU**

On a VBST network, devices exchange VBST BPDUs to calculate the spanning tree topology. The format of VBST BPDUs differs from that of STP and RST BPDUs in the following aspects, as shown in [Figure 1](#EN-US_CONCEPT_0000001563768673__fig14331942171519):

* The destination MAC address in a VBST BPDU is 0100-0CCC-CCCD whereas that in an STP or RST BPDU is 0180-C200-0000.
* A 4-byte 802.1Q tag is added between the source MAC address and protocol length fields in a VBST BPDU.
* Based on the spanning tree protocol running on the remote device, the Data field in an STP or RST BPDU is used as the Data field in a VBST BPDU. By default, the Data field in an RST BPDU is used as the Data field in a VBST BPDU. However, a 6-byte Originating VLAN field is added to the end of an STP or RST BPDU, including the Type, Length, and VLAN ID fields.
  
  + Type: 2 bytes long, and the value is fixed at 0x0000.
  + Length: 2 bytes long, and the value is fixed at 2.
  + VLAN ID: 2 bytes long, and the value is the ID of the VLAN where the BPDU is originated.
* The BID in a VBST BPDU is different from that in an STP, RST, or MST BPDU. In VBST, the BID consists of the bridge priority (leftmost 4 bits), VLAN ID (subsequent 12 bits), and bridge MAC address (rightmost 48 bits).

**Figure 1** Comparisons between the formats of the STP/RST BPDU and VBST BPDU  
![](figure/en-us_image_0000001564008621.png)

#### VBST Topology Calculation

VBST supports VLAN-based topology calculation, whereby VLAN-tagged VBST BPDUs are sent in each VLAN and topology calculation is performed separately. The topology calculation method of VBST is the same as that of STP/RSTP. For details, see "STP/RSTP Topology Calculation" in STP/RSTP/MSTP Configuration. [Figure 2](#EN-US_CONCEPT_0000001563768673__fig288941454015) shows the topology calculation results of STP/RSTP and VBST.

* Through topology calculation, STP/RSTP generates a spanning tree with DeviceD as the root bridge for both VLAN 2 and VLAN 3. The links between DeviceA and DeviceF and between DeviceB and DeviceE are blocked. Although HostB and HostD belong to VLAN 2, they cannot communicate with each other because the link between DeviceB and DeviceE is blocked, and the link between DeviceC and DeviceD does not allow packets of VLAN 2 to pass through.
* Through topology calculation, VBST generates spanning trees for VLAN 2 and VLAN 3 with root bridges DeviceF and DeviceD, respectively. Traffic in VLAN 2 and VLAN 3 is forwarded through their respective spanning trees, so that the traffic is load balanced over the paths from DeviceB to DeviceE and from DeviceC to DeviceD.

**Figure 2** Topology calculation results of STP/RSTP and VBST  
![](figure/en-us_image_0000001563768697.png)

#### Fast Convergence of VBST

VBST supports the Proposal/Agreement mechanism in common and enhanced modes. For details, see "Fast RSTP and MSTP Convergence" in STP/RSTP/MSTP Configuration.


#### VBST Protection

VBST supports BPDU protection, TC protection, root protection, and loop prevention. For details, see "Understanding Protection Functions in RSTP/MSTP" in STP/RSTP/MSTP Configuration.


#### Interworking Between VBST and STP/RSTP

On a live network, VBST-enabled devices may connect to STP/RSTP-enabled devices. As VBST and STP/RSTP use different BPDU formats, interworking problems arise. To implement interworking between VBST and STP/RSTP, take the following measures:

* For an access port, a VBST-enabled device uses STP BPDUs (if the remote device runs STP) or RST BPDUs (if the remote device runs RSTP) to communicate with the remote device based on the VLAN to which the access port belongs. Topology calculation is performed as defined by STP/RSTP. As STP/RSTP does not differentiate VLANs, a spanning tree shared by VLANs is formed.
* For a trunk port:
  + When a VBST-enabled device connects to an RSTP-enabled device, the former uses RST BPDUs in VLAN 1 and VBST BPDUs with the Data field of RST BPDUs in other VLANs to communicate with the latter.
  + When a VBST-enabled device connects to an STP-enabled device, the former uses STP BPDUs in VLAN 1 and VBST BPDUs with the Data field of STP BPDUs in other VLANs to communicate with the latter.

The following describes how a spanning tree is formed, as shown in [Figure 3](#EN-US_CONCEPT_0000001563768673__fig16922154972114). STP/RSTP is deployed on DeviceA and DeviceB, and VBST is deployed on DeviceC and DeviceD. The four devices are connected through trunk ports, and the ports on DeviceA through DeviceD allow packets from VLAN 1 and VLAN 10 to pass through.

An STP/RSTP-enabled device can send and receive STP/RST BPDUs, but can only transparently transmit VBST BPDUs. As such, a spanning tree is formed in VLAN 1 as defined in STP/RSTP.

![](public_sys-resources/note_3.0-en-us.png) 

When an STP/RSTP-enabled device is a campus switch, it cannot transparently transmit VBST BPDUs.


**Figure 3** Interworking between VBST and STP/RSTP through trunk ports  
![](figure/en-us_image_0000001512689226.png)

For the purposes of this example, assume that the blocked port of the spanning tree in VLAN 1 is located on DeviceD. As VBST runs on DeviceD, and the blocked port exists in VLAN 1, DeviceD can still receive and forward VBST BPDUs with VLAN ID 10. Loops occur in VLAN 10, so spanning tree calculation is triggered there. DeviceA and DeviceB transparently transmit VBST BPDUs with VLAN ID 10, so only four ports on DeviceC and DeviceD participate in spanning tree calculation in VLAN 10. The spanning trees in VLAN 1 and VLAN 10 are then formed, as shown in [Figure 3](#EN-US_CONCEPT_0000001563768673__fig16922154972114).

Assume that the blocked port of the spanning tree in VLAN 1 is located on DeviceB. STP/RSTP runs on DeviceB. After a port on DeviceB is blocked, DeviceB cannot forward VBST BPDUs with VLAN ID 10 and no loop occurs in VLAN 10. Consequently, spanning tree calculation in VLAN 10 is not triggered. VBST BPDUs with VLAN ID 10 can be forwarded along the spanning tree in VLAN 1 (VLAN 10 and VLAN 1 share the spanning tree), as shown in [Figure 3](#EN-US_CONCEPT_0000001563768673__fig16922154972114).

In order to implement load balancing when a VBST-enabled device connects to an STP/RSTP-enabled device, the trunk ports must be used to connect both devices and the blocked port must be located on the VBST-enabled device. It is recommended that trunk ports be used for interworking between VBST and STP/RSTP.


#### Interworking Between VBST and PVST/PVST+/Rapid PVST+

On a live network, a VBST-enabled device may connect to a device enabled with PVST/PVST+/Rapid PVST+.

* For an access port:
  
  A VBST-enabled device uses STP BPDUs (if the remote device runs PVST/PVST+) or RST BPDUs (if the remote device runs Rapid PVST+) to communicate with the remote device based on the VLAN to which the access port belongs. Topology calculation is performed as defined by STP/RSTP. As STP/RSTP does not differentiate VLANs, a spanning tree shared by VLANs is formed.
* For a trunk port:
  
  + When a VBST-enabled device connects to a device enabled with Rapid PVST+, the former uses RST BPDUs (and VBST BPDUs with the Data field of RST BPDUs) in VLAN 1 and VBST BPDUs with the Data field of RST BPDUs in other VLANs to communicate with the latter.
  + When a VBST-enabled device connects to a device enabled with PVST+, the former uses STP BPDUs (and VBST BPDUs with the Data field of STP BPDUs) in VLAN 1 and VBST BPDUs with the Data field of STP BPDUs in other VLANs to communicate with the latter.
  + When a VBST-enabled device connects to a PVST-enabled device, packet exchange is similar to that in scenarios where a VBST-enabled device connects to a device enabled with PVST+. The difference, however, is that the VBST-enabled device and the PVST-enabled device send only VBST BPDUs with the Data field of STP BPDUs in VLAN 1.
  
  As both devices can identify the BPDUs carrying VLAN information, a VLAN-based spanning tree is formed. The connection between a VBST-enabled device and a device enabled with PVST/PVST+/Rapid PVST+ through trunk ports is similar to that between two VBST-enabled devices.