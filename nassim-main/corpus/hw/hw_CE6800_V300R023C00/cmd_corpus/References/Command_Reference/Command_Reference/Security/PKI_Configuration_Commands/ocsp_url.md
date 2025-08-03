ocsp url
========

ocsp url

Function
--------



The **ocsp url** command configures the Uniform Resource Locator (URL) address for the Online Certificate Status Protocol (OCSP) server.

The **undo ocsp url** command deletes the URL address of the OCSP server.



By default, an OCSP server does not have a URL address.


Format
------

**ocsp url** [ **esc** ] *url-address*

**undo ocsp url**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **esc** | Indicates that the URL address is in ASCII mode. | - |
| *url-address* | Indicates the OCSP server's URL address. | The value is a string starting with http:// and consisting of 1 to 128 case-sensitive characters without spaces. |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a certificate to be checked through OCSP does not contain the AIA option, run this command to configure the OCSP server's URL. If the certificate contains the AIA option, run the **ocsp-url from-ca** command to configure the PKI entity to obtain OCSP server's URL from the AIA option.

**Precautions**

The certificate revocation status can be checked only after the PKI realm is associated with a specified CA using the **ca-name** command.The command line containing the question mark (?) cannot be directly entered on the device. The keyword esc is used to support the input of the URL containing the question mark (?) in ASCII format. The URL must be in \x3f format, where 3f is the hexadecimal ASCII code of the question mark (?). For example, if the actual URL to be configured is http://www.abc.com?page1, the actual URL to be entered is http://www.abc.com\x3fpage1. If the administrator needs to configure both the question mark (?) and \x3f (http://www.abc.com?page1\x3f), the escape character \ is used, that is, the URL to be entered is http://www.abc.com\x3fpage1\\x3f.


Example
-------

# Set the OCSP server's URL address to http://10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] pki realm test
[*HUAWEI-pki-realm-test] ocsp url http://10.1.1.1

```