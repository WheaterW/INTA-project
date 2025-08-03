Configuring an IPv6 Prefix List
===============================

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low latency mode does not support this configuration.


#### Context

IP prefix lists are classified as IPv4 prefix lists that apply to IPv4 routes or IPv6 prefix lists that apply to IPv6 routes. IPv4 prefix lists and IPv6 prefix lists share the same implementation. For details, see [Configuring an IPv4 Prefix List](vrp_route-policy_cfg_0004.html). [Table 1](#EN-US_TOPIC_0000001697353745__table7854510144616) describes the wildcard address-based IPv6 route matching rules.

**Table 1** Implementation of wildcard address-based route matching rules (IPv6)
| Whether *greater-equal* and *less-equal* Are Configured | Condition | Matching Rule | Command Example |
| --- | --- | --- | --- |
| Neither *greater-equal* nor *less-equal* is configured. | After the processing, *ipv6-address* and *masklen* are :: and 0, respectively. | Matches only the default IPv6 route. | An IPv6 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ipv6-prefix aa index 10 permit 2001:db8::1 0 Error: Failed to add the address prefix list ::/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ipv6-prefix aa index 10 permit :: 0 ```  Matching rule: Only the default IPv6 route is permitted. |
| After the processing, *ipv6-address* and *masklen* are :: and *X* (non-0 value), respectively. | Matches all IPv6 routes with the mask length of *X*. | Pre-processing:  ``` ip ipv6-prefix aa index 10 permit ::1:1 96 ```  Post-processing:  ``` ip ipv6-prefix aa index 10 permit :: 96 ```  Matching rule: The IPv6 routes with the mask length of 96 are permitted. |
| *greater-equal* is configured, but *less-equal* is not. | After the processing, *ipv6-address* and *masklen* are :: and 0, respectively. | Matches all the IPv6 routes whose mask lengths are within the range of *greater-equal* to 128. | An IPv6 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ipv6-prefix aa index 10 permit 2001:db8::1 0 greater-equal 16 Error: Failed to add the address prefix list ::/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ipv6-prefix aa index 10 permit :: 0 greater-equal 16 less-equal 128 ```  Matching rule: The IPv6 routes whose mask lengths are within the range of 16 to 128 are permitted. |
| After the processing, *ipv6-address* and *masklen* are :: and *X* (non-0 value), respectively. | Matches all the IPv6 routes whose mask lengths are within the range of *greater-equal* to 128. | Pre-processing:  ``` ip ipv6-prefix aa index 10 permit ::1:1 96 greater-equal 120 ```  Post-processing:  ``` ip ipv6-prefix aa index 10 permit :: 96 greater-equal 120 less-equal 128 ```  Matching rule: The IPv6 routes whose mask lengths are within the range of 120 to 128 are permitted. |
| *greater-equal* is not configured, but *less-equal* is configured. | After the processing, *ipv6-address* and *masklen* are :: and 0, respectively. | Matches all the IPv6 routes whose mask lengths are within the range of 0 to *less-equal*. | An IPv6 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ipv6-prefix aa index 10 permit 2001:db8::1 0 less-equal 120 Error: Failed to add the address prefix list ::/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ipv6-prefix aa index 10 permit :: 0 less-equal 120 ```  Matching rule: The IPv6 routes whose mask lengths are within the range of 0 to 120 are permitted. |
| After the processing, *ipv6-address* and *masklen* are :: and *X* (non-0 value), respectively. | Matches all the IPv6 routes whose mask lengths are within the range of *X* to *less-equal*. | Pre-processing:  ``` ip ipv6-prefix aa index 10 permit ::1:1 96 less-equal 120 ```  Post-processing:  ``` ip ipv6-prefix aa index 10 permit :: 96 greater-equal 96 less-equal 120 ```  Matching rule: The IPv6 routes whose mask lengths are within the range of 96 to 120 are permitted. |
| Both *greater-equal* and *less-equal* are configured. | After the processing, *ipv6-address* and *masklen* are :: and 0, respectively. | Matches all the IPv6 routes whose mask lengths are within the range of *greater-equal* to *less-equal*. | An IPv6 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ipv6-prefix aa index 10 permit 2001:db8::1 0 greater-equal 5 less-equal 30 Error: Failed to add the address prefix list ::/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ipv6-prefix aa index 10 permit :: 0 greater-equal 5 less-equal 30 ```  Matching rule: The IPv6 routes whose mask lengths are within the range of 5 to 30 are permitted. |
| After the processing, *ipv6-address* and *masklen* are :: and *X* (non-0 value), respectively. | Matches all the IPv6 routes whose mask lengths are within the range of *greater-equal* to *less-equal*. | Pre-processing:  ``` ip ipv6-prefix aa index 10 permit ::1:1 96 greater-equal 120 less-equal 124 ```  Post-processing:  ``` ip ipv6-prefix aa index 10 permit :: 96 greater-equal 120 less-equal 124 ```  Matching rule: The IPv6 routes whose mask lengths are within the range of 120 to 124 are permitted. |



#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IPv6 prefix list.
   ```
   [ip ipv6-prefix](cmdqueryname=ip+ipv6-prefix) ipv6-prefix-name [ index index-number ] matchMode  ipv6-address masklen [ match-network ] [ greater-equal greater-equal-value ] [ less-equal less-equal-value ]
   ```
3. (Optional) Configure a description for the IPv6 prefix list.
   ```
   [ip ipv6-prefix](cmdqueryname=ip+ipv6-prefix) ip-prefix-name description text
   ```
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Example

An IPv6 prefix list is identified by its name, and each IPv6 prefix list contains one or multiple entries. Each entry can independently specify a matching range in the form of a network prefix and is identified by an index. An IPv6 prefix list named **abcd** is used as an example.

```
#
ip ipv6-prefix abcd index 10 permit 2001:db8:1::1 64
ip ipv6-prefix abcd index 20 permit 2001:db8:2::2 64
```

During route matching, the system checks the entries identified by indexes in ascending order. If a route matches an entry, it is no longer matched against the next entry.

By default, the device denies all unmatched routes. If all entries are in **deny** mode, all routes will be denied by the IPv6 prefix list. In this case, after multiple entries are specified in deny mode, define an entry **permit :: 0 less-equal 128** to permit all the other IPv6 routes.

![](public_sys-resources/note_3.0-en-us.png) 

If more than one prefix entry is defined, at least one of them must be in **permit** mode.



#### Verifying the Configuration

Run the [**display ip ipv6-prefix**](cmdqueryname=display+ip+ipv6-prefix) [ *pf6Name* ] command to check information about the specified IPv6 prefix list.