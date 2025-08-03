Configuring an Eth-Trunk Interface in Manual 1:1 Master/Backup Mode to Connect to a Non-Huawei Device
=====================================================================================================

To allow a Huawei device to communicate with a non-Huawei device that uses master and backup interfaces (both in the up state), configure an Eth-Trunk interface in manual 1:1 master/backup mode on the Huawei device.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172362887__fig_dc_vrp_ethtrunk_cfg_006501), a non-Huawei device uses master and backup interfaces (both in the up state) to directly connect to a Huawei device. However, communication may fail because network administrator cannot identify the master and backup interfaces on the connected non-Huawei device during network planning or maintenance and therefore cannot correctly specify the master and backup interfaces when configuring the Eth-Trunk interface in manual 1:1 master/backup mode.

**Figure 1** Network diagram of configuring an Eth-Trunk interface in manual 1:1 master/backup mode for communication with a non-Huawei device  
![](images/fig_dc_vrp_ethtrunk_cfg_006501.png)

To address this problem, run the [**inactive-port shutdown enable**](cmdqueryname=inactive-port+shutdown+enable) command on the Huawei device to forcibly set the backup member interface in the Eth-Trunk interface in manual 1:1 master/backup mode to the down state. This configuration allows the non-Huawei device to communicate with the Huawei device both through the master interfaces, ensuring communication.

If the master member interface for forwarding traffic fails, the system automatically disables the forcible down state of the backup member interface and restores the backup member interface to the up state so that it can communicate with the non-Huawei device.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The [**inactive-port shutdown enable**](cmdqueryname=inactive-port+shutdown+enable) and [**preempt enable**](cmdqueryname=preempt+enable) commands are mutually exclusive in this scenario.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   An Eth-Trunk interface is created, and its view is displayed.
3. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The Eth-Trunk interface is switched to the Layer 2 mode.
4. Run [**mode**](cmdqueryname=mode) **manual backup**
   
   
   
   The Eth-Trunk interface is configured to work in manual 1:1 master/backup mode.
5. Run [**inactive-port shutdown enable**](cmdqueryname=inactive-port+shutdown+enable)
   
   
   
   The backup member interface in the Eth-Trunk interface that works in manual 1:1 master/backup mode is forcibly set to the down state.
6. Run [**trunkport**](cmdqueryname=trunkport) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-64>
   
   
   
   Interfaces are added to the Eth-Trunk interface in batches.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before adding an interface to an Eth-Trunk interface, ensure that the following condition is met:
   
   * Member interfaces cannot be configured with services or Layer 3 configurations such as IP addresses.
   * Member interfaces cannot be manually configured with MAC addresses.
   * Before adding a Layer 2 interface to an Eth-Trunk interface, run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to configure the Eth-Trunk interface to work in Layer 3 mode.
   * An Ethernet interface can be added to only one Eth-Trunk interface. Before adding it to another Eth-Trunk interface, delete it from the existing Eth-Trunk interface.
   
   An interface can be added to an Eth-Trunk interface in the Eth-Trunk interface view or in the interface view. For details, see [Adding Interfaces to an Eth-Trunk Interface](dc_vrp_ethtrunk_cfg_0023.html).
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The Eth-Trunk member interface view is displayed.
9. Run [**port-master**](cmdqueryname=port-master)
   
   
   
   The master member interface is specified.
   
   Only one master interface can be specified between the two member interfaces in an Eth-Trunk interface in manual 1:1 master/backup mode.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, check whether the configuration takes effect.

Run the [**display interface**](cmdqueryname=display+interface) command. The command output shows that the interface status is **TRUNK BACKUP DOWN**.