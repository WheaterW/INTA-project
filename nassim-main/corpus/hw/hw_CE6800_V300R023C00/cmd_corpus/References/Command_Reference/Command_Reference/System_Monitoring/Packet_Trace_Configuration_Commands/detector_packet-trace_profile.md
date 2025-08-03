detector packet-trace profile
=============================

detector packet-trace profile

Function
--------



The **detector packet-trace profile** command configures a packet trace profile.

The **undo detector packet-trace profile** command deletes a packet trace profile.



By default, no packet trace profile is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**detector packet-trace profile** *profile-name* **packet** *packet-value*

**detector packet-trace profile** *profile-name* **source-mac** *source-mac-address* **destination-mac** *destination-mac-address* [ **vlan** *vlan-id* [ **8021p** *8021p-value* ] ] **source-ip** *source-ip-address* **destination-ip** *destination-ip-address* [ **dscp** *dscp-value* ] [ **ttl** *ttl-value* ] **tcp** **source-port** *source-port* **destination-port** *destination-port* [ **payload** *tcp-payload-value* ]

**detector packet-trace profile** *profile-name* **source-mac** *source-mac-address* **destination-mac** *destination-mac-address* [ **vlan** *vlan-id* [ **8021p** *8021p-value* ] ] **source-ip** *source-ip-address* **destination-ip** *destination-ip-address* [ **dscp** *dscp-value* ] [ **ttl** *ttl-value* ] **udp** **source-port** *source-port* **destination-port** *destination-port* [ **payload** *udp-payload-value* ]

**detector packet-trace profile** *profile-name* **source-mac** *source-mac-address* **destination-mac** *destination-mac-address* [ **vlan** *vlan-id* [ **8021p** *8021p-value* ] ] **source-ip** *source-ip-address* **destination-ip** *destination-ip-address* [ **dscp** *dscp-value* ] [ **ttl** *ttl-value* ] **icmp** **icmp-type** *icmp-type-value* **icmp-code** *icmp-code-value* [ **payload** *icmp-payload-value* ]

**undo detector packet-trace profile** *profile-name* [ **packet** *packet-value* ]

**undo detector packet-trace profile** *profile-name* **source-mac** *source-mac-address* **destination-mac** *destination-mac-address* [ **vlan** *vlan-id* [ **8021p** *8021p-value* ] ] **source-ip** *source-ip-address* **destination-ip** *destination-ip-address* [ **dscp** *dscp-value* ] [ **ttl** *ttl-value* ] **tcp** **source-port** *source-port* **destination-port** *destination-port* [ **payload** *tcp-payload-value* ]

**undo detector packet-trace profile** *profile-name* **source-mac** *source-mac-address* **destination-mac** *destination-mac-address* [ **vlan** *vlan-id* [ **8021p** *8021p-value* ] ] **source-ip** *source-ip-address* **destination-ip** *destination-ip-address* [ **dscp** *dscp-value* ] [ **ttl** *ttl-value* ] **udp** **source-port** *source-port* **destination-port** *destination-port* [ **payload** *udp-payload-value* ]

**undo detector packet-trace profile** *profile-name* **source-mac** *source-mac-address* **destination-mac** *destination-mac-address* [ **vlan** *vlan-id* [ **8021p** *8021p-value* ] ] **source-ip** *source-ip-address* **destination-ip** *destination-ip-address* [ **dscp** *dscp-value* ] [ **ttl** *ttl-value* ] **icmp** **icmp-type** *icmp-type-value* **icmp-code** *icmp-code-value* [ **payload** *icmp-payload-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a packet trace profile. | The value is a string of 1 to 31 case-sensitive characters. It cannot start with underline (\_) or contain > $ \* ^ |, and spaces. |
| **packet** *packet-value* | Specifies the content of the detection packet. | When the content of a detection packet is specified, the value of packet-value is a string of 64 to 512 characters. The value is in hexadecimal notation and its length must be 2n (n = 32, 33, 34, ..., 256). The payload length ranges from 64 bytes to 512 bytes. |
| **source-mac** *source-mac-address* | Specifies the source MAC address. | The value is in the H-H-H format. H is a hexadecimal number that contains 1-4 digits, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **destination-mac** *destination-mac-address* | Specifies the destination MAC address of the detection packet. | The value is in the H-H-H format. H is a hexadecimal number that contains 1-4 digits, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **vlan** *vlan-id* | Indicates the VLAN ID of the detection packet. | For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **8021p** *8021p-value* | Specifies the 802.1p priority of the detection packet. | The value is an integer ranging from 0 to 7. The default value is 0. |
| **source-ip** *source-ip-address* | Specifies the source IP address of the detection packet. | The value is in dotted decimal notation. |
| **destination-ip** *destination-ip-address* | Specifies the destination IP address of the detection packet. | The value is in dotted decimal notation. |
| **dscp** *dscp-value* | Specifies the DSCP field of the detection packet. | The value is an integer ranging from 0 to 63. The default value is 0. |
| **ttl** *ttl-value* | Specifies the TTL of the detection packet. | The value is an integer ranging from 1 to 255. The default value is 255. |
| **tcp** | Indicates that the detection packet is a TCP packet. | - |
| **source-port** *source-port* | Specifies the source port number of the detection packet, which is a TCP or UDP packet. | The value is an integer that ranges from 0 to 65535. |
| **destination-port** *destination-port* | Specifies the destination port number of the detection packet, which is a TCP or UDP packet. | The value is an integer that ranges from 0 to 65535. |
| **payload** | Specifies the payload of the detection packet. | - |
| *tcp-payload-value* | Specifies the payload when the detection packet is a TCP packet. | When the detection packet is a TCP packet, the value of payload-value is a string of 20 to 908 characters. The value is in hexadecimal notation and its length must be 2n (n = 10, 11, 12, ..., 454). The payload length ranges from 10 bytes to 454 bytes. If this parameter is not specified, the value 00000000000000000000 is used. |
| **udp** | Indicates that the detection packet is a UDP packet. | - |
| *udp-payload-value* | Specifies the payload when the detection packet is a UDP packet. | When the detection packet is a UDP packet, the value of payload-value is a string of 44 to 932 characters. The value is in hexadecimal notation and its length must be 2n (n = 22, 23, 24, ..., 466). The payload length ranges from 22 bytes to 466 bytes. If this parameter is not specified, the value 00000000000000000000000000000000000000000000 is used. |
| **icmp** | Specifies that the detection packet is an ICMP packet. | - |
| **icmp-type** *icmp-type-value* | Specifies the ICMP type when the detection packet is an ICMP packet. | The value is an integer that ranges from 0 to 255. |
| **icmp-code** *icmp-code-value* | Specifies the ICMP code when the detection packet is an ICMP packet. | The value is an integer that ranges from 0 to 255. |
| *icmp-payload-value* | Specifies the payload when the detection packet is an ICMP packet. | When the detection packet is an ICMP packet, the value of payload-value is a string of 52 to 940 characters. The value is in hexadecimal notation and its length must be 2n (n = 26, 27, 28, ..., 470). The payload length ranges from 26 bytes to 470 bytes. If this parameter is not specified, the value 0000000000000000000000000000000000000000000000000000 is used. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To detect the forwarding result and forwarding path of packets of certain type on a physical interface, run the detector packet-trace profile command to configure a detection packet template and bind the template to the physical interface.


Example
-------

# Configure a packet trace profile tcp\_test and set the detection packet type to TCP.
```
<HUAWEI> system-view
[~HUAWEI] detector packet-trace profile tcp_test source-mac 00e0-fc12-3456 destination-mac 00e0-fc56-7890 vlan 100 8021p 1 source-ip 10.1.1.1 destination-ip 10.1.1.2 dscp 23 ttl 10 tcp source-port 20 destination-port 30 payload 0efc00020001104488386500810060368906000000000000000000000000002e2302000100fffffc01980000000000000000

```

# Configure a packet trace profile udp\_test and set the detection packet type to UDP.
```
<HUAWEI> system-view
[~HUAWEI] detector packet-trace profile udp_test source-mac 00e0-fc12-3456 destination-mac 00e0-fc56-7890 vlan 100 8021p 1 source-ip 10.1.1.1 destination-ip 10.1.1.2 dscp 23 ttl 10 udp source-port 20 destination-port 30 payload 0efc00020001104488386500810060368906000000000000000000000000002e2302000100fffffc019800000000000000

```

# Configure a packet trace profile icmp\_test and set the detection packet type to ICMP.
```
<HUAWEI> system-view
[~HUAWEI] detector packet-trace profile icmp_test source-mac 00e0-fc12-3456 destination-mac 00e0-fc56-7890 vlan 100 8021p 1 source-ip 10.1.1.1 destination-ip 10.1.1.2 dscp 23 ttl 10 icmp icmp-type 18 icmp-code 0 payload 0efc00020001104488386500810060368906000000000000000000000000002e2302000100fffffc01980000000000000000

```

# Configure a packet trace profile packet\_test and specify the content packet packet-value.
```
<HUAWEI> system-view
[~HUAWEI] detector packet-trace profile packet_test packet 0efc00020001104488386500810060368906000000000000000000000000002e2302000100fffffc0198000000000000000b001400000000020000002020000f8000084000010000000007d0200b10448838650020001044883865000000000000000000000000000000000088000000000008400001000100010000880000000000084000010001000100000000000000000000000000000000000000000000000000000000000000000000973d5e8f42000000

```

# Delete a specified packet trace profile.
```
<HUAWEI> system-view
[~HUAWEI] undo detector packet-trace profile packet_test

```

# Delete specified TCP, UDP, and ICMP packet trace profiles.
```
<HUAWEI> system-view
[~HUAWEI] undo detector packet-trace profile tcp_test source-mac 00e0-fc12-3456 destination-mac 00e0-fc56-7890 vlan 100 8021p 1 source-ip 10.1.1.1 destination-ip 10.1.1.2 dscp 23 ttl 10 tcp source-port 20 destination-port 30 payload 0efc00020001104488386500810060368906000000000000000000000000002e2302000100fffffc01980000000000000000
[~HUAWEI] undo detector packet-trace profile udp_test source-mac 00e0-fc12-3456 destination-mac 00e0-fc56-7890 vlan 100 8021p 1 source-ip 10.1.1.1 destination-ip 10.1.1.2 dscp 23 ttl 10 udp source-port 20 destination-port 30 payload 0efc00020001104488386500810060368906000000000000000000000000002e2302000100fffffc019800000000000000
[~HUAWEI] undo detector packet-trace profile icmp_test source-mac 00e0-fc12-3456 destination-mac 00e0-fc56-7890 vlan 100 8021p 1 source-ip 10.1.1.1 destination-ip 10.1.1.2 dscp 23 ttl 10 icmp icmp-type 18 icmp-code 0 payload 0efc00020001104488386500810060368906000000000000000000000000002e2302000100fffffc01980000000000000000

```