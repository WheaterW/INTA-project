display ip extcommunity-list encapsulation
==========================================

display ip extcommunity-list encapsulation

Function
--------

The **display ip extcommunity-list encapsulation** command displays configurations of a specified or all encapsulation extended community filters.



Format
------

**display ip extcommunity-list encapsulation** [ *name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies the name of an encapsulation extended community filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

An extended community filter is mainly used to filter EVPN routes.

You can run the
**display ip extcommunity-list encapsulation** command to:

* Check the configurations of existing encapsulation extended community filters.
* Check whether an encapsulation extended community filter is deleted successfully after running the **undo ip extcommunity-list encapsulation** command.

**Precautions**

Before using the **display ip extcommunity-list encapsulation** command, note the following:

* If encapsulation-name is specified, the command displays the configurations of the specified encapsulation extended community filter only.
* If encapsulation-name is not specified, the command displays the configurations of all encapsulation extended community filters.
* If no encapsulation extended community filters exist or the specified encapsulation extended community does not exist, the command does not display information.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display configurations of encapsulation extended community filters.
```
<HUAWEI> display ip extcommunity-list encapsulation
Named Extended Community Encapsulation basic list: a
    index: 10            deny       0:8
Named Extended Community Encapsulation advanced list: b
    index: 10            permit     0:*

```


**Table 1** Description of the
**display ip extcommunity-list encapsulation** command output

| Item | Description |
| --- | --- |
| Named Extended Community Encapsulation basic list | Name of the basic encapsulation extended community filter. |
| Named Extended Community Encapsulation advanced list | Name of the advanced encapsulation extended community filter. |
| deny | Deny matching mode. |
| permit | Permit matching mode. |
| index | Index of the encapsulation extended community filter. |