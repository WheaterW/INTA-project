Checking Statistics About Outbound Interfaces in IPv6 PIM-SM Entries
====================================================================

You can determine whether the number of existing outbound interfaces in IPv6 PIM-SM entries exceeds the upper limit by checking statistics about outbound interfaces in IPv6 PIM-SM entries.

#### Context

Statistics about outbound interfaces in IPv6 PIM-SM entries include the following information:

* Upper limit on the number of outbound interfaces in IPv6 PIM-SM entries
* Upper alarm threshold for the number of outbound interfaces in IPv6 PIM-SM entries
* Lower alarm threshold for the number of outbound interfaces in IPv6 PIM-SM entries
* Number of existing outbound interfaces in IPv6 PIM-SM entries
* Number of existing outbound interfaces in (\*, G) entries
* Number of existing outbound interfaces in (S, G) entries

#### Procedure

* Run the [**display multicast ipv6 global outgoing-interface pim sm statistics**](cmdqueryname=display+multicast+ipv6+global+outgoing-interface+pim+sm+statistics) command to check statistics about outbound interfaces in IPv6 PIM-SM entries.