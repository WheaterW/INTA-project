display capture-packet file
===========================

display capture-packet file

Function
--------



The **display capture-packet file** command displays the content of a specified file for storing obtained packets.




Format
------

**display capture-packet file** *filename* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filename* | Specifies the name of the file for storing obtained packets. | The value is a string of 5 to 255 case-sensitive characters, spaces not supported. |
| **verbose** | Displays detailed information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the device is configured to remotely obtain packets, you can analyze the obtained packets to check whether the data is correct and locate data problems. You do not need to download the files for storing obtained packets. Instead, you can run this command to view the content of the files.The content of the packet header obtaining file is displayed in the command output as a hexadecimal character string. You can convert the content into a binary file and use the Wireshark to view the packet information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the instance named capture.cap.
```
<HUAWEI> display capture-packet file flash:/logfile/capture.cap

28 6E D4 89 D4 BD D4 94 E8 59 12 33 08 00 45 28
00 34 6E 7C 40 00 3A 06 9A A7 0A 03 BA 25 0A 78
68 D8 01 BB 99 3C 34 77 47 91 7F 73 9C 4B 80 10
00 3D 9D 26 00 00 01 01 08 0A 3D BE 55 1F 13 40
C9 04

28 6E D4 89 D4 BD D4 94 E8 59 12 33 08 00 45 28
00 9F 6E 7D 40 00 3A 06 9A 3B 0A 03 BA 25 0A 78
68 D8 01 BB 99 3C 34 77 47 91 7F 73 9C B0 80 18
00 3D A5 07 00 00 01 01 08 0A 3D BE 55 1F 13 40
C9 04 14 03 03 00 01 01 16 03 03 00 60 BF 01 E7
DC C0 9F 39 31 7B 10 9F A5 6B 35 67 F9 07 EF D3
26 9B 24 15 1A 89 14 0D 5E EF 19 E4 70 D9 98 1C
9D 34 60 17 91 E7 55 CB F0 95 9C 7A 36 74 30 A5
40 D3 A2 BD 48 8B A9 4E D1 49 F7 F8 14 22 EE 21
26 C0 58 4E EA 01 46 11 14 ED 7F 0B 8D B6 21 02
C4 EF 4B 4B FC F1 28 76 7F 06 F8 2D CE

```

# View details about an instance for obtaining packets and set the name of the file for sorting obtained packets to capture.cap.
```
<HUAWEI> display capture-packet file flash:/logfile/capture.cap verbose


packet NO        : 1                  
packet length is : 66
capture-time     : 2019-08-23 07:00:54.314356
  L2 Type : Ethernet                     
    Source mac   : 00e0-fc12-3456    
    Dest mac     : 00e0-fc12-3457
    Ethernet type/length : 0x0800
  L3 Type : IPv4                
  Protocol Num   : 6
    Source Ip    : 10.3.186.37
    Dest Ip      : 10.120.104.216
  L4 Type : TCP               
    Source Port  : 443            
    Dest  Port   : 39228
                           
28 6E D4 89 D4 BD D4 94 E8 59 12 33 08 00 45 28
00 34 6E 7C 40 00 3A 06 9A A7 0A 03 BA 25 0A 78
68 D8 01 BB 99 3C 34 77 47 91 7F 73 9C 4B 80 10
00 3D 9D 26 00 00 01 01 08 0A 3D BE 55 1F 13 40
C9 04


packet NO        : 2
packet length is : 173
capture-time     : 2019-08-23 07:00:54.314521
  L2 Type : Ethernet
    Source mac   : 00e0-fc12-3456
    Dest mac     : 00e0-fc12-3457
    Ethernet type/length : 0x0800
  L3 Type : IPv4  
  Protocol Num   : 6
    Source Ip    : 10.3.186.37
    Dest Ip      : 10.120.104.216
  L4 Type : TCP      
    Source Port  : 443
    Dest  Port   : 39228                    
                                                                         
28 6E D4 89 D4 BD D4 94 E8 59 12 33 08 00 45 28
00 9F 6E 7D 40 00 3A 06 9A 3B 0A 03 BA 25 0A 78
68 D8 01 BB 99 3C 34 77 47 91 7F 73 9C B0 80 18
00 3D A5 07 00 00 01 01 08 0A 3D BE 55 1F 13 40
C9 04 14 03 03 00 01 01 16 03 03 00 60 BF 01 E7
DC C0 9F 39 31 7B 10 9F A5 6B 35 67 F9 07 EF D3
26 9B 24 15 1A 89 14 0D 5E EF 19 E4 70 D9 98 1C
9D 34 60 17 91 E7 55 CB F0 95 9C 7A 36 74 30 A5
40 D3 A2 BD 48 8B A9 4E D1 49 F7 F8 14 22 EE 21
26 C0 58 4E EA 01 46 11 14 ED 7F 0B 8D B6 21 02
C4 EF 4B 4B FC F1 28 76 7F 06 F8 2D CE

```

**Table 1** Description of the **display capture-packet file** command output
| Item | Description |
| --- | --- |
| packet NO | Packet sequence number in the file for storing obtained packets. |
| packet length | Length of each packet in the file for storing obtained packets. |
| capture-time | Time when the packet header with the specified number is obtained. |
| L2 Type | Layer 2 protocol type. |
| Ethernet type/length | Ethernet type. |
| Source mac | Source MAC address. |
| Source Ip | Source IP address. |
| Source Port | Source port. |
| Dest mac | Destination MAC address. |
| Dest Ip | Destination IP address. |
| Dest Port | Destination port number. |
| L3 Type | Layer 3 protocol type. |
| Protocol Num | Protocol number. |
| L4 Type | Layer 4 protocol type. |