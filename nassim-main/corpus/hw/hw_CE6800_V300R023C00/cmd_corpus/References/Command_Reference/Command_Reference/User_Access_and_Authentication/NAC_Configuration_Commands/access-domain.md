access-domain
=============

access-domain

Function
--------



The **access-domain** command configures the default domain and forcible domain for user authentication in an authentication profile.

The **undo access-domain** command deletes the configured default domain and forcible domain.



By default, no default or forcible domain is configured in an authentication profile and the global default domain is adopted in user authentication.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**access-domain** *name* [ **dot1x** ] \* [ **force** ]

**undo access-domain** [ **dot1x** ] \* [ **force** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies a domain name. | The value must be the name of an existing domain. The value is a string of 1 to 64 case-insensitive characters, spaces not supported. |
| **dot1x** | Specifies a default or forcible domain for 802.1X authentication users. | - |
| **force** | Specifies the configured domain as a forcible domain.  If this parameter is not specified, the configured domain is a default domain. | - |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device manages users in domains. For example, AAA schemes and authorization information are bound to domains. During user authentication, the device assigns users to specified domains based on the domain names contained in user names. However, user names entered by many users on actual networks do not contain domain names. In this case, you can configure a default domain in an authentication profile. If users using this profile enter user names that do not contain domain names, the device manages the users in the default domain.On actual networks, user names entered by some users contain domain names and those entered by other users do not. The device uses different domains to manage the users. Because authentication, authorization and accounting (AAA) information in the domains are different, users use different AAA information. To ensure that users using the same authentication profile use the same AAA information, you can configure a forcible domain in the authentication profile for the users. The device then manages the users in the forcible domain regardless of whether entered user names contain domain names or not.

**Prerequisites**

A domain has been configured using the **domain** command in the AAA view.

**Precautions**

When you configure a default or forcible domain in an authentication profile, the domain takes effect as follows:

* If the user authentication mode (dot1x) is not specified, the domain takes effect for all access authentication users using the authentication profile. If the user authentication mode is specified, the domain takes effect only for specified users.
* If both a default domain and a forcible domain are configured, the device authenticates users in the forcible domain.
* This function takes effect only for users who go online after this function is successfully configured.


Example
-------

# Configure the forcible domain huawei in the authentication profile p1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain huawei
[*HUAWEI-aaa-domain-huawei] quit
[*HUAWEI-aaa] quit
[*HUAWEI] authentication-profile name p1
[*HUAWEI-authen-profile-p1] access-domain huawei force

```