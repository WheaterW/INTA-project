acl name (ARP-based ACL)
========================

acl name (ARP-based ACL)

Function
--------



The **acl name** command creates an ARP-based ACL and displays the ACL view. If the ARP-based ACL to be created already exists, running this command directly displays the ACL view.



By default, no ARP-based ACL is created.


Format
------

**acl name** *arp-acl-name* **arp**

**acl name** *arp-acl-name* [ **number** ] *arp-acl-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp** | Creates an ARP-based ACL with a keyword. | - |
| **name** *arp-acl-name* | Creates an ARP-based ACL with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **number** *arp-acl-number* | Creates an ARP-based ACL with a number. | The value is an integer ranging from 23000 to 23999. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An ARP-based ACL defines rules for filtering packets based on the source or destination IP or MAC addresses of ARP packets. To create an ARP-based ACL, run the acl command.



**Configuration Impact**



The **undo acl all** command deletes all types of ACLs on a device. If the ACLs being deleted are applied to services, these services are interrupted. Before deleting an ACL, ensure that the ACL is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created ARP-based ACL. Then the ACL rule can be applied to match packets.Run the **description** command to configure a description for a created ARP-based ACL. The description can contain the functions of the ARP-based ACL, facilitating applications.




Example
-------

# Create an ARP-based ACL named arp-acl.
```
<HUAWEI> system-view
[~HUAWEI] acl name arp-acl arp

```

# Create an ARP-based ACL named arp-acl and numbered 23999.
```
<HUAWEI> system-view
[~HUAWEI] acl name arp-acl number 23999

```