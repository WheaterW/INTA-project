Configuring Priority Mappings for MPLS Packets
==============================================

This section describes how to configure priority mappings for MPLS packets and the application environment of this function.

#### Context

A priority mapping based on BA classification maps network-specific traffic priorities between two networks of different types so that the traffic priorities can remain unchanged while traffic is being transmitted between various networks.

When the NE40E serves as the border Router for different networks, the original external priorities (EXP values) in the MPLS packets that go into the NE40E are all mapped to the internal priorities represented by service classes of DiffServ and colors. When the NE40E sends out a packet, the internal priority is mapped back to the external priority.

Generally, the priority mappings of MPLS packets are configured on the core device of the network.


#### Pre-configuration Tasks

Before configuring priority mappings for MPLS packets, complete the following tasks:

* Configure physical parameters for interfaces.
* Configure link layer attributes for interfaces to work properly.
* Configure IP addresses for interfaces.
* Enable a routing protocol for communication between devices.

In VS mode, this configuration is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**diffserv domain**](cmdqueryname=diffserv+domain) *ds-domain-name*
   
   
   
   A DiffServ domain is defined and its view is displayed.
3. Define traffic policies on the Router based on the actual situation.
   
   
   * To define a traffic policy for incoming MPLS traffic, run the [**mpls-exp-inbound**](cmdqueryname=mpls-exp-inbound) *exp* **phb** *service-class* [ *color* ] command.
   * To define a traffic policy for outgoing MPLS traffic, run the [**mpls-exp-outbound**](cmdqueryname=mpls-exp-outbound) *service-class* *color* **map** *exp-value* command.
   
   The system predefines a default domain. If you do not configure priority mappings in Step 3 for the DiffServ domain, the system uses the default mappings. The default domain describes the default mappings from the EXP values of MPLS packets to QoS service classes and colors, or from QoS service classes and colors to the EXP values of MPLS packets. You can change the mappings in the default domain. The EXP values of the packets from an upstream device are mapped to QoS service classes and colors. Their mappings are shown in [Table 1](#EN-US_TASK_0172371268__tab_dc_ne_qos_cfg_005206). The QoS service classes and colors of the packets entering a downstream device are mapped to EXP values. Their mappings are shown in [Table 2](#EN-US_TASK_0172371268__tab_dc_ne_qos_cfg_005208).
   
   The default mappings between the EXP values of MPLS packets and QoS service classes are shown in [Table 1](#EN-US_TASK_0172371268__tab_dc_ne_qos_cfg_005206).
   
   **Table 1** Default mappings between the EXP values and QoS service classes
   | EXP | Service | Color | EXP | Service | Color |
   | --- | --- | --- | --- | --- | --- |
   | 0 | BE | Green | 4 | AF4 | Green |
   | 1 | AF1 | Green | 5 | EF | Green |
   | 2 | AF2 | Green | 6 | CS6 | Green |
   | 3 | AF3 | Green | 7 | CS7 | Green |
   
   The default mappings between the EXP values of MPLS packets and QoS service classes are shown in [Table 2](#EN-US_TASK_0172371268__tab_dc_ne_qos_cfg_005208).
   
   **Table 2** Default mappings between the EXP values and QoS service classes
   | Service | Color | MPLS EXP |
   | --- | --- | --- |
   | BE | Green | 0 |
   | AF1 | Green, Yellow, Red | 1 |
   | AF2 | Green, Yellow, Red | 2 |
   | AF3 | Green, Yellow, Red | 3 |
   | AF4 | Green, Yellow, Red | 4 |
   | EF | Green | 5 |
   | CS6 | Green | 6 |
   | CS7 | Green | 7 |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
7. Run [**trust upstream**](cmdqueryname=trust+upstream) { *ds-domain-name* | **default** }
   
   
   
   The DiffServ domain is bound to the interface, and BA classification is enabled on the interface.
8. (Optional) Run [**mpls l2vc diffserv domain**](cmdqueryname=mpls+l2vc+diffserv+domain) { **5p3d** | *domain-name* | **default** }
   
   
   
   A DiffServ domain to which the private network label priority to be marked belongs is bound to a VLL interface.
9. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. (Optional) Run [**slot**](cmdqueryname=slot) *slot-id*
    
    
    
    The slot view is displayed.
11. (Optional) Run [**mpls-inner-exp phb disable vll**](cmdqueryname=mpls-inner-exp+phb+disable+vll)
    
    
    
    The device is disabled from obtaining the private network label priority for downstream traffic on the PW interface in VLL scenarios.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

Run the following commands to check the previous configuration.

* Run the [**display diffserv domain**](cmdqueryname=display+diffserv+domain) [ *ds-domain-name* ] [ **8021p** | **atm** | **dscp** | **exp** ] [ **inbound**| **outbound** ] command to check the DiffServ domain configuration.
* Run the [**display diffserv domain application**](cmdqueryname=display+diffserv+domain+application) *ds-domain-name* command to check the interface list applied to a specified DiffServ domain.