Configuring Parameters for Interworking with a Non-Huawei Device
================================================================

Configuring Parameters for Interworking with a Non-Huawei Device

#### Context

The following parameters can be configured for a device to interwork with a non-Huawei device using an Eth-Trunk:

* **Ignoring the value of the Reserved field in the received LACPDUs**: When an Eth-Trunk is set up between two Huawei devices, if the two ends are configured with different LACP preemption delays, they will negotiate using the Reserved field in LACPDUs, in which case the Eth-Trunk uses the larger value as the preemption delay. When an Eth-Trunk is set up between a Huawei device and a non-Huawei device, if the Reserved field in LACPDUs on the non-Huawei device is different from that on the Huawei device, LACP flapping occurs, causing service interruptions. To address this problem, you can enable the Huawei device to ignore the value of the Reserved field in LACPDUs.
* **Configuring the CollectorMaxDelay field in LACPDUs**: When a non-Huawei device is dual-homed to two Huawei devices through an Eth-Trunk in static LACP mode, if the two Huawei devices use different system software, the default value of the CollectorMaxDelay field in LACPDUs may be different. As a result, Eth-Trunk member interfaces on the non-Huawei device receive LACPDUs with different CollectorMaxDelay values. In this situation, the CPU usage of some non-Huawei devices will increase, affecting device performance. To address this problem, change the value of the CollectorMaxDelay field on one Huawei device to ensure that LACPDUs sent by the two Huawei devices carry the same CollectorMaxDelay value.
* **Configuring the key value of Eth-Trunk member interfaces in LACP**: When a non-Huawei device that does not support E-Trunk is dual-homed to two Huawei devices functioning as PEs, you need to manually configure the same system ID, system priority, and portkey value for the two PEs to ensure that the links of both PEs can be selected.

#### Procedure

* Configure the local device to ignore the value of the Reserved field in the LACPDUs sent by non-Huawei devices.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable the device to ignore the value of the Reserved field in received LACPDUs.
     
     
     ```
     [lacp ignore aggregation delay](cmdqueryname=lacp+ignore+aggregation+delay)
     ```
     
     
     
     By default, the device identifies the value of the Reserved field in received LACPDUs.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the value of the CollectorMaxDelay field in LACPDUs when the local device connects to a non-Huawei device.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface.
     
     
     ```
     [interface](cmdqueryname=interface) eth-trunk trunk-id
     ```
  3. Configure the value of the CollectorMaxDelay field in LACPDUs.
     
     
     ```
     [lacp collector delay](cmdqueryname=lacp+collector+delay) delay-time
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the key value of Eth-Trunk member interfaces in LACP when the local device connects to a non-Huawei device.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface.
     
     
     ```
     [interface](cmdqueryname=interface) eth-trunk trunk-id
     ```
  3. Configure the key value of Eth-Trunk member interfaces in LACP.
     
     
     ```
     lacp portkey portkey
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```