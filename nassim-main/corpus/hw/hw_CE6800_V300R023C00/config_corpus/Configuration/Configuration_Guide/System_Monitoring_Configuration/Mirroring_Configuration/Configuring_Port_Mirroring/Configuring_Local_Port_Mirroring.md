Configuring Local Port Mirroring
================================

Configuring Local Port Mirroring

#### Prerequisites

The task of [Configuring an Observing Port](galaxy_mirror_cfg_0031.html) has been completed.


#### Context

Port mirroring copies the packets passing through a port to an observing port, which then sends mirrored packets to a monitoring device. Local port mirroring is used when an observing port is directly connected to a monitoring device.

![](public_sys-resources/note_3.0-en-us.png) 

* For fragments, port mirroring mirrors fragments received on ports.
* Enabling the port mirroring function helps locate network faults. However, this function may affect device performance. Exercise caution when using this function. Disable the port mirroring function after network fault locating is complete.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view, that is, the view of the interface to be configured as a mirrored port.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the interface to mirror traffic to an observing port or an observing port group.
   
   
   ```
   [port-mirroring observe-port](cmdqueryname=port-mirroring+observe-port) { observe-port-index | group group-id } { both | inbound | outbound }
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display port-mirroring**](cmdqueryname=display+port-mirroring) command to check the mirroring configuration.