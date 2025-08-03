display traffic classifier
==========================

display traffic classifier

Function
--------



The **display traffic classifier** command displays the traffic classifier configuration on the device.




Format
------

**display traffic classifier** [ *classifier-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **classifier** *classifier-name* | Displays the configuration of a specified traffic classifier. If the name of a traffic classifier is not specified, the configuration of all traffic classifiers is displayed. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display traffic classifier command displays the configuration of a specified traffic classifier or all traffic classifiers. The command output helps you check the traffic classifier configuration and locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of all traffic classifiers on the device.
```
<HUAWEI> display traffic classifier
  Traffic Classifier Information:  
    Classifier: c1
      Type: AND
      Rule(s):
        if-match vlan 120
                                        
    Classifier: c2
      Type: AND
      Rule(s): 
        if-match vlan 110
             
    Classifier: c3
      Type: AND
      Rule(s):
        if-match vlan 100
             
Total classifier number is 3

```

**Table 1** Description of the **display traffic classifier** command output
| Item | Description |
| --- | --- |
| Classifier | Traffic classifier name. To create a traffic classifier, run the traffic classifier command. |
| Total classifier number is 3 | Total number of created traffic classifiers. |
| Type | Relationship between rules in the traffic classifier. To configure the relationship between rules in a traffic classifier, run the traffic classifier command. |
| Rule(s) | Rule in a traffic classifier. |