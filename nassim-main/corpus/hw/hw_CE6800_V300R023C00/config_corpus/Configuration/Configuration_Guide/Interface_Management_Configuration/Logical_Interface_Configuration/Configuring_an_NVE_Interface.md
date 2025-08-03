Configuring an NVE Interface
============================

Configuring an NVE Interface

#### Context

NVE interfaces are used to implement Layer 2 connectivity on a VXLAN by establishing VXLAN tunnels between NVEs and encapsulating/decapsulating VXLAN packets.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported by the CE6885-LL (low-latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an NVE interface and enter its view.
   
   
   ```
   [interface nve](cmdqueryname=interface+nve) interface-number
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```