display dhcp relay
==================

display dhcp relay

Function
--------



The **display dhcp relay** command displays configuration information about a DHCP relay agent.




Format
------

**display dhcp relay** { **configuration** | **all** | **interface** { *interface-type* *interface-number* | *interface-name* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **configuration** | Displays configuration information about DHCP relay agents configured globally and on all interfaces. | - |
| **all** | Displays configuration information about DHCP relay agents configured on all interfaces. | - |
| **interface** *interface-type* *interface-number* | Displays configuration information about a DHCP relay agent configured on a specified interface. | - |
| *interface-name* | Displays configuration information about a DHCP relay agent configured on a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check configuration information about DHCP relay agents configured globally and on interfaces.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configuration information about DHCP relay agents on all interfaces.
```
<HUAWEI> display dhcp relay configuration
  DHCP relay global running information :
  DHCP relay adrress cycle           : Disable (default)
  DHCP relay trust option82          : Enable  (default)
  DHCP relay request server-match    : Enable  (default)
  DHCP relay reply forward all       : Disable (default)
 DHCP relay agent running information of interface Vbdif100 :
 Relay select           : Enable
 Server IP address [00] : 10.1.1.1
 Gateway switch         : Disable
 GIADDR source interface : LoopBack1
 Link-selection insert  : enable
 Link-selection subnet ip address  : 6.6.6.6
 Server-id-override insert  : Disable
 Vss-control insert  : Disable
 Giaddr outgoing-interface-address  : Disable
 DHCP relay agent running information of interface Vlanif5 :
 Relay select           : Disable
 Server group name      : group1
 Gateway switch         : enable
 Link-selection insert  : Disable
 Server-id-override insert  : Disable
 Vss-control insert  : Disable
 Giaddr outgoing-interface-address  : Disable
 DHCP relay agent running information of interface Vlanif100 :
 Relay select           : Disable
 Server IP address [00] : 10.2.2.3
 Gateway switch         : Disable
 Link-selection insert  : Disable
 Server-id-override insert  : Disable
 Vss-control insert  : Disable
 Giaddr outgoing-interface-address  : Disable

```

**Table 1** Description of the **display dhcp relay** command output
| Item | Description |
| --- | --- |
| DHCP relay global running information | Configuration information about DHCP relay agents configured globally. |
| DHCP relay adrress cycle | Whether the DHCP server polling function is enabled on a DHCP relay agent.   * Enable: The DHCP server polling function is enabled on a DHCP relay agent. * Disable: The DHCP server polling function is disabled on a DHCP relay agent.   To configure this item, run the ip relay address cycle command. |
| DHCP relay trust option82 | Whether Option 82 is enabled on a DHCP relay agent.   * Enable: Option 82 is enabled on a DHCP relay agent. * Disable: Option 82 is disabled on a DHCP relay agent.   To configure this item, run the dhcp relay trust option82 command. |
| DHCP relay request server-match | Whether a DHCP relay agent is enabled to check the DHCP server identifier (Option54) in a DHCP Request message to be forwarded.   * Enable: A DHCP relay agent is enabled to check the DHCP server identifier (Option54) in a DHCP Request message to be forwarded. * Disable: A DHCP relay agent is disabled from checking the DHCP server identifier (Option54) in a DHCP Request message to be forwarded.   To configure this item, run the dhcp relay request server-match enable command. |
| DHCP relay reply forward all | Whether a DHCP relay agent is enabled to forward all DHCP ACK messages.   * Enable: A DHCP relay agent is enabled to forward all DHCP ACK messages. * Disable: A DHCP relay agent is disabled from forwarding all DHCP ACK messages.   To configure this item, run the dhcp relay reply forward all enable command. |
| DHCP relay agent running information of interface if | DHCP relay agent configuration of an interface. |
| Relay select | Whether the DHCP relay function is enabled:   * Enable: The DHCP relay function is enabled. * Disable: The DHCP relay function is disabled.   To set this parameter, run the dhcp select relay command. |
| Server group name | DHCP server group name.  To configure this item, run the dhcp relay server-group command. |
| Server IP address [x] | IP address of a DHCP server in the DHCP server group. The value x is the index of a DHCP server.  To configure this item, run the server command. |
| Gateway switch | Whether automatic gateway switchover is enabled on a DHCP relay agent. The value can be:   * Enable: The automatic gateway switchover on a DHCP relay agent is enabled. * Disable: The automatic gateway switchover on a DHCP relay agent is disabled.   To configure this item, run the dhcp relay gateway-switch enable command. |
| GIADDR source interface | Source interface of DHCP relayed packets.  To configure this item, run the dhcp relay giaddr source-interface command. |
| Link-selection insert | Whether the function of inserting the Link-selection suboption of the Option82 field into DHCP packets is enabled. The value can be:   * Enable: The function of inserting the Link-selection suboption of the Option82 field into DHCP packets is enabled. * Disable: The function of inserting the Link-selection suboption of the Option82 field into DHCP packets is disabled.   To configure this item, run the dhcp option82 link-selection insert enable command. |
| Link-selection subnet ip address | Specifies the IP address corresponding to the Sub5 field in Option 82. |
| Server-id-override insert | Whether the function of inserting Option 82's suboption server-id-override is enabled:   * Enable: The function of inserting Option 82's suboption server-id-override is enabled. * Disable: The function of inserting Option 82's suboption server-id-override is disabled.   To set this parameter, run the dhcp option82 server-id-override insert enable command. |
| Vss-control insert | Whether the function of inserting Option 82's suboption vss-control is enabled:   * Enable: The function of inserting Option 82's suboption vss-control is enabled. * Disable: The function of inserting Option 82's suboption vss-control is disabled.   To set this parameter, run the dhcp option82 vss-control insert enable command. |
| Giaddr outgoing-interface-address | Whether the function of configuring the relay agent address as the IP address of the outbound interface is enabled:   * Enable: The function of configuring the relay agent address as the IP address of the outbound interface is enabled. * Disable: The function of configuring the relay agent address as the IP address of the outbound interface is disabled.   To set this parameter, run the dhcp relay giaddr outgoing-interface-address command. |