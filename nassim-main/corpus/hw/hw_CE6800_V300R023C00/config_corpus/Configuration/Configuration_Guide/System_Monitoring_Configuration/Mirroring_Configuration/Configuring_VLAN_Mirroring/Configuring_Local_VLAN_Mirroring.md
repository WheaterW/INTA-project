Configuring Local VLAN Mirroring
================================

Configuring Local VLAN Mirroring

#### Prerequisites

The task of [Configuring an Observing Port](galaxy_mirror_cfg_0031.html) has been completed.


#### Context

VLAN mirroring copies the packets received and sent by active interfaces in a VLAN to an observing port, which then sends mirrored packets to a monitoring device. Local VLAN mirroring is used when an observing port is directly connected to a monitoring device.

![](public_sys-resources/note_3.0-en-us.png) 

To perform inbound VLAN mirroring on the packets that require VLAN mapping, configure inbound VLAN mirroring in the view of the mapped VLAN specified in VLAN mapping. The original packets for which VLAN mapping is to be performed are mirrored.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure VLAN mirroring.
   
   
   ```
   [mirroring observe-port](cmdqueryname=mirroring+observe-port) { observe-port-index | group group-id } { inbound | outbound | both }
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display port-mirroring**](cmdqueryname=display+port-mirroring) command to check the mirroring configuration.