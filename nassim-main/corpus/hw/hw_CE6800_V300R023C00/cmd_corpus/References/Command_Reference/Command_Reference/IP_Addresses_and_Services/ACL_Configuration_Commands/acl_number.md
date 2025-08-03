acl number
==========

acl number

Function
--------



The **acl number** command creates an ACL and displays the ACL view. If an ACL already exists, this command directly displays the ACL view.

The **undo acl number** command deletes a created ACL.



By default, no ACL has been created.


Format
------

**acl** [ **number** ] *basic-acl-number*

**acl** [ **number** ] *user-acl-number*

**acl** [ **number** ] *advance-acl-number*

**acl** [ **number** ] *link-acl-number*

**acl** [ **number** ] *arp-acl-number*

**undo acl** [ **number** ] *basic-acl-number*

**undo acl** [ **number** ] *user-acl-number*

**undo acl** [ **number** ] *advance-acl-number*

**undo acl** [ **number** ] *link-acl-number*

**undo acl all**

**undo acl** [ **number** ] *arp-acl-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl-number* | Creates a basic ACL with a number. | The value is an integer ranging from 2000 to 2999. |
| *user-acl-number* | Creates a user-defined ACL with a number. | The value is an integer ranging from 5000 to 5999. |
| *advance-acl-number* | Creates an advanced ACL with a number. | The value is an integer ranging from 3000 to 3999. |
| *link-acl-number* | Creates a Layer 2 ACL with a number. | The value is an integer ranging from 4000 to 4999. |
| *arp-acl-number* | Creates an ARP-based ACL with a number. | The value is an integer ranging from 23000 to 23999. |
| **all** | All the ACLs. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



This command is used to create an ACL with a specified number and display the ACL view. If the ACL to be created already exists, this command directly displays the ACL view.



**Configuration Impact**



The **undo acl all** command deletes all types of ACLs on a device. If the ACLs being deleted are applied to services, these services are interrupted. Before deleting an ACL, ensure that the ACL is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created ACL. Then the ACL rule can be applied to match packets.Run the **description** command to configure a description for a created advanced ACL. The description can contain the functions of the advanced ACL, facilitating applications.




Example
-------

# Create a Layer 2 ACL numbered 4999.
```
<HUAWEI> system-view
[~HUAWEI] acl number 4999

```

# Create an advanced ACL numbered 3999.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3999

```

# Create an ARP-based ACL numbered 23999.
```
<HUAWEI> system-view
[~HUAWEI] acl number 23999

```

# Create a basic ACL numbered 2999.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2999

```

# Create a user-defined ACL numbered 5999.
```
<HUAWEI> system-view
[~HUAWEI] acl number 5999

```