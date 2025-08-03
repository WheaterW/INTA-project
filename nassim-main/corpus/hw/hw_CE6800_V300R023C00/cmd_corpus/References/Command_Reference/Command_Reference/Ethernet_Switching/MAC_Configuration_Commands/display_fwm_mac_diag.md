display fwm mac diag
====================

display fwm mac diag

Function
--------



The **display fwm mac diag** command displays information about the DB table, software table, and hardware table of MAC addresses learned by the device.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display fwm mac diag slot** *slotid* **chip** *chipid* **mac-address** *mac-addr* **bridge-domain** *bdid*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display fwm mac diag slot** *slotid* **chip** *chipid* **mac-address** *mac-addr* **vlan** *vlanid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **chip** *chipid* | Chip information. | The value is an integer ranging from 0 to 8. |
| **mac-address** *mac-addr* | MAC address. | The value is in the format of H-H-H, in which each H is a hexadecimal number of 1 to 4 digits, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **bridge-domain** *bdid* | Bridge domain information.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer. |
| **slot** *slotid* | Slot information. | The value is a string of 1 to 31 case-sensitive characters without spaces. |
| **vlan** *vlanid* | VLAN information. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run the **display fwm mac diag** command to view the entries in the database table, software table, and hardware table corresponding to the MAC addresses learned by the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the DB table, FWM software table, and ODA hardware table related to the blackhole MAC address 00e0-fc12-3456.
```
<HUAWEI> display fwm mac diag slot 1 chip 0 mac-address 00e0-fc12-3456 vlan 100

# BrdType:   0-VLAN   2-BD
-------------------------------------------------------------
     Slot         :   1     
     Chip         :   0
     Mac-Address  :   00e0-fc12-3456
     BrdType      :   0
     BrdID        :   100
-------------------------------------------------------------
 [DB]:
           VSI ID :   100
             MCID :   612
         MAC TYPE :   3(BlackHole)
   STP Inst Index :   -
      STP Inst ID :   -
        STP State :   -
        Port Name :   -
             PVID :   -

 [FWM]:
             Mode :   Normal 
    Mac Info Flag :   0 
    Mac Port Type :   0
     UpdateReason :   DynSyn                                                                                                        
       UpdateTime :   2023-2-16 19:31:2
    UpdateExtInfo :   Mac syn senderSlot[1]                                                                                       
      Output Port :   Ifindex         Ifname             Ifinfo
                      -               -                  -

 [ODA]:
           PortID :   -
        MacRemote :   -
      TrunkEnable :   -
           Static :   2
            TB/TP :   -
                                    mac learn mode    port bridge    trunk id    pvid    fwd type
        Port Name :         -           -               -             -         -         -

```

# Display detailed information about the DB table, FWM software table, and ODA hardware table related to the MAC address 00e0-fc12-3456 in M-LAG dual-active mode.
```
<HUAWEI> display fwm mac diag slot 1 chip 0 mac-address 00e0-fc12-3456 bridge-domain 500

# BrdType:   0-VLAN   2-BD
-------------------------------------------------------------
     Slot         :   1     
     Chip         :   0
     Mac-Address  :   00e0-fc12-3456
     BrdType      :   2
     BrdID        :   500
-------------------------------------------------------------
 [DB]:
         MAC TYPE :   -
      VXLAN VSIID :   -
         VP Index :   -
        Port Name :   -
             PVID :   -

 [FWM]:
             Mode :   Active-Active 
        Lst Index :   56 
        SVP Index :   514
     UpdateReason :   DynSyn                                                                                                        
       UpdateTime :   2023-2-16 19:31:2
    UpdateExtInfo :   Mac syn senderSlot[1]   
      Output Port :   Ifindex         Ifname             Ifinfo         Nhpindex         Active
       MLAG PORT      79              Eth-Trunk1.1       0                 258           * 
       PEER LINK      78              Eth-Trunk100       4                 -           - 
                
 [ODA]:
           VSI Id :   4127
     VP/NHP Index :   258
       Mac Remote :   1
 VpSPortTrunkFlag :   1
      TrunkEnable :   0
          HitFlag :   0
           Static :   0

```

**Table 1** Description of the **display fwm mac diag** command output
| Item | Description |
| --- | --- |
| mac learn mode | MAC address learning mode. |
| Slot | Slot ID entered when the MAC address is queried. |
| Chip | Chip ID entered when the MAC address is queried. |
| Mac-Address | Entered MAC address to be queried. |
| BrdType | MAC address type. The value 0 indicates that the MAC address is related to a VLAN, and the value 2 indicates that the MAC address is related to a BD. |
| BrdID | VLAN ID or BD ID entered when the MAC address is queried. |
| MAC TYPE | MAC address type. The values are as follows: 0: unidentified; 2: static MAC address; 3: blackhole MAC address. |
| VXLAN VSIID | VSI index in the VXLAN scenario. |
| VP Index | VP index in the VXLAN scenario in the DB table. |
| Port Name | Port name. |
| PVID | Default VLAN ID of a port. |
| Mode | Application scenario of the current MAC address. Common scenarios (Normal), M-LAG active-standby scenarios (Active-Standby), and M-LAG dual-active scenarios (Active-Active) are supported. |
| Mac Info Flag | Information flag contained in the current MAC address. |
| Mac Port Type | Type of the interface corresponding to the current MAC address. 0: common physical interface; 1: trunk interface; 3: LVPN type; 4: EVN remote MAC address; 6: BD interface; 8: FRR type; 9: VP type. |
| Mac Remote | Whether the MAC address is synchronized from the remote end or other boards. 0: no; 1: yes. |
| SVP Index | SVP index in the software table in a BD scenario. |
| UpdateReason | Reason for updating the MAC address in the software table. The values are as follows:  "Undefined",  "ArpDupGwMacToBlackhole",  "EvpnMacAdd",  "MlagRemoteToLocalSyn",  "RemoteTrunkMacNoHitSwToLocal",  "AgingDumpSyn",  "LearnDumpSyn",  "Learn",  "DynSyn" , "MacAddToInsertSw",  "NacMacAdd",  "StaticReplaceDyn",  "StickyMacAdd". |
| UpdateTime | Time when MAC addresses in the software table are updated. |
| UpdateExtInfo | Auxiliary information about MAC address update in the software table. Currently, UpdateExtInfo: Mac syn senderSlot[1] is displayed only when UpdateReason is DynSyn. [] indicates the slot ID of the synchronization party. If all slots are synchronized, 0xffffffff is displayed. |
| Output Port | Outbound interface information, including the interface index IfIndex, interface name IfName, and interface information IfInfo in common mode. IfInfo displays the TB/TP information of a physical interface, trunk ID of a trunk interface, or "destination IP address -> source IP address" of a tunnel interface. In an M-LAG scenario, in addition to the preceding information, the outbound interface information also includes the NHP indexes of the M-LAG and peer-link interfaces and whether the M-LAG and peer-link interfaces carry traffic (Active displays \*). |
| VSI ID | VSI index in the VLAN scenario. |
| VSI Id | VSI index in the hardware table in the VXLAN scenario. |
| VP/NHP Index | VP or NHP index in the hardware table. |
| VpSPortTrunkFlag | VpSPortTrunkFlag flag in the hardware table. |
| TrunkEnable | Whether the port is a trunk port. 0: no; 1: yes. |
| HitFlag | Whether the MAC address is matched in the hardware table. 0: no; 1: yes. |
| Static | Static MAC address type. 0: non-static MAC address; 1: static MAC address; 2: blackhole MAC address. |
| MCID | Multicast ID corresponding to the VLAN ID or BD ID. |
| STP Inst Index | Index of an STP instance. |
| STP Inst ID | ID of an STP instance. |
| STP State | STP status of the corresponding physical port. |
| PortID | Port ID, which generally refers to the TP value of the port. |
| MacRemote | Whether the MAC address is synchronized from the remote end or other cards. 0: no; 1: yes. |
| TB/TP | Target board and target port information of the port. |
| port bridge | Port bridge status. |
| trunk id | Trunk ID of the corresponding trunk interface. |
| pvid | Default VLAN ID of a port in the hardware table. |
| fwd type | Forwarding type of a port in the hardware table. |
| Lst Index | LST index corresponding to the actual outbound interface of the current traffic. |