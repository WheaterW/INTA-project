acl (Service-RESTCONF view)
===========================

acl (Service-RESTCONF view)

Function
--------



The **acl** name command configures an HTTP ACL.

The **undo acl** command deletes an HTTP ACL.



By default, no ACL is configured.


Format
------

**acl** *acl-name*

**acl** *acl-number*

**undo acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-name* | Specifies the name of ACL rule. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *acl-number* | Specifies the ID of an ACL. | For basic ACL, the value is an integer ranging from 2000 to 2999.  For advanced ACL, the value is an integer ranging from 3000 to 3999. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

An ACL is a series of sequential rules composed of permit and deny clauses. To configure a named HTTP ACL, run the **acl** command. This limits the clients allowed to access HTTP servers, enhancing security.

**Prerequisites**

The ACL has been created using the **acl** command.

**Precautions**

If the ACL configured in this command has not been created in the system view, no client is allowed to access HTTP servers.


Example
-------

# Configure an HTTP ACL named policy1.
```
<HUAWEI> system-view
[~HUAWEI] acl name policy1
[*HUAWEI-acl4-basic-policy1] quit
[*HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] acl policy1

```

# Configure an HTTP ACL numbered 2100.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2100
[*HUAWEI-acl4-basic-2100] quit
[*HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] acl 2100

```