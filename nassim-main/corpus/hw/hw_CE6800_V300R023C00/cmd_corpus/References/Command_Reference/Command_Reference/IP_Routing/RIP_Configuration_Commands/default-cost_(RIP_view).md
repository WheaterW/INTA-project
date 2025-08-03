default-cost (RIP view)
=======================

default-cost (RIP view)

Function
--------



The **default-cost** command sets the default cost for imported routes.

The **undo default-cost** command sets the default cost to 0 for imported routes.



By default, the cost for imported routes is 0.


Format
------

**default-cost** *cost*

**undo default-cost**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost* | Specifies the default cost for imported routes. | The value is an integer in the range 0 to 15. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run one of the following commands to set the cost for imported routes and the costs configured using the commands are in descending order of priorities.

* apply cost
* import-route (RIP)
* default-cost (RIP)

Example
-------

# Set the default cost for imported routes to 2.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] default-cost 2

```