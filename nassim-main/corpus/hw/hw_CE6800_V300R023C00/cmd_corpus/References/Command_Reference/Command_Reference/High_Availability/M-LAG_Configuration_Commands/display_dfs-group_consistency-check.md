display dfs-group consistency-check
===================================

display dfs-group consistency-check

Function
--------



The **display dfs-group consistency-check** command displays the configuration of M-LAG master and backup devices.




Format
------

**display dfs-group consistency-check** { **global** | **interface** { **m-lag** *m-lag-id* | **peer-link** *peer-linkid* } | **static-arp** | **static-mac** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Displays the configuration of M-LAG master and backup devices in the system. | - |
| **interface** | Displays the configuration of M-LAG master and backup devices on the M-LAG member interface. | - |
| **m-lag** *m-lag-id* | Specifies the M-LAG ID. | The value is an integer ranging from 1 to 2048. |
| **peer-link** *peer-linkid* | Specifies the peer-link ID. | The value is 1. |
| **static-arp** | Displays static ARP entry information on the M-LAG master and backup devices. | - |
| **static-mac** | Displays static MAC address entry information on the M-LAG master and backup devices. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the display dfs-group consistency-check command to check the configuration in the system and on the M-LAG member interface when M-LAG consistency check is enabled.

**Precautions**

You can run the **display dfs-group consistency-check global** command to check the global configuration information about M-LAG configuration consistency check. In the command output, a maximum of 16 check results can be displayed for each check item.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration in the system when M-LAG consistency check is enabled.
```
<HUAWEI> display dfs-group consistency-check global
-----------------------------------------------------------------------------------
Configuration           Type   Local value               Peer value
-----------------------------------------------------------------------------------
STP Enable                 1   Disable                   Enable
STP Mode                   1   RSTP                      MSTP
BD(VNI)                    2   1(1),2(2),100(--)         --,--,100(100)
BD(MAPPING VNI)            2   1(2),2(3),100(--)         --,--,100(101)
BDIF                       2   1,2                       --,--
BDIF(IPV4)                 2   1(1.1.1.2:24),            --,
                               100(10.1.1.21:24)         100(10.1.1.20:24)
BDIF(MAC)                  2   2(00e0-fc12-3456)         --
VLAN                       2   55,99,101,130,152,500,    --,--,--,--,--,--,
                               1000,1001,1111,2001,      --,--,--,--,
                               2222                      --
VLANIF                     2   41,--,--,152,500,1000,    --,42,100,--,--,--,
                               1001                      --
VLANIF(IPV4)               2   41(192.168.1.1:16),       --,
                               --,                       42(192.168.2.1:24),
                               500(192.168.3.1:24),      --,
                               1000(172.16.1.1:24),      --,
                               1001(172.16.2.1:24)       --
VLANIF(VRRP4)              2   152(1/172.16.3.1)         --
V-STP                      1   Enable                    Disable
Election mode              2   ARP,IGMP,--               --,--,DHCP
STP Vlan Disable           1   55,99,101,130             --,--,--,--
-----------------------------------------------------------------------------------

```

# Display the configuration on the M-LAG member interface when M-LAG consistency check is enabled.
```
<HUAWEI> display dfs-group consistency-check interface m-lag 1
-----------------------------------------------------------------------------------
Configuration           Type   Local value               Peer value
-----------------------------------------------------------------------------------
VLAN                       2   30                        --
STP Enable                 1   Enable                    Disable
LACP M-LAG System-Id       1   0001-0001-0001            0001-0001-0002
LACP M-LAG Priority        1   100                       200
STP Edged-port             1   Enable                    Disable
-----------------------------------------------------------------------------------

```

# Display static ARP entry information when M-LAG consistency check is enabled.
```
<HUAWEI> display dfs-group consistency-check static-arp
-----------------------------------------------------------------------------------------------
M : MAC          V : VLAN          C : CE-VLAN     I : M-Lag ID
N : VNI          S : Source IP     P : Peer IP
-----------------------------------------------------------------------------------------------
IP address       Local value(M/V/C/I/N/S/P)              Peer value(M/V/C/I/N/S/P)
-----------------------------------------------------------------------------------------------
1.1.1.3          00e0-fc12-3456, --, --, --, --, --, --  00e0-fc12-3457, --, --, --, --, --, --
-----------------------------------------------------------------------------------------------

```

# Display the peer-link configuration when M-LAG consistency check is enabled.
```
<HUAWEI> display dfs-group consistency-check interface peer-link 1
-----------------------------------------------------------------------------------
Configuration           Type   Local value               Peer value
-----------------------------------------------------------------------------------
STP Enable                 1   Enable                    Disable
LACP Mode                  1   Static                    Dynamic
Exclude VLAN               2   100,200,300,--            400,--,--,--
-----------------------------------------------------------------------------------

```

**Table 1** Description of the **display dfs-group consistency-check** command output
| Item | Description |
| --- | --- |
| Configuration | Configuration item. For details about the configurations that can be checked, see the M-LAG configuration consistency check list. |
| Type | Configuration type:  1: key configuration.  2: common configuration. |
| Local value | M-LAG configuration of the local device. |
| Peer value | M-LAG configuration of the remote device. |
| IP address | IP address in a static ARP entry. |