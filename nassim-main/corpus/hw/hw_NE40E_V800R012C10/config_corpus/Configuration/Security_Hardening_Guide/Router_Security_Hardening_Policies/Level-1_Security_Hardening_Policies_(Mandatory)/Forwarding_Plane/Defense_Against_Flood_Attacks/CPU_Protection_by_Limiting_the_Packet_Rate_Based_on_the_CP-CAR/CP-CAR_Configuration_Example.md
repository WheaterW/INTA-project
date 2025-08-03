CP-CAR Configuration Example
============================

CP-CAR Configuration Example

#### Networking Requirements

Security requirements for Routers are as follows:

* Save system resources by preventing excessive usage of CPU resources.
* Prevent attackers from manipulating managed Routers using management packets.
* Record attack packet information for fault analysis and location.
* Notify users of dropped packets by reporting an alarm.

#### Configuration Roadmap

The roadmap for configuring attack defense on the Router is as follows:

* Identify and group the protocols used by various services on the Router and differentiate normal service traffic from malicious traffic.
* Configure a CPU defense policy to specify the match sequence of traffic sent to the CPU.
  1. Configure TCP/IP attack defense check to prevent TCP/IP attacks.
  2. Configure application layer association. Configure the application layer association check to enable the router to check the bandwidth of received packets.
  3. Configure a processing policy for authorized packets. This policy enables the Router to compare normal protocol packets and packets to be protected against the whitelist and user-defined flows. If matching the whitelist or user-defined flows, these packets will be sent to the CPU over different channels with different bandwidth based on priorities.
  4. Configure a processing policy for unauthorized packets and unknown packets. This policy enables the Router to compare unauthorized packets and unknown packets against the blacklist. If matching the blacklist, these packets will be dropped or sent to the CPU over channels with limited bandwidth at a lower priority.
  5. Configure attack source tracing, so that dropped packets can be recorded for fault analysis and location.
  6. Enable the packet drop alarm function.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  
  By default, TCP SYN flood attack defense is enabled. TCP SYN flood attack defense takes precedence over the configured blacklist function. Therefore, the ACL specified for TCP SYN flood attack defense other than the ACL specified in the **blacklist acl** command is used to filter TCP SYN packets.
  
  Before using the ACL specified in the **blacklist acl** command to filter TCP SYN packets, run the **undo tcpsyn-flood enable** command to disable TCP SYN flood attack defense.
  
  If TCP SYN flood attack defense is disabled, the TCP SYN packets that fail to match the ACL specified in the **blacklist acl** command will be sent to the CPU. Therefore, exercise caution when running the **undo tcpsyn-flood enable** command.
* Configure management plane protection to prevent unauthorized users from launching attacks through non-management interfaces (management plane) using management packets.

#### Data Preparation

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The data used in this example is for your reference only. For configuration data required for live networks, contact Huawei engineers.



**Table 1** Service information related to Device
| Category | Traffic Type | Priority | Action | Remarks |
| --- | --- | --- | --- | --- |
| Trusted network segment | Source IP address | High | User-defined flow 1. The rate limit is 1 Mbit/s. | Packets from the trusted network segment of the Router are filtered using ACL 3331. |
| Routing protocol | BGP | High | User-defined flow 2. The rate limit is 512 kbit/s. | Protocol packets are filtered using ACL 3332.  NOTE:  The device supports BGP dynamic link protection. BGP protocol packets for which BGP routes are established match the whitelist and sent to the CPU. The ACL limits the BGP protocol packets for which BGP routes are not established. |
| LDP | High | User-defined flow 3. The rate limit is 512 kbit/s. | Packets coming from the source IP addresses of LDP peers and directly-connected address are filtered using ACL 3333. |
| OSPF,RIP | High | User-defined flow 4. The rate limit is 1 Mbit/s. | Packets coming from the source IP addresses of OSPF neighbors are filtered using ACL 3334. |
| ISIS | NA | NA | IS-IS is a Layer 2 protocol and does not involve the ACL. |
| Reliability protocol | VRRP | High | User-defined flow 5. The rate limit is 1300 kbit/s. | Virtual Router protocol packets are filtered using ACL 3335. |
| Multicast protocol | PIM | High | User-defined flow 6. The rate limit is 1 Mbit/s. | PIM packets are filtered using ACL 3336. |
| IGMP | High | User-defined flow 7. The rate limit is 512 kbit/s. | IGMP packets are filtered using ACL 3337. |
| MSDP | Low | User-defined flow 8. The rate limit is 512 kbit/s. | MSDP packets are filtered using ACL 3338. |
| Reserved multicast addresses | High | User-defined flow 9. The rate limit is 512 kbit/s. | Packets coming from multicast addresses 224.0.0.0 to 224.0.0.255 are filtered using ACL 3339. |
| Reserved broadcast address | Low | User-defined flow 10. The rate limit is 512 kbit/s. | Packets coming from the broadcast address 255.255.255.255 are filtered using ACL 3340. |
| Access protocol | SSH | Medium | User-defined flow 11. The rate limit is 512 kbit/s. | Protocol packets are filtered using ACL 3341. |
| TELNET  NOTE:  Use the STelnet protocol because this protocol is not secure. |
| FTP  NOTE:  Use the SFTP protocol because this protocol is not secure. | Low | User-defined flow 12. The rate limit is 512 kbit/s. | Protocol packets are filtered using ACL 3342. |
| TFTP  NOTE:  Use the SFTP protocol because this protocol is not secure. |
| Network management protocol | SNMP | Low | User-defined flow 13. The rate limit is 1 Mbit/s. | Protocol packets are filtered using ACL 3343. |
| Service protocol | TACACS | Low | User-defined flow 14. The rate limit is 1 Mbit/s. | Protocol packets are filtered using ACL 3344. |
| NTP | Low | User-defined flow 15. The rate limit is 150 kbit/s. | Protocol packets are filtered using ACL 3345. |
| Tool protocol | ICMP | Low | User-defined flow 16. The rate limit is 512 kbit/s. | ICMP TTL-threshold-crossing packets, port unreachable packets, response packets, and response acknowledgement packets are filtered using ACL 3346. |
| LSPPING | High | User-defined flow 17. The rate limit is 1 Mbit/s. | Protocol packets are filtered using ACL 3347. |
| Others | Packets of unknown protocols | Low | 512 kbit/s best-effort bandwidth is reserved. | Protocol packets are filtered using ACL 3348. |
| Attack packets or unauthorized protocol packets (blacklist) | Low | The bandwidth is 0. | Protocol packets are filtered using ACL 3330. |



#### Procedure

1. Configure a CPU defense policy.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] cpu-defend policy 10
   [*DeviceA-cpu-defend-policy-10] commit
   ```
2. Configure defense against TCP/IP packet attacks.
   ```
   [*DeviceA-cpu-defend-policy-10] fragment-flood enable
   [*DeviceA-cpu-defend-policy-10] udp-packet-defend enable
   [*DeviceA-cpu-defend-policy-10] abnormal-packet-defend enable
   [*DeviceA-cpu-defend-policy-10] commit
   ```
3. Set the match sequence of packets to be sent to the CPU.
   
   The match sequence of packets to be sent to the CPU is as follows: TCPSYN packets -> packet fragments -> dynamic link protection -> management protocol ACL -> whitelist -> user-defined flow -> blacklist.
   
   ```
   [~DeviceA-cpu-defend-policy-10] process-sequence tcpsyn-flood fragment-flood dynamic-link-protection management-acl whitelist user-defined-flow blacklist
   [*DeviceA-cpu-defend-policy-10] commit
   ```
4. Configure the match rules of a blacklist.
   
   It is recommended to add unauthorized user packets, invalid protocol packets, and attack packets into the blacklist and configure the policy action as discard. Use ACL 3330 to match these packets.
   
   ```
   [~DeviceA] acl number 3330
   [*DeviceA-acl-adv-3330] rule deny ip source 10.1.1.0 0.0.0.255
   [*DeviceA-acl-adv-3330] commit
   [~DeviceA-acl-adv-3330] quit
   ```
5. Configure the action of a blacklist.
   ```
   [~DeviceA-cpu-defend-policy-10] blacklist acl 3330
   [*DeviceA-cpu-defend-policy-10] car blacklist cir 0
   ```
   ```
   [*DeviceA-cpu-defend-policy-10] commit
   ```
6. Configure a user-defined flow.
   * Add the IP address of a trusted network segment to ACL 3331.
     ```
     <DeviceA> system-view 
     [~DeviceA] acl number 3331
     [*DeviceA-acl-adv-3331] rule permit ip source 10.1.2.0 0.0.0.255
     [*DeviceA-acl-adv-3331] rule permit ip source 10.1.3.0 0.0.0.255
     [*DeviceA-acl-adv-3331] commit
     [~DeviceA-acl-adv-3331] quit
     ```
   * Add BGP to ACL 3332.
     
     The device supports BGP dynamic link protection. BGP protocol packets for which BGP routes are established match the whitelist and sent to the CPU. This ACL limits the BGP peer protocol packets for which BGP routes are not established.
     
     ```
     [~DeviceA] acl number 3332
     ```
     ```
     [*DeviceA-acl-adv-3332] rule permit tcp source 10.12.1.0 0.0.0.255 destination-port eq bgp
     [*DeviceA-acl-adv-3332] rule permit tcp source 10.12.1.0 0.0.0.255 source-port eq bgp
     ```
     ```
     [*DeviceA-acl-adv-3332] commit
     ```
   * Add LDP to ACL 3333.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The establishment of an LDP session is different from that of a BGP session. LDP establishes a connection using TCP but maintains the peer relationship using UDP. This process involves not only the peer address, but also the IP address of the directly connected interface. Perform the following steps to establish an LDP session:
     
     Run the **display mpls ldp peer** command to obtain peer information:
     
     ```
     [*DeviceA-acl-adv-3332] display mpls ldp peer 
              LDP Peer Information in Public network 
      ------------------------------------------------------------------------------ 
      Peer-ID                TransportAddress   DiscoverySource 
      ------------------------------------------------------------------------------ 
      1.1.1.32:0             1.1.1.32           GigabitEthernet0/3/1 
      ------------------------------------------------------------------------------ 
      TOTAL: 1 Peer(s) Found. 
     ```
     
     View the IP address of the interface directly connected to the local device.
     
     ```
     [*DeviceA-GigabitEthernet0/3/1]display this 
     # 
     interface GigabitEthernet0/3/1 
     undo shutdown 
     ip address 11.11.11.2 255.255.255.0 
     mpls 
     mpls ldp 
     #
     ```
     
     Local LDP discovers peers through bidirectional Hello packets. Hello packets are UDP packets with the source address being the local interface address and destination address being the multicast IP address. Remote LDP discovers peers similarly. The only difference is that the destination address is changed to the configured remote peer address. Add the peer's Hello packets to the ACL.
     
     ```
     [~DeviceA] acl number 3333
     [*DeviceA-acl-adv-3333] rule permit udp source 11.11.11.1 0 destination-port eq 646
     [*DeviceA-acl-adv-3333] rule permit udp source 11.11.11.1 0 source-port eq 646
     [*DeviceA-acl-adv-3333] commit
     ```
     
     The local LDP transport address is carried in the Hello packet payload. After using the LDP Hello packet to discover the peer and obtain the transport address of the peer, the device attempts to establish an LDP session using TCP to transmit notification messages. In TCP interaction, the device with a larger transport address initiates a TCP connection setup request, with the destination port number of 646 and a random source port number. You can skip this step and add two ACL rules.
     
     ```
     [*DeviceA-acl-adv-3333] rule permit tcp source 1.1.1.32 0 destination-port eq 646
     [*DeviceA-acl-adv-3333] rule permit tcp source 1.1.1.32 0 source-port eq 646
     [*DeviceA-acl-adv-3333] commit
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a device has multiple LDP peers, add four ACL rules for each peer address.
     + ACL rules can be configured based on the source IP address + port number or solely on the port number. ACL rules configured based on the source IP address + port number are more secure, but complicated in information collection. ACL rules configured based solely on the port number are less secure, but easy to configure. Choose either of the preceding methods as needed. A simplified configuration procedure is as follows:
     ```
     [~DeviceA-acl-adv-3332] acl number 3333 
     [*DeviceA-acl-adv-3333] rule permit tcp source-port eq 646 
     [*DeviceA-acl-adv-3333] rule permit tcp destination-port eq 646 
     [*DeviceA-acl-adv-3333] rule permit udp source-port eq 646 
     [*DeviceA-acl-adv-3333] rule permit udp destination-port eq 646
     [*DeviceA-acl-adv-3333] commit
     ```
   * Add OSPF and RIP to ACL 3334.
     ```
     [~DeviceA] acl number 3334
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The device supports OSPF dynamic link protection. OSPF protocol packets for which OSPF routes are established match the whitelist and sent to the CPU. This ACL limits the OSPF protocol packets for which OSPF routes are not established.
     
     ```
     [*DeviceA-acl-adv-3334] rule 5 permit ospf
     ```
     ```
     [*DeviceA-acl-adv-3334] commit
     ```
     
     Configuring ACL rules for RIP is similar to configuring ACL rules for OSPF.
   * Add VRRP to ACL 3335.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     VRRP is an IP-based protocol, and its protocol number is 112. VRRP sends packets based on the IP addresses of virtual interfaces on peers. The protocol number and IP addresses of virtual interfaces need to be added to the ACL for protection. VRRP peer information can be obtained using the **display vrrp** command.
     
     ```
     [~DeviceA] acl number 3335
     [*DeviceA-acl-adv-3335] rule permit 112 source 11.11.11.100 0
     [*DeviceA-acl-adv-3335] quit
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a device has multiple VRRP peers, define an ACL rule for each peer address.
     + ACL rules can be configured based on the source IP address + port number or solely on the port number. ACL rules configured based on the source IP address + port number are more secure, but complicated in information collection. ACL rules configured based solely on the port number are less secure, but easy to configure. Choose either of the preceding methods as needed. A simplified configuration procedure is as follows:
     ```
     [~DeviceA-acl-adv-3335] rule 5 permit 112
     ```
     ```
     [*DeviceA-acl-adv-3335] commit
     ```
   * Multicast protocols.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     PIM is a multicast protocol, and the port number is 103.
     
     ```
     [~DeviceA] acl number 3336
     [*DeviceA-acl-adv-3336] rule permit 103
     [*DeviceA-acl-adv-3336] quit
     ```
     ```
     [~DeviceA] acl number 3337
     [*DeviceA-acl-adv-3337] rule permit igmp
     [*DeviceA-acl-adv-3337] commit
     [~DeviceA-acl-adv-3337] quit
     ```
     ```
     [~DeviceA] acl number 3338
     [*DeviceA-acl-adv-3338] rule permit udp destination-port eq 639
     [*DeviceA-acl-adv-3338] rule permit udp source-port eq 639
     [*DeviceA-acl-adv-3338] rule permit tcp destination-port eq 639
     [*DeviceA-acl-adv-3338] rule permit tcp source-port eq 639
     [*DeviceA-acl-adv-3338] commit
     [~DeviceA-acl-adv-3338] quit
     ```
   * Add reserved multicast addresses from 224.0.0.0 to 224.0.0.255 to ACL 3339.
     ```
     [~DeviceA] acl number 3339
     [*DeviceA-acl-adv-3339] rule permit ip destination 224.0.0.0 0.0.0.255
     [*DeviceA-acl-adv-3339] commit
     [~DeviceA-acl-adv-3339] quit
     ```
   * Add reserved broadcast address 255.255.255.255 to ACL 3340.
     ```
     [~DeviceA] acl number 3340
     [*DeviceA-acl-adv-3340] rule permit ip destination 255.255.255.255 0
     [*DeviceA-acl-adv-3340] commit
     [~DeviceA-acl-adv-3340] quit
     ```
   * Add Telnet and SSH to ACL 3341.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Telnet and SSH are TCP-based protocols. They are used for login and are very important protocols. Therefore, the two protocols are added to a separate ACL for protection. The device supports Telnet and SSH dynamic link protection. Telnet and SSH protocol packets for which Telnet and SSH links are established match the whitelist and sent to the CPU. This ACL limits the Telnet and SSH protocol packets for which Telnet and SSH links are not established. The SSH port number is 22.  Configuring the device to drop management protocol packets with unknown source addresses is recommended.
     
     ```
     [~DeviceA] acl number 3341
     [*DeviceA-acl-adv-3341] rule permit tcp source 192.168.1.0 0.0.0.255 source-port eq telnet
     [*DeviceA-acl-adv-3341] rule permit tcp source 192.168.1.0 0.0.0.255 destination-port eq telnet
     [*DeviceA-acl-adv-3341] rule permit tcp source 192.168.1.0 0.0.0.255 source-port eq 22
     [*DeviceA-acl-adv-3341] rule permit tcp source 192.168.1.0 0.0.0.255 destination-port eq 22
     [*DeviceA-acl-adv-3341] quit
     ```
     ```
     [*DeviceA-acl-adv-3341] rule deny tcp destination-port eq telnet
     [*DeviceA-acl-adv-3341] rule deny tcp destination-port eq 22
     [*DeviceA-acl-adv-3341] commit
     ```
   * Add FTP and TFTP to ACL 3342.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     FTP is based on TCP whereas TFTP is based on UDP. Each source address requires three ACL rules.
     
     ```
     [~DeviceA] acl number 3342
     [*DeviceA-acl-adv-3342] rule permit udp source 192.168.1.0 0.0.0.255 destination-port eq tftp
     [*DeviceA-acl-adv-3342] rule permit tcp source 192.168.1.0 0.0.0.255 source-port eq ftp
     [*DeviceA-acl-adv-3342] rule permit tcp source 192.168.1.0 0.0.0.255 destination-port eq ftp
     [*DeviceA-acl-adv-3342] quit
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The ranges of FTP and TFTP source address segments must be confirmed by carriers.
     + ACL rules can be configured based on the source IP address + port number or solely on the port number. ACL rules configured based on the source IP address + port number are more secure, but complicated in information collection. ACL rules configured based solely on the port number are less secure, but easy to configure. Choose either of the preceding methods as needed. A simplified configuration procedure is as follows:
     ```
     [*DeviceA-acl-adv-3342] rule permit udp destination-port eq tftp 
     [*DeviceA-acl-adv-3342] rule permit tcp source-port eq ftp 
     [*DeviceA-acl-adv-3342] rule permit tcp destination-port eq ftp
     [*DeviceA-acl-adv-3342] commit
     ```
   * Add SNMP to ACL 3343.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A network management system (NMS) is deployed on most live networks. An NMS server sends a large number of UDP request packets, and devices send UDP reply packets through SNMP ports. As a large number of packets need to be exchanged, these devices need to be added to a separate ACL for protection.
     
     The source address segment added to the ACL must be confirmed by the customer. Otherwise, the NMS servers with IP addresses not being listed in the ACL will fail to manage the device. SNMP is a system management protocol. Configuring the device to drop SNMP protocol packets with unknown source addresses is recommended.
     
     ```
     [~DeviceA] acl number 3343
     [*DeviceA-acl-adv-3343] rule permit udp source 10.20.20.0 0.0.0.255 source-port eq snmp
     [*DeviceA-acl-adv-3343] rule permit udp source 10.20.20.0 0.0.0.255 destination-port eq snmp
     ```
     ```
     [*DeviceA-acl-adv-3343] rule deny udp destination-port eq snmp
     [*DeviceA-acl-adv-3343] commit
     ```
   * Add Tacacs to ACL 3344.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Tacacs is a service protocol. Both the Tacacs protocols: TCP-based Huawei enhanced Tacacs and UDP-based standard Tacacs need to be added to the ACL 3344.
     
     ```
     [~DeviceA] acl number 3344
     [*DeviceA-acl-adv-3344] rule permit tcp source 5.5.5.5 0 source-port eq tacacs
     [*DeviceA-acl-adv-3344] rule permit tcp source 6.6.6.6 0 destination-port eq tacacs
     [*DeviceA-acl-adv-3344] rule permit udp source 5.5.5.5 0 source-port eq tacacs-ds
     [*DeviceA-acl-adv-3344] rule permit udp source 6.6.6.6 0 destination-port eq tacacs-ds
     [*DeviceA-acl-adv-3344] quit
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The TACACS source address segment added to the ACL must be confirmed by carriers.
     + ACL rules can be configured based on the source IP address + port number or solely on the port number. ACL rules configured based on the source IP address + port number are more secure, but complicated in information collection. ACL rules configured based solely on the port number are less secure, but easy to configure. Choose either of the preceding methods as needed. A simplified configuration procedure is as follows:
     ```
     acl number 3344 
      rule permit tcp source-port eq tacacs 
      rule permit tcp destination-port eq tacacs   
      rule permit udp source-port eq tacacs-ds 
      rule permit udp destination-port eq tacacs-ds 
     ```
   * Add NTP to ACL 3345.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     NTP is a service protocol, and the port number is 123.
     
     ```
     [~DeviceA] acl number 3345
     [*DeviceA-acl-adv-3345] rule permit udp source 172.16.0.0 0.0.255.255 source-port eq 123 
     [*DeviceA-acl-adv-3345] rule permit udp source 172.16.0.0 0.0.255.255 destination-port eq 123
     [*DeviceA-acl-adv-3345] commit
     [~DeviceA-acl-adv-3345] quit
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The NTP source address segment added to the ACL must be confirmed by carriers.
     + ACL rules can be configured based on the source IP address + port number or solely on the port number. ACL rules configured based on the source IP address + port number are more secure, but complicated in information collection. ACL rules configured based solely on the port number are less secure, but easy to configure. Choose either of the preceding methods as needed. A simplified configuration procedure is as follows:
     ```
     acl number 3345 
      rule permit udp source- port eq 123 
      rule permit udp destination- port eq 123 
     ```
   * Add ICMP and Tracert to ACL 3346.
     ```
     [~DeviceA] acl number 3346
     [*DeviceA-acl-adv-3346] rule permit icmp icmp-type echo
     [*DeviceA-acl-adv-3346] rule permit icmp icmp-type echo-reply
     [*DeviceA-acl-adv-3346] rule permit icmp icmp-type ttl-exceeded
     [*DeviceA-acl-adv-3346] rule permit icmp icmp-type port-unreachable
     [*DeviceA-acl-adv-3346] rule permit icmp icmp-type Fragmentneed-DFset
     [*DeviceA-acl-adv-3346] rule permit icmp
     [*DeviceA-acl-adv-3346] rule permit udp destination-port range 33434 33678
     [*DeviceA-acl-adv-3346] quit
     ```
   * Add Ping-LSP to ACL 3347.
     ```
     [~DeviceA] acl number 3347
     [*DeviceA-acl-adv-3347] rule permit udp destination-port eq 3503
     [*DeviceA-acl-adv-3347] commit
     [~DeviceA-acl-adv-3347] quit
     ```
   * Add unknown protocols to ACL 3348.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If unauthorized protocol packets and attack packets are limited by ACL 3330 to which the blacklist is bound, and authorized protocol packets and packets from the trusted network segments is limited by ACLs from 3331 to 3347, other protocol packets are considered as packets of unknown protocols and limited by ACL 3348. The corresponding user-defined flow configures a best-effort bandwidth for these packets of unknown protocols and sends them to the CPU with low priority.
     
     This configuration is optional. If no ACL is configured to filter packets of unknown protocols, these packets are sent to the CPU from the default channel. Ensure that the system can process authorized service and protocol packets based on the preceding configurations before you configure this ACL and corresponding user-defined flow for packets of unknown protocols.
     
     ```
     [~DeviceA] acl number 3348
     [*DeviceA-acl-adv-3348] rule permit udp
     [*DeviceA-acl-adv-3348] rule permit tcp
     [*DeviceA-acl-adv-3348] rule permit ip
     [*DeviceA-acl-adv-3348] commit
     [~DeviceA-acl-adv-3348] quit
     ```
7. Configure a user-defined flow.
   
   After classifying packets using an ACL, create user-defined flows to direct protocol packets to different channels.
   
   * Configure the action of user-defined flow 1.
     
     User-defined flow 1 uses ACL 3331 to match packets from the trusted network segment that is allowed to access the local device. Set the priority of user-defined flow 1 to high and bandwidth to 1 Mbit/s. The configuration is as follows:
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 1 acl 3331
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 1 cir 1000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 1 high
     ```
   * Configure the action of user-defined flow 2.
     
     User-defined flow 2 uses ACL 3332 to match BGP packets. As BGP is a routing protocol, set the priority to high and bandwidth to 512 kbit/s for user-defined flow 2. In addition, configure the alarm function for user-defined flow 2. The configuration is as follows: You can adjust the threshold for dropping packets and interval for reporting alarms.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 2 acl 3332
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 2 cir 512 cbs 1000000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 2 high
     [*DeviceA-cpu-defend-policy-10] alarm drop-rate user-defined-flow 2 enable
     [*DeviceA-cpu-defend-policy-10] alarm drop-rate user-defined-flow 2 threshold 100 interval 60
     ```
   * Configure the action of user-defined flow 3.
     
     User-defined flow 3 uses ACL 3333 to match LDP packets. Set its priority to high and bandwidth to 512 kbit/s. In addition, configure the alarm function for user-defined flow 3. You can adjust the threshold for dropping packets and interval for reporting alarms.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 3 acl 3333
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 3 cir 512 cbs 1000000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 3 high
     [*DeviceA-cpu-defend-policy-10] alarm drop-rate user-defined-flow 3 enable
     [*DeviceA-cpu-defend-policy-10] alarm drop-rate user-defined-flow 3 threshold 100 interval 60
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     LDP is easy to flap. If more than three LDP packets get lost, LDP may go Down. The attack defense alarm function must be configured.
   * Configure the action of user-defined flow 4.
     
     User-defined flow 4 uses ACL 3334 to match OSPF and RIP packets. Set its priority to high and bandwidth to 1 Mbit/s. In addition, configure the alarm function for user-defined flow 4. You can adjust the threshold for dropping packets and interval for reporting alarms.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 4 acl 3334
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 4 cir 1000 cbs 1000000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 4 high
     [*DeviceA-cpu-defend-policy-10] alarm drop-rate user-defined-flow 4 enable
     [*DeviceA-cpu-defend-policy-10] alarm drop-rate user-defined-flow 4 threshold 100 interval 60
     ```
   * Configure the action of user-defined flow 5.
     
     User-defined flow 5 uses ACL 3335 to match VRRP packets. As VRRP is a reliability protocol, set the priority of user-defined flow 5 to high and the bandwidth to 1.3 Mbit/s. The configuration is as follows:
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 5 acl 3335
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 5 cir 1300 cbs 1000000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 5 high
     ```
   * Configure the action of user-defined flow 6.
     
     User-defined flow 6 uses ACL 3336 to implement rate limit for PIM packets.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 6 acl 3336
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 6 cir 1000 cbs 1000000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 6 high
     ```
   * Configure the action of user-defined flow 7.
     
     User-defined flow 7 uses ACL 3337 to implement rate limit for IGMP packets.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 7 acl 3337
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 7 cir 512 cbs 512000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 7 high
     ```
   * Configure the action of user-defined flow 8.
     
     User-defined flow 8 uses ACL 3338 to implement rate limit for MSDP packets.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 8 acl 3338
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 8 cir 512 cbs 512000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 8 low
     ```
   * Configure the action of user-defined flow 9.
     
     User-defined flow 9 uses ACL 3339 to implement rate limit for packets with the broadcast address. The live network is prone to suffer attacks launched using default reserved multicast addresses. Therefore, reserved multicast addresses are added to an independent ACL. To protect other types of protocol packets, set the CIR of the packets with the default reserved multicast address to 512 kbit/s. The configuration is as follows:
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 9 acl 3339
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 9 cir 512 cbs 40000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 9 high
     ```
   * Configure the action of user-defined flow 10.
     
     User-defined flow 10 uses ACL 3340 to implement rate limit for packets with the broadcast address. The destination IP address is the broadcast address 255.255.255.255. Limit the processing bandwidth to 512 kbit/s and set the priority to low to protect other protocols.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 10 acl 3339
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow cir 512 cbs 20000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 10 low
     ```
   * Configure the action of user-defined flow 11.
     
     User-defined flow 11 uses ACL 3341 to match access protocol packets. Access protocol packets require low bandwidth and have no requirements for real-time transmission. Therefore, set the priority to low for them.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 11 acl 3341
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 11 cir 512 cbs 300000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 11 middle
     ```
   * Configure the action of user-defined flow 12.
     
     User-defined flow 12 uses ACL 3342 to match FTP and TFTP packets. Set the priority to low and the bandwidth to 512 kbit/s or lower. The configuration is as follows:
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 12 acl 3342
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 12 cir 512 cbs 5120
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 12 low
     ```
   * Configure the action of user-defined flow 13.
     
     User-defined flow 13 uses ACL 3343 to match SNMP packets. SNMP traffic is heavy but has low requirements for real-time transmission. Therefore, set the priority to low and bandwidth to 1 Mbit/s. The configuration is as follows:
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 13 acl 3343
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 13 cir 1000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 13 low
     ```
   * Configure the action of user-defined flow 14.
     
     User-defined flow 14 uses ACL 3341 to protect TACACS protocol packets. TACACS traffic is heavy but has low requirements for real-time transmission. Therefore, set the priority to low and bandwidth to 1 Mbit/s. The configuration is as follows:
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 14 acl 3344
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 14 cir 1000 cbs 1000000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 14 low
     ```
   * Configure the action of user-defined flow 15.
     
     User-defined flow 15 uses ACL 3345 to implement rate limit for NTP packets. Set the bandwidth to 150 kbit/s and priority to low.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 15 acl 3345
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 15 cir 150 cbs 15000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 15 low
     ```
   * Configure the action of user-defined flow 16.
     
     User-defined flow 16 uses ACL 3346 to match ICMP packets. ICMP is frequently used in network access. Set the priority to low and bandwidth to 512 kbit/s.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 16 acl 3346
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 16 cir 512 cbs 256000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 16 low
     ```
   * Configure the action of user-defined flow 17.
     
     User-defined flow 17 uses ACL 3347 to match LSP ping packets. Set the CIR to 1 Mbit/s and priority to high.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 17 acl 3347
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 17 cir 1000 cbs 40000 
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 17 high
     ```
   * Configure the action of user-defined flow 18.
     
     User-defined flow 18 uses ACL 3348 to implement rate limit for unknown protocol packets. Before configuring user-defined flow 18, ensure that all services on the device have been filtered using the previous user-defined flows. Otherwise, do not configure user-defined flow 18 and route the unknown protocol packets along the specific channel.
     
     ```
     [*DeviceA-cpu-defend-policy-10] user-defined-flow 18 acl 3348
     [*DeviceA-cpu-defend-policy-10] car user-defined-flow 18 cir 512 cbs 1000000
     [*DeviceA-cpu-defend-policy-10] priority user-defined-flow 18 low
     [*DeviceA-cpu-defend-policy-10] commit
     ```
8. Apply an attack defense policy.
   ```
   [~DeviceA] slot 1
   [*DeviceA-slot-1] cpu-defend-policy 10
   [*DeviceA-slot-1] commit
   [~DeviceA-slot-1] quit
   ```

#### Configuration Files

```
#
 sysname DeviceA
#
cpu-defend policy 10
 blacklist acl 3330
 user-defined-flow 1 acl 3331
 user-defined-flow 2 acl 3332
 user-defined-flow 3 acl 3333
 user-defined-flow 4 acl 3334
 user-defined-flow 5 acl 3335
 user-defined-flow 6 acl 3336
 user-defined-flow 7 acl 3337
 user-defined-flow 8 acl 3338
 user-defined-flow 9 acl 3339
 user-defined-flow 10 acl 3340
 user-defined-flow 11 acl 3341
 user-defined-flow 12 acl 3342
 user-defined-flow 13 acl 3343
 user-defined-flow 14 acl 3344
 user-defined-flow 15 acl 3345
 user-defined-flow 16 acl 3346
 user-defined-flow 17 acl 3347
 user-defined-flow 18 acl 3348
 alarm drop-rate user-defined-flow 2 threshold 100 interval 60
 alarm drop-rate user-defined-flow 3 threshold 100 interval 60
 alarm drop-rate user-defined-flow 4 threshold 100 interval 60
 car blacklist cir 0
 car user-defined-flow 1 cir 1000
 car user-defined-flow 2 cir 512 cbs 1000000
 car user-defined-flow 3 cir 512 cbs 1000000
 car user-defined-flow 4 cir 1000 cbs 1000000
 car user-defined-flow 5 cir 1300 cbs 1000000
 car user-defined-flow 6 cir 1000 cbs 1000000
 car user-defined-flow 7 cir 512 cbs 512000
 car user-defined-flow 8 cir 512 cbs 5120
 car user-defined-flow 9 cir 512 cbs 40000
 car user-defined-flow 10 cir 512
 car user-defined-flow 11 cir 512 cbs 300000
 car user-defined-flow 12 cir 512 cbs 5120
 car user-defined-flow 13 cir 1000
 car user-defined-flow 14 cir 1000 cbs 1000000
 car user-defined-flow 15 cir 150 cbs 15000
 car user-defined-flow 16 cir 512 cbs 256000
 car user-defined-flow 17 cir 1000 cbs 40000
 car user-defined-flow 18 cir 512 cbs 1000000
 priority user-defined-flow 1 high
 priority user-defined-flow 2 high
 priority user-defined-flow 3 high
 priority user-defined-flow 4 high
 priority user-defined-flow 5 high
 priority user-defined-flow 6 high
 priority user-defined-flow 7 high
 priority user-defined-flow 8 low
 priority user-defined-flow 9 high
 priority user-defined-flow 10 low
 priority user-defined-flow 11 middle
 priority user-defined-flow 12 low
 priority user-defined-flow 13 low
 priority user-defined-flow 14 low
 priority user-defined-flow 15 low
 priority user-defined-flow 16 low
 priority user-defined-flow 17 high
 priority user-defined-flow 18 low
 process-sequence tcpsyn-flood fragment-flood dynamic-link-protection management-acl whitelist user-defined-flow blacklist
#
#
acl number 3330
 rule 5 deny ip source 10.1.1.0 0.0.0.255
#
acl number 3331
 rule 5 permit ip source 10.1.2.0 0.0.0.255
 rule 10 permit ip source 10.1.3.0 0.0.0.255
#
acl number 3332
 rule 5 permit tcp  source 10.12.1.0 0.0.0.255 destination-port eq bgp
 rule 10 permit tcp  source 10.12.1.0 0.0.0.255 source-port eq bgp

#
acl number 3333
 rule 5 permit udp source 11.11.11.1 0 destination-port eq 646
 rule 10 permit udp source 11.11.11.1 0 source-port eq 646
 rule 15 permit tcp source 1.1.1.32 0 destination-port eq 646
 rule 20 permit tcp source 1.1.1.32 0 source-port eq 646
#
acl number 3334
 rule 5 permit ospf
#
acl number 3335
 rule 5 permit 112 source 11.11.11.100 0
#
acl number 3336
 rule 5 permit 103
#
acl number 3337
 rule 5 permit igmp
#
acl number 3338
 rule 5 permit udp destination-port eq 639
 rule 10 permit udp source-port eq 639
 rule 15 permit tcp destination-port eq 639
 rule 20 permit tcp source-port eq 639
#
acl number 3339
 rule 5 permit ip destination 224.0.0.0 0.0.0.255
#
acl number 3340
 rule 5 permit ip destination 255.255.255.255 0
#
acl number 3341
 rule 5 permit tcp source 192.168.1.0 0.0.0.255 source-port eq telnet
 rule 10 permit tcp source 192.168.1.0 0.0.0.255 destination-port eq telnet
 rule 15 permit tcp source 192.168.1.0 0.0.0.255 source-port eq 22
 rule 20 permit tcp source 192.168.1.0 0.0.0.255 destination-port eq 22
 rule 100 deny tcp destination-port eq telnet
 rule 105 deny tcp destination-port eq 22
#
acl number 3342
 rule 5 permit udp source 192.168.1.0 0.0.0.255 destination-port eq tftp
 rule 10 permit tcp source 192.168.1.0 0.0.0.255 source-port eq ftp
 rule 15 permit tcp source 192.168.1.0 0.0.0.255 destination-port eq ftp
#
acl number 3343
 rule 5 permit udp source 10.20.20.0 0.0.0.255 source-port eq snmp
 rule 10 permit udp source 10.20.20.0 0.0.0.255 destination-port eq snmp
 rule 100 deny udp destination-port eq snmp
#
acl number 3344
 rule 5 permit tcp source 5.5.5.5 0 source-port eq tacacs
 rule 10 permit tcp source 6.6.6.6 0 destination-port eq tacacs
 rule 15 permit udp source 5.5.5.5 0 source-port eq tacacs-ds
 rule 20 permit udp source 6.6.6.6 0 destination-port eq tacacs-ds
#
acl number 3345
 rule 5 permit udp source 172.16.0.0 0.0.255.255 source-port eq ntp
 rule 10 permit udp source 172.16.0.0 0.0.255.255 destination-port eq ntp
#
acl number 3346
 rule 5 permit icmp icmp-type echo
 rule 10 permit icmp icmp-type echo-reply
 rule 15 permit icmp icmp-type ttl-exceeded
 rule 20 permit icmp icmp-type port-unreachable
 rule 25 permit icmp icmp-type fragmentneed-DFset
 rule 30 permit icmp
 rule 35 permit udp destination-port range 33434 33678
#
acl number 3347
 rule 5 permit udp destination-port eq 3503
#
acl number 3348
 rule 5 permit udp
 rule 10 permit tcp
 rule 15 permit ip
#
slot 1
 cpu-defend-policy 10
#
return
```

#### Verifying the Security Hardening Result

* Run the **display cpu-defend policy** *policy-number* command to check the ACL rules for filtering packets to be sent to the CPU.
* Run the **display cpu-defend car** { **blacklist** | **index** *index* | *protocol* | **user-defined-flow** *flow-id* | **whitelist** } **statistics** [ **slot** *slot-id* ] command to check statistics about the packets dropped by CAR.