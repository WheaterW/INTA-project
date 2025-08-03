Configuring a VBDIF Interface
=============================

Configuring a VBDIF Interface

#### Context

A BD is a Layer 2 broadcast domain used to forward VXLAN data packets. VBDIF interfaces can be used to implement communication between different VXLAN networks and between VXLAN and non-VXLAN networks, and connect a Layer 2 network to a Layer 3 network.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported by the CE6885-LL (low-latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VBDIF interface and enter its view.
   
   
   ```
   [interface vbdif](cmdqueryname=interface+vbdif) bd-id
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```