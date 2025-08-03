Configuring an IP Prefix List
=============================

An IP prefix list matches IPv4 or IPv6 address prefixes, which are defined by an IP address and a mask length.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure an IP prefix list.
   
   
   * To configure an IPv4 prefix list, run the [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) *ip-prefix-name* [ **index** *index-number* ] { **permit** | **deny** } *ip-address* *mask-length* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ] command.
     
     The mask length range can be expressed as *mask-length* <= *greater-equal-value* <= *less-equal-value* <= 32. If only **greater-equal** is specified, the prefix range is [*greater-equal-value*, 32]. If only **less-equal** is specified, the prefix range is [*mask-length*, *less-equal-value*].
     
     An IPv4 prefix list is identified by its name, and each list contains one or multiple entries. Each entry is identified by an index, and can uniquely specify a matching range in the form of a network prefix. An IPv4 prefix list named **abcd** is used as an example.
     
     ```
     #
     ```
     ```
     ip ip-prefix abcd index 10 permit 10.0.0.0 8
     ```
     ```
     ip ip-prefix abcd index 20 permit 10.1.0.0 16
     ```
     
     During route matching, the system checks the entries identified by indexes in ascending order. If a route matches an entry, it is no longer matched against the next entry.
     
     The IP prefix list on the NE40E denies all unmatched routes by default. If all entries are in **deny** mode, all routes will be denied by the IP prefix list. In this case, after multiple entries are specified in **deny** mode, define an entry **permit 0.0.0.0 0 less-equal 32** to permit all the other IPv4 routes.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If more than one prefix entry is defined, at least one of them must be in **permit** mode.
   * To configure an IPv6 prefix list, run the [**ip ipv6-prefix**](cmdqueryname=ip+ipv6-prefix) *ipv6-prefix-name* [ **index** *index-number* ] { **permit** | **deny** } *ipv6-address* *prefix-length* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ] command.
     
     An IPv6 prefix list is identified by its name, and each IPv6 prefix list contains one or multiple entries. Each entry can independently specify a matching range in the form of a network prefix and is identified by an index. An IPv6 prefix list named **abcd** is used as an example.
     
     ```
     #
     ```
     ```
     ip ipv6-prefix abcd index 10 permit 2001:db8:1:: 64
     ```
     ```
     ip ipv6-prefix abcd index 20 permit 2001:db8:2:: 64
     ```
     
     During route matching, the system checks the entries identified by indexes in ascending order. If a route matches an entry, the route is no longer matched against the next entry.
     
     The IP prefix list on the NE40E denies all unmatched routes by default. If all entries are in **deny** mode, all routes will be denied by the IP prefix list. In this case, after multiple entries are specified in deny mode, define an entry **permit :: 0 less-equal 128** to permit all the other IPv6 routes.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If more than one prefix entry is defined, at least one of them must be in **permit** mode.
3. (Optional) Configure a description for an IP prefix list.
   
   
   * To configure a description for an IPv4 prefix list, run the [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) *ip-prefix-name* [**description**](cmdqueryname=description) *text* command.
   * To configure a description for an IPv6 prefix list, run the [**ip ipv6-prefix**](cmdqueryname=ip+ipv6-prefix) *ipv6-prefix-name* [**description**](cmdqueryname=description) *text* command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.