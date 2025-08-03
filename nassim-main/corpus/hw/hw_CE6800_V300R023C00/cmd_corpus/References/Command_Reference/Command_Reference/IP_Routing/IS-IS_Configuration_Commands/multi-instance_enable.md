multi-instance enable
=====================

multi-instance enable

Function
--------



The **multi-instance enable** command configures a conventional IS-IS process as an IS-IS multi-instance process.

The **undo multi-instance enable** command restores an IS-IS multi-instance process to a conventional IS-IS process.



By default, an IS-IS process is a conventional process, and its IID is 0.


Format
------

**multi-instance enable iid** *iid-value*

**undo multi-instance enable** [ **iid** *iid-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **iid** *iid-value* | Specifies the IID of an IS-IS multi-instance process. | The value is an integer ranging from 1 to 65535. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Traditionally, only one IS-IS process can be configured on an interface. If multiple IS-IS processes are required, multiple interfaces are needed, and the interface configuration workload is heavy. To reduce the interface count and configuration workload, you can run the multi-instance enable command to configure IS-IS multi-instance processes. A conventional IS-IS process and multiple IS-IS multi-instance processes can be configured on the same interface.If no IID is manually configured for an IS-IS process, this process is referred to as a conventional IS-IS process; if an IID is manually configured for an IS-IS process, this process is referred to as an IS-IS multi-instance process.



**Precautions**



This command conflicts with bfdall-interfacesenable and ipv6bfdall-interfacesenable commands.




Example
-------

# Configure conventional IS-IS process 1 as an IS-IS multi-instance process with the IID of 3.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[~HUAWEI-isis-1] multi-instance enable iid 3

```