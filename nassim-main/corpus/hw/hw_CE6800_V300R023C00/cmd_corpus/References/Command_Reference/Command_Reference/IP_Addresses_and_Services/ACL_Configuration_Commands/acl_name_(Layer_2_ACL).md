acl name (Layer 2 ACL)
======================

acl name (Layer 2 ACL)

Function
--------



The **acl name** command creates a Layer 2 ACL and displays the ACL view. If the Layer 2 ACL to be created already exists, running this command directly displays the ACL view.



By default, no Layer 2 ACL is created.


Format
------

**acl name** *link-acl-name* **link**

**acl name** *link-acl-name* [ **number** ] *link-acl-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *link-acl-name* | Creates a Layer 2 ACL with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **link** | Creates a Layer 2 ACL with a keyword. | - |
| **number** *link-acl-number* | Creates a Layer 2 ACL with a number. | The value is an integer ranging from 4000 to 4999. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A Layer 2 ACL defines rules for filtering packets based on Layer 2 information, such as the source MAC addresses, destination MAC addresses, and Layer 2 protocol types of packets. To create a Layer 2 ACL, run the acl command.



**Configuration Impact**



The **undo acl all** command deletes all types of ACLs on a device. If the ACLs being deleted are applied to services, these services are interrupted. Before deleting an ACL, ensure that the ACL is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created advanced ACL. Then the ACL rule can be applied to match packets.Run the **description** command to configure a description for a created advanced ACL. The description can contain the functions of the advanced ACL, facilitating applications.




Example
-------

# Create a Layer 2 ACL named link-acl.
```
<HUAWEI> system-view
[~HUAWEI] acl name link-acl link

```

# Create a Layer 2 ACL named link-acl and numbered 4999.
```
<HUAWEI> system-view
[~HUAWEI] acl name link-acl number 4999

```