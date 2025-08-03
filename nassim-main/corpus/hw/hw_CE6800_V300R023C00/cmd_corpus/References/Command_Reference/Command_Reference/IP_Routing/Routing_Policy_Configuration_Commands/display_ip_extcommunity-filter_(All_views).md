display ip extcommunity-filter (All views)
==========================================

display ip extcommunity-filter (All views)

Function
--------

The **display ip extcommunity-filter** command displays detailed configurations of the VPN-Target extended community filter.



Format
------

**display ip extcommunity-filter** *extcomm-filter-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *extcomm-filter-name* | Specifies the VPN-Target extended community filter name. | The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

The extended community attribute is a private attribute of BGP. An extended community filter is used to filter VPN routes.

You can run the
**display ip extcommunity-filter** command to:

* Check detailed information about a configured VPN-Target extended community filter.
* Check whether the VPN-Target extended community filter is successfully deleted after running the **undo ip extcommunity-filter** command.

**Precautions**

When you run the **display ip extcommunity-filter** command:

* The configuration of a specified VPN-Target extended community filter is displayed if the number or name of the VPN-Target extended community filter is specified.
* The configuration of all VPN-Target extended community filters is displayed if neither the number nor the name of the VPN-Target extended community filter is specified.
* No information is displayed if the VPN-Target extended community filter does not exist in the system or the VPN-Target extended community filter to be queried does not exist.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display all VPN-Target extended community filters.
```
<HUAWEI> display ip extcommunity-filter
Extended Community filter Number: 10
  index: 10     permit rt 100:10
Extended Community filter Number: 200
  index: 10     permit 650
Extended Community filter basic filter: bas-abc
  index: 10     permit rt 200:10
Extended Community filter advanced filter: adv-abc
  index: 10     deny 1.1.1.1

```


**Table 1** Description of the
**display ip extcommunity-filter (All views)** command output

| Item | Description |
| --- | --- |
| Extended Community filter Number | Number of VPN-Target extended community filter. |
| Extended Community filter basic filter | Name of basic VPN-Target extended community filter. |
| Extended Community filter advanced filter | Name of advanced VPN-Target extended community filter name. |
| permit | Matching mode (permit). |
| rt | Extended community attribute of the route target (RT). |
| deny | Matching mode (deny). |
| index | Sequence number of VPN-Target extended community filter. |