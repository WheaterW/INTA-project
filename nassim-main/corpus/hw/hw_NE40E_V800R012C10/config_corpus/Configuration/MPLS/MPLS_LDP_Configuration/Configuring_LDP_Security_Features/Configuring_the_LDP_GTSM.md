Configuring the LDP GTSM
========================

The LDP Generalized TTL Security Mechanism (GTSM) needs to be configured on the LDP peers at both ends of an LDP session.

#### Context

The GTSM checks TTL values to verify packets and defends devices against attacks. LDP peers with the GTSM and a valid TTL range configured check TTLs in LDP messages exchanged between them. If the TTL in an LDP message is out of the valid range, this LDP message is considered invalid and discarded. The GTSM defends against CPU-based attacks initiated using a great number of forged packets and protects upper-layer protocols.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**gtsm peer**](cmdqueryname=gtsm+peer+valid-ttl-hops) *ip-address* **valid-ttl-hops** *hops*
   
   
   
   The LDP GTSM is configured.
   
   
   
   If the value of *hops* is set to the maximum number of valid hops permitted by the GTSM, when the TTL values carried in the packets sent by an LDP peer are within the range [255 â hops + 1, 255], the packets are accepted; otherwise, the packets are discarded.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.