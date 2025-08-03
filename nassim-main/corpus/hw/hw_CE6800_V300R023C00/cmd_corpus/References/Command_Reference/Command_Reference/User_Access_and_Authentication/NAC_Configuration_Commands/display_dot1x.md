display dot1x
=============

display dot1x

Function
--------



The **display dot1x** command displays 802.1X authentication information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display dot1x** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]

**display dot1x statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** [ *interface-type* *interface-number* ] | Displays 802.1X authentication information on a specified interface. If this parameter is not specified, 802.1X authentication information on all interfaces is displayed. | Displays 802.1X authentication information on a specified interface. If no parameter is specified, 802.1X authentication information on all interfaces is displayed. |
| *interface-name* | Displays 802.1X authentication information of a specified interface. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| **statistics** | Displays 802.1X authentication statistics.  802.1X authentication statistics are displayed only when this parameter is specified. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view configuration results of all configuration commands in 802.1X authentication and statistics about 802.1X packets.

The command output helps you to check whether the current 802.1X authentication configuration is correct and isolate faults accordingly.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display 802.1X authentication information.
```
<HUAWEI> display dot1x
  Max users: 10000
  Current users: 0
  Global default domain is default
  Dot1x abnormal-track cache-record-num: 20
  Quiet function is Enabled
  Mc-trigger is Disabled
  Mc-trigger port-up-send is Disabled
  Parameter set:Quiet Period                  60s   Quiet-times         10
                Tx Period                     30s   Mac-bypass Delay   30s
                                                                                                                                    
 10GE1/0/1 status: UP  802.1x protocol is Enabled                                                                                  
  Dot1x access profile is dot1x_access_profile                                                                                      
  Authentication mode is multi-authen                                                                                               
  Authentication method is EAP                                                                                                      
  Reauthentication is disabled                                                                                                      
  Dot1x retry times: 2                                                                                                              
  Authenticating users: 0                                                                                                           
  Current users: 0                                                                                                                  
                                                                                                                                    
  Authentication Success: 0          Failure: 0                                                                                     
  Enter Enquence        : 0                                                                                                         
  EAPOL Packets: TX     : 0          RX     : 0                                                                                     
  Sent      EAPOL Request/Identity Packets  : 0                                                                                     
            EAPOL Request/Challenge Packets : 0                                                                                     
            Multicast Trigger Packets       : 0                                                                                     
            EAPOL Success Packets           : 0                                                                                     
            EAPOL Failure Packets           : 0                                                                                     
  Received  EAPOL Start Packets             : 0                                                                                     
            EAPOL Logoff Packets            : 0                                                                                     
            EAPOL Response/Identity Packets : 0                                                                                     
            EAPOL Response/Challenge Packets: 0

```

# Display 802.1X statistics.
```
<HUAWEI> display dot1x statistics
  Dropped   EAPOL Access Flow Control       : 0   
            EAPOL Check Sysmac Error        : 0   
            EAPOL Get Vlan ID Error         : 0   
            EAPOL Packet Flow Control       : 0   
            EAPOL Online User Reach Max     : 0   
            EAPOL Static or BlackHole Mac   : 0   
            EAPOL Get Vlan Mac Error        : 0   
            EAPOL Temp User Exist           : 0   
            EAPOL No Replace Dot1x          : 0   
            EAPOL Auth Order Mac Dot1x      : 0   
  
  DHCP      Enter Enqueue                        : 0   
            Processed Packet                     : 0   
            Dropped Packet                       : 0   
  
  ARP       Enter Enqueue                        : 0   
            Processed Packet                     : 0   
            Dropped Packet                       : 0   
  
  ND        Enter Enqueue                        : 0   
            Processed Packet                     : 0   
            Dropped Packet                       : 0   
  
  DHCPv6    Enter Enqueue                        : 0   
            Processed Packet                     : 0   
            Dropped Packet                       : 0   
  
  ANY-L2    Enter Enqueue                        : 0   
            Processed Packet                     : 0   
            Dropped Packet                       : 0   

  Sent      Authentication Request               : 0   
            Cut Request                          : 0   
            Cut Command Ack                      : 0   
            Authentication Ack Fail Aff          : 0   
            Update Ip                            : 0   
            Wlan Eap Authentication Request      : 0   
            Wlan Eap Authentication Request Ack  : 0   
            Wlan Eap Send Pmk                    : 0   
            Wlan Eap Reauthenticate Send Pmk     : 0   
            Update User Online Time              : 0    

  Received  Authentication Ack                   : 0   
            Reauthenticate Command               : 0   
            Cut Command                          : 0   
            Cut Ack                              : 0
            Sam Nac Ack                          : 0
            Notify Server Up                     : 0   
            Wlan Eap Authentication Request      : 0   
            Wlan Mac Authentication Request      : 0

```

**Table 1** Description of the **display dot1x** command output
| Item | Description |
| --- | --- |
| Max users | Maximum number of global online users.  To set the maximum number of global online users, run the dot1x max-user command. |
| Current users | Number of online users. |
| Current users | Number of current online users on the interface. |
| Quiet function is Enabled | Whether the quiet function is enabled for users.  To enable the quiet function, run the dot1x quiet-period command. |
| Parameter set | Settings of 802.1X parameters. |
| Authentication Request | Number of authentication request messages. |
| Authentication Ack Fail Aff | Number of times the user is disconnected after the wireless user authentication fails. |
| Authentication Ack | Number of authentication acknowledgment messages. |
| Enter Enqueue | Number of packets entering the queue. |
| EAPOL Request/Identity Packets | Number of global EAPoL Request/Identity packets. |
| EAPOL Request/Challenge Packets | Number of global EAPoL Request/Challenge packets. |
| EAPOL Response/Identity Packets | Number of global EAPoL Response/Identity packets. |
| EAPOL Response/Challenge Packets | Number of global EAPoL Response/Challenge packets. |
| Sent | Statistics about transmitted packets. |
| Online user(s) info | Online user information:   * UserId: user ID. * MAC/VLAN: MAC address or VLAN ID. * AccessTime: access time. * UserName: user name. * Total: total number of online users. * printed: number of online users. |
| Mc-trigger port-up-send is Disabled | The function of triggering 802.1X authentication through multicast packets immediately after an interface goes Up is enabled.  To configure the function, run the dot1x mc-trigger port-up-send enable command. |
| Dropped | Number of discarded EAP packets.   * EAPOL Access Flow Control: number of packets discarded because the user access rate is exceeded. * EAPOL Check Sysmac Error: number of packets that are discarded because the device MAC address is incorrect. * EAPOL Get Vlan ID Error: number of packets that are discarded because the obtained VLAN ID is incorrect. * EAPOL Packet Flow Control: number of packets that are discarded because the packet access rate is exceeded. * EAPOL Online User Reach Max: number of packets discarded because the number of online users reaches the maximum. * EAPOL Static or BlackHole Mac: number of packets that are discarded because the MAC address of the packets is a static MAC address or blackhole MAC address. * EAPOL Get Vlan Mac Error: number of packets that are discarded because the obtained VLAN MAC address is incorrect. * EAPOL Temp User Exist: number of packets discarded because temporary users exist. * EAPOL no replace dot1x: number of EAP Start packets discarded during 802.1X authentication for MAC address authentication users who have been successfully authenticated. |
| Dropped Packet | Number of discarded packets. |
| DHCP | DHCP packet statistics. |
| Processed Packet | Number of processed packets. |
| ARP | ARP packet statistics. |
| ND | ND packet statistics. |
| DHCPv6 | DHCPv6 packet statistics. |
| Cut Request | Number of logout request messages. |
| Cut Command Ack | Number of acknowledgment messages of logout request messages. |
| Cut Command | Number of logout request messages. |
| Cut Ack | Number of acknowledgment messages of logout request messages. |
| Update Ip | Number of IP address update messages. |
| Update User Online Time | Number of times the user online time is updated. |
| Wlan Eap Authentication Request | Number of EAP authentication request messages initiated by the WLAN module. |
| Wlan Eap Authentication Request Ack | Number of response messages for EAP authentication requests initiated by the WLAN module. |
| Wlan Eap Send Pmk | Number of response messages for EAP authentication requests initiated by the WLAN module. |
| Wlan Mac Authentication Request | Number of MAC authentication request messages initiated by the WLAN module. |
| Reauthenticate Command | Number of re-authentication messages. |
| Notify Vlanif Mac Authentication | Number of MAC authentication request messages of a VLANIF interface. |