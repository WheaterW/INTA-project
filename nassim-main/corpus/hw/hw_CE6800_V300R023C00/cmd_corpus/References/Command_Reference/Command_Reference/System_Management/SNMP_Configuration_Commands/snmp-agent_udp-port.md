snmp-agent udp-port
===================

snmp-agent udp-port

Function
--------



The **snmp-agent udp-port** command changes the port number monitored by the SNMP agent.

The **undo snmp-agent udp-port** command restores the default port number monitored by the SNMP agent.



By default, the port number monitored by the SNMP agent is 161.


Format
------

**snmp-agent udp-port** *port-number*

**undo snmp-agent udp-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the port number. | The value is 161 or an integer ranging from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The SNMP agent is an agent running on network devices. By default, the SNMP agent manages devices by monitoring port 161 on a device and responding to messages sent by the NMS. As the port number monitored is fixed, this brings security risks. For example, all attack packets may be sent to this port, which causes a network congestion.To improve device security, run the **snmp-agent udp-port** command to change the port number monitored by the SNMP agent.

**Configuration Impact**

After executing this command, SNMP Agent will listen on the newly set port. The original SNMP connection will be disconnected. The network management needs to use a new port number to connect to the device.

**Precautions**

The specified port number must be the same as that configured using the **snmp-agent udp-port** command. Otherwise, the NMS cannot be connected to the device.


Example
-------

# Set the port number monitored by the SNMP agent to 1065.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent udp-port 1065

```