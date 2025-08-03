Configuring a Load Balancing Mode for VXLAN Packets
===================================================

Configuring a Load Balancing Mode for VXLAN Packets

#### Context

![](../public_sys-resources/note_3.0-en-us.png) 

Only the following device models support the configuration of the load balancing mode for VXLAN packets: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.

Equal-Cost Multi-Path Routing (ECMP) implements load balancing and link backup among multiple paths. It applies to a network where multiple links to the same destination are available. If a traditional routing technology is used, packets are forwarded to the destination through one link only (with others remaining in a backup or inactive state), and switching between links requires a certain amount of time when dynamic routes are used. Unlike traditional routing technologies, ECMP can use multiple links to increase transmission bandwidth and to take over traffic from a faulty link without any delay or packet loss. ECMP can be performed on VXLAN packets based on the following factors:

* Inner source IP address of packets (inner-src-ip)
* Inner destination IP address of packets (inner-dst-ip)
* Inner transport-layer source port of packets (inner-l4-sport)
* Inner transport-layer destination port of packets (inner-l4-dport)
* Inner transport layer protocol of packets (inner-protocol)
* Source port number (src-interface)
* VNI of VXLAN packets (vni)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the ECMP view.
   
   
   ```
   [load-balance ecmp](cmdqueryname=load-balance+ecmp)
   ```
3. Configure a load balancing mode for VXLAN packets.
   
   
   ```
   [vxlan](cmdqueryname=vxlan+%28ECMP%29) { inner-src-ip | inner-dst-ip | inner-l4-sport | inner-l4-dport | inner-protocol | src-interface | vni } *
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```