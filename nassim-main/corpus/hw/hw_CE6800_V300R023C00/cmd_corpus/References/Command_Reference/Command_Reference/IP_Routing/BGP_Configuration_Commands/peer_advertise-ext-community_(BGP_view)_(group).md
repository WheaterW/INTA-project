peer advertise-ext-community (BGP view) (group)
===============================================

peer advertise-ext-community (BGP view) (group)

Function
--------



The **peer advertise-ext-community** command enables a device to advertise an extended community attribute to its peer.

The **undo peer advertise-ext-community** command cancels the existing configuration.



By default, a device does not advertise extended community attribute to its peer.


Format
------

**peer** *group-name* **advertise-ext-community**

**undo peer** *group-name* **advertise-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer advertise-ext-community** command is used to enable a device to advertise an extended community attribute to a specified peer.

**Precautions**

Before running the **peer advertise-ext-community** command to configure extended community attributes, you can use a routing policy to define specific community attributes.


Example
-------

# Configure a device to advertise an extended community attribute to its peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test advertise-ext-community

```