Configuring Basic DCN Functions
===============================

This chapter describes how to enable DCN globally, enable DCN on an interface, enable the automatic NE report function on a GNE, and configure NE IDs and NE IP addresses.

#### Usage Scenario

The construction of a large network requires significant human and material resources if software commissioning engineers have to configure devices on site, causing high operational expenditure (OPEX). DCN can reduce the OPEX by allowing GNEs to manage NEs. DCN enables NMSs to rapidly detect new NEs and remotely manage the NEs.

The DCN technique offers a mechanism to implement plug-and-play. After each NE is initialized, it generates an NE IP address based on its NE ID, creates a mapping entry for the NE ID and NE IP address, adds the mapping entry to its DCN core routing table, and uses OSPF to advertise the mapping entry to all other NEs on the DCN. Therefore, all the NEs on the DCN can communicate with each other.

The DCN feature allows NMSs to use GNEs to manage NEs. A GNE supports the automatic NE report function, enabling the GNE to automatically report a new NE's information to NMSs immediately after the GNE detects the new NE. Then the NMSs can manage the new NE in time. In addition, a GNE can send a trap to its interworking NMSs when the number of NEs connected to the GNE reaches the alarm threshold. Then the NMSs will generate alarms to inform users of this information.


#### Pre-configuration Tasks

Before configuring basic DCN functions, complete the following tasks:

* Configure reachable routes between the GNE and NMSs.
* Configure reachable routes between the GNE and NEs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When the GNE is connected to an NE for the first time, the SSH default user account is used for login.




#### Procedure

1. Enable DCN Globally.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**dcn**](cmdqueryname=dcn) command to enable the DCN function globally.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Enable DCN on an interface and specify a DCN VLAN.
   
   
   
   By default, DCN is enabled on some interfaces. For details, see [Table 1](#EN-US_TASK_0172361405__table1338383833213).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After an interface is switched to a FlexE interface, the DCN status does not change.
   
   The default DCN enabling rule of a subcard with adjustable interface bandwidth is the same as that of a subcard with only one type of interface bandwidth and is not affected by the adjustable bandwidth.
   
   
   **Table 1** Rules for enabling DCN on interfaces by default
   | Interfaces on Fixed Boards | Ethernet Interfaces on Flexible Cards | POS Interface on Flexible Cards | E1 and CPOS Interfaces on Subcards That Support the DCN Function |
   | --- | --- | --- | --- |
   | DCN is enabled on all interfaces by default. | In transport mode:  * For subcards with multiple interface bandwidths, DCN is enabled on the first four interfaces by default. * For a subcard with only one type of interface bandwidth:   + For a subcard with eight or more interfaces, DCN is enabled on the first four interfaces by default.   + For a subcard with five to seven interfaces, DCN is enabled on the first two interfaces by default.   + For a subcard with four or fewer interfaces, DCN is enabled on the first interface by default. In non-transport mode:  DCN is enabled on all interfaces by default. | * For a subcard with eight or more interfaces, DCN is enabled on the first four interfaces by default. * For a subcard with four to seven interfaces, DCN is enabled on the first two interfaces by default. * For a subcard with less than four interfaces, DCN is enabled on the first interface by default. | * For channelized interfaces, DCN is enabled on interfaces 2, 18, 34, and 50 by default. * For unchannelized interfaces, DCN is enabled on interfaces 2 and 18 by default in transport mode; DCN is enabled on interfaces 1 and 17 by default in non-transport mode. |
   
   
   
   In router mode:
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   3. Run the [**dcn (interface view)**](cmdqueryname=dcn+%28interface+view%29) command to enable DCN on the interface.
   4. Run the [**dcn vlan**](cmdqueryname=dcn+vlan) { *beginVlan* [ **to** *endVlan* ] } &<1â4094> command to specify a DCN VLAN.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A DCN VLAN can be a service VLAN in router mode.
   
   
   
   In transport mode:
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   3. Run the [**dcn**](cmdqueryname=dcn) command to enable DCN on the interface.
   4. Run the [**dcn vlan**](cmdqueryname=dcn+vlan) *beginvlan-id* command to specify a DCN VLAN.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In transport mode, only one DCN VLAN can be configured. And it is conflicted with service VLAN.
3. Configure the automatic NE report function on a GNE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**dcn**](cmdqueryname=dcn) command to enter the DCN view.
   3. Run the [**auto-report**](cmdqueryname=auto-report) command to enable the automatic NE report function.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Configure an NEID and NEIP.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**set neid**](cmdqueryname=set+neid) *ne-id* command to set an NEID.
   3. Run the [**dcn**](cmdqueryname=dcn) command to enter the DCN view.
   4. Run the [**ne-ip**](cmdqueryname=ne-ip) *ip-address* { *ip-mask* | *mask-length* } command to set an NEIP.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. (Optional) Configure the bandwidth for DCN interfaces to send packets.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**dcn**](cmdqueryname=dcn) command to enter the DCN view.
   3. Run the [**bandwidth**](cmdqueryname=bandwidth) { **ethernet** *bandwidth* | **pos** *bandwidth* | **serial** *bandwidth* } command to configure bandwidth for DCN interfaces to send packets.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Perform the following operations to check the configurations:

* Run the [**display neid**](cmdqueryname=display+neid) command to check the NE ID.
* Run the [**display dcn brief**](cmdqueryname=display+dcn+brief) command to check configurations of the GNE.
* Run the [**display dcn ne-info**](cmdqueryname=display+dcn+ne-info) command to check information about the DCN core routing table.
* Run the [**display dcn global**](cmdqueryname=display+dcn+global) command to check whether DCN is enabled globally.
* Run the [**display dcn default-port**](cmdqueryname=display+dcn+default-port) command to check the interface on which DCN is enabled by default.
* Run the [**display dcn interface**](cmdqueryname=display+dcn+interface) [ *interface-type* *interface-number* ] command to check DCN configurations and traffic statistics of an interface.
* Run the [**display dcn warning**](cmdqueryname=display+dcn+warning) command to check DCN trap information.
#### Follow-up Procedure

An NMS's IP address is a public IP address, and a GNE's NE IP address is a Layer 3 VPN address. To implement address conversion, specify the interface that connects a GNE to an NMS, bind the interface to a DCN VPN instance, and set an IP address for the interface. After DCN is enabled globally on the GNE, it automatically generates a DCN VPN instance named **\_\_dcn\_vpn\_\_**. Detailed operations are as follows:

* Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
* Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind a DCN VPN instance.
* Run the [**ip address**](cmdqueryname=ip+address) { *mask* | *mask-length* } command to set an interface IP address.