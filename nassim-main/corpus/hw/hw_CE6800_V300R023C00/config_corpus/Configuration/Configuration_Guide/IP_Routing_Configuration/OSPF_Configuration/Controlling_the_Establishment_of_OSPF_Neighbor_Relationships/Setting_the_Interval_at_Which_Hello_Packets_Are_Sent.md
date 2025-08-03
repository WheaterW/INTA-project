Setting the Interval at Which Hello Packets Are Sent
====================================================

Setting the Interval at Which Hello Packets Are Sent

#### Prerequisites

Before setting the interval at which Hello packets are sent, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

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
   [ospf timer hello](cmdqueryname=ospf+timer+hello) interval [ conservative ]
   ```
   
   To speed up OSPF convergence in the case of a link failure, configuring BFD for OSPF is recommended. If the remote end does not support BFD for OSPF or you do not want to configure BFD for OSPF, you are advised to specify **conservative** when you run the [**ospf timer hello**](cmdqueryname=ospf+timer+hello) command. In conservative mode, the value set for the Dead timer using the [**ospf timer dead**](cmdqueryname=ospf+timer+dead) command takes effect even if the value is less than 10 seconds. If **conservative** is not specified in the [**ospf timer hello**](cmdqueryname=ospf+timer+hello) command and the Dead timer is set to be less than 10 seconds, the actual Dead timer is not less than 10 seconds. As a result, OSPF convergence is time-consuming, and services are compromised.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The Hello interval should not be less than the time a device takes to perform a master/slave main control board switchover. Otherwise, an intermittent protocol interruption may occur during a switchover. The default timer value is recommended.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check OSPF interface information. The **Hello** field in the command output indicates the interval at which Hello packets are sent.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check brief OSPF information. The **Hello** field in the command output indicates the interval at which Hello packets are sent.