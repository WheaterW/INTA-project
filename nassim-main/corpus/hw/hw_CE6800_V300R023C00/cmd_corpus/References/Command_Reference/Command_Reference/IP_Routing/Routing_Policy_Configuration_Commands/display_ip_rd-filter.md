display ip rd-filter
====================

display ip rd-filter

Function
--------

The **display ip rd-filter** command displays detailed information about the configured route distinguisher (RD) filter.



Format
------

**display ip rd-filter** [ *rdfIndex* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rdfIndex* | Specifies the number of an RD filter. | The value is an integer in the range from 1 to 1024. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To view detailed information about the configured RD filter, run the **display ip rd-filter** command.

If rd-filter-number is not specified, the
**display ip rd-filter** command displays detailed information about all configured RD filters.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display detailed information about the configured RD filter.
```
<HUAWEI> display ip rd-filter
Route Distinguisher Filter 1
        index: 10     permit 1.1.1.1:1 2.2.2.2:* 100:1 200:*
Route Distinguisher Filter 2
        index: 10     deny 1:1 2:2
        index: 20     permit 1:* 2:*

```


**Table 1** Description of the
**display ip rd-filter** command output

| Item | Description |
| --- | --- |
| Route Distinguisher Filter | Number of the RD filter. |
| permit | Matching mode, which is permit. |
| deny | Deny matching mode. |
| index | Sequence number of the RD filter. |