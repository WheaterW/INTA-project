Configuring an Explicit Path
============================

GMPLS UNI cannot automatically discover paths between an IP network and a transport network. To ensure successful GMPLS UNI establishment, configure an explicit path on the ingress EN to traverse data channel interfaces on the ingress EN, ingress CN, egress EN, and egress CN.

#### Context

Determine whether you need to configure an explicit path based on a tunnel calculation mode:

* If paths are calculated separately at the IP and optical layers, configure an explicit path.
* If PCE is used to calculate a patch across both the IP and optical layers, you do not need to configure an explicit path. This is because PCE automatically calculates a path for a tunnel.

A GMPLS UNI tunnel originates from the ingress EN. An explicit path must be configured on the ingress EN for a GMPLS UNI tunnel.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

An explicit path for a GMPLS UNI tunnel, different from that for an MPLS TE tunnel, must pass through only four data channel interfaces on the ingress EN, ingress CN, egress EN, and egress CN. The four hops must be configured in the following sequence: ingress EN, ingress CN, egress EN, and egress CN.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**explicit-path**](cmdqueryname=explicit-path) *path-name*
   
   
   
   An explicit path is created and the explicit path view is displayed.
3. Run [**next hop**](cmdqueryname=next+hop) *ip-address*
   
   
   
   A next-hop address is specified for the explicit path.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Perform Step 3 for four consecutive times to complete the configuration of the explicit path for a GMPLS UNI tunnel.
4. (Optional) Perform the following steps to modify the configured explicit path:
   1. Run [**add hop**](cmdqueryname=add+hop+after+before) *ip-address1* { **after** | **before** } *ip-address2*
      
      
      
      A node is added to the explicit path.
   2. Run [**modify hop**](cmdqueryname=modify+hop) *ip-address1* *ip-address2*
      
      
      
      The address of a node is changed to the address of another existing node.
   3. Run [**delete hop**](cmdqueryname=delete+hop) *ip-address*
      
      
      
      A node is deleted from the explicit path.
5. (Optional) Run [**list hop**](cmdqueryname=list+hop) [ *ip-address* ]
   
   
   
   Information about nodes on the explicit path is displayed.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.