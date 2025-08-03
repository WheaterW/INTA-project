qos lr(Management interface view)
=================================

qos lr(Management interface view)

Function
--------



The **qos lr pps** command sets the rate limit on the management interface.

The **undo qos lr** pps command restores the default rate limit on the management interface.



By default, the rate limit on the management interface is 3000 pps.


Format
------

**qos lr pps** *packets*

**undo qos lr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pps** *packets* | Specifies the maximum number of packets that are allowed to pass per second. | The value is an integer that ranges from 100 to 10240. The default value is 3000. |



Views
-----

Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If there is heavy traffic on the management interface caused by malicious attacks or network exceptions, the CPU is overloaded and services are interrupted. To prevent this problem, run the **qos lr pps** command to set the rate limit of packets on the management interface.

**Precautions**

If a small rate limit is used, FTP and Telnet functions may be affected.If you run the **qos lr pps** command multiple times on the same interface, only the latest configuration takes effect.


Example
-------

# Set the rate limit of MEth0/0/0 to 100 pps.
```
<HUAWEI> system-view
[~HUAWEI] interface meth 0/0/0
[~HUAWEI-MEth0/0/0] qos lr pps 100

```