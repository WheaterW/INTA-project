Configuring the Format of MST BPDUs Sent and Received by a Port (for MSTP)
==========================================================================

Configuring the Format of MST BPDUs Sent and Received by a Port (for MSTP)

#### Context

Two MST BPDU formats are available: dot1s (defined in IEEE 802.1s) and legacy (proprietary BPDU format).

On an MSTP-enabled network where Huawei and non-Huawei devices are connected, you can designate the BPDU format or configure a port to automatically adjust the MST BPDU format. With this function, the port automatically adopts the BPDU format on the peer end.


#### Procedure

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
4. Configure the format of MST BPDUs received and sent by the port.
   
   
   ```
   [stp compliance](cmdqueryname=stp+compliance) { auto | dot1s | legacy }
   ```
   
   By default, the auto format is used.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] **interface** *interface-type* *interface-number* command and check the Port Protocol Type field to verify the format of MST BPDUs received and sent by the port.