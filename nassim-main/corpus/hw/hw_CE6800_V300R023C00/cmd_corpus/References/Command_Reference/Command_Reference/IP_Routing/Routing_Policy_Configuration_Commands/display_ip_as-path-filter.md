display ip as-path-filter
=========================

display ip as-path-filter

Function
--------

The **display ip as-path-filter** command displays the detailed configurations of the AS\_Path filter.



Format
------

**display ip as-path-filter** [ *as-path-filter-number* | *as-path-filter-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-path-filter-number* | Specifies the number of an AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string ranging from 1 to 51. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To check detailed configurations of an AS\_Path filter, run the display ip as-path-filter command.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the configured AS\_Path filter.
```
<HUAWEI> display ip as-path-filter
As path filter number: 1
          index: 10     permit    1.1 100,200
As path filter name: abc
          index: 10     deny      2.2 200,400

```


**Table 1** Description of the
**display ip as-path-filter** command output

| Item | Description |
| --- | --- |
| As path filter number | Number of an AS\_Path filter. |
| As path filter name | Name of an AS\_Path filter. |
| permit | Matching mode: permit. |
| deny | Matching mode: deny. |
| index | Sequence number of an AS\_Path filter. |