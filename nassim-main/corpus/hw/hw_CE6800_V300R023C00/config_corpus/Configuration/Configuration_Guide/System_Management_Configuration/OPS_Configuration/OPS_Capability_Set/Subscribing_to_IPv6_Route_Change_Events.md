Subscribing to IPv6 Route Change Events
=======================================

Subscribing to IPv6 Route Change Events

#### Application Phase

Subscription phase


#### Function Prototype

result1\_value, result2\_description = \_ops.route.subscribe6(tag, network, maskLen, minLen=None, maxLen=None, vpnName="\_public\_", optype="all", protocol="all")


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| tag | Specifies conditions. | The value is a string of 1 to 8 case-sensitive characters, consists of letters, digits, and underscores (\_), and starts with a letter. The value of **tag** cannot be **and**, **or**, or **not**. If only one condition is subscribed to in the script, the value can be an empty string. If multiple conditions are subscribed to, the value cannot be empty and must be unique in the script. |
| network | Specifies an IPv6 route prefix. | The value is in the IPv6 address format, such as 2001:db8:1::2. |
| maskLen | Specifies a mask length. | The value is an integer ranging from 0 to 128. |
| minLen | Specifies the minimum mask length. | The value is an integer that must be greater than or equal to the **maskLen** value.  The default value is **None**, indicating the minimum mask length is 0. |
| maxLen | Specifies the maximum mask length. | The value is an integer that must be greater than or equal to the **minLen** value.  The default value is **None**, indicating the maximum mask length is 0. |
| vpnName | Specifies the name of the VPN instance in which route change events are to be subscribed to. | The value is a string of 1 to 31 characters.  If the parameter is not specified, change events of the corresponding public network routes are subscribed to by default. |
| type | Specifies an IPv6 route change event type. | The value is of the enumerated type:   * add: Routes are added. * remove: Routes are deleted. * modify: Routes are modified. * all: Indicates all route changes.   The default value is **all**. |
| protocol | Specifies a route type. | The value is a character string, which can be:   * direct: direct routes * static: static routes * isis: IS-IS routes * bgp: BGP routes * unr: user network routes * all: all routes   The default value is **all**. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

This API can only be used in \_ops\_condition() of the maintenance assistant script.

* A route change event can be triggered only when active routes change.
* A route change event is not triggered when route recursion results change or inactive routes change.
* The add event is triggered when an active route with a high preference is added.
* The remove and add events are triggered when an active route is deleted and a sub-optimal route becomes active.
* A maximum of three route change events can be triggered per second. If multiple route changes match the subscription conditions, a maximum of 100 events can be triggered.
* You can specify a VPN instance to subscribe to change events of VPN routes. If no VPN instance is specified, change events of the corresponding public network routes are subscribed to by default.
* The specified VPN instance must be an existing one on the device, and the IPv6 address must have been enabled in the VPN instance. If either condition is not met, the subscription rule does not take effect.
* After a specified VPN instance is deleted, the corresponding subscription rule is also deleted.

#### Usage Examples

When a route with the prefix 2001:db8:1::2/64 is added to or deleted from the VPN instance **testVPN**, a route change event is triggered.

```
test.py
def ops_condition(_ops): 
       ret, reason = _ops.route.subscribe6("con0", "2001:db8:1::2", maskLen=64, vpnName="testVpn", optype="all", protocol="all") 
       ret, reason = _ops.correlate("con0") 
       return ret 
def ops_execute(_ops): 
       a, description = _ops.context.save("test.py",'Route event trigger')  
       return 0
```