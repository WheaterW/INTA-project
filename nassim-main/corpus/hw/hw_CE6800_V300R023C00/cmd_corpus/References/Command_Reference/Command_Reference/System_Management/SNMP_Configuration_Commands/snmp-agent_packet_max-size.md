snmp-agent packet max-size
==========================

snmp-agent packet max-size

Function
--------



The **snmp-agent packet max-size** command sets the maximum size of an SNMP message that the SNMP agent can send and receive.

The **undo snmp-agent packet max-size** command restores the default maximum size.



The default maximum size of an SNMP message that the SNMP agent can send and receive is 12000 bytes.


Format
------

**snmp-agent packet max-size** *byte-count*

**undo snmp-agent packet max-size**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *byte-count* | Specifies the maximum size of an SNMP message that the SNMP agent can send and receive. | The value is an integer ranging from 484 to 17940, in bytes. The default value is 12000. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set the maximum size of an SNMP message that the SNMP agent sends or receives, run the **snmp-agent packet max-size** command.Increasing the maximum size of an SNMP message helps prevent the problem that the NMS obtains the incomplete information about the device status.Decreasing the maximum size of an SNMP message helps prevent the problem that the NMS or device discards an SNMP message because its size exceeds the processing capability of the NMS or device.

**Configuration Impact**

The maximum size configured using the **snmp-agent packet max-size** command takes effect for the SNMP messages of all SNMP versions.NOTE:You need to increase the size of an SNMP message based on network conditions, which helps prevent transmission efficiency of SNMP messages from deteriorating.

**Precautions**

You need to increase the size of an SNMP message based on network conditions, which helps prevent transmission efficiency of SNMP messages from deteriorating.


Example
-------

# Set the maximum size of an SNMP message that the SNMP agent can receive or send to 1042 bytes.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent packet max-size 1042

```