Enabling STP/RSTP/MSTP
======================

Enabling STP/RSTP/MSTP

#### Context

Enabling STP, RSTP, or MSTP on a ring network immediately triggers spanning tree calculation on the network. Parameters such as device priority and port priority can affect spanning tree calculation. Network flapping may occur if these parameters are changed during calculation. To ensure a quick, stable spanning tree calculation process, set parameters such as device priority and port priority before enabling STP, RSTP, or MSTP.

![](public_sys-resources/note_3.0-en-us.png) 

* On a network running STP/RSTP/MSTP, configure the core device as the root bridge to ensure the stability of the Layer 2 network. Failing to do so may cause service interruptions if deployment of new devices on the network triggers switchover of the root bridge.
* On a device enabled with STP/RSTP/MSTP, when a terminal connects to the device, the device performs spanning tree calculation again. As a result, it takes a long time for the terminal to obtain an IP address. In this case, configure the device port connected to the terminal as the edge port or disable the spanning tree protocol on this port.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable STP, RSTP, or MSTP.
   
   
   ```
   [stp enable](cmdqueryname=stp+enable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```