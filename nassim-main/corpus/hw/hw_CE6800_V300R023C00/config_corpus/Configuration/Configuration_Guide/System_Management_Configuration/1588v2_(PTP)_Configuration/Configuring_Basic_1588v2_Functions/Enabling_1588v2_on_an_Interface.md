Enabling 1588v2 on an Interface
===============================

Enabling 1588v2 on an Interface

#### Context

After 1588v2 is enabled globally, you must also enable 1588v2 on an interface to make 1588v2 functions take effect. In addition, you can configure the asymmetry delay correction value to be used by the interface for delay compensation on the 1588v2 network.

Perform the following steps on each 1588v2 device:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   interface interface-type interface-number
   ```
3. Enable 1588v2 on the interface.
   
   
   ```
   [ptp enable](cmdqueryname=ptp+enable)
   ```
   
   By default, 1588v2 is not enabled on an interface.
4. (Optional) Configure an asymmetry delay correction value for the interface to send 1588v2 messages.
   
   
   ```
   [ptp asymmetry-correction](cmdqueryname=ptp+asymmetry-correction) { negative negative-asymmetry-correction-value | positive positive-asymmetry-correction-value }
   ```
   
   By default, no asymmetry delay correction value is configured for an interface to send 1588v2 messages.
5. (Optional) Configure the mode in which a 1588v2 device uses clock synchronization packets to carry timestamps.
   
   
   ```
   [ptp clock-step](cmdqueryname=ptp+clock-step) { one-step | two-step }
   ```
   
   By default, packets carry timestamps in **one-step** mode.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

After configuring PTP on an interface, you can run the [**ptp announce-drop enable**](cmdqueryname=ptp+announce-drop+enable) command on the interface to configure the interface to drop Announce packets.

Announce packets are used for PTP clock synchronization. When a user-side interface and the current interface meet clock synchronization requirements, you can configure the interface to drop Announce packets to retain the current master-slave hierarchy. After the interface receives Announce messages, it drops the messages and does not participate in establishing the master-slave hierarchy. This saves system resources.![](public_sys-resources/note_3.0-en-us.png) 

By default, an interface does not drop Announce packets.