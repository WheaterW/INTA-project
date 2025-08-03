dns domain
==========

dns domain

Function
--------



The **dns domain** command configures a domain name suffix.

The **undo dns domain** command deletes a domain name suffix.



By default, no domain name suffix is configured.


Format
------

**dns domain** *domain-name* [ **vpn-instance** *vpn-instance-name* ]

**undo dns domain** [ *domain-name* [ **vpn-instance** *vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-name* | Specifies the suffix of a domain name. | The value is a string of 1 to 63 case-insensitive characters without spaces. The value can contain digits, letters, underscores (\_), hyphens (-), and periods (.). |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the domain name suffix applies. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The domain name suffixes of some servers or hosts accessed by the DNS client are usually the same. Pre-defining some domain name suffixes allows you to enter only parts of a domain name to be resolved. The system automatically adds a specific suffix to the domain name before resolving the domain name.For instance, if you configure "com" in the suffix list and enter "example" in a domain name query, the system automatically associates "example" with the suffix "com" and searches for "example.com." You may encounter the following situations during a resolution process:

* If you enter a domain name without a period (.), such as example, the system considers it as a host name and adds a domain name suffix to the domain name for query. If there is no matched domain name, the system searches for an IP address mapped to "example."
* If you enter a domain name with a dot (.) in the middle, for example, www.example, the system directly uses this domain name for query. If the system does not find a matched entry, it adds every configured suffix to search for an IP address mapped to the domain name.
* If you enter a domain name with a period (.) at the end, for example, example.com., the system removes the period (.) at the end of the domain name and uses the remaining part for query. If the query fails, the system adds suffixes to the domain name for query.Note 1: All the preceding queries (original domain names and changed domain names) are performed locally. If no query result is obtained, the DNS server is queried.Note 2: When the local static domain name configuration is queried, only the original requested domain name is used for query. The domain name suffix or other information is not added for query.

**Precautions**

The device supports a maximum of 10 domain name suffixes. To configure multiple domain name suffixes, you can run the dns domain command repeatedly.If the name of the suffix to be deleted is specified, the specified suffix is deleted. Otherwise, all the suffixes are deleted.


Example
-------

# Configure the domain name suffix com.cn for vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] dns domain com.cn vpn-instance vpn1

```

# Configure a domain name suffix as com.cn.
```
<HUAWEI> system-view
[~HUAWEI] dns domain com.cn

```