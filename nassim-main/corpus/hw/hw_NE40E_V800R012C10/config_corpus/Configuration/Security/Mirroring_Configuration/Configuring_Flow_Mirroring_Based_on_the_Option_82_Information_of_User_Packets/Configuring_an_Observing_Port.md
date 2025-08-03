Configuring an Observing Port
=============================

An observing port is used to copy the traffic on a mirrored port to a packet analyzer. To prevent running services from being adversely affected, do not use the observing port as a service port.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**port-observing observe-index**](cmdqueryname=port-observing+observe-index) *observe-index* [ **without-filter** ]
   
   
   
   The interface is configured as an observing port.
   
   
   
   An observing port sends the traffic obtained from the mirrored port to a packet analyzer without filtering or modifying frames. On the input side, frames are mirrored before having their headers removed. On the output side, frames are mirrored after being modified.
4. (Optional) Run [**port-observing with-linklayer-header**](cmdqueryname=port-observing+with-linklayer-header)
   
   
   
   Local mirroring is configured to mirror packets from their link layer headers.
5. (Optional) Run [**port-observing pop-label**](cmdqueryname=port-observing+pop-label) { **one** | **two** | **all** } [ **sub-interface** **extend** ]
   
   
   
   The observing port is enabled to remove MPLS labels from packets.
   
   
   
   The [**port-observing pop-label**](cmdqueryname=port-observing+pop-label) and [**port-observing dest-mac**](cmdqueryname=port-observing+dest-mac) commands are mutually exclusive.
6. (Optional) Run [**port-observing dest-mac**](cmdqueryname=port-observing+dest-mac) *dest-mac-address*
   
   
   
   A destination MAC address is configured for mirrored packets of the observing port.
   
   
   
   The [**port-observing dest-mac**](cmdqueryname=port-observing+dest-mac) *dest-mac-address* and [**port-observing pop-label**](cmdqueryname=port-observing+pop-label) commands are mutually exclusive.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.