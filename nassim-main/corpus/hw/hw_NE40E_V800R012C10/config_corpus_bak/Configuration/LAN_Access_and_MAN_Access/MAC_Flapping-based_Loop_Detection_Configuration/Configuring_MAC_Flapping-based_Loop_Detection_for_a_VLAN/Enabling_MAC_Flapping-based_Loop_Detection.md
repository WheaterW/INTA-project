Enabling MAC Flapping-based Loop Detection
==========================================

After MAC flapping-based loop detection is enabled on devices, the devices can detect loops based on MAC address entry flapping and block interfaces or pseudo wires (PWs) to eliminate the loops.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   The VLAN view is displayed.
3. Run [**loop-detect eth-loop**](cmdqueryname=loop-detect+eth-loop) **loop-times** *loop-times* **detect-cycle** *detect-cycle-time* **cycles** *cycles* { **alarm-only** | **retry-times** *retry-times* **block-time** *block-time* }
   
   
   
   MAC flapping-based loop detection is enabled for the VLAN, and its parameters are configured.
   
   
   
   **retry-times** *retry-times* and **block-time** *block-time* must both be specified. For example, *retry-times* is specified as 2 and *block-time* as 100s. When detecting loops in the VSI, the device blocks interfaces using the following methods:
   1. When detecting a loop on an interface for the first time, the device keeps the interface blocked for 100s.
   2. During the first detection cycle (specified by *detect-cycle-time*) after the first blocking period ends (the blocked interface recovers), if the device detects a loop, it keeps the interface blocked for 2 x 100s.
   3. During the second detection cycle (specified by *detect-cycle-time*) after the second blocking period ends, if the device detects a loop, it keeps the interface blocked for 4 x 100s.
   4. During the third detection cycle (specified by *detect-cycle-time*) after the third blocking period ends, if the device detects a loop, it keeps the interface blocked permanently. The reason for the permanent blocking is that three loops occur after the first blocking period ends, which exceeds the maximum number of loops specified by *retry-times*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If no loops are detected during *detect-cycle-time*\*30, the blocking count is cleared. If a loop is detected later *block-time* is restored.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   On an STP-capable Layer 2 network, packets with the same source MAC address may form loops. To prevent loops, an interface must be blocked, and an alarm must be reported to the NMS. To allow both STP and MAC flapping-based loop detection to be enabled, run the [**loop-detect eth-loop assist-stp enable**](cmdqueryname=loop-detect+eth-loop+assist-stp+enable) command.
   
   STP and MAC flapping-based loop detection have different blocking principles and may block different interfaces on a network, leading to temporary traffic interruptions. Therefore, exercise caution when running the [**loop-detect eth-loop assist-stp enable**](cmdqueryname=loop-detect+eth-loop+assist-stp+enable) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.