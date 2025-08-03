Configuring a Static Load Balancing Mode
========================================

Configuring a Static Load Balancing Mode

#### Context

A default static load balancing mode is pre-defined for different types of packets on the device. If traffic is load balanced evenly on the network, the default load balancing mode can fulfill requirements. However, if traffic is load balanced unevenly, you can configure a static load balancing mode based on traffic models through either of the following methods:

* Configure a global enhanced load balancing profile with a load balancing mode specified for each type of packets. This configuration takes effect globally.
* Configure a load balancing mode for each type of packets on an Eth-Trunk interface. This configuration takes effect on the current Eth-Trunk interface only.

The load balancing mechanisms for known and unknown unicast packets are different.

* For known unicast packets, you can configure both the load balancing mode and hash algorithm in a global enhanced load balancing profile and on an Eth-Trunk interface. The following describes which configuration takes precedence.
  + Load balancing mode: If the default load balancing mode is applied to all types of packets on an Eth-Trunk interface and a global enhanced load balancing profile is configured, the load balancing modes specified in the global enhanced load balancing profile take precedence. If any type of packets on an Eth-Trunk interface uses a non-default load balancing mode (for example, only the load balancing mode of Layer 2 packets is changed), the load balancing modes for all types of packets configured on the Eth-Trunk interface take effect preferentially even if a global enhanced load balancing profile is configured at the same time.
  + Hash algorithm: If the default hash algorithm is applied to an Eth-Trunk interface and a global enhanced load balancing profile is configured at the same time, the hash algorithm specified in the global enhanced load balancing profile takes precedence. If an Eth-Trunk interface uses a non-default hash algorithm, this non-default hash algorithm takes effect preferentially even if a global enhanced load balancing profile is configured at the same time.

* For unknown unicast packets, only the load balancing mode and hash algorithm in the global enhanced load balancing profile takes effect.

Since only outgoing traffic can be load balanced, the load balancing mode on one end of a link does not affect that on the other, and so there is no need for the load balancing modes to be the same on both ends. The load balancing mode is related to the packet type, but not the packet forwarding process. The device identifies the type of the Layer 3 packet carried in an Ethernet frame. For example, if the device identifies an IPv4 packet, it applies the load balancing mode configured for IPv4 packets to the IPv4 packet even if only Layer 2 forwarding needs to be performed on the IPv4 packet. If the device identifies a non-IP or non-MPLS packet, the device applies the load balancing mode configured for Layer 2 packets to this packet.

Only Eth-Trunk interfaces on the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ support the forwarding of packets with the same source and destination addresses. Specifically, a network connection's bidirectional packets with the same source and destination addresses are forwarded by the same Eth-Trunk interface. During network traffic analysis, a device is required to analyze bidirectional traffic between communicating parties. During this process, the packets of such communicating parties must be forwarded to the same device for analysis, which requires the device to forward packets with the same source address through the same outbound interface. When mirroring the packets of communicating parties to the analysis server, the device sends those with the same source and destination IP or MAC addresses through the same Eth-Trunk interface. As a result, the server can analyze bidirectional traffic.


#### Procedure

* Configuring a static load balancing mode based on a global enhanced load balancing profile
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Configure the device to perform hash calculation on GTP packets based on the TEID field in the profile.
     
     
     ```
     load-balance gtp teid
     ```
     
     By default, this function is disabled.
     
     This command is not supported by the CE6885-LL (low latency mode).
  3. Create a static load balancing profile and enter the static load balancing profile view, or enter the view of an existing static load balancing profile.
     
     
     ```
     [load-balance profile](cmdqueryname=load-balance+profile) profile-name
     ```
     
     The device supports only one load balancing profile. The default load balancing profile is named **default**. A newly created load balancing profile will overwrite an existing one.
  4. Configure load balancing modes for different types of packets separately. Run one or several of the following commands as required. Skip this step if you want to use the default load balancing mode.
     
     
     + Configure a load balancing mode for IPv4 packets in the profile.
       
       For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
       
       ```
       [ip](cmdqueryname=ip) [ src-ip | dst-ip | l4-src-port | l4-dst-port | protocol | src-mac | dst-mac | flowlabel | src-interface | dest-qp | session-id ] *
       ```
       
       By default, IPv4 packets are load balanced based on **session-id**, **dest-qp**, **src-ip**, **dst-ip**, **l4-src-port**, and **l4-dst-port**.
       
       For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
       
       ```
       [ip](cmdqueryname=ip) [ src-ip | dst-ip | protocol | l4-src-port | l4-dst-port ] *
       ```
       
       By default, IPv4 packets are load balanced based on **src-ip**, **dst-ip**, **l4-src-port**, and **l4-dst-port**.
     + Configure a load balancing mode for IPv6 packets in the profile.
       
       This step is supported only by the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.
       
       ```
       [ipv6](cmdqueryname=ipv6) [ src-ip | dst-ip | protocol | l4-src-port | l4-dst-port ] *
       ```
       
       By default, IPv6 packets are load balanced based on **src-ip**, **dst-ip**, **l4-src-port**, and **l4-dst-port**.
     + Configure a load balancing mode for MPLS packets in the profile.
       
       For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
       
       ```
       [mpls](cmdqueryname=mpls) [ top-label | 2nd-label | 3rd-label | src-ip | dst-ip | src-interface | src-mac | dst-mac | l4-src-port | l4-dst-port | protocol ] *
       ```
       
       By default, MPLS packets are load balanced based on the two outer labels (**top-label** and **2nd-label**).
       
       For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
       
       ```
       [mpls](cmdqueryname=mpls) [ src-ip | dst-ip | top-label | 2nd-label ] *
       ```
       
       By default, MPLS packets are load balanced based on the two outer labels (**top-label** and **2nd-label**).
       
       For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ:
       ```
       [mpls](cmdqueryname=mpls) [ src-ip | dst-ip | top-label | 2nd-label | 3rd-label | src-mac | dst-mac | src-interface | l4-src-port | l4-dst-port | protocol | fourth-label | fifth-label ] * 
       ```
       
       By default, MPLS packets are load balanced based on **top-label** and **2nd-label**.
       
       This command is not supported by the CE6885-LL (low latency mode).
     + Configure a load balancing mode for Layer 2 packets in the profile.
       ```
       [l2](cmdqueryname=l2) [ src-mac | dst-mac | src-interface | eth-type | vlan ] *
       ```
       
       By default, Layer 2 packets are load balanced based on **src-mac**, **dst-mac**, and **vlan**.
  5. Configure the device to perform hash calculation on tunnel packets based on their inner or outer header in the profile.
     
     
     ```
     [tunnel](cmdqueryname=tunnel) { inner-header | outer-header }
     ```
     
     By default, hash calculation is performed on tunnel packets based on their outer header.
     
     This command is not supported by the CE6885-LL (low latency mode).
  6. Configure the device to perform hash calculation on MAC-in-MAC packets based on their inner or outer header in the profile.
     
     
     
     This step is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
     
     ```
     [mac-in-mac](cmdqueryname=mac-in-mac) { outer-header | inner-header }
     ```
     
     By default, hash calculation is performed on MAC-in-MAC packets based on their outer header.
     
     This command is not supported by the CE6885-LL (low latency mode).
  7. Configure the hash algorithm value or the start hash value for load balancing on an Eth-Trunk interface in the profile.
     
     
     
     For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ:
     
     ```
     [eth-trunk](cmdqueryname=eth-trunk) { seed seed-data | hash-mode hash-mode-id } *
     ```
     
     By default, the hash algorithm value for load balancing is 1 and the start hash value is 1.
     
     For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
     
     ```
     [eth-trunk](cmdqueryname=eth-trunk) hash-mode hash-mode-id 
     ```
     
     By default, the hash algorithm value for load balancing is 1.
  8. Configure the calculation result offset of the hash algorithm for load balancing in the profile.
     
     
     
     This step is supported only by the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
     
     ```
     [eth-trunk](cmdqueryname=eth-trunk) universal-id [ universal-id ]
     ```
     
     By default, the calculation result offset of the hash algorithm for load balancing is 1.
  9. (Optional) Configure an Eth-Trunk interface to forward packets with the same source and destination addresses in the profile.
     
     
     
     This step is supported only by the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
     
     ```
     [mode symmetry](cmdqueryname=mode+symmetry)
     ```
     
     By default, an Eth-Trunk interface does not forward packets with the same source and destination addresses.
     
     This command is not supported by the CE6885-LL (low latency mode).
  10. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Configuring a load balancing mode for an Eth-Trunk interface
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface.
     
     
     ```
     [interface](cmdqueryname=interface) eth-trunk trunk-id
     ```
  3. Configure load balancing modes for different types of packets. Run one or several of the following commands as required. Skip this step if you want to use the default load balancing mode.
     
     
     + Configure a load balancing mode for IP packets.
       
       For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
       
       ```
       [load-balance ip](cmdqueryname=load-balance+ip) [ src-ip | dst-ip | l4-src-port | l4-dst-port | protocol | src-mac | dst-mac | flowlabel | src-interface | dest-qp | session-id ] *
       ```
       
       By default, IP packets are load balanced based on **src-ip**, **dst-ip**, **l4-src-port**, **l4-dst-port**, **dst-qp**, and **session-id**.
       
       For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
       
       ```
       [load-balance](cmdqueryname=load-balance) { dst-ip | src-ip | src-dst-ip | dst-mac | src-mac | src-dst-mac | round-robin | enhanced profile profile-name }
       ```
       
       By default, packets are load balanced based on **src-dst-ip** on an Eth-Trunk interface.
       
       When the **enhanced profile** parameter is configured, the Eth-Trunk interface uses the configuration in the global load balancing profile configured using the [**load-balance profile**](cmdqueryname=load-balance+profile) command.
     + Configure a load balancing mode for MPLS packets.
       
       For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
       
       ```
       [load-balance mpls](cmdqueryname=load-balance+mpls) [ top-label | 2nd-label | 3rd-label | src-ip | dst-ip | src-interface | src-mac | dst-mac | l4-src-port | l4-dst-port | protocol ] *
       ```
       
       By default, MPLS packets are load balanced based on the two outer labels (**top-label** and **2nd-label**).
     + Configure a load balancing mode for Layer 2 packets.
       
       For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
       
       ```
       [load-balance l2](cmdqueryname=load-balance+l2) [ vlan | src-mac | dst-mac | eth-type | src-interface ] *
       ```
       
       By default, Layer 2 packets are load balanced based on **src-mac**, **dst-mac**, and **vlan**.
  4. Configure a hash algorithm for load balancing on the Eth-Trunk interface.
     
     
     
     This step is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM.
     
     ```
     [load-balance hash-mode](cmdqueryname=load-balance+hash-mode) hash-mode-value
     ```
     
     By default, the hash algorithm value for load balancing on an Eth-Trunk interface is 1.
  5. Configure resilient hashing on the Eth-Trunk interface.
     
     
     ```
     [load-balance enhanced resilient](cmdqueryname=load-balance+enhanced+resilient)
     ```
     
     By default, resilient hashing is disabled.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Resilient hashing reduces the chances of traffic switching to other links when member links are added to or deleted from an Eth-Trunk. For example, an Eth-Trunk consists of three member links. If one link fails, all traffic is reallocated and load balanced over the other two links if resilient hashing is not configured. If resilient hashing is configured, the traffic that has been allocated to the other two links is still transmitted over them, and the traffic on the faulty link is evenly distributed to these links, minimizing the impact on services. After the faulty link recovers, some traffic is switched from the other two links to the recovered link, but the traffic volume on each is not the same as that before the link fault.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) [ *trunk-id* [ **verbose** ] ] command to check the load balancing mode of a specified Eth-Trunk interface based on the **Hash Arithmetic** field.
* Run the [**display load-balance profile**](cmdqueryname=display+load-balance+profile) [ *profile-name* ] command to view detailed information about a specified load balancing profile.
* Run the [**display load-balance eth-trunk**](cmdqueryname=display+load-balance+eth-trunk) *trunk-id* command to check the load balancing mode that takes effect on a specified Eth-Trunk interface.

#### Follow-up Procedure

* Display the outbound interface that is calculated based on the input 5-tuple information and source and destination MAC addresses.
  
  [**display load-balance forwarding-path unicast interface eth-trunk**](cmdqueryname=display+load-balance+forwarding-path+unicast+interface+eth-trunk) *trunk-id* **src-interface** *interface-type interface-number* { **ethtype** *ethtype-number* | **vlan** *vlan-id* | [ [ **src-ip** *src-ip-data* | **dst-ip** *dst-ip-data* ] \* | [ **src-ipv6** *src-ipv6-data* | **dst-ipv6** *dst-ipv6-data* ] \* ] | **src-mac** *src-mac-data* | **dst-mac** *dst-mac-data* | **protocol** { *protocol-number* | [**icmp**](cmdqueryname=icmp) | [**igmp**](cmdqueryname=igmp) | [**ip**](cmdqueryname=ip) | [**ospf**](cmdqueryname=ospf) | [**tcp**](cmdqueryname=tcp) [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | [**udp**](cmdqueryname=udp) [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \* **slot** *slot-id*
  
  This command is not supported by the CE6885-LL (low latency mode).
* Display the outbound interface of packets that contain specified 5-tuple information, source MAC address, and destination MAC address. The query result is displayed only when traffic passes through this outbound interface.
  
  [**display port forwarding-path**](cmdqueryname=display+port+forwarding-path) { **src-ip** *src-ip-data* [ *ip-mask-len* | *source-ip-mask* ] | **dst-ip** *dst-ip-data* [ *ip-mask-len* | *dst-ip-mask* ] | **src-mac** *src-mac-data* | **dst-mac** *dst-mac-data* | **protocol** { *protocol-number* | [**gre**](cmdqueryname=gre) | [**icmp**](cmdqueryname=icmp) | [**igmp**](cmdqueryname=igmp) | [**ip**](cmdqueryname=ip) | [**ipinip**](cmdqueryname=ipinip) | [**ospf**](cmdqueryname=ospf) | [**tcp**](cmdqueryname=tcp) [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | [**udp**](cmdqueryname=udp) [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \*
  
  This command is not supported by the CE6885-LL (low latency mode).