direct-routes
=============

direct-routes

Function
--------



The **direct-routes** command enables the direct routes delivered by IS-IS to carry IS-IS route attributes.

The **undo direct-routes** command restores the default configuration.



By default, the direct routes delivered by IS-IS carry their own route attributes.


Format
------

**direct-routes protocol-attribute-update**

**undo direct-routes protocol-attribute-update**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **protocol-attribute-update** | Enables the direct routes delivered by IS-IS to carry IS-IS route attributes. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the cost and tag values of direct routes delivered by IS-IS are both 0. Interface 1 is enabled in IS-IS process 1. When IS-IS process 2 imports the routes of IS-IS process 1, the routes of interface 1 can be imported, but the cost attribute is 0 by default. After this command is run, the interface inherits the cost and tag values configured in IS-IS process 1.

**Prerequisites**

An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.


Example
-------

# Enable the direct routes delivered by IS-IS to carry IS-IS route attributes.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] direct-routes protocol-attribute-update

```