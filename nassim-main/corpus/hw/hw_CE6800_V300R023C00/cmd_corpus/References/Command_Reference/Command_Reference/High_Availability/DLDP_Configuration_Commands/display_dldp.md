display dldp
============

display dldp

Function
--------



The **display dldp** command displays DLDP status globally or on a specific interface.




Format
------

**display dldp** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **brief** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays DLDP information on a specified interface. | - |
| **brief** | Displays the DLDP status. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view DLDP status, run the display dldp command to display DLDP status globally or on a specific interface.If no parameter is specified, information about DLDP status on all DLDP-enabled interfaces on a device is displayed.

**Prerequisites**

DLDP has been enabled globally using the **dldp enable** command.Before running the **display dldp interface interface-type interface-number** command, you must run the **dldp enable** command to enable DLDP on the interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief DLDP information on the device.
```
<HUAWEI> display dldp brief
2022-12-02 17:13:12.425
Local IF            Local State     Neighbor MAC    Neighbor IF     Exptime(s)
------------------------------------------------------------------------------
100GE1/0/1          advertisement   00-e0-fc-12-34-56            7             10

```

# Display all DLDP information on a device.
```
<HUAWEI> display dldp
DLDP global status              : enable
DLDP interval(s)                : 5
DLDP work mode                  : enhance
DLDP authentication mode        : none
DLDP unidirectional shutdown    : auto
DLDP delaydown timer(s)         : 1
The number of enabled ports     : 1
The number of global neighbors  : 1

Interface  25GE1/0/1
DLDP port state                 : advertisement
DLDP link state                 : up
Local port index                : 1
The neighbor number of the port : 1

   Neighbor MAC address         : 00-e0-fc-12-34-56
   Neighbor port index          : 1
   Neighbor state               : two way
   Neighbor aged time(s)        : 14
   Neighbor created time        : 2022-12-19 21:32:51

```

# Display the DLDP status of the interface.
```
<HUAWEI> display dldp interface 100GE1/0/1
Interface  100GE1/0/1
DLDP port state                 : advertisement
DLDP link state                 : up 
The neighbor number of the port : 0

```

**Table 1** Description of the **display dldp** command output
| Item | Description |
| --- | --- |
| Local port index | Index of a local port. |
| Neighbor port index | Index of a neighbor port. |
| Neighbor state | Peer status. |
| Neighbor aged time(s) | Time period after which a peer ages. |
| Neighbor created time | Time at which a peer was created. |
| Neighbor MAC address | MAC address of a peer device. |
| DLDP global status | Whether DLDP is enabled globally:   * enable: enabled. * disable: disabled. |
| DLDP interval(s) | Interval at which Advertisement packets are sent, in seconds. |
| DLDP work mode | DLDP working mode:   * enhance: enhanced. * normal: normal. |
| DLDP authentication mode | DLDP authentication mode. |
| DLDP unidirectional shutdown | DLDP port shutdown mode:   * manual: manual. * auto: automatic. |
| DLDP delaydown timer(s) | Delay time for an interface to respond to a port-Down event, in seconds. |
| DLDP port state | Current status of the DLDP state machine of a port:   * Inactive: DLDP is enabled and the link is Down. * Active: DLDP is enabled and the link is Up, or the peer entries have been cleared. * Advertisement: All peers are bidirectionally reachable or DLDP has been in Active state for more than 5 seconds before entering Advertisement state. This is a stable state in which no unidirectional link has been detected. * Probe: A port enters this state after receiving packets from an unknown peer and sends Probe packets to probe whether the link is unidirectional. In this state, a Probe timer starts and an Echo timeout timer starts for each peer to be probed. * Disable: A port enters this state when DLDP detects the existence of a unidirectional link or when a peer disappears when DLDP works in the enhanced mode. In this state, the port sends and receives DLDPDUs only. * DelayDown: When DLDP detects a port-Down event, a port in Active, Advertisement, or Probe DLDP link state goes to DelayDown state. The port does not remove the peer entry and go to Inactive state. Ports in this state retain peer information and the DelayDown timer starts. |
| DLDP link state | Interface status:   * up. * down. |
| The number of enabled ports | Number of ports on which DLDP is enabled. |
| The number of global neighbors | Number of DLDP peers. |
| The neighbor number of the port | Number of peer ports. |
| Interface | Name of a DLDP-enabled port. |