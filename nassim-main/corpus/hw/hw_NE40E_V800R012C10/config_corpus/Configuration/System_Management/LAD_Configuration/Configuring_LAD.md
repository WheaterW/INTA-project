Configuring LAD
===============

Link Automatic Discovery (LAD) allows a device to issue link discovery requests and generates neighbor information based on the received link discovery replies. The device then saves local and neighbor information in the local MIB. The NMS can query neighbor information in the MIB and generate the topology of the entire network, helping network administrators locate inappropriate configurations.

#### Usage Scenario

LAD discovers physical and logical links when devices are connected directly or over a Layer 2 network. The information provided by LAD helps network administrators promptly obtain detailed network topology and changes in the topology and monitor the network status in real time, ensuring security and stability for network communication. On the network shown in [Figure 1](#EN-US_TASK_0172360330__fig_dc_vrp_lad_cfg_000301), before the NMS collects the topology of Device A and Device B, enable LAD on Device A and Device B so that Device A can send LAD packets to Device B and Device B can respond with LAD packets. After Device A receives LAD packets, it generates neighbor information and saves it in the local MIB, helping the NMS obtain the network topology.

**Figure 1** LAD networking  
![](images/fig_dc_vrp_lad_cfg_000301.png)  


#### Pre-configuration Tasks

Before configuring LAD, configure reachable routes between devices and the NMS and configure NETCONF parameters.

The LAD function is enabled globally on the device.


#### Procedure

* Enable LAD on Device A and Device B.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
     
     
     
     The view of an interface on which LAD is to be enabled is displayed.
  3. (Optional) Run [**link-detect enable**](cmdqueryname=link-detect+enable)
     
     
     
     LAD is enabled on the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable Device A to send LAD packets to Device B.
  1. Run [**link detect**](cmdqueryname=link+detect) { { **interface** { *interface-name* | { *interface-type* *interface-number* } } } | { **slot** *slot-id* } | **all** }
     
     
     
     Device A is enabled to send LAD packets to Device B.

#### Checking the Configurations

After configuring LAD, check the configurations.

* Run the [**display link neighbor**](cmdqueryname=display+link+neighbor) { **slot** *slot-id* | **interface** *interface-type* *interface-number* | **all** } command to check neighbor information of interfaces.
* Run the [**display link neighbor all**](cmdqueryname=display+link+neighbor+all) command to view neighbor information of all interfaces.