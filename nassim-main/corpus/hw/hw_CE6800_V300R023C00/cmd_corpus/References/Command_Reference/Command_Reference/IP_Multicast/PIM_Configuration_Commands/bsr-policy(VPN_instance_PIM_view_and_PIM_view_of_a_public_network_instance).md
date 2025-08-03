bsr-policy(VPN instance PIM view/PIM view of a public network instance)
=======================================================================

bsr-policy(VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **bsr-policy** command limits the range of valid bootstrap router (BSR) addresses, so that a Router discards messages received from the BSRs not in the specified address range, preventing BSR spoofing.

The **undo bsr-policy** command restores the default configuration.



By default, the range of valid BSR addresses is not limited, so that a Router considers messages received from all BSRs valid.


Format
------

**bsr-policy** { *bsrPolicyAclNum* | **acl-name** *acl-name* }

**undo bsr-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bsrPolicyAclNum* | Specifies the number of a basic ACL, which defines a policy for filtering BSR messages based on source addresses. | The value is an integer ranging from 2000 to 2999.  The value of this parameter must be the same as that of the basic-acl-number parameter specified in the acl command. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM-SM network that uses the BSR mechanism, any Router can be configured as a candidate-bootstrap router (C-BSR) and participate in a BSR election. The winner of the BSR election is responsible for advertising RP information on the network. These mechanisms leave chances for BSR spoofing.

* Some malicious hosts construct pseudo BSR messages and send the messages to the Routers, attempting to change rendezvous point (RP) mappings on the Routers.Common preventive measures for such attacks: BSR messages are multicast packets with the TTL being 1. Such BSR spoofing commonly occurs on network edge Routers. Since the BSR resides inside the network while hosts reside outside the network, you can enable the Routers to perform neighbor and RPF checks on received BSR messages to filter out pseudo BSR messages.
* Attackers control some Routers on the network or a Router accesses the network illegally. The attacker can set the controlled Router as a C-BSR and make the C-BSR win the BSR election to control RP information advertisement on the network.Common preventive measures for such attacks: A Router will flood BSR messages on the network after being configured as a C-BSR. BSR messages are multicast packets being forwarded hop by hop, with the TTL being 1. Therefore, you can configure neighbors not to accept the BSR messages flooded by this Router using the **bsr-policy** command on each Router to set the range of valid BSR addresses. For example, you can set the addresses on 1.1.1.1/32 and 1.1.1.2/32 as valid BSR addresses. The Routers then do not accept or forward the messages from the BSR beyond the ranges, preventing invalid BSRs.The preceding two solutions can ensure the BSR security on the network; however, if an attacker controls a valid BSR, such a problem still exists.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

After the **bsr-policy** command is run, the Router accepts only the BSR messages passing the filtration.

**Precautions**

The **bsr-policy** command requires an ACL configured using the **acl** command. To set the range of source addresses of BSR messages, specify the source parameter in the **rule** command.


Example
-------

# In the public network instance, specify addresses on 10.1.1.0/24 as valid BSR addresses.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2001
[*HUAWEI-acl4-basic-2001] rule permit source 10.1.1.0 0.0.0.255
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] bsr-policy 2001

```