(Optional) Configuring a Sub-timeslot Granularity for a FlexE Card
==================================================================

The sub-timeslot granularity of a FlexE card restricts the bandwidth configuration of a FlexE client. By default, the sub-timeslot granularity of a FlexE card is 5 Gbit/s.

#### Context

To configure a bandwidth lower than 5 Gbit/s for a FlexE client, set the sub-timeslot granularity of the FlexE client to 1 Gbit/s or 1.25 Gbit/s first.

Bandwidth configuration rules for FlexE clients based on different sub-timeslot granularities are as follows:

* If the sub-timeslot granularity is 5 Gbit/s (default value), the bandwidth of a FlexE client can be set to an integer multiple of 5 Gbit/s, such as 5 Gbit/s, 10 Gbit/s, or 15 Gbit/s.
* If the sub-timeslot granularity is 1 Gbit/s, the bandwidth of a FlexE client can be set to 1 Gbit/s, 2 Gbit/s, 3 Gbit/s, 4 Gbit/s, or an integer multiple of 5 Gbit/s.
* If the sub-timeslot granularity is 1.25 Gbit/s, the bandwidth of a FlexE client can be set to 1.25 Gbit/s, 2.5 Gbit/s, 3.75 Gbit/s, or an integer multiple of 5 Gbit/s.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set flexe sub-time-slot granula**](cmdqueryname=set+flexe+sub-time-slot+granula) **slot***slotID* **card** *cardID* { **1G** | **1.25G** | **5G** }
   
   
   
   A sub-timeslot granularity is configured for a specified FlexE card.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.