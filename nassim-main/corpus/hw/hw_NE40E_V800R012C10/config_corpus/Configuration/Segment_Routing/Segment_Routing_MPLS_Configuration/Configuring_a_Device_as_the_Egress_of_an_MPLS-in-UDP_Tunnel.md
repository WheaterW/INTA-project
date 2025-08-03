Configuring a Device as the Egress of an MPLS-in-UDP Tunnel
===========================================================

This section describes how to configure a device as the egress of an MPLS-in-UDP tunnel.

#### Usage Scenario

MPLS in UDP is a DCN overlay technology that encapsulates MPLS or SR-MPLS packets into UDP packets, allowing the packets to traverse some networks that do not support MPLS or SR-MPLS.

A device can be configured only as the egress of an MPLS-in-UDP tunnel to properly process MPLS-in-UDP packets. Running the [**mpls-in-udp**](cmdqueryname=mpls-in-udp) command does not trigger the establishment of an MPLS-in-UDP tunnel.


#### Pre-configuration Tasks

Before configuring a device as the egress of an MPLS-in-UDP tunnel, configure an SR-MPLS tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls-in-udp**](cmdqueryname=mpls-in-udp)
   
   
   
   The MPLS-in-UDP capability is enabled, and the MPLS-in-UDP view is displayed.
3. Run [**source-ip-validate list**](cmdqueryname=source-ip-validate+list) **destination-ip** *ip-addr*
   
   
   
   A destination IP address is specified for the IP address verification list, and the MPLS-in-UDP-List view is displayed.
4. Run [**source-ip**](cmdqueryname=source-ip) *ip-addr*
   
   
   
   A source IP address is specified for the IP address verification list.
5. Run [**validate-list enable**](cmdqueryname=validate-list+enable)
   
   
   
   The device is enabled to verify the source IP address mapped to the specified destination IP address.
   
   Source address verification secures MPLS-in-UDP tunnels. After the [**validate-list enable**](cmdqueryname=validate-list+enable) command is run and the device receives an MPLS-in-UDP packet, the device verifies the source IP address. The device discards the packet if the verification fails.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.