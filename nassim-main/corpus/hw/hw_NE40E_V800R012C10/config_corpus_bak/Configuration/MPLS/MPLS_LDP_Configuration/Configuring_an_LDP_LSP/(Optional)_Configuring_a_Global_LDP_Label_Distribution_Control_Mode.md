(Optional) Configuring a Global LDP Label Distribution Control Mode
===================================================================

An LDP label distribution control mode can be globally configured to enable a local node to control the sequence of distributing labels to upstream nodes.

#### Context

A label distribution control mode defines how an LSR distributes labels during the establishment of an LSP.

There are two label distribution control modes:

* **Label distribution control in independent mode**
  
  In independent label distribution control mode, a local LSR independently distributes and binds a label to a FEC and notifies the upstream LSR of the label without waiting for a label from the downstream LSR.
  
  + If the label advertisement mode is DU and the label distribution control mode is independent, an LSR directly distributes a label to its upstream LSR, without waiting for a label from the downstream LSR.
  + If the label advertisement mode is DoD and the distribution control mode is independent, an LSR distributes a label to its upstream LSR after receiving a label request from the upstream LSR, without waiting for a label from the downstream LSR.
* **Label distribution control in ordered mode**
  
  In ordered label distribution control mode, an LSR sends the label mapping of a FEC to the upstream device only if the LSR has received the Label Mapping message from the next hop of the FEC or if the LSR is the egress of the FEC.
  
  + If the label advertisement mode is DU and the label distribution control mode is ordered, an LSR distributes a label to its upstream device only after receiving a Label Mapping message from the downstream device.
  + If the label advertisement mode is DoD and the label distribution control mode is ordered, the downstream LSR of a directly connected LSR distributes a label to the upstream LSR only after receiving a Label Mapping message from the directly connected LSR.

The default label distribution control mode is recommended.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp+vpn-instance) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MPLS-LDP or MPLS-LDP-VPN instance view is displayed.
3. Run [**label distribution control-mode**](cmdqueryname=label+distribution+control-mode+independent+ordered) { **independent** | **ordered** }
   
   
   
   The global LDP label distribution control mode is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.