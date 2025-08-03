Enabling MSTP
=============

After basic Multiple Spanning Tree Protocol (MSTP) functions are configured on a device, enabling the MSTP function is required so that MSTP can work properly.

#### Context

After MSTP is enabled on a ring network, MSTP immediately calculates spanning trees on the network. Configurations on the device, such as, the device priority and port priority, will affect spanning tree calculation. Any change of the configurations may cause network flapping. Therefore, to ensure rapid and stable spanning tree calculation, perform basic configurations on the device and its ports and enable MSTP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp enable**](cmdqueryname=stp+enable)
   
   
   
   MSTP is enabled on the device.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   On an STP-capable Layer 2 network, packets with the same source MAC address may form loops. To prevent loops, an interface must be blocked, and an alarm must be reported to the NMS. However, STP and MAC flapping-based loop detection are mutually exclusive by default. To allow both STP and MAC flapping-based loop detection to be enabled, run the [**loop-detect eth-loop assist-stp enable**](cmdqueryname=loop-detect+eth-loop+assist-stp+enable) command.
   
   STP and MAC flapping-based loop detection have different blocking principles and may block different interfaces on a network, leading to temporary traffic interruptions. Therefore, exercise caution when running the [**loop-detect eth-loop assist-stp enable**](cmdqueryname=loop-detect+eth-loop+assist-stp+enable) command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.