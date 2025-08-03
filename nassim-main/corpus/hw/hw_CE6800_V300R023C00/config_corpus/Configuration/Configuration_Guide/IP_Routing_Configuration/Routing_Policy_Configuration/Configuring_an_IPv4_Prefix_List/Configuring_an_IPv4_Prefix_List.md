Configuring an IPv4 Prefix List
===============================

Configuring an IPv4 Prefix List

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IPv4 prefix list. 
   
   
   ```
   [ip ip-prefix](cmdqueryname=ip+ip-prefix) ip-prefix-name [ index index-number ] matchMode ipv4-address masklen [ greater-equal greater-equal-value ] [ less-equal less-equal-value ]
   ```
   
   A rule for setting parameters used to define a mask length range is *masklen* <= *greater-equal-value* <= *less-equal-value* <= 32. If only **greater-equal** is specified, the range of the IP prefix is [*greater-equal-value*, 32]. If only **less-equal** is specified, the range of the IP prefix is [*mask-length*, *less-equal-value*].
3. (Optional) Configure a description for the IPv4 prefix list.
   
   
   ```
   [ip ip-prefix](cmdqueryname=ip+ip-prefix) ip-prefix-name description text
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

An IPv4 prefix list is identified by its name, and each IPv4 prefix list contains one or multiple entries. Each entry is identified by an index, and can uniquely specify a matching range in the form of a network prefix. An IPv4 prefix list named **abcd** is used as an example.

```
#
ip ip-prefix abcd index 10 permit 10.0.0.0 8
ip ip-prefix abcd index 20 permit 10.1.0.0 16
```

During route matching, a device matches routes against entries in ascending order by index. If a route matches an entry, the device does not continue to match the route against a next entry.

By default, the device denies all unmatched routes. If all entries are in **deny** mode, all routes will be denied by the IPv4 prefix list. In this case, after multiple entries are specified in deny mode, define an entry **permit 0.0.0.0 0 less-equal 32** to permit all the other IPv4 routes.

![](public_sys-resources/note_3.0-en-us.png) 

If more than one IPv4 prefix entry is defined, at least one entry needs to be in permit mode.

#### Verifying the Configuration

Run the [**display ip ip-prefix**](cmdqueryname=display+ip+ip-prefix) [ *pfName* ] command to check information about the IPv4 prefix list.