Configuring a Load Balancing Mode for GRE Packets
=================================================

Configuring a Load Balancing Mode for GRE Packets

#### Context

Equal-Cost Multi-Path (ECMP) implements load balancing and link backup among multiple paths. ECMP applies to a network where multiple links to the same destination are available. If a traditional routing technology is used, packets are forwarded to the destination through only one link; the other links remain in backup or inactive state; switching between links requires a certain period when dynamic routes are used. Unlike traditional routing technologies, ECMP can use multiple links to increase transmission bandwidth and to take over traffic from a faulty link without any delay or packet loss. ECMP can be performed on GRE packets based on the following factors:

* Inner source IP address of packets (inner-src-ip)
* Inner destination IP address of packets (inner-dst-ip)
* Inner transport-layer source port of packets (inner-l4-sport)
* Inner transport-layer destination port of packets (inner-l4-dport)
* Inner transport layer protocol of packets (inner-protocol)
* Source port number (src-interface)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the ECMP view.
   
   
   ```
   [load-balance ecmp](cmdqueryname=load-balance+ecmp)
   ```
3. Configure a load balancing mode for GRE packets.
   
   
   ```
   [ip-tunnel](cmdqueryname=ip-tunnel) { inner-src-ip | inner-dst-ip | inner-l4-sport | inner-l4-dport | inner-protocol | src-interface } *
   ```
   
   By default, GRE packets are load balanced based on inner-src-ip, inner-dst-ip, inner-l4-sport, and inner-l4-dport. Perform this task if you need to change the load balancing mode of GRE packets.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```