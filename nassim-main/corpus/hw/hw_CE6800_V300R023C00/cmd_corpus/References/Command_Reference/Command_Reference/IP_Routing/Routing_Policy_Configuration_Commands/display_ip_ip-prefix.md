display ip ip-prefix
====================

display ip ip-prefix

Function
--------

The **display ip ip-prefix** command displays the IP prefix list.



Format
------

**display ip ip-prefix** [ *pfName* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pfName* | Specifies the name of the IP prefix list to be displayed. If ip-prefix-name is not specified, all the configured IP prefix lists are displayed. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To view details of the IP prefix list, the number of routes that match the route-policy, and the number of routes that do not match the route-policy, run the **display ip ip-prefix** command.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the IP prefix list named p1.
```
<HUAWEI> display ip ip-prefix p1
ip-prefix p1
Description prefixok
  total permitted: 0             denied: 0   
    index 10           permit 10.1.1.1/32                          ge 24  le 32
    index 4294967295   permit 10.133.133.133/32                    ge 24
ip-prefix ab
  total permitted: 0             denied: 0                          
    index 10           permit 10.1.1.1/32
    index 20           deny   10.3.3.3/32

```


**Table 1** Description of the
**display ip ip-prefix** command output

| Item | Description |
| --- | --- |
| ip-prefix | Name of the IPv4 prefix list. |
| Description | Description of an IPv4 prefix list. This field is displayed only after a description is configured using the ip ip-prefix ip-prefix-name description text command. |
| permit | Contents of the entry in the IP prefix list. |
| ge | Greater than or equal to. |
| le | Less than or equal to. |
| total permitted | Number of routes that match the route-policy. |
| index | Index of the entry in the IP prefix list. |
| denied | Number of unmatched routes. |