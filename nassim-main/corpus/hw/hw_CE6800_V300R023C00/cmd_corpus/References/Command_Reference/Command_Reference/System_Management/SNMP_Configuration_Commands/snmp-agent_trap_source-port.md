snmp-agent trap source-port
===========================

snmp-agent trap source-port

Function
--------



The **snmp-agent trap source-port** command specifies the number of a source port that sends trap messages.

The **undo snmp-agent trap source-port** command restores the default number of the source port that sends trap messages.



By default, the source port that sends trap messages is a random port.


Format
------

**snmp-agent trap source-port** *port-number*

**undo snmp-agent trap source-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies a number for a source port that sends trap messages. | The value is an integer ranging from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve network security, run the snmp-agent trap source-port command to configure a specific port to send trap messages. Therefore, the user terminal's firewall allows packets with the specified port number to pass.

**Precautions**

If a device sends packets to the NMS in Inform mode, and the snmp-agent trap source-port command is run to specify the source port number, SNMP uses the new source port instead of the original port to receive response packets from the NMS. As a result, SNMP cannot use the original port to receive response packets from the NMS, and packets are retransmitted.


Example
-------

# Set the number of the source port that sends SNMP agent trap messages to 1057.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap source-port 1057
Warning: This operation will change the source port number of all trap packets.
Continue?  [Y/N]:y
Info: Succeeded in changing the source port number of trap packets. 
[*HUAWEI]

```