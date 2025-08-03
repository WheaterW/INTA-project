Configuring an EVC to Transmit Layer 2 Multicast Services
=========================================================

To improve network resource usage and implement on-demand multicast data forwarding in an EVC scenario, configure an EVC to transmit Layer 2 multicast services.

#### Context

On a Layer 2 multicast network, a Layer 2 device sets up mappings between interfaces and multicast MAC addresses by analyzing Internet Group Management Protocol (IGMP) packets transmitted between Layer 3 devices and users. The mapping information helps implement on-demand multicast data forwarding at the data link layer. If Layer 2 multicast devices use multiple different access modes on a network, service management and configuration are complicated and difficult. To resolve this issue, configure an EVC to transmit Layer 2 multicast services, implementing simplified network planning and management.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled globally.
3. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
4. (Optional) Run [**igmp-snooping designated-vlan**](cmdqueryname=igmp-snooping+designated-vlan) *vlan-id*
   
   
   
   The transparent transmission function is enabled in the BD for IGMP snooping messages with a specified VLAN ID.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can be run only in the BD that contains dot1q sub-interfaces with the default traffic behavior.
5. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled in the BD view.
6. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   
   
   An EVC Layer 2 sub-interface is specified, and its view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) EVC Layer 2 multicast can be configured only for termination-type user sub-interfaces (If the traffic encapsulation type is untag, do not configure any traffic behavior; if the traffic encapsulation type is dot1q, configure the traffic behavior of pop single; if the traffic encapsulation type is QinQ, configure the traffic behavior of pop double).
7. (Optional) Run [**igmp-snooping static-router-port**](cmdqueryname=igmp-snooping+static-router-port) [ **dot1q** **vid** *vid* | **qinq** **pe-vid** *pe-vid* **ce-vid** *ce-vid* ]
   
   
   
   A static router interface is specified.
   
   
   
   To have multicast traffic received through a specific router interface, use this command to specify the interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.