port (Monitor link group view)
==============================

port (Monitor link group view)

Function
--------



The **port** command adds an interface to a Monitor Link group and specifies the interface as an uplink or downlink interface.

The **undo port** command deletes an uplink or downlink interface from a Monitor Link group.



By default, no interface is added to a Monitor Link group.


Format
------

**port** { *interface-type* *interface-number* | *interface-name* } { **uplink** | **downlink** [ *downlink-id* ] }

**undo port** { { [ *interface-type* *interface-number* | *interface-name* ] { **uplink** | **downlink** *downlink-id* } } | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface to be added to a Monitor Link group.   * interface-type specifies the type of the interface. | - |
| *interface-number* | Specifies an interface to be added to a Monitor Link group.   * interface-number specifies the number of the interface. | - |
| *interface-name* | Specifies the interface to be added to a Monitor Link group.   * interface-type specifies the name of an interface. | - |
| **uplink** | Specifies the interface as an uplink interface. | - |
| **downlink** *downlink-id* | Specifies the interface as a downlink interface and the downlink interface number. | The value is an integer ranging from 1 to 512. If you do not specify <downlink-id>, the downlink interface number is assigned based on the configuration order. |
| **all** | Deletes all member interfaces from a Monitor Link group. | - |



Views
-----

Monitor link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A Monitor Link group consists uplink interfaces and downlink interfaces. If all uplink interfaces fail, Monitor Link sets the downlink interfaces to Down. After configuring a Monitor Link group, run the port command to add uplink and downlink interfaces to the Monitor Link group. Monitor Link checks the uplink interface in the Monitor Link group and sets the downlink interface status accordingly.



**Prerequisites**



A Monitor Link has been created using the monitor-link group command.



**Precautions**



The specified interface cannot be added to different Monitor Link groups.




Example
-------

# Add to Monitor Link group 1 and specify the interface as downlink interface 1.
```
<HUAWEI> system-view
[~HUAWEI] monitor-link group 1
[*HUAWEI-mtlk-group1] port 100GE1/0/1 downlink 1

```

# Add 100GE to Monitor Link group 1 and specify the interface as the uplink interface.
```
<HUAWEI> system-view
[~HUAWEI] monitor-link group 1
[*HUAWEI-mtlk-group1] port 100GE1/0/1 uplink

```