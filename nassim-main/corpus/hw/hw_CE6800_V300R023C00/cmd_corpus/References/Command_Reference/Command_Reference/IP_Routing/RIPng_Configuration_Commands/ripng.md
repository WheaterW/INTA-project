ripng
=====

ripng

Function
--------



The **ripng** command creates and enables a RIPng process.

The **undo ripng** command terminates a specified RIPng process.



By default, the RIPng process ID is 1, and a RIPng process is not bound to any IPv6 VPN instance.


Format
------

**ripng** *process-id* [ **vpn-instance** *vpn-instance-name* ]

**ripng** [ **vpn-instance** *vpn-instance-name* ]

**undo ripng** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of a RIPng process. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of an IPv6 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure RIPng-related parameters, run the ripng command to create a RIPng process first.RIPng supports multi-process. Multiple RIPng processes can run on the same device, independent of each other. Route exchange between different RIPng processes is similar to route exchange between different routing protocols.

**Precautions**

A VPN instance can be associated with a RIPng process only when the RIPng process is created. After a RIPng process is created, it cannot be associated with any VPN instance.If the **undo ripng** command is run, all configurations in the RIPng process are deleted. Therefore, exercise caution when running the command.


Example
-------

# Create RIPng process 1 and bind it to an IPv6 address family-enabled VPN instance vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ripng 1 vpn-instance vpn1

```

# Create a specified RIPng process.
```
<HUAWEI> system-view
[~HUAWEI] ripng 100

```