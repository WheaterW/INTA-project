Overview of IPv4 User-Side Multicast
====================================

This section describes the definition and purpose of user-side multicast.

#### Definition

User-side multicast enables a BRAS to identify users of a multicast program.

In [Figure 1](#EN-US_CONCEPT_0172367607__fig_dc_vrp_bras-multicast_cfg_000101), when the set top box (STB) and phone users go online, they send Internet Group Management Protocol (IGMP) Report messages of a multicast program to the BRAS. After receiving the messages, the BRAS identifies the users and sends a Protocol Independent Multicast (PIM) Join message to the network-side rendezvous point (RP) or the source's designated router (DR). The RP or source's DR creates multicast forwarding entries for the users and receives the required multicast traffic from the source. The BRAS finally sends the multicast traffic to the STB and phone users based on their forwarding entries and replication modes. The multicast replication in this example is based on sessions.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Now user-side multicast supports IPv4 and IPv6. For IPv4 users, user-side multicast applies to both private and public networks. For IPv6 users, user-side multicast applies only to public networks.

On Layer 2, user-side multicast supports the PPPoE and IPoE access modes for common users and the IPoE access mode for E-Line users.


**Figure 1** User-side multicast  
![](images/fig_dc_vrp_bras-multicast_cfg_000101.png)

#### Purpose

Because conventional multicast does not provide a method to identify users, carriers cannot effectively manage multicast users who access services such as Internet Protocol television (IPTV). Such users can join multicast groups, without notification, by sending Internet Group Management Protocol (IGMP) Report messages. To identify these users and allow for improved management of them, Huawei provides the user-side multicast feature.