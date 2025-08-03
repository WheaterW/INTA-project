acl name (user-defined ACL)
===========================

acl name (user-defined ACL)

Function
--------



The **acl name** command creates a user-defined ACL and displays the ACL view. If the user-defined ACL to be created already exists, running this command directly displays the ACL view.



By default, no user-defined ACL is created.


Format
------

**acl name** *user-acl-name* **user**

**acl name** *user-acl-name* [ **number** ] *user-acl-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **user** | Creates a user-defined ACL with a keyword. | - |
| **name** *user-acl-name* | Creates a user-defined ACL with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **number** *user-acl-number* | Creates a user-defined ACL with a number. | The value is an integer ranging from 5000 to 5999. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A user-defined ACL defines rules for filtering packets based on contents extracted from a specified offset. To create a user-defined ACL, run the acl command.



**Configuration Impact**



The **undo acl all** command deletes all types of ACLs on a device. If the ACLs being deleted are applied to services, these services are interrupted. Before deleting an ACL, ensure that the ACL is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created user-defined ACL. Then the ACL rule can be applied to match packets. Run the **description** command to configure a description for a created user-defined ACL. The description can contain the functions of the user-defined ACL, facilitating applications.




Example
-------

# Create a user-defined ACL named user-acl and numbered 5999.
```
<HUAWEI> system-view
[~HUAWEI] acl name user-acl number 5999

```

# Create a user-defined ACL named user-acl.
```
<HUAWEI> system-view
[~HUAWEI] acl name user-acl user

```