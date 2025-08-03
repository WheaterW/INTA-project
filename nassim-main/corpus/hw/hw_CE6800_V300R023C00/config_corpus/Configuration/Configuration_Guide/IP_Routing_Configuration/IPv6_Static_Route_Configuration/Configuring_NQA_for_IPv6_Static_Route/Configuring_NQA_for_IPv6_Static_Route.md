Configuring NQA for IPv6 Static Route
=====================================

Configuring NQA for IPv6 Static Route

#### Prerequisites

Before configuring NQA for IPv6 static route, you have completed the following task:

* Set data link layer protocol parameters for interfaces to ensure that the data link layer protocol status of each interface is up.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an NQA test instance and enter the test instance view.
   
   
   ```
   [nqa](cmdqueryname=nqa) test-instance admin-name test-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Running the [**undo nqa all-test-instance**](cmdqueryname=undo+nqa+all-test-instance) command will delete the parameters of the NQA test instance bound to the static route. As a result, the static route status may change, and services may be interrupted.
3. Configure an NQA test instance of the ICMP or TCP type.
   
   
   ```
   [test-type](cmdqueryname=test-type) { icmp | tcp }
   ```
4. Configure a destination address for the NQA test instance.
   
   
   ```
   [destination-address](cmdqueryname=destination-address) ipv6 destAddress6
   ```
5. Perform one of the following operations to start the NQA test instance.
   
   
   ```
   [start](cmdqueryname=start) at [ yyyy/mm/dd ] hh:mm:ss [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
   [start](cmdqueryname=start) delay { seconds second | hh:mm:ss } [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
   [start](cmdqueryname=start) now [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
   [start](cmdqueryname=start) daily hh:mm:ss to hh:mm:ss [ begin { yyyy/mm/dd | yyyy-mm-dd } ] [ end { yyyy/mm/dd | yyyy-mm-dd } ]
   ```
6. Exit the NQA view and return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Associate an IPv6 static route with the NQA test instance.
   
   
   ```
   [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length { interface-type interface-number [ nexthop-ipv6-address ] | vpn-instance vpn-instance-name nexthop-ipv6-address |  nexthop-ipv6-address } [ preference preference | tag tag ]* track nqa admin-name test-name [ description text ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The destination address of an NQA test instance cannot be the destination address of an associated IPv6 static route.
   
   If the IPv6 static route to be associated with an NQA test instance is already associated with a different NQA test instance, the static route is disassociated from the first NQA test instance once it becomes associated with the new NQA test instance.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```