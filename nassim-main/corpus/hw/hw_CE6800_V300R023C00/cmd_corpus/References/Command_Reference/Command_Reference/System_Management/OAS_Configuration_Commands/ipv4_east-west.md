ipv4 east-west
==============

ipv4 east-west

Function
--------



The **ipv4 east-west** command configures the destination IP address and MTU for east-west traffic in an open system.

The **undo ipv4 east-west** command deletes the destination IP address and MTU for east-west communication in an open system.



By default, no east-west address is configured.


Format
------

**ipv4 east-west** { **destination** *destAddress* | **mtu** *mtuValue* }

**undo ipv4 east-west** { **destination** *destAddress* | **mtu** *mtuValue* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **destination** *destAddress* | Specifies the east-west address of an open system. | The value is in dotted decimal notation. |
| **mtu** *mtuValue* | Specifies the MTU value for east-west communication. | The value is an integer ranging from 1500 to 9600. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

In the openness solution, a service app needs to communicate with a third-party app in the Linux operating system (east-west communication between two systems on a device). The communication requires a specified IP address. The east-west IP address can be configured using this command. The service app subscribes to the information to determine whether the communication is east-west communication or internal communication.


Example
-------

# Set the IP address for east-west communication to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] oas enable
[*HUAWEI] oas
[*HUAWEI-oas] ipv4 east-west destination 10.1.1.1

```

# Set the MTU for east-west communication to 1600.
```
<HUAWEI> system-view
[~HUAWEI] oas enable
[*HUAWEI] oas
[*HUAWEI-oas] ipv4 east-west mtu 1600

```