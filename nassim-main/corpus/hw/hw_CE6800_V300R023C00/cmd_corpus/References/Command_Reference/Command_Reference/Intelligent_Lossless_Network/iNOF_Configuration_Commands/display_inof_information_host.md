display inof information host
=============================

display inof information host

Function
--------



The **display inof information host** command displays information about hosts managed by devices on the iNOF network.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display inof information host** [ **local** | **remote** | { *ip-address* | *ipv6-address* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local** | Specifies information about hosts connected to the local device. | - |
| **remote** | Specifies host information learned from the reflector. | - |
| *ip-address* | Specifies the IPv4 address of a host. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a host. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check information about hosts managed by devices on the iNOF network.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# On an iNOF reflector, display information about hosts managed on the iNOF network. (The iNOF zone isolation function has been enabled.)
```
<HUAWEI> display inof information host
Initiator: The terminal that initiates NVMe sessions and sends NVMe commands.
Target: The terminal that waits for the initiator's commands and provides required input/output data transmission.
Invalid: The host role is unknown or not obtained. 
IPv4 Info:
--------------------------------------------------------------------------------------------------------------------------------------
Host                                     Type   AccessDevice                             AccessInterface  HardZoning  Role
--------------------------------------------------------------------------------------------------------------------------------------
192.168.1.155                            local  192.168.2.151                            Eth-Trunk10      Normal      Initiator
                                         remote 192.168.2.152                            Eth-Trunk10      Normal      Initiator
192.168.1.156                            local  192.168.2.151                            100GE1/0/3       Abnormal    Target  
192.168.1.157                            remote 192.168.2.153                            Eth-Trunk11      Normal      Initiator&Target
192.168.1.158                            remote 192.168.2.153                            100GE1/0/2       Normal      Target
--------------------------------------------------------------------------------------------------------------------------------------
IPv6 Info:
--------------------------------------------------------------------------------------------------------------------------------------
Host                                     Type   AccessDevice                             AccessInterface  HardZoning  Role
--------------------------------------------------------------------------------------------------------------------------------------
2001:DB8:1::5                            local  2001:DB8:2::1                            Eth-Trunk10      Normal      Initiator
                                         remote 2001:DB8:2::2                            Eth-Trunk10      Normal      Initiator
2001:DB8:1::6                            local  2001:DB8:2::1                            100GE1/0/3       Abnormal    Target  
2001:DB8:1::7                            remote 2001:DB8:2::3                            Eth-Trunk11      Normal      Initiator&Target
2001:DB8:1::8                            remote 2001:DB8:2::3                            100GE1/0/2       Normal      Target
--------------------------------------------------------------------------------------------------------------------------------------

```

# On an iNOF client, display information about hosts managed on the iNOF network.
```
<HUAWEI> display inof information host
Initiator: The terminal that initiates NVMe sessions and sends NVMe commands.
Target: The terminal that waits for the initiator's commands and provides required input/output data transmission.
Invalid: The host role is unknown or not obtained. 
IPv4 Info:
--------------------------------------------------------------------------------------------------------------------------------------
Host                                     Type   AccessDevice                             AccessInterface  HardZoning  Role
--------------------------------------------------------------------------------------------------------------------------------------
192.168.1.155                            remote 192.168.2.151                            Eth-Trunk10      --          Initiator
                                         local  192.168.2.152                            Eth-Trunk10      Normal      Initiator
192.168.1.156                            remote 192.168.2.151                            100GE1/0/3       --          Target  
192.168.1.157                            local  192.168.2.153                            Eth-Trunk11      Normal      Initiator&Target
192.168.1.158                            local  192.168.2.153                            100GE1/0/2       Normal      Target
--------------------------------------------------------------------------------------------------------------------------------------
IPv6 Info:
--------------------------------------------------------------------------------------------------------------------------------------
Host                                     Type   AccessDevice                             AccessInterface  HardZoning  Role
--------------------------------------------------------------------------------------------------------------------------------------
2001:DB8:1::5                            remote 2001:DB8:2::1                            Eth-Trunk10      --          Initiator
                                         local  2001:DB8:2::2                            Eth-Trunk10      Normal      Initiator
2001:DB8:1::6                            remote 2001:DB8:2::1                            100GE1/0/3       --          Target  
2001:DB8:1::7                            local  2001:DB8:2::3                            Eth-Trunk11      Normal      Initiator&Target
2001:DB8:1::8                            local  2001:DB8:2::3                            100GE1/0/2       Normal      Target
--------------------------------------------------------------------------------------------------------------------------------------

```

# On an iNOF reflector, display information about hosts managed on the iNOF network. (The iNOF zone isolation function is disabled.)
```
<HUAWEI> display inof information host
Initiator: The terminal that initiates NVMe sessions and sends NVMe commands.
Target: The terminal that waits for the initiator's commands and provides required input/output data transmission.
Invalid: The host role is unknown or not obtained. 
IPv4 Info:
--------------------------------------------------------------------------------------------------------------------------------------
Host                                     Type   AccessDevice                             AccessInterface  HardZoning  Role
--------------------------------------------------------------------------------------------------------------------------------------
192.168.1.155                            local  192.168.2.151                            Eth-Trunk10      Disable     Initiator
                                         remote 192.168.2.152                            Eth-Trunk10      Disable     Initiator
192.168.1.156                            local  192.168.2.151                            100GE1/0/3       Disable     Target  
192.168.1.157                            remote 192.168.2.153                            Eth-Trunk11      Disable     Initiator&Target
192.168.1.158                            remote 192.168.2.153                            100GE1/0/2       Disable     Target
--------------------------------------------------------------------------------------------------------------------------------------
IPv6 Info:
--------------------------------------------------------------------------------------------------------------------------------------
Host                                     Type   AccessDevice                             AccessInterface  HardZoning  Role
--------------------------------------------------------------------------------------------------------------------------------------
2001:DB8:1::5                            local  2001:DB8:2::1                            Eth-Trunk10      Disable     Initiator
                                         remote 2001:DB8:2::2                            Eth-Trunk10      Disable     Initiator
2001:DB8:1::6                            local  2001:DB8:2::1                            100GE1/0/3       Disable     Target  
2001:DB8:1::7                            remote 2001:DB8:2::3                            Eth-Trunk11      Disable     Initiator&Target
2001:DB8:1::8                            remote 2001:DB8:2::3                            100GE1/0/2       Disable     Target
--------------------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display inof information host** command output
| Item | Description |
| --- | --- |
| IPv4 Info | IPv4 information. |
| Host | Host IP address. |
| Type | Access type of a host:   * local: The host is connected to the local device. * remote: The host is connected to a remote device. |
| AccessDevice | Access device. The options are as follows:   * IP address of the host access device, which can be configured using the service-address command. * --: No IP address is configured on the host access device. |
| AccessInterface | Access interface. |
| HardZoning | Effective status of the iNOF zone isolation function on the interface to which a host is connected:   * Normal: The iNOF zone isolation function takes effect. * Abnormal: The iNOF zone isolation function is abnormal and does not take effect. * --: The local device is an iNOF client and the interface to which the host is connected is on the remote device. Check whether the iNOF zone isolation function takes effect on the remote device. On the iNOF reflector, you can view the effective status of the iNOF zone isolation function on the remote device. On the iNOF client, you cannot view the effective status of the iNOF zone isolation function on the remote device. * Disable: The iNOF zone isolation function is disabled. * Processing: The iNOF zone isolation function is being updated or delivered. |
| Role | Host role.   * Initiator: initiates NVMe sessions and sends NVMe commands. * Target: transmits input and output data based on the commands from the initiator. * Initiator&Target: has both initiator and target capabilities. * Invalid: The host role is unknown or not obtained. |
| IPv6 Info | IPv6 information. |