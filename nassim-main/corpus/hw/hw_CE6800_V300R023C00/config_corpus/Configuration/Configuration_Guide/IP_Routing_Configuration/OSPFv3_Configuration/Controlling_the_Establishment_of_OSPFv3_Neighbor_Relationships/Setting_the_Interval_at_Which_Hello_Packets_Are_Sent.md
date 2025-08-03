Setting the Interval at Which Hello Packets Are Sent
====================================================

Setting the Interval at Which Hello Packets Are Sent

#### Prerequisites

Before setting the interval at which Hello packets are sent, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the interval at which the interface sends Hello packets.
   
   
   ```
   [ospfv3 timer hello](cmdqueryname=ospfv3+timer+hello) interval [ conservative ] [ instance instance-id ]
   ```
   
   To speed up OSPFv3 convergence in the case of a link failure, configuring BFD for OSPFv3 is recommended. If you do not want to configure BFD for OSPFv3 or the remote end does not support it, you are advised to specify **conservative** when running the [**ospfv3 timer hello**](cmdqueryname=ospfv3+timer+hello) command. In conservative mode, the value set for the Dead timer using the [**ospfv3 timer dead**](cmdqueryname=ospfv3+timer+dead) command takes effect even if the value is less than 10 seconds. If the [**ospfv3 timer hello**](cmdqueryname=ospfv3+timer+hello) **conservative** command is not run, OSPFv3 convergence may be time-consuming, and services may be compromised.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The Hello interval should not be less than the time a device takes to perform a master/slave main control board switchover. Otherwise, an intermittent protocol interruption may occur during a switchover. The default timer value is recommended.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information. The **Hello** field in the command output indicates the interval at which Hello packets are sent.