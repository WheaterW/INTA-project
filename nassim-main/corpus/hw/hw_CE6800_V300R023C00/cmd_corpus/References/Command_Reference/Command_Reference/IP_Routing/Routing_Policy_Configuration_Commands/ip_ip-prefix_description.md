ip ip-prefix description
========================

ip ip-prefix description

Function
--------



The **ip ip-prefix description** command configures the description information of the IP prefix list.

The **undo ip ip-prefix description** command deletes the description information of the IP prefix list.



By default, no description information of the IP prefix list is configured.


Format
------

**ip ip-prefix** *ip-prefix-name* **description** *text*

**undo ip ip-prefix** *ip-prefix-name* **description** [ *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-prefix-name* | Specifies the name of an IP prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported.  When double quotation marks are used around the string, spaces are allowed in the string. |
| **description** *text* | Specifies the description information of the IP prefix list. | It is a string of 1 to 80 characters case-sensitive characters, with spaces supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An IP prefix list can be used as a filter or as filtering conditions of a route-policy when it is used with the **if-match** command.




Example
-------

# Configure an IP prefix list named p1.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p1 description aa

```