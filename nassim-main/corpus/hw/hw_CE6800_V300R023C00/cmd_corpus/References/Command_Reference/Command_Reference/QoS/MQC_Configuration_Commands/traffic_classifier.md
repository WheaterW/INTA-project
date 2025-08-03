traffic classifier
==================

traffic classifier

Function
--------



The **traffic classifier** command creates a traffic classifier and displays the traffic classifier view, or directly displays the view of an existing traffic classifier.

The **undo traffic classifier** command deletes a traffic classifier.



By default, no traffic classifier is created in the system.


Format
------

**traffic classifier** *classifier-name* [ **type** { **and** | **or** } ]

**undo traffic classifier** *classifier-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *classifier-name* | Specifies the name of a traffic classifier. | The value is a string of 1 to 31 case-sensitive characters without spaces and question marks, and must start with letters or digits. |
| **type** | Specifies the relationship between rules in a traffic classifier. If this parameter is not specified, the relationship between rules is OR by default. | - |
| **and** | Indicates that the relationship between rules is AND.  After this parameter is specified, the following situations occur:?If a traffic classifier contains ACL rules, packets match the traffic classifier only when the packets match one ACL rule and all the non-ACL rules.  ?If a traffic classifier does not contain ACL rules, packets match the traffic classifier only when the packets match all the non-ACL rules. | - |
| **or** | Indicates that the relationship between rules is OR.  After this parameter is specified, packets match a traffic classifier if the packets match one or more rules. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A traffic classifier classifies traffic of a certain type using matching rules. To provide differentiated services for service flows, bind a traffic classifier and a traffic behavior (see traffic behavior) to a traffic policy and apply the traffic policy.

A traffic classifier can be created based on Layer 2 information such as the 802.1p priority in the VLAN ID, VLAN ID, or Layer 2 protocol type, and Layer 3 information such as the DSCP priority or IP priority, or ACLs.

**Precautions**

* To delete a traffic classifier, unbind the traffic policy containing the traffic classifier from the system, an interface, or a VLAN where the traffic policy is applied and unbind the traffic classifier from the traffic behavior.
* On the device, a maximum of 2048 traffic classifiers can be created and multiple rules can be configured in a traffic classifier.
* Non-conflicting rules can be configured in a traffic classifier.


Example
-------

# Create a traffic classifier c1 and enter the traffic classifier view.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1]

```