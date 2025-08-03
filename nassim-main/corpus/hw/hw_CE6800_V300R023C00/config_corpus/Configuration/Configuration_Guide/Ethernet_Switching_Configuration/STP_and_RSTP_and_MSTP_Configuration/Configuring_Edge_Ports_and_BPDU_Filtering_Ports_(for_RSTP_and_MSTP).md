Configuring Edge Ports and BPDU Filtering Ports (for RSTP/MSTP)
===============================================================

Configuring Edge Ports and BPDU Filtering Ports (for RSTP/MSTP)

#### Context

RSTP or MSTP defines a port that is located at the network edge and directly connected to a terminal device as an edge port.

Edge ports do not receive or process configuration BPDUs or participate in RSTP or MSTP calculation. They can change from the Disabled state to the Forwarding state in an instant, as if RSTP or MSTP were disabled.

Edge ports send BPDUs. If the BPDUs are sent to other networks, flapping may occur on these networks. BPDU filtering can be configured on the edge ports to disable them from processing and sending BPDUs.

![](public_sys-resources/note_3.0-en-us.png) 

If all ports on a device are configured as edge ports and BPDU filtering ports in the system view, all of the device's ports will be in Forwarding state and none of them will send BPDUs or negotiate parameters related to the spanning tree protocol with directly connected ports on the peer device. However, this may cause network loops, leading to broadcast storms. Exercise caution when configuring these ports.

If a port is configured as an edge port and BPDU filtering port in the interface view, the port will not process or send BPDUs and cannot negotiate parameters related to the spanning tree protocol with the directly connected port on the peer device. Exercise caution when configuring this port.

Automatic edge port detection is enabled by default after RSTP or MSTP is enabled for a port. If the port does not receive a BPDU within (2 x Hello Time + 1) seconds, the port will be specified as an edge port automatically. If it receives BPDUs within the specified time, it will be specified as a non-edge port.

Automatic edge port detection does not take effect in the following cases:

* The [**stp edged-port enable**](cmdqueryname=stp+edged-port+enable) or [**stp edged-port disable**](cmdqueryname=stp+edged-port+disable) command has been configured in the interface view.
* The [**stp edged-port default**](cmdqueryname=stp+edged-port+default) command has been configured in the system view.

Terminals cannot participate in RSTP or MSTP calculation or respond to BPDUs. To configure a device port connected to a terminal, you can use either of the following methods:

* Configure the port as an edge port and enable BPDU filtering.
* Disable RSTP or MSTP on the port to keep it in the Forwarding state.

For optimal availability and security, you are recommended to configure the port as an edge port. If a loop occurs on the terminal, the port will automatically become a non-edge port and the loop is eliminated after the spanning tree is recalculated. You can enable BPDU protection to prevent malicious spoofing BPDU attacks against the device. For details, see [Configuring BPDU Protection](vrp_stp_cfg_1111.html).


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

Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ] command to check the edge port configuration based on the Port Edged field.