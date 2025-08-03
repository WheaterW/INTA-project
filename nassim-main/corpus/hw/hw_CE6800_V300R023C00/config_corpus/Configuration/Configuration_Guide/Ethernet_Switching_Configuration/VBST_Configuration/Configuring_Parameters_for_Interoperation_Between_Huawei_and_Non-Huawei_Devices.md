Configuring Parameters for Interoperation Between Huawei and Non-Huawei Devices
===============================================================================

Configuring Parameters for Interoperation Between Huawei and Non-Huawei Devices

#### Context

When Huawei devices running VBST are connected to non-Huawei devices, the following parameters can be configured:

* Proposal/Agreement (P/A) mechanism
  
  The P/A mechanism (rapid transition mechanism) supports two modes: common and enhanced. The same mode must be configured on Huawei and non-Huawei devices to ensure proper communication between devices. You can configure Huawei devices to work in the same P/A mechanism where the non-Huawei devices work.
* Discarding non-standard STP/RST BPDUs sent by HanDreamnet switches
  
  On a network with Huawei devices and HanDreamnet switches, non-standard STP/RST BPDUs sent by HanDreamnet switches may cause transient loops. To prevent this, configure ports on Huawei devices to discard the non-standard STP/RST BPDUs received from HanDreamnet switches.
* Switchback delay
  
  When a VBST-enabled Huawei device is connected to a PVST-enabled non-Huawei device that does not support the P/A mechanism, the negotiation on the two ends is not synchronized and network convergence time increases. If the non-Huawei device is the root bridge and the Huawei device has an alternate port, in addition to the local port connected to the non-Huawei device, you can enable the switchback delay function on the local port. The switchback delay is 2 x Forward Delay + 8 seconds. This ensures that the port on the peer device completes the spanning tree calculation before the local port performs the spanning tree switchover when the status of the port on the peer device changes. In this way, services are not interrupted during the port status switchover. After the switchback delay function is enabled on a port, the function takes effect in all VLANs to which the port joins. If the device does not have an alternate port in a specific VLAN, the status of the local port can recover after a delay of 2 x Forward Delay + 8 seconds, even when a link fault is rectified. Therefore, you should exercise caution when enabling this function.

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
4. Set the parameters for interoperation with non-Huawei devices as needed.
   
   
   * Configure the interface to use the common P/A mechanism.
     ```
     [stp no-agreement-check](cmdqueryname=stp+no-agreement-check)
     ```
     
     By default, an interface uses the enhanced P/A mechanism.
   * Configure the interface to discard non-standard STP/RST BPDUs sent by HanDreamnet switches.
     ```
     [stp agreement-legacy](cmdqueryname=stp+agreement-legacy)
     ```
     
     By default, an interface does not discard non-standard STP/RST BPDUs sent by HanDreamnet switches.
   * Configure the switchback delay function on the interface.
     ```
     [stp revertive slow](cmdqueryname=stp+revertive+slow)
     ```
     
     By default, the switchback delay function is disabled on an interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the interface view to check the parameters for interoperation with non-Huawei devices.