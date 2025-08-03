MSTP Topology Calculation
=========================

MSTP Topology Calculation

#### Basic Concepts of MSTP

An MSTP network consists of one or more Multiple Spanning Tree (MST) regions, each of which contains one or more Multiple Spanning Tree Instances (MSTIs). An MSTI is a tree network consisting of devices running STP, RSTP, or MSTP.

**Figure 1** MSTP network hierarchy  
![](figure/en-us_image_0000001345238529.png)

**MST Region**

An MST region contains a collection of interconnected devices that have the following characteristics:

* Having MSTP enabled
* Same region name
* Same VLAN-to-MSTI mappings
* Same MSTP revision level

A LAN can be composed of several MST regions that are directly or indirectly connected, and multiple devices can be grouped into an MST region using MSTP configuration commands.

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001292238704__fig11837185218315), MST region 4 contains DeviceB, DeviceC, DeviceD, and DeviceE, and has three MSTIs.

**Figure 2** MST region  
![](figure/en-us_image_0000001345478673.png)

**VLAN Mapping Table**

The VLAN mapping table maps VLANs to MSTIs.

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001292238704__fig11837185218315), the VLAN mapping table of MST region 4 specifies that:

* VLAN 1 is mapped to MSTI 1.
* VLAN 2 is mapped to MSTI 2.
* Other VLANs are mapped to MSTI 3.

**CST, IST, CIST, and SST**

* A Common Spanning Tree (CST) connects all MST regions on a network.
  
  If each MST region is considered a node, the CST is calculated by STP or RSTP based on all the nodes. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001292238704__fig1943761219), the MST regions are connected to form a CST.
* An Internal Spanning Tree (IST) resides within an MST region.
  
  It can be considered as a special MSTI with the ID of 0 and is called MSTI 0.
  
  An IST is a segment of the Common and Internal Spanning Tree (CIST) in an MST region. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001292238704__fig1943761219), the devices in an MST region are connected to form an IST.
* A CIST is calculated by STP or RSTP and connects all the devices on a network. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001292238704__fig1943761219), the CIST is the complete spanning tree formed by the ISTs and the CST.
* A Single Spanning Tree (SST) is formed in either of the following situations:
  + A device running STP or RSTP belongs to only one spanning tree.
  + An MST region has only one device.

**Regional Root, CIST Root, and Master Bridge**

* Regional roots are classified into IST and MSTI regional roots.
  
  IST regional roots: In the MST regions on the network shown in [Figure 1](#EN-US_CONCEPT_0000001292238704__fig1943761219), the devices closest to the CIST root are IST regional roots.
  
  MSTI regional roots: An MST region can contain multiple spanning trees, each called an MSTI. An MSTI regional root is the root of the MSTI. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001292238704__fig1943761219), each MSTI has its own regional root.
* CIST root is the root bridge of a CIST, such as DeviceA shown in [Figure 1](#EN-US_CONCEPT_0000001292238704__fig1943761219).
* The master bridge is the IST master, which is the device closest to the CIST root in a region, such as the yellow device shown in [Figure 1](#EN-US_CONCEPT_0000001292238704__fig1943761219).
  
  The CIST root is always the master bridge of the MST region that it is in.

#### MSTP Topology Calculation

MSTP divides an entire Layer 2 network into multiple MST regions and calculates the CST. In an MST region, multiple spanning trees are calculated, each of which is called an MSTI. Of these MSTIs, MSTI 0 is also known as the IST. Just like STP, MSTP uses configuration BPDUs to calculate spanning trees, except that the configuration BPDUs are MSTP-specific.

**Vectors**

Both MSTIs and the CIST are calculated based on vectors, which are carried in MST BPDUs. So, calculating MSTIs and the CIST requires devices to exchange MST BPDUs.

* The following vectors participate in the CIST calculation:
  
  {root ID, external root path cost, regional root ID, internal root path cost, designated device ID, designated port ID, receiving port ID}
* The following vectors participate in the MSTI calculation:
  
  {regional root ID, internal root path cost, designated device ID, designated port ID, receiving port ID}

The vectors in curly braces are listed in descending order of priority. [Table 1](#EN-US_CONCEPT_0000001292238704__tab_dc_fd_stp_001401) describes the vectors.

**Table 1** Vector description
| **Vector Name** | **Description** |
| --- | --- |
| Root ID | Indicates the root device for the CIST. The root ID consists of the priority value (16 bits) and MAC address (48 bits).  The priority value is the priority of MSTI 0. |
| External root path cost (ERPC) | Indicates the path cost from a CIST regional root to the root. All devices in an MST region have the same ERPC. The ERPC is 0 for all devices in an MST region with the CIST root. |
| Regional root ID | Indicates the MSTI regional root. The regional root ID consists of the priority value (16 bits) and MAC address (48 bits).  The priority value is the priority of MSTI 0. |
| Internal root path cost (IRPC) | Indicates the path cost from the local bridge to the regional root. The IRPC on a regional edge port is greater than that saved on a non-regional edge port. |
| Designated device ID | Indicates the nearest upstream bridge along the path from the local bridge to the regional root for the CIST or MSTIs. If the local bridge is the root or the regional root, this ID is the local bridge ID. |
| Designated port ID | Indicates the port on the designated device connected to the root port on the local bridge. The port ID consists of the priority value (4 bits) and port number (12 bits). The priority value must be a multiple of 16. |
| Receiving port ID | Indicates the port receiving the BPDU. The port ID consists of the priority value (4 bits) and port number (12 bits). The priority value must be a multiple of 16. |

****Comparison Principles****

For a vector, the smaller the priority value, the higher the priority.

Vectors are compared in the following order:

1. Root device IDs
2. ERPCs
3. Regional root IDs
4. IRPCs
5. Designated device IDs
6. Designated port IDs
7. Receiving port IDs

If the priority of a vector carried in the configuration BPDU received by a port is higher than that in the configuration BPDU saved on the port, the port replaces the saved configuration BPDU with the received one and updates the global configuration BPDU saved on the device. Otherwise, the port discards the received BPDU.

**CIST Calculation**

After completing the configuration BPDU comparison, the device with the highest priority on the entire network is selected as the CIST root. MSTP calculates an IST for each MST region, and calculates a CST to interconnect MST regions. On the CST, each MST region is considered a device. The CST and ISTs constitute a CIST for the entire network.

**MSTI Calculation**

In an MST region, MSTP calculates an MSTI for each VLAN based on mappings between VLANs and MSTIs, with each MSTI calculated independently. The calculation process is similar to the process in which STP calculates a spanning tree.

MSTIs have the following characteristics:

* The spanning tree is calculated independently for each MSTI, and spanning trees of MSTIs are independent of each other.
* The calculation method of spanning trees of MSTIs is similar to that of STP.
* Spanning trees of MSTIs can have different roots and topologies.
* Each MSTI sends BPDUs in its spanning tree.
* The topology of each MSTI is determined by command configurations.
* A port can be configured with different spanning tree parameters for different MSTIs.
* A port can play different roles or have different states in different MSTIs.

On an MSTP-enabled network, a VLAN packet is forwarded along the following paths:

* Along an MSTI (in an MST region)
* Along a CST (between MST regions)