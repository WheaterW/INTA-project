display ssm-mapping policy
==========================

display ssm-mapping policy

Function
--------



The **display ssm-mapping policy** command displays the mapping rules of an SSM mapping policy configured on a device.




Format
------

**display ssm-mapping policy** *SsmMapPlcName* [ **group** *group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *SsmMapPlcName* | Specifies the name of an SSM mapping policy. | The value is a string of 1 to 31 case-insensitive characters without spaces. |
| **group** *group-address* | Displays SSM mapping rules of a specified multicast group. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the mapping rules of an SSM mapping policy configured on a device, run the display **ssm-mapping policy** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the mapping rules of the multicast group with the group address of 225.0.0.1 in an SSM mapping policy named policy1.
```
<HUAWEI> display ssm-mapping policy policy1 group 225.0.0.1
SSM-Mapping IPv4 conversion table: policy1
 Total 2 entries,  Total 2 entries matched
 00001. (1.1.1.1, 225.0.0.1)
 00002. (2.2.2.2, 225.0.0.1)

```

# Display the mapping rules of an SSM mapping policy named policy1.
```
<HUAWEI> display ssm-mapping policy policy1
SSM-Mapping IPv4 conversion table: policy1
 Total 2 entries,  Total 2 entries matched
00001. (1.1.1.1, 225.0.0.0/24)
00002. (2.2.2.2, 225.0.0.0/24)

```

**Table 1** Description of the **display ssm-mapping policy** command output
| Item | Description |
| --- | --- |
| SSM-Mapping IPv4 conversion table | SSM mapping rule table. |
| Total 2 entries, Total 2 entries matched | Total number of SSM mapping entries and total number of matching entries. |
| 00001. (1.1.1.1, 225.0.0.1) | ID and content of an (S, G) entry. |
| 00001. (1.1.1.1, 225.0.0.0/24) | ID and content of an (Source, Group/mask) entry. |