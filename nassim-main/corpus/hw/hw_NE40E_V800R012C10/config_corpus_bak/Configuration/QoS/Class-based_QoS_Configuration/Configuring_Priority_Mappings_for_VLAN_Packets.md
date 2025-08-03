Configuring Priority Mappings for VLAN Packets
==============================================

This section describes how to configure priority mappings for VLAN packets and the application environment of this function.

#### Context

Traffic policy based on BA classification is used to map the priority of traffic on one type of network to another type. That is, to transmit the traffic in the other network according to the original priority.

When the NE40E serves as the border Router for different networks, the original external priorities (802.1p values) in the VLAN packets that go into the NE40E are all mapped to the internal priorities of the router represented by service classes of DiffServ and colors. When the NE40E sends out the packet, the internal priority is mapped back to the external priority.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If unified scheduling is required for all upstream traffic on an interface, you can run the [**qos default-service-class**](cmdqueryname=qos+default-service-class) command to configure the upstream traffic on the interface to enter the specific queues and provide corresponding services. After this command is run, other packets cannot be enabled to enter the queues, and BA classification cannot be enabled.



#### Pre-configuration Tasks

Before configuring priority mappings for VLAN packets, complete the following tasks:

* Configure physical parameters for interfaces.
* Configure link layer attributes for interfaces to work properly.
* Configure IP addresses for interfaces.
* Enable a routing protocol for communication between devices.

In VS mode, this configuration is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**diffserv domain**](cmdqueryname=diffserv+domain) { *ds-domain-name* | **default** | **5p3d** } [ **domain-id** *domain-id-value* ]
   
   
   
   A DiffServ domain is defined and the DiffServ domain view is displayed.
3. Define traffic policies on the Router based on the actual situation.
   
   
   * To define a traffic policy for incoming VLAN traffic, run the [**8021p-inbound**](cmdqueryname=8021p-inbound) *8021p-value* **phb** *service-class* [ *color* ] command.
   * To define a traffic policy for outgoing VLAN traffic, run the [**8021p-outbound**](cmdqueryname=8021p-outbound) *service-class* *color* **map** *8021p-value* command.
   
   The system predefines the 5p3d domain profile and default domain profile for VLAN packets.
   
   * The 5p3d domain profile describes the mappings between the 802.1p priorities of VLAN packets, QoS service classes, and colors. You can modify the mappings in the 5p3d domain profile. The 802.1p priorities of packets from an upstream device are mapped to QoS service classes and colors, and [Table 1](#EN-US_TASK_0172371267__tab_dc_ne_qos_cfg_005111) shows the mappings. The QoS service classes and colors of packets to a downstream device are mapped to 802.1p priorities, and [Table 2](#EN-US_TASK_0172371267__tab_dc_ne_qos_cfg_005112) shows the mappings.
     
     **Table 1** Mapping from the 802.1p value to the service-class and color
     | 802.1p | Service | Color |
     | --- | --- | --- |
     | 0 | BE | Yellow |
     | 1 | BE | Green |
     | 2 | AF2 | Yellow |
     | 3 | AF2 | Green |
     | 4 | AF4 | Yellow |
     | 5 | AF4 | Green |
     | 6 | CS6 | Green |
     | 7 | CS7 | Green |
     
     
     **Table 2** Mapping from the service-class and color to the 802.1p value
     | Service | Color | 802.1p |
     | --- | --- | --- |
     | BE | Green | 1 |
     | BE | Yellow | 0 |
     | BE | Red | 0 |
     | AF1 | Green | 1 |
     | AF1 | Yellow | 0 |
     | AF1 | Red | 0 |
     | AF2 | Green | 3 |
     | AF2 | Yellow | 2 |
     | AF2 | Red | 2 |
     | AF3 | Green | 3 |
     | AF3 | Yellow | 2 |
     | AF3 | Red | 2 |
     | AF4 | Green | 5 |
     | AF4 | Yellow | 4 |
     | AF4 | Red | 4 |
     | EF | Green | 5 |
     | EF | Yellow | 4 |
     | EF | Red | 4 |
     | CS6 | Green, Yellow, Red | 6 |
     | CS7 | Green, Yellow, Red | 7 |
   * The default domain profile describes the default mappings between the 802.1p priorities of VLAN packets, QoS services classes, and colors. You can modify the mappings in the default domain profile. The 802.1p priorities of packets from an upstream device are mapped to QoS service classes and colors, and [Table 3](#EN-US_TASK_0172371267__tab_dc_ne_qos_cfg_005113) shows the mappings. The QoS service classes and colors of packets to a downstream device are mapped to 802.1p priorities, and [Table 4](#EN-US_TASK_0172371267__tab_dc_ne_qos_cfg_005114) shows the mappings.
     
     **Table 3** Default mapping from the IP Precedence/MPLS EXP/802.1p to the service-class and color
     | IP Precedence/MPLS EXP/802.1p | Service | Color |
     | --- | --- | --- |
     | 0 | BE | Green |
     | 1 | AF1 | Green |
     | 2 | AF2 | Green |
     | 3 | AF3 | Green |
     | 4 | AF4 | Green |
     | 5 | EF | Green |
     | 6 | CS6 | Green |
     | 7 | CS7 | Green |
     
     
     **Table 4** Default mapping from the service-class and color to IP Precedence/MPLS EXP/802.1p
     | Service | Color | IP Precedence/MPLS EXP/802.1p |
     | --- | --- | --- |
     | BE | Green, Yellow, Red | 0 |
     | AF1 | Green, Yellow, Red | 1 |
     | AF2 | Green, Yellow, Red | 2 |
     | AF3 | Green, Yellow, Red | 3 |
     | AF4 | Green, Yellow, Red | 4 |
     | EF | Green, Yellow, Red | 5 |
     | CS6 | Green, Yellow, Red | 6 |
     | CS7 | Green, Yellow, Red | 7 |
4. (Optional) In the interface view, run [**field dei enable vlan**](cmdqueryname=field+dei+enable+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] }&<1-10> | **all** }
   
   
   
   The DEI function is enabled for packets in a specified VLAN range on the interface. After BA classification is enabled, packets enter queues based on service priorities and are colored based on the CFI field.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The DEI function takes effect only when it is configured together with BA classification and 802.1p priorities are trusted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Perform the following operations based on the interfaces on which a traffic policy is used:
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the L3VPN DiffServ mode is pipe and traffic needs to be scheduled based on the 802.1p value, run the [**diffserv-mode pipe mapping-8021p mpls-pop**](cmdqueryname=diffserv-mode+pipe+mapping-8021p+mpls-pop) command in the system view to enable the MPLS egress PE to fill the 802.1p value in outgoing packets.
   
   * Apply a traffic policy to VLAN packets on a Layer 3 interface.
     1. Run the [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number.subnumber* command to enter the sub-interface view.
     2. Bind an interface to a DiffServ domain. Perform the following configurations based on the application scenario:![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The application scenarios of the two configurations are different. The [**qos phb enable**](cmdqueryname=qos+phb+enable) command maps priorities only for downstream traffic. To map priorities for both upstream and downstream traffic, run the [**trust upstream**](cmdqueryname=trust+upstream) command.
        
        
        + Run the [**trust upstream**](cmdqueryname=trust+upstream) { **5p3d** | *ds-domain-name* | **default** } command to bind the sub-interface to a DiffServ domain.
        + Run the [**qos phb enable**](cmdqueryname=qos+phb+enable) { *ds-domain-name* | **default** } command to bind the sub-interface to a DiffServ domain.![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          The **qos phb enable** command is mutually exclusive with the [**trust upstream**](cmdqueryname=trust+upstream) and [**qos phb disable**](cmdqueryname=qos+phb+disable) commands on an interface.
     3. Run the [**trust**](cmdqueryname=trust) { **8021p** | **inner-8021p** | **outer-8021p** } [ **inbound** | **outbound** ] command to enable 802.1p value-based BA classification.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + Before running the [**trust 8021p**](cmdqueryname=trust+8021p) command on an interface, you must run the [**trust upstream**](cmdqueryname=trust+upstream) command to bind the interface to a DiffServ domain. Otherwise, the [**trust 8021p**](cmdqueryname=trust+8021p) configuration does not take effect.
        + After you add an interface to a DiffServ domain, the traffic policy configured for the domain automatically takes effect for the incoming and outgoing traffic on the interface.
   
   
   * Apply a traffic policy to VLAN packets on a Layer 2 interface.
     1. Run the [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number* command to enter the view of a Layer 3 interface.
     2. Run the [**portswitch**](cmdqueryname=portswitch) command to change the interface mode from Layer 3 to Layer 2.
     3. Run the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** } command to add the Layer 2 interface to specific VLANs in tagged mode.
     4. Bind an interface to a DiffServ domain. Perform the following configurations based on the application scenario:![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The application scenarios of the two configurations are different. The [**qos phb enable vlan**](cmdqueryname=qos+phb+enable+vlan) command maps priorities only for downstream traffic. To map priorities for both upstream and downstream traffic, run the [**trust upstream vlan**](cmdqueryname=trust+upstream+vlan) command.
        
        
        + Run the [**trust upstream**](cmdqueryname=trust+upstream) { **5p3d** | *ds-domain-name* | **default** } [ **inbound** | **outbound** ] **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command to bind a downstream interface to a DiffServ domain for priority mapping.
        + Run the [**qos phb enable**](cmdqueryname=qos+phb+enable) { *ds-domain-name* | **default** | **5p3d** } **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command to bind a downstream interface to a DiffServ domain for priority mapping.![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          The **qos phb enable** command is mutually exclusive with the [**trust upstream vlan**](cmdqueryname=trust+upstream+vlan) and [**qos phb disable**](cmdqueryname=qos+phb+disable) commands on an interface.
     5. Run the [**trust 8021p**](cmdqueryname=trust+8021p) [ **inbound** | **outbound** ] **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command to enable 802.1p value-based BA classification.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following commands to check the previous configuration.

* Run the [**display diffserv domain**](cmdqueryname=display+diffserv+domain) [ *ds-domain-name* ] [ **8021p** | **dscp** | **exp** ] [ **inbound** | **outbound** ] command to check the DiffServ domain configuration.
* Run the [**display diffserv domain application**](cmdqueryname=display+diffserv+domain+application) *ds-domain-name* command to check the interface list applied to a specified DiffServ domain.