display traffic-analysis tcp cache
==================================

display traffic-analysis tcp cache

Function
--------



The **display traffic-analysis tcp cache** command displays detailed information about intelligent traffic analysis results for TCP flows.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-analysis tcp ipv4 cache** [ [ **client** **ip** *cip* | **client** **vni** *cvniid* | **client** **port** *cport* | { **client** **interface** *cifname* | **client** **interface** *ciftype* *interface-number* } | **server** **ip** *sip* | **server** **vni** *svniid* | **server** **port** *sport* | { **server** **interface** *sifname* | **server** **interface** *siftype* *interface-number* } ] \* ] **slot** *slot-id*

**display traffic-analysis tcp ipv6 cache** [ [ **client** **ipv6** *cip-v6-address* | **client** **vni** *cvniid* | **client** **port** *cport* | { **client** **interface** *cifname* | **client** **interface** *ciftype* *interface-number* } | **server** **ipv6** *sip-v6-address* | **server** **vni** *svniid* | **server** **port** *sport* | { **server** **interface** *sifname* | **server** **interface** *siftype* *interface-number* } ] \* ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **client** | Specifies a client. | - |
| **ip** *cip* | Specifies the IP address of a client. | The value is in dotted decimal notation. |
| **ip** *sip* | Specifies the IP address of a server. | The value is in dotted decimal notation. |
| **vni** | Specifies a VXLAN Network Identifier (VNI). | - |
| *cvniid* | Specifies the VNI of a client. | The value is an integer that ranges from 1 to 16777215. |
| **port** | Specifies the interface number. | - |
| *cport* | Specifies the port number of a client. | The value is an integer. The value ranges from 0 to 65535. |
| **interface** | Specifies an interface. | - |
| *cifname* | Specifies the interface name on a client. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| *ciftype* | Specifies the interface type on a client. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| *interface-number* | Specifies the interface index. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **server** | Specifies a server. | - |
| *svniid* | Specifies the VNI of a server. | The value is an integer that ranges from 1 to 16777215. |
| *sport* | Specifies the port number of a server. | The value is an integer. The value ranges from 0 to 65535. |
| *sifname* | Specifies the interface name on a server. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| *siftype* | Specifies the interface type on a server. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **slot** | Specifies a slot ID. | - |
| *slot-id* | Specifies the ID of a device. | The value must be set according to the device configuration. |
| **ipv6** *cip-v6-address* | Specify traffic analysis client IPv6. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv6** *sip-v6-address* | Specify traffic analysis server IPv6. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv6** | Displays the IPv6 flow table. | - |
| **ipv4** | Displays the IPv4 flow table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view detailed information about intelligent traffic analysis results for TCP flows on a switch in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed information about intelligent traffic analysis results for TCP flows on a switch.
```
<HUAWEI> display traffic-analysis tcp  ipv4 cache slot 1
NOTE:  S2C: server to client  C2S: client to server                                                                                 
Traffic analysis cache information:                                                                                                 
-------------------------------------------------------------------------------                                                     
ClientIP            ClientPort          C2S Interface1      C2S Interface2                                                          
ServerIP            ServerPort          S2C Interface1      S2C Interface2                                                          
C2S RTT             C2S Packets         C2S PacketLossUp    C2S PacketLoss                                                          
S2C RTT             S2C Packets         S2C PacketLossUp    S2C PacketLoss                                                          
C2S Vni             S2C Vni             FlowStatus          Time                                                                    
-------------------------------------------------------------------------------  
10.1.1.1            1024                Eth-Trunk10         Eth-Trunk1                                                                
10.1.2.1            24                  --                  --                                                                      
0                   48331               0                   1                                                                   
0                   7788                0                   0                                                                       
--                  --                  ESTABLISH           2019-06-05 19:58:28
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-analysis tcp cache** command output
| Item | Description |
| --- | --- |
| ClientIP | Client's IP address. |
| ClientPort | Port number of a client. |
| C2S Interface1 | Inbound interface 1 on which statistics about the TCP packets from the client to the server are collected. |
| C2S Interface2 | Inbound interface 2 on which statistics about the TCP packets from the client to the server are collected. If a flow does not enter the local device from another interface, the parameter value is --. |
| C2S Vni | VNI of inner TCP packets encapsulated in VXLAN packets from the client to the server. |
| C2S RTT | RTT of TCP packets from the client to the server. |
| C2S Packets | Number of TCP packets sent from the client to the server. |
| C2S PacketLossUp | Number of TCP packets discarded on the upstream device when packets are sent from the client to the server. |
| C2S PacketLoss | Total number of TCP packets that are discarded when they are sent from the client to the server. |
| ServerIP | IP address of a server. |
| ServerPort | Port number of a server. |
| S2C Interface1 | Inbound interface 1 on which statistics about the TCP packets from the server to the client are collected. |
| S2C Interface2 | Inbound interface 2 on which statistics about the TCP packets from the server to the client are collected. If a flow does not enter the local device from another interface, the parameter value is --. |
| S2C Packets | Number of TCP packets sent from the server to the client. |
| S2C PacketLossUp | Number of TCP packets discarded on the upstream device when packets are sent from the server to the client. |
| S2C PacketLoss | Total number of TCP packets that are discarded when they are sent from the server to the client. |
| S2C Vni | VNI of inner TCP packets encapsulated in VXLAN packets from the server to the client. |
| FlowStatus | Flow status of the current TCP flow table. The values are as follows:  -SYN.  -SYN&ACK.  -ACK.  -ESTABLISH: TCP connection has been established.  -FIN/RST: TCP connection has been terminated. |
| Time | Time when a flow is created. |