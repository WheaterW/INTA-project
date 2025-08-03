Configuring Separate Reporting of IPv4 and IPv6 Alarms
======================================================

Configuring Separate Reporting of IPv4 and IPv6 Alarms

#### Prerequisites

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low-latency mode does not support IPv6 functions.

By default, BFD IPv4 and BFD IPv6 sessions use the same trap message to report alarms. The trap message names are hwBfdSessUp and hwBfdSessDown. If both BFD IPv4 and IPv6 sessions exist on a link and the traffic is heavy, trap suppression is triggered. When the session link status changes, only the IPv4 or IPv6 trap messages are reported. As a result, alarms are lost.

To resolve this problem, you can configure separate reporting of IPv4 and IPv6 alarms. When the link status of a BFD IPv6 session changes, a new trap message is used to report the alarm. The trap message names are hwBfdIPv6SessUp and hwBfdIPv6SessDown. The BFD IPv4 session uses the original trap messages for reporting alarms. Alarms for BFD IPv4 and BFD IPv6 sessions are separated to prevent alarm loss during traffic suppression.

Before configuring separate reporting of IPv4 and IPv6 alarms, complete the following tasks:

* Enable BFD globally.
* Create a BFD session.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally and enter the global BFD view.
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Configure the device to use different trap messages to report BFD IPv4 and BFD IPv6 session alarms.
   ```
   [ipv6-trap separated](cmdqueryname=ipv6-trap+separated)
   ```
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display this**](cmdqueryname=display+this) command in the global BFD view to check whether the configuration takes effect.
* When BFD IPv4 and BFD IPv6 session status alarms are generated on a device, run the [**display trapbuffer**](cmdqueryname=display+trapbuffer) command to check whether BFD IPv4 and BFD IPv6 sessions use different trap messages to report alarms.