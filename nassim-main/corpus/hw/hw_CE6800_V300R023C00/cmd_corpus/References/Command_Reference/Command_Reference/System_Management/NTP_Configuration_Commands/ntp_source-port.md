ntp source-port
===============

ntp source-port

Function
--------



The **ntp source-port** command changes the source port number of NTP packets.

The **undo ntp source-port** command restores the port number for sending NTP packets to a random port.



By default, the port number for sending NTP packets is randomly allocated.


Format
------

**ntp source-port** *portNum*

**undo ntp source-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *portNum* | Specifies the number of the port that sends NTP packets. | The number is an integer that can be 123, or ranges from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure the port that sends NTP packets as a fixed port, run this command. The user firewall can filter packets based on this port to improve the security of network packets.

**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function. To enable the NTP server function, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.




Example
-------

# Set the port number for sending NTP packets to 1026.
```
<HUAWEI> system-view
[~HUAWEI] ntp source-port 1026

```