Device Roles, Port Roles, and Port States
=========================================

After a spanning tree protocol is enabled on devices, the devices start spanning tree calculation by exchanging [Bridge Protocol Data Units (BPDUs)](vrp_stp_cfg_1067.html). After the role of each device, the role of each port on each device, and the state of each port are determined, spanning tree calculation and convergence are complete, and the network is stabilized.

#### Device Role

The key to loop prevention is to generate a tree-shaped network where there must be a root bridge (RB). It is the logical center, but not necessarily the physical center, of the network. All devices except root bridges are non-root bridges on the network. The devices that function as root bridges change dynamically with the network topology.

There is only one root bridge on a network running STP or RSTP whereas there can be multiple root bridges on an MSTP network as there can be multiple spanning trees.


#### Port Role

[Table 1](#EN-US_CONCEPT_0000001345478617__table546825444219) lists the port roles supported in STP, RSTP, and MSTP, among which the root port (RP) and designated port (DP) are the basic port roles.

Compared with STP, RSTP adds three port roles: alternate port, backup port, and edge port.

MSTP adds two extra port roles to those defined in RSTP: master port and regional edge port.

**Table 1** Port roles defined in STP, RSTP, and MSTP
| Spanning Tree Protocol | Root Port | Designated Port | Alternate Port | Backup Port | Edge Port | Master Port | Regional Edge Port |
| --- | --- | --- | --- | --- | --- | --- | --- |
| STP | â | â | x | x | x | x | x |
| RSTP | â | â | â | â | â | x | x |
| MSTP | â | â | â | â | â | â | â |

**Root Port**

The root port is the port with the smallest path cost to the root bridge and is responsible for forwarding data to the root bridge. A device running STP or RSTP has only one root port; however, the root bridge does not have a root port.

**Designated Port**

[Table 2](#EN-US_CONCEPT_0000001345478617__tab_dc_fd_stp_000503) defines the designated port and designated bridge.

**Table 2** Designated bridge and designated port
| Reference Object | Designated Bridge | Designated Port |
| --- | --- | --- |
| Device | A directly connected device that forwards configuration BPDUs to the device. | Designated bridge's port that forwards configuration BPDUs to the device. |
| LAN | A device that forwards configuration BPDUs to the LAN. | Designated bridge's port that forwards configuration BPDUs to the LAN. |

In [Figure 1](#EN-US_CONCEPT_0000001345478617__fig16744155024212), AP 1 and AP 2 are ports of DeviceA, BP 1 and BP 2 are ports of DeviceB, and CP 1 and CP 2 are ports of DeviceC.

* DeviceA sends configuration BPDUs to DeviceB through AP 1. DeviceA is the designated bridge of DeviceB, and AP 1 is the designated port on DeviceA.
* DeviceB and DeviceC are connected to the LAN. If DeviceB sends configuration BPDUs to the LAN, DeviceB is the designated bridge for the LAN, and BP 2 is the designated port on DeviceB.

**Figure 1** Designated bridge and designated port  
![](figure/en-us_image_0000001291918988.png)

**Alternate Port**

An alternate port backs up the root port and provides an alternate path from the designated bridge to the root bridge. It is blocked after learning the configuration BPDUs sent by other bridges.

**Backup Port**

A backup port backs up a designated port and provides a backup path from the root bridge to the related network segment. It is blocked after learning the configuration BPDUs sent by itself.

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001345478617__fig2165508171), CP 2 on DeviceC is the root port, and CP 1 is the alternate port. If CP 2 fails, CP 1 becomes the root port. On DeviceB, BP 1 is the designated port and BP 2 is the backup port. If BP 1 fails, BP 2 becomes the designated port.

**Figure 2** Alternate port and backup port  
![](figure/en-us_image_0000001345238521.png)

**Edge Port**

An edge port is located at the edge of a network and directly connected to a terminal device. This port does not participate in spanning tree calculation and can transition to Forwarding state immediately.

Edge port detection starts after a spanning tree protocol is enabled on a port. If the port fails to receive BPDUs within (2 x [Hello timer intervals](vrp_stp_cfg_1068.html#EN-US_CONCEPT_0000001292398344__section4282551598) + 1) seconds, the port is set to an edge port. Otherwise, the port is set to a non-edge port. Edge port detection does not take effect for manually configured edge ports.

**Master Port**

The following describes the basic concepts of MSTP before describing the master port and regional edge port. An MSTP network consists of one or more Multiple Spanning Tree (MST) regions, each of which contains one Internal Spanning Tree (IST). A Common Spanning Tree (CST) connects all MST regions on the network. All ISTs and the CST form a Common and Internal Spanning Tree (CIST). The CIST root is the root bridge of the CIST.

A master port is the nearest port in an MST region to the CIST root, and sends packets of an MST region to the CIST root.

**Regional Edge Port**

A regional edge port is located at the edge of an MST region and connects to another MST region or a Single Spanning Tree (SST).

Master ports are special regional edge ports, functioning as root ports on CISTs and master ports in instances.

On the network shown in [Figure 3](#EN-US_CONCEPT_0000001345478617__fig113051223667), DeviceA, DeviceB, DeviceC, and DeviceD form an MST region. AP 1, DP 1, and DP 2 in the MST region are directly connected to other regions and are edge ports in this MST region. AP 1 on DeviceA, being the nearest port in the region to the CIST root, is the master port.

**Figure 3** Master port and regional edge ports  
![](figure/en-us_image_0000001345478665.png)

#### Port States

**STP Port State**

[Table 3](#EN-US_CONCEPT_0000001345478617__table2093315106241) describes five port states on a device running STP. [Figure 4](#EN-US_CONCEPT_0000001345478617__fig16972458833) shows the state transitions of an STP port.

**Table 3** STP port states
| Port State | Description |
| --- | --- |
| Disabled | A port in Disabled state is down and does not process BPDUs or forward user traffic. |
| Blocking | A port in Blocking state receives and processes BPDUs, and does not forward user traffic. |
| Listening | This is a transitional state, where spanning tree calculation starts. The port sends and receives BPDUs, but does not forward user traffic. |
| Learning | This is a transitional state, where the device establishes a MAC address table. The port in this state receives and sends BPDUs, but does not forward user traffic. |
| Forwarding | A port in Forwarding state forwards user traffic and processes BPDUs. Only the root port and designated port can enter the Forwarding state. |


**Figure 4** STP port state transitions  
![](figure/en-us_image_0000001292398380.png)

1. If the port is up or enabled with STP, it enters the Blocking state from the Disabled state.
2. If the port is selected as the root port or designated port, it enters the Listening state.
3. If the Forward Delay timer of the port expires, it enters the Learning or Forwarding state.
4. If a port is no longer the root port or designated port, it enters the Blocking state.
5. If a port is down or has STP disabled, it enters the Disabled state.

![](public_sys-resources/note_3.0-en-us.png) 

By default, a Huawei network device works in MSTP mode. After a device transitions from the MSTP mode to STP mode, its STP ports support only those states defined in MSTP, which are Forwarding, Learning, and Discarding. For details, see RSTP/MSTP Port States.

**RSTP/MSTP Port States**

RSTP/MSTP supports three port states, as shown in [Table 4](#EN-US_CONCEPT_0000001345478617__tab_dc_fd_stp_000506).

**Table 4** RSTP/MSTP port states
| Port State | Description |
| --- | --- |
| Forwarding | A port in Forwarding state sends and receives BPDUs. It also forwards user traffic and learns MAC addresses. |
| Learning | This is a transitional state, where the device establishes a MAC address table. The port in Listening state receives and sends BPDUs, but does not forward user traffic. |
| Discarding | A port in Discarding state only receives BPDUs. It does not forward user traffic or learn MAC addresses. |

Port states are not necessarily related to port roles. [Table 5](#EN-US_CONCEPT_0000001345478617__tab_dc_fd_stp_001203) lists possible states for different port roles. The value **Yes** indicates that the port supports this state whereas the value **No** indicates that the port does not support this state.

**Table 5** Mapping between port states and port roles
| Port State | Root Port/Master Port | Designated Port | Edge Port/Regional Edge Port | Alternate Port | Backup Port |
| --- | --- | --- | --- | --- | --- |
| Forwarding | Yes | Yes | Yes | No | No |
| Learning | Yes | Yes | Yes | No | No |
| Discarding | Yes | Yes | Yes | Yes | Yes |