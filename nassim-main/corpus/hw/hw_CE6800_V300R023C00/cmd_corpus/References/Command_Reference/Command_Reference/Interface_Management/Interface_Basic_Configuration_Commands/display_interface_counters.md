display interface counters
==========================

display interface counters

Function
--------



The **display interface counters** command displays statistics about a specific interface on a device.




Format
------

**display interface counters** [ **rate** ] [ **inbound** | **outbound** ] [ *interface-name* | *interface-type* [ *interface-number* ] ]

**display interface counters** [ **rate** ] [ **inbound** | **outbound** ] [ *interface-type* ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rate** | Indicates the packet rate, which is calculated based on interface counters. If the packet rate is not specified, interface counters of specified interfaces will be listed. | - |
| **inbound** | Indicates statistics about incoming traffic. | - |
| **outbound** | Indicates statistics about outgoing traffic. | - |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies the interface type.  If interface-type is not specified, statistics about all interfaces are displayed. | - |
| *interface-number* | Specifies the interface number.  If interface-number is not specified, statistics about all interfaces of a specific type are displayed. | - |
| **slot** *slot-id* | Specifies the slot number.  If slot slot-id is not specified, statistics about the interface in all slots are displayed. | The value is a string of 1 to 23 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view statistics about a specific interface, run the **display interface counters** command, which helps locate interface faults.



**Precautions**



Before running the **display interface counters** command to display the traffic statistics information on an interface, you are advised to run the **reset interface counters** command to clear the traffic statistics on the interface.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about 100GE1/0/1 interface on the device.
```
<HUAWEI> display interface counters rate 100GE 1/0/1
Inbound
Interface   Octets(bytes/s) Unicast(pkts/s) Multicast(pkts/s) Broadcast(pkts/s)
100GE1/0/1                0               0                 0                 0
Outbound
Interface   Octets(bytes/s) Unicast(pkts/s) Multicast(pkts/s) Broadcast(pkts/s)
100GE1/0/1                0               0                 0                 0

```

# Display statistics about all interfaces on a device.
```
<HUAWEI> display interface counters
Inbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                      0             0               0               0
100GE1/0/1                      0             0               0               0
MEth0/0/0                       0             0           16651            3531
NULL0                           0             0               0               0
Outbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                      0             0               0               0
100GE1/0/1                      0             0               0               0
MEth0/0/0                       0             0               0               0
NULL0                           0             0               0               0

```

# Display statistics about all physically Up interfaces on the board in slot 1.
```
<HUAWEI> display interface counters slot 1
Inbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                      0             0               0               0
100GE1/0/1                      0             0               0               0
Outbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                      0             0               0               0
100GE1/0/1                      0             0               0               0

```

**Table 1** Description of the **display interface counters** command output
| Item | Description |
| --- | --- |
| Interface | Type and number of an interface. |
| Octets(bytes) | Total bytes of the incoming or outgoing traffic on the interface. |
| Unicast(pkts) | Total numbers of the incoming or outgoing unicast packets on the interface. |
| Multicast(pkts) | Total numbers of the incoming or outgoing multicast packets on the interface. |
| Broadcast(pkts) | Total numbers of the incoming or outgoing broadcast packets on the interface. |