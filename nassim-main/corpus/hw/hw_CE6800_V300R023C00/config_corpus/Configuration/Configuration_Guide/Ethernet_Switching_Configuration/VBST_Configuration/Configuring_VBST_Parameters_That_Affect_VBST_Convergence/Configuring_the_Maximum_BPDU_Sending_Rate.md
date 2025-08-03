Configuring the Maximum BPDU Sending Rate
=========================================

Configuring the Maximum BPDU Sending Rate

#### Context

The more BPDUs that are sent by an interface within a Hello Time timer, the higher the interface BPDU sending rate, and the more resources are occupied in the system. Appropriately limiting the BPDU sending rate can prevent excess bandwidth usage caused by route flapping.

To set the same maximum BPDU sending rate for all interfaces on a device, run the [**stp transmit-limit**](cmdqueryname=stp+transmit-limit) command in the system view.

The [**stp transmit-limit**](cmdqueryname=stp+transmit-limit) command configuration in the interface view takes precedence over that in the system view. That is, if this command is configured in both the system view and interface view, the configuration in the interface view takes effect.


#### Procedure

* In the system view, set the maximum number of BPDUs that each interface can send per second.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Set the maximum number of BPDUs that each interface can send per second.
     
     
     ```
     [stp transmit-limit](cmdqueryname=stp+transmit-limit) packet-number
     ```
     
     By default, an interface sends a maximum of six BPDUs per second.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* In the interface view, set the maximum number of BPDUs that the specified interface can send per second.
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
  4. Set the maximum number of BPDUs that the interface can send per second.
     
     
     ```
     [stp transmit-limit](cmdqueryname=stp+transmit-limit) packet-number
     ```
     
     By default, the maximum number of BPDUs that an interface sends per second is the value configured using the [**stp transmit-limit**](cmdqueryname=stp+transmit-limit) command in the system view. If the [**stp transmit-limit**](cmdqueryname=stp+transmit-limit) command is not configured in the system view, an interface sends a maximum of six BPDUs per second.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) [ *vlan-id* ] **information** [ **global** ] command and check the Transit Limit field to verify the maximum BPDU send rate of the specified interface.