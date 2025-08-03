default-cost (RIPng view)
=========================

default-cost (RIPng view)

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

RIPng view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can perform any of the following operations to set the cost for imported routes and the costs configured in the operations are in descending order of priorities:

* Run the **apply cost** command to set the cost for routes.
* Run the import-route (RIPng) command to set the cost for imported routes.
* Run the default-cost (RIPng) command to set the default cost for imported routes.

Example
-------

# Set the default cost for imported routes to 2.
```
<HUAWEI> system-view
[~HUAWEI] ripng 100
[*HUAWEI-ripng-100] default-cost 2

```