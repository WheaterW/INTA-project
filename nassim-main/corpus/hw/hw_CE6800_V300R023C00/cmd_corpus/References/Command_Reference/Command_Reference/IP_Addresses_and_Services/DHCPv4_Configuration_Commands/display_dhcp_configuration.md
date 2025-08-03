display dhcp configuration
==========================

display dhcp configuration

Function
--------



The **display dhcp configuration** command displays the configuration of a DHCP public module.




Format
------

**display dhcp configuration**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check the configuration of a DHCP public module.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of a DHCP public module.
```
<HUAWEI> display dhcp configuration
 DHCP global running information :
 DHCPv4                                      : Enable
 DHCPv6                                      : Enable
 DHCP anti-attack check duplicate option     : Disable  (default)
 DHCP anti-attack check udp-checksum         : Enable   (default)
 DHCP anti-attack check magic-cookie         : Disable  (default)
 DHCP udp-checksum                           : Disable  (default)

```

**Table 1** Description of the **display dhcp configuration** command output
| Item | Description |
| --- | --- |
| DHCP global running information | Global configuration of a DHCP public module. |
| DHCP anti-attack check duplicate option | Whether the function of checking and discarding DHCP packets with duplicate options is enabled. The value can be:   * Enable: The function is enabled. * Disable (default): The function is disabled. By default, the function of checking and discarding DHCP packets with duplicate options is disabled.   To configure this parameter, run the dhcp anti-attack check duplicate option command. |
| DHCP anti-attack check udp-checksum | Whether the function of checking the UDP header checksum in a DHCP packet and discarding a DHCP packet with an incorrect checksum is enabled. The value can be:   * Enable (default): The function is enabled. By default, a device checks the UDP header checksum in a DHCP packet and discards a DHCP packet with an incorrect checksum. * Disable: The function is disabled.   To configure this parameter, run the dhcp anti-attack check duplicate option command. |
| DHCP anti-attack check magic-cookie | Whether the function of checking the magic cookie field in a DHCP packet and discarding a DHCP packet with an incorrect magic cookie field value is enabled. The value can be:   * Enable: The function is enabled. * Disable (default): The function is disabled. By default, a device does not check the magic cookie field in a DHCP packet but directly forwards a DHCP packet with an incorrect magic cookie field value.   To configure this parameter, run the dhcp anti-attack check magic-cookie command. |
| DHCP udp-checksum | Whether a device is enabled to add the UDP header checksum to DHCP packets to be sent. The value can be:   * Enable: The function is enabled. * Disable (default): The function is disabled. By default, the UDP header checksum carried in DHCP packets sent by a device is 0, and the peer device does not verify the checksum.   To configure this parameter, run the dhcp udp-checksum enable command. |
| DHCPv4 | Whether DHCPv4 is enabled. The value can be:   * Enable: The function is enabled. * Disable (default): The function is disabled. By default, DHCPv4 is disabled.   To configure this parameter, run the dhcp enable [ipv4] command. |
| DHCPv6 | Whether DHCPv6 is enabled. The value can be:   * Enable: The function is enabled. * Disable (default): The function is disabled. By default, DHCPv6 is disabled.   To configure this parameter, run the dhcp enable [ipv6] command. |