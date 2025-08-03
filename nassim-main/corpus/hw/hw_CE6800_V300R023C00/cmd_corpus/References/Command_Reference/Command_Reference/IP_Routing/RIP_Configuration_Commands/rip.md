rip
===

rip

Function
--------



The **rip** command enables a specified RIP process in the system view.

The **undo rip** command disables a RIP process.



By default, no RIP process is enabled.


Format
------

**rip** *process-id* [ **vpn-instance** *vpn-instance-name* ]

**rip** [ **vpn-instance** *vpn-instance-name* ]

**undo rip** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Indicates the ID of a RIP process. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If no VPN instance is specified, the RIP process is run in the global or default instance. RIP must be started first so that global RIP parameters can be configured. However, the configurations of interface-related parameters are not restricted.If the **undo rip process-id** command is run, all configurations in the RIP process are deleted. Therefore, exercise caution when using the command.

**Precautions**

RIP packets can be sent only when the MTU of the interface is greater than or equal to 52 bytes.


Example
-------

# Enable RIP and set the RIP process ID to 1.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1]

```

# Enable RIP multi-instance for RIP process 100 and set the instance name to abc.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[*HUAWEI-vpn-instance-abc] ipv4-family
[*HUAWEI-vpn-instance-abc-af-ipv4] quit
[*HUAWEI-vpn-instance-abc] quit
[*HUAWEI] rip 100 vpn-instance abc

```