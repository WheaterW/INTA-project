ip ip-prefix
============

ip ip-prefix

Function
--------



The **ip ip-prefix** command configures an IP prefix list or one entry in the IP prefix list.

The **undo ip ip-prefix** command deletes an IP prefix list or one entry in the IP prefix list.



By default, no IP prefix list is configured.


Format
------

**ip ip-prefix** *ip-prefix-name* [ **index** *index-number* ] *matchMode* *ipv4-address* *masklen* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]

**undo ip ip-prefix** *ip-prefix-name* [ **index** *index-number* ]

**undo ip ip-prefix** *ip-prefix-name* *ipv4-address* *masklen* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters. The character string can contain spaces if it is enclosed in double quotation marks (""). |
| **index** *index-number* | Specifies the sequence number of the entry in the IP prefix list. | The value is an integer ranging from 1 to 4294967295.  By default, the sequence number increases with a step of 10 according to the configuration order, and the first number is 10. |
| *matchMode* | Specifies the matching mode of the IP prefix list. | The value is an enumerated type:   * permit: Specifies the matching mode of the IP prefix list as permit. In permit mode, if the IP address to be filtered is in the defined prefix range, the IP address matches the route-policy and no longer match against the next entry. Otherwise, the IP address continues to match against the next entry. * deny: Specifies the matching mode of the IP prefix list as deny. In deny mode, if the IP address to be filtered is in the defined prefix range, the IP address fails to match the route-policy and cannot match against the next entry. Otherwise, the IP address continues to match against the next entry. |
| *ipv4-address* | Specifies the IP address. | It is in dotted decimal notation. |
| *masklen* | Specifies the mask length. | The value is an integer ranging from 0 to 32. |
| **match-network** | Matches the network address. match-network is used to match routes to a specified network address and can be configured only when ipv4-address is 0.0.0.0. For example, ip ip-prefix prefix1 permit 0.0.0.0 8 matches all the routes with the mask length of 8, and ip ip-prefix prefix1 permit 0.0.0.0 8 match-network matches all the routes with the mask length ranging from 0.0.0.1 to 0.255.255.255. | - |
| **greater-equal** *greater-equal-value* | Specifies the minimum value of the mask length range. | The value of greater-equal-value is subject to the following rule: masklen<=greater-equal-value<=less-equal-value<=32. |
| **less-equal** *less-equal-value* | Specifies the maximum value of the mask length range. | The value of less-equal-value is subject to the following rule: masklen<=greater-equal-value<=less-equal-value<=32. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An IP prefix list can be used as a filter or as filtering conditions of a route-policy when it is used with the **if-match** command.Each entry in an IP prefix list can be used as a filtering rule. When a route to be filtered matches an entry, whether the route matches the IP prefix list is determined by the matching mode. A route to be filtered matches an entry or entries based on the following rules:

* Sequential matching: The route has to match the entries in the IP prefix list in ascending order of their <producer-pid> values. Therefore, specifying <producer-pid> in a required sequence is recommended.
* One-time matching: If a route matches one entry, the route matches the IP prefix list and will not be matched against the next entry.
* Matching failure by default: If a route fails to match any of the entries, it fails to match the IP prefix list.The following example shows how different IP prefix lists take effect on the routes 1.1.1.0/24, 1.1.1.1/32, 1.1.1.0/26, 2.2.2.0/24, and 1.1.0.0/16.
* Case1:ip ip-prefix aa index 10 permit 1.1.1.0 24Matching result: Only the route 1.1.1.0/24 is permitted, and the other routes are denied.Note: This is a single-node accurate matching case, which indicates that only the route whose destination IP address and mask are the same as those specified by the entry meets the filtering conditions. In addition, permit is configured as the matching mode. Therefore, the route 1.1.1.0/24 is permitted, and other routes are denied because they fail to meet the filtering conditions.
* Case2:ip ip-prefix aa index 10 deny 1.1.1.0 24Matching result: All routes are denied.Note: This is also a single-node accurate matching case. deny is configured as the matching mode. Therefore, the route 1.1.1.0/24 is denied, and the other routes are denied based on the rule of matching failure by default because they fail to meet the filtering conditions.
* Case3:ip ip-prefix aa index 10 permit 1.1.1.0 24 less-equal 32Matching result: The routes 1.1.1.0/24, 1.1.1.1/32, and 1.1.1.0/26 are permitted, and the other routes are denied.Note: This is also a single-node accurate matching case. permit is configured as the matching mode, and less-equal is set to 32. Therefore, the routes with 1.1.1.0 as the prefix and the mask ranging from 24 to 32 can be permitted, and the other routes are denied based on the rule of matching failure by default because they fail to meet the filtering conditions.
* Case4:ip ip-prefix aa index 10 permit 1.1.1.0 24 greater-equal 24 less-equal 32Matching result: The routes 1.1.1.0/24, 1.1.1.1/32, and 1.1.1.0/26 are permitted, and the other routes are denied.Note: This is also a single-node accurate matching case. permit is configured as the matching mode, greater-equal is set to 24, and less-equal is set to 32. Therefore, the routes with 1.1.1.0 as the prefix and the mask ranging from 24 to 32 can be permitted, and the other routes are denied based on the rule of matching failure by default because they fail to meet the filtering conditions. This case is similar to case 3 in terms of the matching result.
* Case5:ip ip-prefix aa index 10 permit 1.1.1.0 24 greater-equal 26Matching result: The routes 1.1.1.1/32 and 1.1.1.0/26 are permitted, and the other routes are denied.Note: This is also a single-node accurate matching case. permit is configured as the matching mode, and greater-equal is set to 26. Therefore, the routes with 1.1.1.0 as the prefix and the mask ranging from 26 to 32 can be permitted, and the other routes are denied based on the rule of matching failure by default because they fail to meet the filtering conditions.
* Case6:ip ip-prefix aa index 10 permit 1.1.1.0/24 greater-equal 26 less-equal 32Matching result: The routes 1.1.1.1/32 and 1.1.1.0/26 are permitted, and the other routes are denied.Note: This is also a single-node accurate matching case. permit is configured as the matching mode, greater-equal is set to 26, and less-equal is set to 32. Therefore, the routes with 1.1.1.0 as the prefix and the mask ranging from 26 to 32 can be permitted, and the other routes are denied based on the rule of matching failure by default because they fail to meet the filtering conditions. This case is similar to case 5 in terms of the matching result.
* Case7:ip ip-prefix aa index 10 deny 1.1.1.0 24ip ip-prefix aa index 20 permit 1.1.1.1 32Matching result: The route 1.1.1.1/32 is permitted, and the other routes are denied.Note: This is a multi-node accurate matching case. deny is configured as the matching mode of the matching entry indexed 10, and therefore the route 1.1.1.0/24 is denied by the matching entry indexed 10 based on the rule of one-time matching. The route 1.1.1.1/32 fails to match the filtering conditions, and it is then matched against the entry indexed 20 for which permit is configured as the matching mode. Consequently, the route 1.1.1.1/32 matches the filtering conditions of the entry indexed 20. The other routes are denied based on the rule of matching failure by default because they fail to meet the filtering conditions.If the IP prefix is 0.0.0.0 and you specify a mask and a mask length range after this IP prefix, all routes with the mask length within the specified mask length range are denied or permitted, regardless of the mask.
* Case8:ip ip-prefix aa index 10 permit 0.0.0.0 8 less-equal 32Matching result: The routes 1.1.1.0/24, 1.1.1.1/32, 1.1.1.0/26, 2.2.2.0/24, and 1.1.0.0/16 are all permitted.Note: The mask length range is from 8 to 32, 0.0.0.0 is specified as the IP address, and permit is configured as the matching mode. Therefore, all routes with the mask length within the range are permitted.
* Case9:ip ip-prefix aa index 10 deny 0.0.0.0 24 less-equal 32ip ip-prefix aa index 20 permit 0.0.0.0 0 less-equal 32Matching result: The route 1.1.0.0/16 is permitted, and the other routes are denied.Note: For the entry indexed 10, the mask length range is from 24 to 32, 0.0.0.0 is specified as the IP address, and deny is configured as the matching mode. Therefore, all routes with the mask length within the range are denied, and the route 1.1.0.0/16 that fails to match its filtering conditions is then matched against the entry indexed 20. For the entry indexed 20, the mask length range is from 0 to 32, 0.0.0.0 is specified as the IP address, and permit is configured as the matching mode. Therefore, the route 1.1.0.0/16 is permitted by the entry indexed 20.
* Case10:ip ip-prefix aa index 10 deny 2.2.2.0 24ip ip-prefix aa index 20 permit 0.0.0.0 0 less-equal 32Matching result: All routes except the route 2.2.2.0/24 are permitted.Note: For the entry indexed 10, deny is configured as the matching mode. Therefore, the route 2.2.2.0/24 that matches its filtering conditions is denied, and the other routes that fail to match the filtering conditions are then matched against the entry indexed 20. For the entry indexed 20, the mask length range is from 0 to 32, 0.0.0.0 is specified as the IP address, and permit is configured as the matching mode. Therefore, all routes except the route 2.2.2.0/24 are permitted by the entry indexed 20.

**Configuration Impact**



If you create an entry whose <producer-pid> has existed in the same IP prefix list but has different filtering rules, the new entry overwrites the existing one.



**Precautions**



Because of the matching failure by default, if one or more than one entry with deny as the matching mode is created, create an entry using the ip ip-prefix ip-prefix-name [ index index-number ] permit 0.0.0.0 0 less-equal 32 command so that all IPv4 routes may match the IP prefix list.If ipv4-address mask-length is specified as 0.0.0.0 0, only default routes are matched.If ipv4-address mask-length is set to 0.0.0.0 0 less-equal 32, all routes are matched.The IP prefix lists in use cannot be deleted.After a configuration is delivered, the device checks the validity of the parameters in the configuration and processes these parameters. After the processing, the generated configuration is the result of the AND calculation between the specified ipv4-address and mask-length. For example, if the specified ipv4-address and mask-length are 1.1.1.1 and 24, respectively, the generated configuration is 1.1.1.0 24.If the ipv4-address in the generated configuration is 0.0.0.0, the configuration matches all IPv4 addresses.




Example
-------

# Configure the IP prefix list named p3 to deny the routes to the IP address range from 0.0.0.1 to 0.255.255.255.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p3 index 10 deny 0.0.0.0 8 match-network
[*HUAWEI] ip ip-prefix p3 index 20 permit 0.0.0.0 0 less-equal 32

```

# Configure the IP prefix list named p2 to permit only the routes with the mask length ranging from 17 to 18.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p2 permit 0.0.0.0 0 greater-equal 17 less-equal 18

```

# Configure an IP prefix list named p1, permitting only the routes with the mask length 17 or 18 and on network segment 10.0.0.0/8.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p1 permit 10.0.0.0 8 greater-equal 17 less-equal 18

```