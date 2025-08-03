Configuring Transparent Transmission of BPDUs
=============================================

Configuring Transparent Transmission of BPDUs

#### Context

When an edge device on a backbone network is connected to edge devices on multiple user networks, the edge device on the backbone network forwards BPDUs through the hardware to improve BPDU forwarding efficiency. By default, a Layer 2 interface is not allowed to forward BPDUs when the device forwards BPDUs through the hardware. As a result, the edge devices on multiple user networks connected to the edge device on the backbone network cannot communicate with each other. In this case, you can configure the device to allow Layer 2 interfaces to forward BPDUs when the device forwards BPDUs through the hardware.

To enable Layer 2 interfaces to forward only tagged BPDUs and send untagged BPDUs to the CPU for processing, configure Layer 2 interfaces to forward tagged BPDUs when the device forwards BPDUs through the hardware in the system view.


#### Procedure

* Configuring transparent transmission of all BPDUs
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Change the interface working mode from Layer 3 to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure the Layer 2 interface to forward BPDUs when the device forwards BPDUs through the hardware.
     
     
     ```
     [bpdu bridge enable](cmdqueryname=bpdu+bridge+enable)
     ```
     
     
     By default, a Layer 2 interface is not allowed to forward BPDUs when the device forwards BPDUs through the hardware.![](public_sys-resources/note_3.0-en-us.png) 
     
     If BPDUs of a certain protocol (for example, STP) need to be forwarded through the hardware, disable the protocol globally before running the [**bpdu bridge enable**](cmdqueryname=bpdu+bridge+enable) command.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configuring transparent transmission of VLAN tagged-BPDUs.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the Layer 2 interface to forward VLAN tagged-BPDUs when the device forwards BPDUs through the hardware.
     
     
     ```
     [bpdu bridge tagged-packet enable](cmdqueryname=bpdu+bridge+tagged-packet+enable)
     ```
     
     By default, a Layer 2 interface is not allowed to forward VLAN tagged-BPDUs when the device forwards BPDUs through the hardware.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```