Configuring BGP4+ Filters
=========================

BGP4+ filters can be used in routing policies or when you want to check BGP4+ running status as required.

#### Context

BGP4+ provides the following types of filters, which can be used to query BGP4+ running status or used in routing policies:

* [AS\_Path filter](#EN-US_TASK_0172366451__step411579934214039)
  
  The AS\_Path filter filters BGP4+ routes by the AS\_Path attribute and filters out unqualified routes. Multiple rules (permit or deny) can be specified in a filter.
* [Community filter](#EN-US_TASK_0172366451__cmd1328648366214039)
  
  The community filter consists of multiple community attribute lists. There are two types of community attribute lists: standard community access lists and extended community access lists.
* [IPv6 address prefix list](#EN-US_TASK_0172366451__cmd638172392510)
  
  Before configuring a conditional BGP4+ route advertisement policy, you need to create an IPv6 address prefix list.

#### Procedure

* Configure the AS\_Path filter.
  1. Run 
     [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip as-path-filter**](cmdqueryname=ip+as-path-filter) { *as-path-filter-number* | *as-path-filter-name* } [ **index**
     *index-number* ]
     *matchMode*
     *regular-expression*
     
     
     
     The AS\_Path filter is configured.
     
     After the [**peer as-path-filter**](cmdqueryname=peer+as-path-filter) command is used to apply a routing policy to BGP4+ routes, the AS\_Path filter filters out unqualified routes.
     
     The AS\_Path filter uses the regular expression to define matching rules. A regular expression consists of the following parts:
     
     + Metacharacter: defines matching rules.
     + General character: defines matching objects.
     
     For example, ^10 indicates that only the AS\_Path attribute with the first value being 10 is matched. A circumflex (^) indicates that the beginning of a character string is matched.
     
     Multiple rules, permit or deny, can be specified in a filter. The relationship between these rules is "OR". This means that if a route meets one of the matching rules, it matches the AS\_Path filter.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For details on the regular expression, see **Regular Expression** in "Command Display Mode" of "How to Use the CLI" in *HUAWEI NE40E-M2 series
     Universal Service Router Configuration Guide - Basic Configuration*.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the community filter.
  
  
  
  Community filters are classified into two types: standard community filters and advanced community filters. Advanced community filters support regular expressions and are more flexible than standard community filters.
  
  
  
  1. Run 
     [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a community filter.
     
     
     + To configure a standard community filter, run the [**ip community-filter basic**](cmdqueryname=ip+community-filter+basic) 
       *basCfName* [ **index**
       *index-val* ] *matchMode* [ *cmntyStr* | *cmntyNum* | **internet**
       | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20> or [**ip community-filter**](cmdqueryname=ip+community-filter) 
       *cfIndex* [ **index**
       *index-val* ] *matchMode* [ *cmntyStr* | *cmntyNum* | **internet**
       | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20> command.
     + To configure an advanced community filter, run the [**ip community-filter**](cmdqueryname=ip+community-filter) { **advanced**
       *comm-filter-name* | *adv-comm-filter-num* } [ **index**
       *index-number* ]
       *matchMode*
       *regular-expression* command.
  3. Run 
     [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a Large-community filter.
  
  
  
  There are two types of Large-community filters: basic Large-community filters and advanced Large-community filters. Advanced Large-community filters support regular expressions and are more flexible than basic Large-community filters.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a Large-Community filter.
     
     
     + To configure a basic Large-Community filter, run the [**ip large-community-filter**](cmdqueryname=ip+large-community-filter)
       **basic**
       *large-comm-filter-name* [ **index**
       *index-number* ] { **permit** | **deny** } { *cmntyStr* } &<1-16> command.
     + To configure an advanced Large-Community filter, run the [**ip large-community-filter**](cmdqueryname=ip+large-community-filter)
       **advanced**
       *large-comm-filter-name* [ **index**
       *index-number* ] { **permit** | **deny** } *regular-expression* command.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an extended community filter.
  1. Run 
     [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations as required to configure an extended community filter.
     
     
     
     To configure a VPN-Target extended community filter:
     
     + To configure a basic VPN-Target extended community filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *basic-extcomm-filter-num* | **basic**
       *basic-extcomm-filter-name* }
       [ **index**
       *index-number* ]  { **deny** | **permit** } { **rt**
       *extCmntyStr* } &<1-16> command.
     + To configure an advanced VPN-Target extended community filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *advanced-extcomm-filter-num* | **advanced**
       *advanced-extcomm-filter-name* }
       [ **index**
       *index-number* ]  { **deny** | **permit** } *regular-expression* command.
     
     To configure an SoO extended community filter:
     
     + To configure a basic SoO extended community filter, run the [**ip extcommunity-list soo basic**](cmdqueryname=ip+extcommunity-list+soo+basic)
       *basic-extcomm-filter-name* [ **index**
       *index-number* ] { **permit** | **deny** } { *site-of-origin* } &<1-16> command.
     + To configure an advanced SoO extended community filter, run the [**ip extcommunity-list soo advanced**](cmdqueryname=ip+extcommunity-list+soo+advanced)
       *advanced-extcomm-filter-name* [ **index**
       *index-number* ] { **permit** | **deny** } *regular-expression* command.
     
     Multiple entries can be defined in an extended community filter. The relationship between the entries is "OR". This means that if a route matches one of the rules, the route matches the filter.
  3. Run 
     [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an IPv6 address prefix list.
  
  
  
  Before configuring a conditional BGP4+ route advertisement policy, you need to create an IPv6 address prefix list.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run **filter-list ipv6-prefix**
     *name*
     
     
     
     An IPv6 address prefix list is created, and its view is displayed.
  3. Run [**prefix**](cmdqueryname=prefix)
     *address*
     *maskLen*
     
     
     
     An IPv6 address and mask are configured for the IPv6 address prefix list.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.