domain(aaa-view)
================

domain(aaa-view)

Function
--------

The **domain** command creates a domain and displays its view.

The **undo domain** command deletes a domain.

By default, there may be two domains called "default\_admin" and "default" on the device. The configuration under these two domains can be modified, but these two domains cannot be deleted.



Format
------

**domain** *domain-name*

**undo domain** *domain-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-name* | Specifies the name of a domain. | The value is a string of 1 to 64 case-insensitive characters. It cannot contain the following symbols: \* ? ". The value cannot be - or --. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The device can manage users through domains. A domain is the minimum user management unit. A domain name can be an ISP name or the name of a service provided by an ISP. A domain can use the default authorization attribute, and be configured with a RADIUS template and authentication and accounting schemes.If the domain to be configured already exists, the domain command displays the domain view.If a user that belongs to this domain is online, you cannot run the **undo domain** command to delete the domain.

**Prerequisites**

To perform AAA for access users, you need to apply the authentication schemes, authorization schemes, and accounting schemes in the domain view. Therefore, authentication, authorization, and accounting schemes must be configured in the AAA view in advance.



Example
-------

# Specify the domain named domain1 and access the domain view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain domain1
[*HUAWEI-aaa-domain-domain1]

```