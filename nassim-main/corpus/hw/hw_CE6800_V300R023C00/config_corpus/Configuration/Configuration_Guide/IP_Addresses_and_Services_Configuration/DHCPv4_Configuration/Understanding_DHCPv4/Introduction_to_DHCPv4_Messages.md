Introduction to DHCPv4 Messages
===============================

Introduction to DHCPv4 Messages

#### DHCPv4 Message Types

A DHCPv4 server and client communicate through DHCPv4 messages, which are transmitted using the User Datagram Protocol (UDP). A DHCPv4 client sends messages to a DHCPv4 server through UDP port 68, and a DHCPv4 server sends messages to a DHCPv4 client through UDP port 67. The following table describes DHCPv4 message types.

**Table 1** DHCPv4 message types
| Message Name | Description |
| --- | --- |
| DHCPDISCOVER | A DHCPDISCOVER message is broadcast by a DHCPv4 client to locate a DHCPv4 server when the client attempts to connect to a network for the first time. |
| DHCPOFFER | A DHCPOFFER message is sent by a DHCPv4 server to respond to a DHCPDISCOVER message. |
| DHCPREQUEST | A DHCPREQUEST message is sent in the following scenarios:   * After a DHCPv4 client starts, it broadcasts a DHCPREQUEST message to respond to a DHCPOFFER message sent by a DHCPv4 server. * After a DHCPv4 client restarts, it broadcasts a DHCPREQUEST message to confirm the configuration including the previously allocated IPv4 address. * After a DHCPv4 client obtains an IPv4 address, it unicasts or broadcasts a DHCPREQUEST message to renew the IPv4 address lease. |
| DHCPACK | A DHCPACK message is sent by a DHCPv4 server to acknowledge a DHCPREQUEST message from a DHCPv4 client. After receiving a DHCPACK message, the DHCPv4 client obtains the configuration parameters including the IPv4 address. |
| DHCPNAK | A DHCPNAK message is sent by a DHCPv4 server to reject a DHCPREQUEST message from a DHCPv4 client. For example, if a DHCPv4 server cannot find matching lease records after receiving a DHCPREQUEST message, it sends a DHCPNAK message to notify the DHCPv4 client that no IPv4 address is available. |
| DHCPDECLINE | A DHCPDECLINE message is sent by a DHCPv4 client to notify a DHCPv4 server that the allocated IPv4 address conflicts with another IPv4 address. The DHCPv4 client then applies to the DHCPv4 server for another IPv4 address. |
| DHCPRELEASE | A DHCPRELEASE message is sent by a DHCPv4 client to release its IPv4 address. After receiving a DHCPRELEASE message, a DHCPv4 server can allocate this IPv4 address to another DHCPv4 client. |
| DHCPINFORM | A DHCPINFORM message is sent by a DHCPv4 client to obtain other network configuration parameters such as the gateway address and DNS server address after the client has obtained an IPv4 address. |



#### DHCPv4 Message Format

The DHCPv4 message format is developed based on the BOOTP message format. Therefore, a DHCPv4 server can also interact with a BOOTP client.

[Figure 1](#EN-US_CONCEPT_0000001564006389__fig_dc_cfg_dhcp_600501) shows the DHCPv4 message format. The number in the brackets indicates the field length, in octets. [Table 2](#EN-US_CONCEPT_0000001564006389__tab_dc_cfg_dhcp_600502) describes each field in a DHCPv4 message.

**Figure 1** DHCPv4 message format  
![](figure/en-us_image_0000001564006429.png)  

**Table 2** Description of each field in a DHCPv4 message
| Field | Length | Description |
| --- | --- | --- |
| op | 1 octet | Message type:  * 1: BOOTREQUEST * 2: BOOTREPLY |
| htype | 1 octet | Hardware type. The most common value is 1, indicating an Ethernet. |
| hlen | 1 octet | Hardware address length. For an Ethernet address, the value of this field is 6. |
| hops | 1 octet | Number of DHCPv4 relay agents that have relayed a DHCPv4 message. This field is set to 0 by a DHCPv4 client or server. Its value increases by 1 each time the message passes through a DHCPv4 relay agent. This field limits the number of DHCPv4 relay agents that a DHCPv4 message can pass through. A maximum of 16 DHCPv4 relay agents are allowed between a DHCPv4 server and client. If the value of hops is greater than 16, DHCPv4 messages are discarded. |
| xid | 4 octets | Random number chosen by a DHCPv4 client, used by the client and server to associate messages and responses between them. |
| secs | 2 octets | Seconds elapsed since a DHCPv4 client obtained or renewed an IPv4 address. |
| flags | 2 octets | Flags field. Only the leftmost bit in this field is valid and other bits are set to 0. The leftmost bit determines whether a DHCPv4 server unicasts or broadcasts a reply message. Options for this field are as follows:  * 0: The DHCPv4 server unicasts a reply message. * 1: The DHCPv4 server broadcasts a reply message. |
| ciaddr | 4 octets | Client IPv4 address. The IPv4 address can be an existing IPv4 address of a DHCPv4 client or an IPv4 address allocated by a DHCPv4 server to a DHCPv4 client. During initialization, the client has no IPv4 address, and the value of this field is 0.0.0.0.  The IPv4 address 0.0.0.0 is only used by a DHCPv4-enabled device to temporarily communicate with other devices during startup. It is an invalid destination address. |
| yiaddr | 4 octets | IPv4 address that a DHCPv4 server assigns to a DHCPv4 client. The DHCPv4 server fills this field into a DHCPv4 reply message. |
| siaddr | 4 octets | IPv4 address of a server from which a DHCPv4 client obtains the boot file. |
| giaddr | 4 octets | IPv4 address of the first DHCPv4 relay agent. If a DHCPv4 server and client are located on different network segments, the first DHCPv4 relay agent fills its own IPv4 address into this field of a DHCPv4 request message and forwards the message to the DHCPv4 server. The DHCPv4 server determines the network segment where the client resides based on the giaddr field, and allocates an IPv4 address on this network segment to the client.  The DHCPv4 server also returns a reply message to the first DHCPv4 relay agent based on the giaddr field. The DHCPv4 relay agent then forwards the message to the client.  If the DHCPv4 request message passes through multiple DHCPv4 relay agents before reaching the DHCPv4 server, the value of this field is the IPv4 address of the first DHCPv4 relay agent and remains unchanged. However, the value of the hops field increases by 1 each time the DHCPv4 request message passes through a DHCPv4 relay agent. |
| chaddr | 16 octets | Client MAC address. This field must be consistent with the htype and hlen fields. When sending a DHCPv4 request message, the client fills its hardware address in this field. For an Ethernet, a 6-octet Ethernet MAC address must be filled in this field when the htype and hlen fields are set to 1 and 6, respectively. |
| sname | 64 octets | Name of the server from which a client obtains the configuration. This field is optional and is filled in by a DHCPv4 server. This field must be filled in with a character string that ends with 0. |
| file | 128 octets | Boot file name specified by the DHCPv4 server for a DHCPv4 client. The DHCPv4 server fills this field and delivers it together with an IPv4 address to the client. This field is optional and must be filled in with a character string that ends with 0. |
| options | Variable | DHCPv4 options field, which has a maximum of 312 octets. This field contains the DHCPv4 message type and configuration parameters allocated by a DHCPv4 server to a client. The configuration parameters include the gateway IPv4 address, DNS server IPv4 address, and IPv4 address lease.  For details about the options field, see [Options Field in a DHCPv4 Message](#EN-US_CONCEPT_0000001564006389__option). |



#### Options Field in a DHCPv4 Message

The options field is located at the end of a DHCPv4 message and is used to store the control information and parameters allocated to a DHCPv4 client. As shown in [Figure 2](#EN-US_CONCEPT_0000001564006389__fig_dc_cfg_dhcp_600502), the options field consists of three parts: Type, Length, and Value. [Table 3](#EN-US_CONCEPT_0000001564006389__tab_dc_cfg_dhcp_600503) describes the three parts.

**Figure 2** Format of the options field  
![](figure/en-us_image_0000001512687042.png)  

**Table 3** Description of the options field
| Option | Length | Description |
| --- | --- | --- |
| Type | 1 octet | Information type |
| Length | 1 octet | Length of the information content |
| Value | Depending on the Length option | Information content |

The value of the DHCPv4 options field ranges from 1 to 255. DHCPv4 options include predefined and user-defined options. [Table 4](#EN-US_CONCEPT_0000001564006389__tab_01) describes some predefined DHCPv4 options.

**Table 4** Description of DHCPv4 options
| Option No. | Description |
| --- | --- |
| 1 | Subnet mask. |
| 3 | Gateway address. |
| 4 | Time server address. |
| 6 | DNS server address. |
| 7 | Log server address. |
| 12 | DHCPv4 client's hostname. |
| 15 | Domain name suffix. |
| 17 | Root path. |
| 28 | Multicast address. |
| 33 | Static route. After a DHCPv4 client receives DHCPv4 messages with this option, it adds the classful static routes contained in the option to its routing table. In classful routes, destination address masks are natural masks and cannot be used for subnetting. If Option 121 exists, Option 33 is ignored. |
| 42 | NTP server address. |
| 43 | Vendor-specific information. |
| 44 | NetBIOS name server. |
| 46 | NetBIOS node type. |
| 50 | Requested IPv4 address. |
| 51 | IPv4 address lease. |
| 52 | Additional option. |
| 53 | DHCPv4 message type. |
| 54 | Server identification. |
| 55 | Parameter request list. A DHCPv4 client uses this option to request specified configuration parameters from a DHCPv4 server. The content of this option is the option values corresponding to the parameters requested by the client. |
| 56 | Message option, which is used to describe the reason why an IP address fails to be allocated. DHCPv4 messages encapsulated with this option are as follows:  * DHCPNAK message sent by a DHCPv4 server. * DHCPDECLINE or DHCPRELEASE message sent by a DHCPv4 client. * DHCPDECLINE message sent by a DHCPv4 relay agent when an IPv4 address conflict is detected or DHCPRELEASE message sent by a DHCPv4 client to release its IPv4 address. * DHCPRELEASE message sent by a DHCP snooping device to release its IPv4 address. |
| 58 | Lease renewal time (T1), which is 50% of the lease. |
| 59 | Lease renewal time (T2), which is 87.5% of the lease. |
| 60 | Vendor category, which identifies the DHCPv4 client type and configuration. |
| 61 | Client identifier. |
| 66 | TFTP server name allocated to DHCPv4 clients. |
| 67 | Boot file name allocated to a DHCPv4 client. |
| 77 | User type. |
| 120 | SIP server IPv4 address.  NOTE:  Currently, only IPv4 addresses can be parsed and domain names cannot be parsed. |
| 121 | Classless route option. This option contains a group of classless static routes. After a DHCPv4 client receives DHCPv4 messages with this option, it adds the classless static routes contained in the option to its routing table. In classless routes, destination address masks can be any value and can be used for subnetting.  NOTE:  A device functioning as a DHCPv4 client can receive static routes delivered from a DHCPv4 server through Option 121. |
| 129 | Call server address. |
| 143 | BootStrap server address list. |
| 148 | Syslog port number information. |
| 150 | Host name of the file server. |
| 184 | Reserved option. You can customize information carried in this option. |

In addition to predefined options, a device supports user-defined options to connect to different terminals, such as IP phones.

* Vendor-specific information option (Option 43)
  
  [Figure 3](#EN-US_CONCEPT_0000001564006389__fig_dc_fd_dhcp_000602) shows the format of Option 43.
  
  **Figure 3** Format of Option 43  
  ![](figure/en-us_image_0000001512846630.png)  
  
  DHCPv4 servers and clients use Option 43 to exchange vendor-specific information.
  
  + When a DHCPv4 server receives a DHCPv4 request message with parameter 43 encapsulated in Option 55, it encapsulates Option 43 in a reply message and sends the message to the DHCPv4 client.
    
    When a device functions as the DHCPv4 server, it can deliver the AC's IPv4 address to connected APs (Huawei devices), facilitating the connection setup between the AC and APs.Option 43 supports suboptions, as shown in [Figure 3](#EN-US_CONCEPT_0000001564006389__fig_dc_fd_dhcp_000602).
  + Sub-option type: type of the suboption. When the device delivers the AC's IPv4 address to APs, the value can be 0x01 (hexadecimal type), 0x02 (IPv4 address type), or 0x03 (ASCII code type).
  + Sub-option length: length of the suboption.
  + Sub-option value: value of the suboption.
* Relay agent information option (Option 82)
  
  Option 82 records the location of a DHCPv4 client. A DHCPv4 relay agent appends Option 82 to a DHCPv4 request message sent from a DHCPv4 client and forwards the message to a DHCPv4 server.
  
  An administrator can use Option 82 to locate a DHCPv4 client and control the security and accounting of the DHCPv4 client. A DHCPv4 server that supports Option 82 can determine policies to flexibly allocate IPv4 addresses and other parameters based on the information in this option.
  
  Option 82 contains a maximum of 254 suboptions. If Option 82 is defined, at least one suboption must be defined.