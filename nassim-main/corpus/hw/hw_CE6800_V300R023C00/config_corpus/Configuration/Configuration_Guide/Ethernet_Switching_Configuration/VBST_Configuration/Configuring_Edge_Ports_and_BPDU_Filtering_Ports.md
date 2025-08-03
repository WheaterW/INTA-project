Configuring Edge Ports and BPDU Filtering Ports
===============================================

Configuring Edge Ports and BPDU Filtering Ports

#### Context

VBST defines a port that is located at the network edge and directly connected to a terminal device as an edge port.

Edge ports do not receive or process configuration BPDUs or participate in VBST calculation. They can instantly change from the disable state to the forwarding state, as if VBST were disabled.

Edge ports send BPDUs, which if sent to other networks may cause flapping to occur. BPDU filtering can be configured on the edge ports to disable them from processing and sending BPDUs.

![](public_sys-resources/note_3.0-en-us.png) 

If all ports on a device are configured as edge ports and BPDU filtering ports in the system view, all of the device's ports will be in the forwarding state and none of them will send BPDUs or negotiate parameters related to the spanning tree protocol with directly connected ports on the peer device. However, this may cause network loops, leading to broadcast storms. Exercise caution when configuring these ports.

After a port is configured as an edge port and a BPDU filtering port in the interface view, the port does not process or send BPDUs and cannot negotiate parameters related to the spanning tree protocol with the directly connected port on the peer device. Exercise caution when configuring a port as an edge port and a BPDU filtering port.

Automatic edge port detection is enabled by default after VBST is enabled for a port. If the port does not receive a BPDU within (2 x Hello Timer + 1) seconds, the port will be specified as an edge port automatically. If it receives BPDUs within the specified time, it will be specified as a non-edge port. In VBST, each VLAN has a Hello timer. When a port is added to multiple VLANs, the port is automatically configured as an edge port if it does not receive BPDUs within (2 x min {Hello Timer} + 1). For example, if a port is simultaneously added to VLAN 2 (Hello Timer: 2 seconds), VLAN 3 (Hello Timer: 3 seconds), and VLAN 4 (Hello Timer: 4 seconds) and the port does not receive any BPDU within 5 seconds (2 x 2 + 1), the port is automatically configured as an edge port. If the [**stp edged-port enable**](cmdqueryname=stp+edged-port+enable) or [**stp edged-port disable**](cmdqueryname=stp+edged-port+disable) command is configured in the interface view or the [**stp edged-port default**](cmdqueryname=stp+edged-port+default) command is configured in the system view, automatic edge port detection does not take effect.

When configuring an edge port, pay attention to the following points:

* After all ports are configured as edge ports and BPDU filtering ports in the system view, no ports on the device send BPDUs or negotiate the VBST status with directly connected ports on the peer device. All ports are in forwarding state, which may cause loops on the network and lead to broadcast storms. Exercise caution when configuring all ports as edge ports and BPDU filtering ports.
* After a port is configured as an edge port and a BPDU filtering port in the interface view, the port does not process or send BPDUs. In this case, the port cannot negotiate the VBST status with the directly connected port on the peer device. Exercise caution when configuring a port as an edge port and a BPDU filtering port.

Terminal devices cannot participate in VBST calculation or respond to BPDUs. To configure a device port connected to a terminal device, you can use either of the following methods:

* Configure the port as an edge port and enable BPDU filtering.
* Disable VBST on the port to keep it in the forwarding state.

For optimal availability and security, you are recommended to configure the port as an edge port. If a loop occurs on the terminal device, the port will automatically become a non-edge port and break the loop. You can enable BPDU protection to prevent malicious BPDU spoofing attacks against the device. For details, see [Configuring BPDU Protection](galaxy_vbst_cfg_0025.html).


#### Procedure

* Configuration in the system view:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure all ports on the device as edge ports.
     
     
     ```
     [stp edged-port default](cmdqueryname=stp+edged-port+default)
     ```
     
     By default, all ports on a device are non-edge ports.
  3. Configure all ports on the device as BPDU filtering ports.
     
     
     ```
     [stp bpdu-filter default](cmdqueryname=stp+bpdu-filter+default)
     ```
     
     By default, all ports on a device are non-BPDU filtering ports.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configuration in the interface view:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure the port as an edge port.
     
     
     ```
     [stp edged-port](cmdqueryname=stp+edged-port) enable
     ```
     
     By default, all ports on a device are non-edge ports.
  5. Configure the port as a BPDU filtering port.
     
     
     ```
     [stp bpdu-filter](cmdqueryname=stp+bpdu-filter) enable
     ```
     
     By default, all ports on a device are non-BPDU filtering ports.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) [ *vlan-id* ] **information** command, check the Edged Port Default field to verify the global edge port configuration, check the Bpdu-filter Default field to verify the global BPDU filtering port configuration, and check the Port Edged field to verify the edge port configuration.
* Run the [**display this**](cmdqueryname=display+this) command in the interface view to check the BPDU filtering port configuration on an interface.