ssl verify certificate-chain minimum-path-length
================================================

ssl verify certificate-chain minimum-path-length

Function
--------



The **ssl verify certificate-chain minimum-path-length** command configures the minimum path length for a digital certificate chain.

The **undo ssl verify certificate-chain minimum-path-length** command cancels the minimum path length configured for a digital certificate chain.



By default, the minimum path length for a digital certificate chain is 1.


Format
------

**ssl verify certificate-chain minimum-path-length** *path-length*

**undo ssl verify certificate-chain minimum-path-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *path-length* | Specifies the minimum path length for a digital certificate chain. | The value is an integer ranging from 1 to 1024. |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Verifying a digital certificate and its path validity can avoid invalid digital certificates and improve security.

**Prerequisites**

An SSL policy has been created using the **ssl policy** command.

**Precautions**

* By default, verification on the basic constraint field pathLenConstraint (path length constraint value) is enabled.
* After the **ssl verify certificate-chain minimum-path-length** command is run, the length of a digital certificate chain is checked. If the minimum certificate path length requirement is not met, the verification fails. The minimum certificate path length refers to the complete certificate chain length for SSL handshake, including the local digital certificate.

Example
-------

# Set the minimum path length of a digital certificate chain to 3.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy abc
[*HUAWEI-ssl-policy-abc] ssl verify certificate-chain minimum-path-length 3

```