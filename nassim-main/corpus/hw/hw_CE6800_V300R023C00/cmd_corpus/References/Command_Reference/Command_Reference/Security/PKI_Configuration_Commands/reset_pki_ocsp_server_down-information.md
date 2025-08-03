reset pki ocsp server down-information
======================================

reset pki ocsp server down-information

Function
--------



The **reset pki ocsp server down-information** command clears the DOWN status information of the OCSP server recorded on the device.




Format
------

**reset pki ocsp server down-information** [ **url** [ **esc** ] *url-addr* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **url** *url-addr* | Specifies the OCSP server's URL address. If no URL address is specified, clear the DOWN status information on all OCSP servers. | The value is a string starting with http:// and consisting of 1 to 128 case-sensitive characters without spaces. |
| **esc** | The URL address in ASCII format is supported. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The device has a mechanism to determine whether the OCSP server is Down. When the device determines that an OCSP server cannot be connected, the device sets the status of the OCSP server to Down and does not send OCSP requests to the OCSP server within 10 minutes. However, this determination mechanism may cause misjudgment, or the server may be disconnected for an instant. You can run this command to manually clear the recorded OCSP server Down information so that the device can continue to send OCSP requests to the server.The command line containing the question mark (?) cannot be directly entered on the device. You can use the keyword esc to input a URL containing the question mark (?) in ASCII format. The format must be \x3f, where 3f is the hexadecimal ASCII code of the question mark (?). For example, if you want to enter http://abc.com?page1, the corresponding URL is http://abc.com\x3fpage1. If you want to enter both ? and \x3f (http://www.abc.com?page1\x3f), the corresponding URL is http://www.abc.com\x3fpage1\\x3f.


Example
-------

# Clear the OCSP server DOWN information of the specified URL.
```
<HUAWEI> reset pki ocsp server down-information

```