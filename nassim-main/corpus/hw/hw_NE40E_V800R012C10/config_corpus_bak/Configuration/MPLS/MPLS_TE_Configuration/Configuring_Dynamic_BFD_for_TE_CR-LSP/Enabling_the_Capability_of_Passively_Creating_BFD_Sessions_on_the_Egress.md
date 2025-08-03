Enabling the Capability of Passively Creating BFD Sessions on the Egress
========================================================================

On a unidirectional LSP, creating a BFD session on the ingress playing the active role triggers the sending of LSP ping request messages to the egress node playing the passive role. Only after the passive role receives the ping packets, a BFD session can be automatically established.

#### Context

Perform the following steps on the egress:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
3. (Optional) Run [**passive-session udp-port**](cmdqueryname=passive-session+udp-port)**3784** **peer***peer-ip*
   
   
   
   The destination UDP port number of a specified passive BFD session is changed.
4. (Optional) Run [**passive-session detect-multiplier**](cmdqueryname=passive-session+detect-multiplier) *multiplier-value* **peer** *peerip-value*
   
   
   
   The detection multiplier is set for the specified passive BFD session.
5. Run [**mpls-passive**](cmdqueryname=mpls-passive)
   
   
   
   The capability of passively creating BFD sessions is enabled.
   
   After this command is run, a BFD session can be created only after the egress receives an LSP ping request message containing the BFD TLV from the ingress.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.