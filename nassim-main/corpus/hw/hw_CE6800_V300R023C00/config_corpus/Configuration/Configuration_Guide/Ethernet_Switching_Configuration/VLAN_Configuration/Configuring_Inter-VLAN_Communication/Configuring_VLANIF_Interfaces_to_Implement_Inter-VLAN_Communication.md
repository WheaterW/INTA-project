Configuring VLANIF Interfaces to Implement Inter-VLAN Communication
===================================================================

Configuring VLANIF Interfaces to Implement Inter-VLAN Communication

#### Prerequisites

Before configuring VLANIF interfaces to implement inter-VLAN communication, you have completed the following task:

* Create VLANs. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).

#### Context

A VLANIF interface is a Layer 3 logical interface most commonly used to implement Layer 3 communication between hosts in different VLANs across different network segments.

Each VLANIF interface corresponds to a VLAN. After an IP address is configured for a VLANIF interface, the VLANIF interface becomes the gateway of the user hosts within that VLAN and forwards packets across network segments at Layer 3.

Inter-VLAN communication through VLANIF interfaces applies only when the hosts in different VLANs are located in different network segments. For fundamentals of the implementation, see [Inter-VLAN Communication Through a Single Device (Using VLANIF Interfaces)](vrp_vlan_cfg_0009.html#EN-US_CONCEPT_0000001176742329__section126740485349) and [Inter-VLAN Communication Through Multiple Devices Using VLANIF Interfaces](vrp_vlan_cfg_0009.html#EN-US_CONCEPT_0000001176742329__section73131523183516).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VLANIF interface and enter the VLANIF interface view.
   
   
   ```
   [interface vlanif](cmdqueryname=interface+vlanif) vlan-id
   ```
3. Configure an IP address for the VLANIF interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
   ```
   
   
   
   If users on multiple network segments need to communicate with each other, configure a primary IP address and multiple secondary IP addresses on a VLANIF interface. In addition, ensure that the IP addresses of VLANIF interfaces are on different network segments.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface vlanif**](cmdqueryname=display+interface+vlanif) [ **vlan-id** ] command to check information about a VLANIF interface.


#### Follow-up Procedure

To prevent users in a VLAN from communicating with users in another VLAN through a VLANIF interface, run the [**shutdown**](cmdqueryname=shutdown) command in the VLANIF interface view. Running this command does not affect intra-VLAN communication.

A VLANIF interface transmits both Layer 2 and Layer 3 traffic. As running the **shutdown** command in the VLANIF interface view blocks only Layer 3 traffic, traffic statistics may continue to increase on the interface even after the [**shutdown**](cmdqueryname=shutdown) command is run. To check traffic statistics, run the [**display interface vlanif**](cmdqueryname=display+interface+vlanif) command.