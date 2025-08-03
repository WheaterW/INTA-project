lldp restart
============

lldp restart

Function
--------



The **lldp restart** command sets the delay time for initializing Link Layer Discovery Protocol (LLDP) on interfaces.

The **undo lldp restart** command restores the default delay time.



The default delay time is 2 seconds.


Format
------

**lldp restart** *delay*

**undo lldp restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay* | Specifies the delay time for initializing LLDP on interfaces. | The value is an integer ranging from 1 to 10, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If LLDP is enabled on an interface, the interface can exchange LLDP packets with neighboring nodes, learning neighbor status information while sending local status information to neighbors. By collecting status information stored on each network device, the NMS can discover the overall network topology. If LLDP alternates between Up and Down on device interfaces, the network will flap frequently.To set the delay for initializing LLDP on interfaces, run the lldp restart-delay command. This command helps prevent network flapping caused by frequent LLDP status changes on interfaces.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Configuration Impact**

The delay value must be appropriately set. You can flexibly adjust this parameter based on the network load:

* The longer the delay, the lower the frequency of network flapping. However, if the delay is too long, the device cannot flexibly trace neighbor status changes. As a result, the device cannot dynamically detect network topology of neighbors.
* The shorter the delay, the faster a device can detect neighbor status changes. This helps the device to detect network topology of neighbors in a timely manner. However, if the delay is too short, the device refreshes status information about neighbors frequently. This causes network topology flapping, increases the system load, and wastes resources.The default delay time is recommended.


Example
-------

# Set the delay time for initializing LLDP on interfaces to 1 second.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] lldp restart 1

```