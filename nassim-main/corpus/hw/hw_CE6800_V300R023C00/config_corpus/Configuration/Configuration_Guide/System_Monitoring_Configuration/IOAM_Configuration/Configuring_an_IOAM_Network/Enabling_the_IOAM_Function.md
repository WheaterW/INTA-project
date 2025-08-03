Enabling the IOAM Function
==========================

Enabling the IOAM Function

#### Context

On an IOAM network, you must enable the IOAM function and configure the device ID and namespace ID for the encapsulation, transit, and decapsulation nodes.

* Device ID: Identifies a device.
* Namespace ID: Only the packets with the same namespace ID as that of a device can be processed according to the device's IOAM process.

![](public_sys-resources/note_3.0-en-us.png) 

In trace and direct-export modes, the IOAM function must be enabled on the encapsulation, transit, and decapsulation nodes.

In edge-to-edge mode, the IOAM function must be enabled on the encapsulation and decapsulation nodes, and this function can be enabled on the transit node as required.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable 1588v2 globally.
   
   
   ```
   [ptp enable](cmdqueryname=ptp+enable)
   ```
   
   By default, 1588v2 is not enabled globally.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   1588v2 needs to be enabled so that timestamps in IOAM packets are correct.
3. Create an IOAM view and enter it, or enter an existing IOAM view.
   
   
   ```
   [ioam](cmdqueryname=ioam)
   ```
4. Enable the IOAM function.
   
   
   ```
   [enable](cmdqueryname=enable)
   ```
   
   By default, the IOAM function is disabled on a device.
5. Configure the device ID.
   
   
   ```
   [device-id](cmdqueryname=device-id) device-id
   ```
   
   By default, the device ID is 0 after an IOAM view is created.
6. Configure the namespace ID.
   
   
   ```
   [namespace-id](cmdqueryname=namespace-id) namespace-id
   ```
   
   By default, the namespace ID is 0 after an IOAM view is created.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```