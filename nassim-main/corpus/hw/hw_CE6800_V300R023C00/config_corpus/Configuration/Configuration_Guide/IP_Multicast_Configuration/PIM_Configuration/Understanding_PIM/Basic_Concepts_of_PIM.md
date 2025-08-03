Basic Concepts of PIM
=====================

Basic Concepts of PIM

#### PIM Device

A PIM device refers to a device on whose interfaces PIM is enabled. PIM devices are classified into the following types:

* Leaf devices: PIM devices (DeviceA, DeviceB, and DeviceC in [Figure 1](#EN-US_CONCEPT_0000001130783610__fig_dc_vrp_multicast_cfg_000401) for example) connected to user hosts. The user hosts connected to leaf devices are not necessarily multicast group members.
* First-hop device: a PIM device (DeviceE in [Figure 1](#EN-US_CONCEPT_0000001130783610__fig_dc_vrp_multicast_cfg_000401) for example) that directly connects to the multicast source and is responsible for forwarding multicast data from the multicast source along the forwarding path.
* Last-hop devices: PIM devices (DeviceA and DeviceB in [Figure 1](#EN-US_CONCEPT_0000001130783610__fig_dc_vrp_multicast_cfg_000401) for example) that directly connect to multicast group members and are responsible for forwarding multicast data to these members along the forwarding path.
* Transit devices: PIM devices (DeviceD in [Figure 1](#EN-US_CONCEPT_0000001130783610__fig_dc_vrp_multicast_cfg_000401) for example) between the first-hop device and the last-hop devices on the multicast forwarding path.

**Figure 1** Multicast forwarding  
![](figure/en-us_image_0000001176743359.png)

#### PIM Routing Entries

The PIM routing table records all PIM routing entries, and the entries are delivered to the multicast forwarding table as forwarding entries to guide the forwarding of multicast messages. PIM has two types of forwarding entries: (S, G) and (\*, G) entries, in which S stands for a multicast source, G for a multicast group, and \* for any multicast source.

* An (S, G) entry applies only to the multicast messages with the source address being S and the group address being G.
* An (\*, G) entry applies to the multicast messages with any multicast source and the multicast group address being G.

When a PIM device receives a multicast message with the source address being S and the group address being G and the message passes the RPF check, the device forwards the message based on the following rules:

* If a matching (S, G) entry exists, the device forwards the message according to the entry.
* If no matching (S, G) entry exists, the device creates an (S, G) entry according to the (\*, G) entry, and then forwards the message according to the (S, G) entry.

PIM routing entries contain information such as the multicast source address, multicast group address, upstream interface, upstream neighbor, and downstream interface list to guide message forwarding. A multicast message is received by one upstream interface and is forwarded through one or more downstream interfaces.


#### MDT

On a PIM network, a point-to-multipoint (P2MP) multicast forwarding path is established for each multicast group. The multicast forwarding path is also called an MDT because of its tree structure.

MDTs are classified into the following types:

* Shortest path tree (SPT): The MDT with the multicast source as the root and group members as leaves is called an SPT. SPTs apply to both PIM-DM and PIM-SM networks.
  
  As shown in [Figure 1](#EN-US_CONCEPT_0000001130783610__fig_dc_vrp_multicast_cfg_000401), the path (DeviceEâDeviceDâDeviceB/DeviceA) is an SPT with Source as the root and HostA and HostB as leaves.
* Rendezvous point (RP) tree: The MDT with an RP as the root and multicast group members as leaves is called an RPT. RPTs apply to PIM-SM networks.