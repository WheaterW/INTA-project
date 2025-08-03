Configuring the Format of BGP 4-Byte AS Numbers
===============================================

You can change the format of BGP 4-byte AS numbers to your desired format.

#### Usage Scenario

By default, a BGP 4-byte AS number is displayed in dotted notation. If you prefer 4-byte AS numbers in integer format, perform this configuration task to change the display format of 4-byte AS numbers from dotted notation to integer.

![](../../../../public_sys-resources/notice_3.0-en-us.png) Changing the format of 4-byte AS numbers will affect matching results of AS\_Path regular expressions and extended community attribute filters. Therefore, if the system is using an AS\_Path regular expression or an extended community attribute filter as an import or export policy, you need to reconfigure the AS\_Path regular expression using the [**ip as-path-filter**](cmdqueryname=ip+as-path-filter) command or the extended community attribute filter using the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) or [**ip extcommunity-list soo**](cmdqueryname=ip+extcommunity-list+soo) command after changing the format of 4-byte BGP AS numbers. Otherwise, routes cannot match the export or import policy, and a network fault occurs.

* If 4-byte AS numbers in integer format are configured, you need to change the format of 4-byte AS numbers in AS\_Path regular expressions or extended community filters to integer accordingly.
* If 4-byte AS numbers in dotted notation are configured, you need to change 4-byte AS numbers in AS\_Path regular expressions and extended community attribute filters to 4-byte AS numbers in dotted notation.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**as-notation plain**](cmdqueryname=as-notation+plain)
   
   
   
   The display format of BGP 4-byte AS numbers is set to the integer format.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**as-notation plain**](cmdqueryname=as-notation+plain) command affects the display format of BGP 4-byte AS numbers in the outputs of display commands and the matching results of AS\_Path regular expressions and extended community filters, but does not affect the configuration format.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring the display format of BGP 4-byte AS numbers, verify the configuration.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ [ *ipv4-address* ] **verbose** ] command to check the format of BGP 4-byte AS numbers.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check whether the result of matching BGP routes against an AS\_Path regular expression or extended community filter has changed. If a change has occurred, reconfigure the AS\_Path regular expression or extended community filter in time.