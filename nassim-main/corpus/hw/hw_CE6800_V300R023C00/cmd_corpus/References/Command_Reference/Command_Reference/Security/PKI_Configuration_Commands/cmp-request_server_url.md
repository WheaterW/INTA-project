cmp-request server url
======================

cmp-request server url

Function
--------



The **cmp-request server url** command specifies the URL address of a CMPv2 server.

The **undo cmp-request server url** command deletes the URL address of a CMPv2 server.



By default, the URL of a CMPv2 server is not configured.


Format
------

**cmp-request server url** [ **esc** ] *url-addr*

**undo cmp-request server url**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **esc** | Specifies the entering of URLs in the ASCII code. | - |
| *url-addr* | Specifies the URL of the CMPv2 server. | The value is a string starting with http:// and consisting of 1 to 128 case-insensitive characters without spaces. |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The URL of the CMPv2 server must be configured before certificate application. Then, the PKI entity sends a certificate application request to the CMPv2 server based on the configured URL.A command line containing the question mark (?) cannot be directly entered on the device. Therefore, use the keyword esc to input a URL containing the question mark (?) in ASCII format. The format must be \x3f, where 3f is a hexadecimal ASCII code of the question mark (?). For example, if a user wants to enter http://abc.com?page1, the corresponding URL is http://abc.com\x3fpage1. If a user wants to enter both? and \x3f (http://www.abc.com?page1\x3f), the corresponding URL is http://www.abc.com\x3fpage1\\x3f.


Example
-------

# Set the URL of the CMPv2 server for CMP session test to http://172.16.73.168:8080.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request server url http://172.16.73.168:8080

```

# Set the URL of the CMPv2 server for CMP session test to http://www.abc.com?page1\x3f.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request server url esc http://www.abc.com\x3fpage1\\x3f

```