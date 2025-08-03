display ip community-filter
===========================

display ip community-filter

Function
--------

The **display ip community-filter** command displays detailed configurations of the community filter.



Format
------

**display ip community-filter** [ *comm-filter-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *comm-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To check detailed configurations of a community filter, run the display ip community-filter command.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display all community filters.
```
<HUAWEI> display ip community-filter
Community filter Number: 10
  index: 10     permit no-export
Community filter Number: 110
  index: 10     permit 110:110
Named Community basic filter: aa
  index: 10     permit 1 internet
Named Community advanced filter: bb
  index: 10     deny ^20

```


**Table 1** Description of the
**display ip community-filter** command output

| Item | Description |
| --- | --- |
| Community filter Number | Number of a community filter. |
| permit | Matching mode (permit). |
| Named Community basic filter | Name of a basic community filter. |
| Named Community advanced filter | Name of an advanced community filter. |
| deny | Matching mode (deny). |
| index | Sequence number of a community filter. |