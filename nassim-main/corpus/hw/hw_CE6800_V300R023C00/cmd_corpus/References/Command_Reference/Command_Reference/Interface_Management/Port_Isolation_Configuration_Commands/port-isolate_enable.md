port-isolate enable
===================

port-isolate enable

Function
--------



The **port-isolate enable** command enables port isolation.

The **undo port-isolate enable** command disables port isolation.



By default, interface isolation is disabled.


Format
------

**port-isolate enable group** *group-id*

**undo port-isolate enable** [ **group** *group-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group** *group-id* | Specifies the ID of a port isolation group. | The value is an integer ranging from 1 to 64. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The port isolation function isolates ports in the same VLAN. Port isolation provides more secure and flexible networking solutions.



**Configuration Impact**



Interfaces in a port isolation group are isolated from each other, but interfaces in different port isolation groups can communicate.



**Precautions**



Management interfaces do not support the **port-isolate enable** command.




Example
-------

# Configure port isolation on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] port-isolate enable group 1

```