Understanding BGP Community Attributes
======================================

Understanding BGP Community Attributes

#### Community Attributes

A community attribute is a group of destination addresses with the same characteristics and is 4 bytes long, in the format of *aa:nn* or a community number.

* aa:nn: aa indicates an AS number and nn indicates the community identifier defined by an administrator. The value of aa or nn ranges from 0 to 65535, which is configurable. For example, if a route is from AS 100 and its community number defined by an administrator is 1, the community is 100:1.
* Community number: is an integer ranging from 0 to 4294967295. As defined in the standard protocol, 0 (0x00000000) through 65535 (0x0000FFFF) and 4294901760 (0xFFFF0000) through 4294967295 (0xFFFFFFFF) are reserved.

The community attribute is used to simplify the application, maintenance, and management of route-policies. With the community attribute used, a group of BGP peers in multiple ASs can share a route-policy. The community attribute that is a route attribute is transmitted between BGP peers and not restricted by the AS. Before advertising a route carrying a community attribute to peers, a BGP device can change the existing community attribute of this route.

The peer group allows a group of peers to share a route-policy while the community attribute allows a group of BGP routes to share a route-policy.

Communities are classified into well-known communities and user-defined communities.


#### Large-Community

The community attribute cannot identify a 4-byte AS number and has only one community attribute identifier. Sometimes, it is not flexible to use the community attribute. The large-community attribute is a new community attribute format defined to solve this problem. It is 12 bytes long and is in the format of *Global Administrator:LocalData1:LocalData2*.

*Global Administrator* can be a complete 4-byte AS number or another value. *Global Administrator*, *LocalData1*, and *LocalData2* are integers ranging from 0 to 4294967295. The values can be set as needed.

The large-community attribute can represent a 2-byte or 4-byte AS number and has two 4-byte LocalData attributes, which facilitates the flexible usage of apply route-policies. For example, the attribute can be set to ME:ACTION:YOU or ASN:Function:Parameter.

The Large-Community attribute extends and can be used together with the community attribute.