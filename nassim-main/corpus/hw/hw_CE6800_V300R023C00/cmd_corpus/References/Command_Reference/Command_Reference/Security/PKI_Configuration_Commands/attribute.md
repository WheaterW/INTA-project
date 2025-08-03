attribute
=========

attribute

Function
--------



The **attribute** command configures attribute rules for the validity time, subject name, issuer name, and alternative subject name of a certificate.

The **undo attribute** command cancels the configuration.



By default, there is no limitation on the validity time, subject name, issuer name, and alternative subject name of a certificate.


Format
------

**attribute** *id* **validity** **from** *begintime* *begindate* **to** *endtime* *enddate*

**attribute** *id* { **alt-subject-name** **fqdn** | { **issuer-name** | **subject-name** } **dn** } { **ctn** | **equ** | **nctn** | **nequ** } *attribute-value*

**attribute** *id* **alt-subject-name** **ip** { **ctn** | **equ** | **nctn** | **nequ** } *ip-address*

**undo attribute** { *id* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *id* | Specifies the number of a certificate attribute rule. | The value is an integer that ranges from 1 to 256. |
| **validity** | Indicates validity time of certificate. | - |
| **from** *begintime* | Indicates the start validity time of certificate. | The value is in the format of HH:MM:SS. HH:MM:SS indicates the hour:minute:second.  The value of HH ranges from 0 to 23; the value of MM and SS ranges from 0 to 59. |
| *begindate* | Indicates the start validity date of certificate. | The value is in the format of YYYY/MM/DD. YYYY indicates year. Its value is an integer that ranges from 2000 to 2037. MM indicates month. Its value is an integer that ranges from 1 to 12. DD indicates day. Its value is an integer that ranges from 1 to 31. |
| **to** *endtime* | Indicates the end validity time of certificate. | The value is in the format of HH:MM:SS. HH:MM:SS indicates the hour:minute:second.  The value of HH ranges from 0 to 23; the value of MM and SS ranges from 0 to 59. |
| *enddate* | Indicates the end validity date of certificate. | The value is in the format of YYYY/MM/DD. YYYY indicates year. Its value is an integer that ranges from 2000 to 2037. MM indicates month. Its value is an integer that ranges from 1 to 12. DD indicates day. Its value is an integer that ranges from 1 to 31. |
| **alt-subject-name** | Specifies the alternative subject name of certificate. | - |
| **fqdn** | Specifies the Fully Qualified Domain Name (FQDN) of a PKI entity. | - |
| **issuer-name** | Indicates the name of certificate issuer. | - |
| **subject-name** | Indicates the subject name of certificate. | - |
| **dn** | Specifies the Distinguished Name (DN) of a PKI entity. | - |
| **ctn** | Indicates the containing operation. | - |
| **equ** | Indicates the "equal" operation. | - |
| **nctn** | Indicates the non-containing operation. | - |
| **nequ** | Indicates the "negative equal" operation. | - |
| *attribute-value* | Specifies a certificate attribute value. | The value is a string of 1 to 256 case-insensitive characters. |
| **ip** | Specifies the IP address of a PKI entity. | - |
| *ip-address* | Indicates an IP address. | An IPv4 address is in dotted decimal notation, whereas an IPv6 address is in colon hexadecimal notation. |
| **all** | Indicates all attribute rules. | - |



Views
-----

Certificate attribute group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To verify the contents of a certificate, configure an attribute rule for the certificate and reference this rule in the certificate attribute-based control rule, which ensures that the certificate meeting specific conditions passes the verification.

**Precautions**

The attribute of a certificate's alternative subject name is not displayed in the format of a domain name. Therefore, dn does not appear in the attribute rule configuration of the alternative subject name.


Example
-------

# Create a certificate attribute rule, which specifies that the DN of the subject name contains character string abcde.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate attribute-group mygroup
[*HUAWEI-pki-attribute-mygroup] attribute 1 subject-name dn ctn abcde

```