Configuring Priority Mappings for IP Packets
============================================

This section describes how to configure the mappings between DSCP values of IP packets, QoS service classes, and colors to implement QoS scheduling of IP packets.

#### Context

Traffic policy based on BA classification is used to map the priority of traffic on one type of network to another type. That is, to transmit the traffic in the other network according to the original priority.

When the NE40E serves as the border Router for different networks, the original external priorities (DSCP values) in the IP packets that go into the NE40E are all mapped to the internal priorities of the router represented by service classes of DiffServ and colors. When the NE40E sends out the packets, the internal priority is mapped back to the external priority.

BA classification is usually implemented on the core devices of the network. It can be implemented on both physical and logical interfaces. If implemented on the logical interface, BA classification can limit traffic congestion on member ports of the logical interface and restrict the priority of packets on the logical interface.

A DiffServ (DS) domain is a group of DiffServ nodes that adopt the same service policies and implement the same PHB aggregate.

The priority of packets is usually accepted or re-defined on the core Router. On the border Router in the IP domain or MPLS domain, DSCP and EXP values also need to be mapped.

The BA classification can map the internal priority to the external priority, and the external priority to the internal priority. However, mapping between traffic of the same type, for example, IP traffic or MPLS traffic, is not supported.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If unified scheduling is required for all upstream traffic on an interface, you can run the [**qos default-service-class**](cmdqueryname=qos+default-service-class) command to configure the upstream traffic on the interface to enter the specific queues and provide corresponding services. After this command is run, other packets cannot be enabled to enter the queues, and BA classification cannot be enabled.



#### Pre-configuration Tasks

Before configuring priority mappings for IP packets, complete the following tasks:

* Configure physical parameters for interfaces.
* Configure link layer attributes for interfaces to work properly.
* Configure IP addresses for interfaces.
* Enable a routing protocol for communication between devices.


#### Procedure

* Configure the mappings between DSCP values of IP packets, service classes, and colors.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**diffserv domain**](cmdqueryname=diffserv+domain) { *ds-domain-name* | **default** | **5p3d** } [ **domain-id** *domain-id-value* ]
     
     
     
     A DiffServ domain is defined, and the DiffServ domain view is displayed.
  3. Define traffic policies on the Router based on the actual situation.
     
     
     + To define a traffic policy for both incoming IPv4 and IPv6 traffic, run the [**ip-dscp-inbound**](cmdqueryname=ip-dscp-inbound) *dscp-value* **phb** *service-class* [ *color* ] or [**ip-dscp-inbound**](cmdqueryname=ip-dscp-inbound) *dscp-value1* **to** *dscp-value2* **phb** *service-class* [ *color* ] [ ****exclude-user-defined**** ] command.
     + To define a traffic policy for both outgoing IPv4 and IPv6 traffic, run the [**ip-dscp-outbound**](cmdqueryname=ip-dscp-outbound) *service-class* *color* **map** *dscp-value* command.
     + To define a traffic policy for incoming IPv4 traffic, run the [**ipv4-dscp-inbound**](cmdqueryname=ipv4-dscp-inbound) *dscp-value* **phb** *service-class* [ *color* ] or [**ipv4-dscp-inbound**](cmdqueryname=ipv4-dscp-inbound) *dscp-value1* **to** *dscp-value2* **phb** *service-class* [ *color* ] [ ****exclude-user-defined**** ] command.
     + To define a traffic policy for outgoing IPv4 traffic, run the [**ipv4-dscp-outbound**](cmdqueryname=ipv4-dscp-outbound) *service-class* *color* **map** *dscp-value* command.
     + To define a traffic policy for incoming IPv6 traffic, run the [**ipv6-dscp-inbound**](cmdqueryname=ipv6-dscp-inbound) *dscp-value* **phb** *service-class* [ *color* ] or [**ipv6-dscp-inbound**](cmdqueryname=ipv6-dscp-inbound) *dscp-value1* **to** *dscp-value2* **phb** *service-class* [ *color* ] [ ****exclude-user-defined**** ] command.
     + To define a traffic policy for outgoing IPv6 traffic, run the [**ipv6-dscp-outbound**](cmdqueryname=ipv6-dscp-outbound) *service-class* *color* **map** *dscp-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If both the [**ipv4-dscp-inbound**](cmdqueryname=ipv4-dscp-inbound) (or [**ipv6-dscp-inbound**](cmdqueryname=ipv6-dscp-inbound)) and [**ip-dscp-inbound**](cmdqueryname=ip-dscp-inbound) commands are run, the traffic policy configured using the [**ipv4-dscp-inbound**](cmdqueryname=ipv4-dscp-inbound) (or [**ipv6-dscp-inbound**](cmdqueryname=ipv6-dscp-inbound)) command takes effect preferentially, and the traffic policy configured using the [**ip-dscp-inbound**](cmdqueryname=ip-dscp-inbound) command takes effect for traffic that is not separately configured. The preceding rules also apply in the outbound direction.
     
     The system predefines a domain named **default** for IP packets. You are not allowed to delete the default domain.
     
     If the priority mapping in [Step 3](#EN-US_TASK_0172371256__substep1903366711214058) is not set in the DiffServ domain, the system uses the default mapping. The default domain describes the default mappings between the DSCP values, QoS service classes, and colors for IP packets. You can change the mappings in the domain. In the default domain, the DSCP values of the packets from an upstream device are mapped to QoS service classes and colors. Their mappings are shown in [Table 1](#EN-US_TASK_0172371256__tab_dc_ne_qos_cfg_005002). The QoS service classes and colors of the packets entering a downstream device are mapped to DSCP values. Their mappings are shown in [Table 2](#EN-US_TASK_0172371256__tab_dc_ne_qos_cfg_005004).
     
     **Table 1** Default mappings between DSCP values and service classes in the default domain
     | DSCP | Service | Color | DSCP | Service | Color |
     | --- | --- | --- | --- | --- | --- |
     | 00 | BE | Green | 32 | AF4 | Green |
     | 01 | BE | Green | 33 | BE | Green |
     | 02 | BE | Green | 34 | AF4 | Green |
     | 03 | BE | Green | 35 | BE | Green |
     | 04 | BE | Green | 36 | AF4 | Yellow |
     | 05 | BE | Green | 37 | BE | Green |
     | 06 | BE | Green | 38 | AF4 | Red |
     | 07 | BE | Green | 39 | BE | Green |
     | 08 | AF1 | Green | 40 | EF | Green |
     | 09 | BE | Green | 41 | BE | Green |
     | 10 | AF1 | Green | 42 | BE | Green |
     | 11 | BE | Green | 43 | BE | Green |
     | 12 | AF1 | Yellow | 44 | BE | Green |
     | 13 | BE | Green | 45 | BE | Green |
     | 14 | AF1 | Red | 46 | EF | Green |
     | 15 | BE | Green | 47 | BE | Green |
     | 16 | AF2 | Green | 48 | CS6 | Green |
     | 17 | BE | Green | 49 | BE | Green |
     | 18 | AF2 | Green | 50 | BE | Green |
     | 19 | BE | Green | 51 | BE | Green |
     | 20 | AF2 | Yellow | 52 | BE | Green |
     | 21 | BE | Green | 53 | BE | Green |
     | 22 | AF2 | Red | 54 | BE | Green |
     | 23 | BE | Green | 55 | BE | Green |
     | 24 | AF3 | Green | 56 | CS7 | Green |
     | 25 | BE | Green | 57 | BE | Green |
     | 26 | AF3 | Green | 58 | BE | Green |
     | 27 | BE | Green | 59 | BE | Green |
     | 28 | AF3 | Yellow | 60 | BE | Green |
     | 29 | BE | Green | 61 | BE | Green |
     | 30 | AF3 | Red | 62 | BE | Green |
     | 31 | BE | Green | 63 | BE | Green |
     
     [Table 2](#EN-US_TASK_0172371256__tab_dc_ne_qos_cfg_005004) shows the default mappings between internal service classes, colors, and DSCP values for IP packets.
     
     **Table 2** Default mappings between service classes and DSCP values
     | Service | Color | DSCP |
     | --- | --- | --- |
     | BE | Green | 0 |
     | AF1 | Green | 10 |
     | AF1 | Yellow | 12 |
     | AF1 | Red | 14 |
     | AF2 | Green | 18 |
     | AF2 | Yellow | 20 |
     | AF2 | Red | 22 |
     | AF3 | Green | 26 |
     | AF3 | Yellow | 28 |
     | AF3 | Red | 30 |
     | AF4 | Green | 34 |
     | AF4 | Yellow | 36 |
     | AF4 | Red | 38 |
     | EF | Green | 46 |
     | CS6 | Green | 48 |
     | CS7 | Green | 56 |
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  7. Run [**trust upstream**](cmdqueryname=trust+upstream) { **5p3d** | *ds-domain-name* | **default** } [ **inbound** | **outbound** ] 
     
     
     
     The DiffServ domain is bound to the interface, and BA classification is enabled on the interface.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the following commands to check the previous configuration.

* Run the [**display diffserv domain**](cmdqueryname=display+diffserv+domain) [ *ds-domain-name* ] [ **8021p** | **dscp** [ **ipv4** | **ipv6** ] | **exp**  ] [ **inbound** | **outbound** ] command to check the DiffServ domain configuration.
* Run the [**display diffserv domain application**](cmdqueryname=display+diffserv+domain+application) *ds-domain-name* command to check the interface list applied to a specified DiffServ domain.