Configuring the Bridge MAC Address for Spanning Tree Calculation
================================================================

Configuring the Bridge MAC Address for Spanning Tree Calculation

#### Context

In some scenarios, two devices must be used as one root bridge to send BPDUs with the same bridge ID. However, each device typically uses a different bridge ID from other devices and has a unique MAC address. For such scenarios, you can configure the same bridge MAC address for the two devices to calculate the spanning tree.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the bridge MAC address for the device to calculate the spanning tree.
   
   
   ```
   [stp bridge-address](cmdqueryname=stp+bridge-address) mac-address
   ```
   
   By default, a device uses its MAC address as the bridge MAC address to calculate the spanning tree.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the following commands and check the CIST Bridge field for the bridge MAC address of the device.

* [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ]
* [**display stp global**](cmdqueryname=display+stp+global)