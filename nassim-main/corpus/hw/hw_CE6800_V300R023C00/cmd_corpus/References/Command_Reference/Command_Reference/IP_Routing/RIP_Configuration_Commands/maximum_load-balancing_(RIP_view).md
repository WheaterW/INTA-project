maximum load-balancing (RIP view)
=================================

maximum load-balancing (RIP view)

Function
--------

By default, load balancing is supported. For details about the maximum number of equal-cost routes, see the parameter value range.


Format
------

**maximum load-balancing** *number*

**undo maximum load-balancing**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the number of equal-cost routes that can load-balance traffic. | The value is an integer ranging from 1 to 128. The default value is 64. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure the maximum number of equal-cost routes for load balancing, run the maximum load-balancing command. Bear memory capacity in mind when configuring the number.

**Configuration Impact**

If you run the command multiple times, only the latest configuration takes effect.


Example
-------

# Set the maximum number of equal-cost routes to 4.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] maximum load-balancing 4

```