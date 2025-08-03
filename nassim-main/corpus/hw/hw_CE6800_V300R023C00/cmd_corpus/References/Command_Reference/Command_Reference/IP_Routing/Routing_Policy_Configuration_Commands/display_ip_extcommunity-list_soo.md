display ip extcommunity-list soo
================================

display ip extcommunity-list soo

Function
--------

The **display ip extcommunity-list soo** command displays detailed configurations of the Source of Origin (SoO) extended community filter.



Format
------

**display ip extcommunity-list soo** [ *extcomm-filter-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *extcomm-filter-name* | Specifies the SoO extended community filter name. | The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

The extended community attribute is a BGP-specific attribute. An extended community filter is used to filter VPN routes.

You can run the
**display ip extcommunity-list soo** command to:

* View detailed information about a configured SoO extended community filter.
* Check whether an SoO extended community filter has been deleted after running the **undo ip extcommunity-list soo** command.

**Precautions**

The **display ip extcommunity-list soo** command:

* Displays the configuration of a specified SoO extended community filter if the name of the SoO extended community filter is specified.
* Displays the configuration of all SoO extended community filters if no SoO extended community filter name is specified.
* Does not display any information if the SoO extended community filter does not exist in the system or the extended community filter that is queried does not exist.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display all SoO extended community filters.
```
<HUAWEI> display ip extcommunity-list soo
Named Extended Community SoO basic list: aaa
  index 10            permit 1.2.3.4:5
Named Extended Community SoO advanced list: bbb
  index 20            deny   0755:*"

```


**Table 1** Description of the
**display ip extcommunity-list soo** command output

| Item | Description |
| --- | --- |
| Named Extended Community SoO basic list | Basic SoO extended community filter name. |
| Named Extended Community SoO advanced list | Advanced SoO extended community filter name. |
| permit | Matching mode (permit). |
| deny | Matching mode (deny). |
| index | Sequence number of an SoO extended community filter. |