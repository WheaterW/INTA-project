Configuring Multicast Services over P2MP TE Tunnel
==================================================

Point-to-multipoint (P2MP) traffic engineering (TE) is a promising solution to multicast service transmission. P2MP TE helps carriers provide high TE capabilities and increased reliability on an IP/MPLS backbone network and reduce network operational expenditure (OPEX).

#### Usage Scenario

IP and MPLS are generally used to forward packets on traditional core and backbone networks. Deployment of multicast services, such as IPTV, multimedia conference, and real-time online games, continues to increase on IP/MPLS networks. These services require sufficient bandwidth, assured quality of service (QoS), and high reliability on the bearer network. Currently, the following multicast solutions are used to run multicast services, but these solutions cannot meet the requirements of multicast services and network carriers:

* IP multicast technology: It can be deployed on live point-to-point (P2P) networks to run multicast services, reducing network upgrade and maintenance costs. Similar to IP unicast, IP multicast does not support QoS or traffic planning and has low reliability. Multicast applications have high requirements on real-time transmission and reliability, and IP multicast technology cannot meet these requirements.
* Establishing a dedicated multicast network: A dedicated multicast network is usually constructed over Synchronous Optical Network (SONET)/Synchronous Digital Hierarchy (SDH). SONET/SDH has high reliability and provides a high transmission rate. However, this network requires high construction costs and OPEX and must be maintained separately.

IP/MPLS backbone network carriers require a multicast solution with high TE capabilities to run multicast services on existing IP/MPLS backbone network devices.

Multicast over P2MP TE tunnels can meet the carriers' requirements by establishing tree tunnels to transmit multicast data. It has the advantages of high IP multicast packet transmission efficiency and assured MPLS TE End-to-End (E2E) QoS.


#### Pre-configuration Tasks

Before configuring multicast services over P2MP TE tunnel, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM](dc_vrp_multicast_cfg_0006.html).
* [Configure a P2MP TE tunnel](dc_vrp_te-p2p_cfg_0133.html).


[Directing Multicast Traffic into a P2MP TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2197.html)

Multicast data traffic can be correctly forwarded over a point-to-multipoint (P2MP) traffic engineering (TE) tunnel only after being directed into the P2MP TE tunnel.

[Directing Multicast Traffic out of a P2MP TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2198.html)

When a point-to-multipoint (P2MP) traffic engineering (TE) tunnel is used to carry multicast services, you must direct multicast traffic out of the P2MP TE tunnel on the tunnel egress so that the multicast traffic can be correctly forwarded after leaving the tunnel.

[(Optional) Configuring Multicast Source Proxy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2199.html)

If a point-to-multipoint (P2MP) traffic engineering (TE) tunnel is used to carry multicast services and a rendezvous point (RP) is deployed on the egress side, configure multicast source proxy. Multicast source proxy enables a multicast source to register with the RP.

[Verifying the Configuration of Multicast over P2MP TE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2200.html)

After configuring multicast over point-to-multipoint (P2MP) traffic engineering (TE) tunnels, verify the configuration.