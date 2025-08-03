Configuring Fault Message Transmission Between Ethernet CFM and Its Bound Interface
===================================================================================

This section describes how to configure fault message transmission between Ethernet CFM and its bound interface in the OAM management view. After the configuration is complete, the link detection results of Ethernet CFM can be associated with the interface status.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172361954__fig_dc_vrp_cfm_cfg_000035), Ethernet CFM is deployed between the PEs. If a fault occurs on the link between the PEs, a CE needs to detect the fault. Additionally, if a fault occurs between a PE and CE, the PE needs to notify the remote PE of the fault to ensure reliable service transmission. To meet the needs, deploy fault message transmission between Ethernet CFM and its associated interface on a PE. For example, deploy fault message transmission between Ethernet CFM and its associated interface on PE2. If Ethernet CFM detects a fault on the link between PE1 and PE2, the physical status of interface 2 associated with Ethernet CFM on PE2 goes down. This triggers CE2 to detect the fault. If interface 2 on PE2 goes down, Ethernet CFM associated with the interface fails. PE2 uses CFM packets to transmit fault messages to PE1.**Figure 1** Fault message transmission between Ethernet CFM and its associated interface  
![](figure/en-us_image_0194937178.png)


#### Pre-configuration Tasks

Before configuring fault message transmission between Ethernet CFM and its bound interface, [configure basic CFM functions](dc_vrp_cfm_cfg_000004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   
   
   The OAM management view is displayed.
3. Configure the association depending on the usage scenario.
   
   
   
   **Table 1** Configurations for fault message transmission between Ethernet CFM and its bound interface
   | Scenario | Configuration Solution 1 | Configuration Solution 2 |
   | --- | --- | --- |
   | Deploying bidirectional fault message transmission between Ethernet CFM and its bound interface | Run the [**oam-bind cfm md ma trigger if-down interface**](cmdqueryname=oam-bind+cfm+md+ma+trigger+if-down+interface) or [**oam-bind interface cfm md ma trigger if-down**](cmdqueryname=oam-bind+interface+cfm+md+ma+trigger+if-down) command to configure bidirectional fault message transmission between Ethernet CFM and its bound interface.  NOTE:  * The function of the [**oam-bind cfm md ma trigger if-down interface**](cmdqueryname=oam-bind+cfm+md+ma+trigger+if-down+interface) command is the same as that of the [**oam-bind interface cfm md ma trigger if-down**](cmdqueryname=oam-bind+interface+cfm+md+ma+trigger+if-down) command. * The [**oam-bind ingress cfm md ma trigger if-down egress interface**](cmdqueryname=oam-bind+ingress+cfm+md+ma+trigger+if-down+egress+interface) and [**oam-bind ingress interface egress cfm md ma trigger if-down**](cmdqueryname=oam-bind+ingress+interface+egress+cfm+md+ma+trigger+if-down) commands are displayed in the configuration file. | You can also run both of the following commands used for unidirectional fault message transmission to configure bidirectional fault message transmission.  Run the following commands in any order (each command configures fault message transmission in a single direction):  * Run the [**oam-bind ingress cfm md ma trigger if-down egress interface**](cmdqueryname=oam-bind+ingress+cfm+md+ma+trigger+if-down+egress+interface) command to configure Ethernet CFM to transmit fault messages to its bound interface. * Run the [**oam-bind ingress interface egress cfm md ma trigger if-down**](cmdqueryname=oam-bind+ingress+interface+egress+cfm+md+ma+trigger+if-down) command to configure an interface bound with Ethernet CFM to transmit fault messages to Ethernet CFM. |
   | Deploying unidirectional fault message transmission between Ethernet CFM and its bound interface | Select either of the following commands based on the direction in which fault messages are transmitted:  * To configure Ethernet CFM to transmit fault messages to its bound interface, run the [**oam-bind ingress cfm md ma trigger if-down egress interface**](cmdqueryname=oam-bind+ingress+cfm+md+ma+trigger+if-down+egress+interface) command. * To configure an interface bound with Ethernet CFM to transmit fault messages to Ethernet CFM, run the [**oam-bind ingress interface egress cfm md ma trigger if-down**](cmdqueryname=oam-bind+ingress+interface+egress+cfm+md+ma+trigger+if-down) command. | None |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.