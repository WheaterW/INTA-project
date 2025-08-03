dhcp set ttl
============

dhcp set ttl

Function
--------



The **dhcp set ttl** command sets the TTL value for DHCP Discover messages after they are forwarded by the DHCP relay agent at Layer 3.

The **undo dhcp set ttl** command restores the default setting.



By default, the TTL value of DHCP Discovery messages decreases by 1 after they are forwarded by the DHCP relay agent at Layer 3.


Format
------

**dhcp set ttl** { **unvaried** | *ttl-value* }

**undo dhcp set ttl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unvaried** | Indicates that the TTL value of DHCP Discovery messages remains unchanged after the messages are forwarded by the DHCP relay agent at Layer 3. That is, the device does not reduce the TTL value by 1. | - |
| *ttl-value* | Specifies a fixed TTL value for DHCP Discovery messages after they are forwarded by the DHCP relay agent at Layer 3. | The value is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **dhcp set ttl** command is used on DHCP relay agents. When a DHCP relay agent forwards DHCP Discovery messages at Layer 3, it reduces the TTL value of the messages by 1 by default. Assume that the TTL value of a DHCP Discovery message received by the DHCP relay agent is 1. If the DHCP relay agent reduces the TTL value by 1, the TTL value changes to 0. The next-hop routing device will discard the message as its TTL value is 0. As a result, the DHCP server cannot receive the DHCP Discovery message forwarded by the DHCP relay agent. To ensure that the DHCP server can receive the DHCP Discovery message sent from the client, run the **dhcp set ttl** command to set the TTL value of the DHCP Discovery message to a non-zero value after the message is forwarded at Layer 3.If the DHCP relay agent connects to a special client whose TTL value of DHCP Discovery messages is 1, and if there are routing devices between the DHCP relay agent and DHCP server, run the **dhcp set ttl ttl-value** command to specify a fixed TTL value (16 is recommended) for DHCP Discovery messages after they are forwarded by the DHCP relay agent at Layer 3.

**Prerequisites**

The DHCP function has been enabled globally using the **dhcp enable** command.


Example
-------

# Set the TTL value of DHCP Discovery messages to 16 after the messages are forwarded by the DHCP relay agent at Layer 3.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp set ttl 16

```