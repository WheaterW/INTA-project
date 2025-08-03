maximum load-balancing (RIPng view)
===================================

maximum load-balancing (RIPng view)

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
| *number* | Specifies the maximum number of equal-cost routes for load balancing. | The value is an integer ranging from 1 to 128. The default value is 64. |



Views
-----

RIPng view


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
[~HUAWEI] ripng 1
[*HUAWEI-ripng-1] maximum load-balancing 4

```