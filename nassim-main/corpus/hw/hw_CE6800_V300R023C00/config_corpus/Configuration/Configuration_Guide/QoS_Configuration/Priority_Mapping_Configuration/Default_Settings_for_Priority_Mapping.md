Default Settings for Priority Mapping
=====================================

[Table 1](#EN-US_CONCEPT_0000001512830146__table19517104681215) describes the default settings for priority mapping.

**Table 1** Default settings for priority mapping
| Parameter | Default Setting |
| --- | --- |
| Priority trusted on an interface | After packets arrive at an interface:  * Layer 2 forwarding mode  If packets carry VLAN tags, the interface trusts 802.1p values; however, if they do not, the interface forwards them based on the default interface priority. * Layer 3 forwarding mode  By default, DSCP values are trusted. |
| Mapping PHBs to DSCP values of outgoing packets on an interface | Disabled |
| Mapping PHBs to 802.1p values of outgoing packets on an interface | Enabled |
| DiffServ domain applied to an interface | DiffServ domain **default** |
| Interface priority | 0 |

In addition, the device defines default packet priority mappings, which are referenced during priority mapping.

#### Default Priority Mappings for Incoming Packets on an Interface

[Table 2](#EN-US_CONCEPT_0000001512830146__en-us_concept_0000001512676750_tb_01) lists the default mappings from 802.1p values of VLAN packets to internal priorities or drop priorities.

![](public_sys-resources/note_3.0-en-us.png) 

The mappings of interface priorities to PHBs and colors are similar to the mappings of 802.1p values to PHBs and colors.


**Table 2** Mapping between 802.1p values and internal priorities or drop priorities in the inbound direction on the device
| 802.1p Value | Internal Priority (CoS) | Drop Priority (Color) |
| --- | --- | --- |
| 0 | BE | Green |
| 1 | AF1 | Green |
| 2 | AF2 | Green |
| 3 | AF3 | Green |
| 4 | AF4 | Green |
| 5 | EF | Green |
| 6 | CS6 | Green |
| 7 | CS7 | Green |

[Table 3](#EN-US_CONCEPT_0000001512830146__en-us_concept_0000001512676750_tb_03) lists the default mappings from DSCP values in IP packets to internal priorities or drop priorities.

**Table 3** Mappings from DSCP values in IP packets to internal priorities or drop priorities in the inbound direction
| DSCP Value | Internal Priority (CoS) | Drop Priority (Color) | DSCP Value | Internal Priority (CoS) | Drop Priority (Color) |
| --- | --- | --- | --- | --- | --- |
| 0 | BE | Green | 32 | AF4 | Green |
| 1 | BE | Green | 33 | AF4 | Green |
| 2 | BE | Green | 34 | AF4 | Green |
| 3 | BE | Green | 35 | AF4 | Green |
| 4 | BE | Green | 36 | AF4 | Yellow |
| 5 | BE | Green | 37 | AF4 | Green |
| 6 | BE | Green | 38 | AF4 | Red |
| 7 | BE | Green | 39 | AF4 | Green |
| 8 | AF1 | Green | 40 | EF | Green |
| 9 | AF1 | Green | 41 | EF | Green |
| 10 | AF1 | Green | 42 | EF | Green |
| 11 | AF1 | Green | 43 | EF | Green |
| 12 | AF1 | Yellow | 44 | EF | Green |
| 13 | AF1 | Green | 45 | EF | Green |
| 14 | AF1 | Red | 46 | EF | Green |
| 15 | AF1 | Green | 47 | EF | Green |
| 16 | AF2 | Green | 48 | CS6 | Green |
| 17 | AF2 | Green | 49 | CS6 | Green |
| 18 | AF2 | Green | 50 | CS6 | Green |
| 19 | AF2 | Green | 51 | CS6 | Green |
| 20 | AF2 | Yellow | 52 | CS6 | Green |
| 21 | AF2 | Green | 53 | CS6 | Green |
| 22 | AF2 | Red | 54 | CS6 | Green |
| 23 | AF2 | Green | 55 | CS6 | Green |
| 24 | AF3 | Green | 56 | CS7 | Green |
| 25 | AF3 | Green | 57 | CS7 | Green |
| 26 | AF3 | Green | 58 | CS7 | Green |
| 27 | AF3 | Green | 59 | CS7 | Green |
| 28 | AF3 | Yellow | 60 | CS7 | Green |
| 29 | AF3 | Green | 61 | CS7 | Green |
| 30 | AF3 | Red | 62 | CS7 | Green |
| 31 | AF3 | Green | 63 | CS7 | Green |



#### Mappings Between Internal Priorities and Inbound Queue Indexes

The internal priority on a device determines the queue from which packets are forwarded. [Table 4](#EN-US_CONCEPT_0000001512830146__en-us_concept_0000001512676750_tab_03) describes the mappings between internal priorities and queues.

**Table 4** Mappings between internal priorities and queue indexes
| Internal Priority (CoS) | Queue Index |
| --- | --- |
| BE | 0 |
| AF1 | 1 |
| AF2 | 2 |
| AF3 | 3 |
| AF4 | 4 |
| EF | 5 |
| CS6 | 6 |
| CS7 | 7 |



#### Default Priority Mappings for Outgoing Packets on an Interface

[Table 5](#EN-US_CONCEPT_0000001512830146__en-us_concept_0000001512676750_tb_02) lists the default mappings from internal priorities or drop priorities to 802.1p values of outgoing VLAN packets.

**Table 5** Mappings from internal priorities or drop priorities to 802.1p values in the outbound direction
| Internal Priority (CoS) | Drop Priority (Color) | 802.1p Value |
| --- | --- | --- |
| BE | Green | 0 |
| BE | Yellow | 0 |
| BE | Red | 0 |
| AF1 | Green | 1 |
| AF1 | Yellow | 1 |
| AF1 | Red | 1 |
| AF2 | Green | 2 |
| AF2 | Yellow | 2 |
| AF2 | Red | 2 |
| AF3 | Green | 3 |
| AF3 | Yellow | 3 |
| AF3 | Red | 3 |
| AF4 | Green | 4 |
| AF4 | Yellow | 4 |
| AF4 | Red | 4 |
| EF | Green | 5 |
| EF | Yellow | 5 |
| EF | Red | 5 |
| CS6 | Green | 6 |
| CS6 | Yellow | 6 |
| CS6 | Red | 6 |
| CS7 | Green | 7 |
| CS7 | Yellow | 7 |
| CS7 | Red | 7 |

[Table 6](#EN-US_CONCEPT_0000001512830146__en-us_concept_0000001512676750_tb_04) lists the default mappings from internal priorities or drop priorities to DSCP values of outgoing IP packets.

**Table 6** Mappings from internal priorities or drop priorities to DSCP values of IP packets in the outbound direction
| Internal Priority (CoS) | Drop Priority (Color) | DSCP Value |
| --- | --- | --- |
| BE | Green | 0 |
| BE | Yellow | 0 |
| BE | Red | 0 |
| AF1 | Green | 10 |
| AF1 | Yellow | 12 |
| AF1 | Red | 14 |
| AF2 | Green | 18 |
| AF2 | Yellow | 20 |
| AF2 | Red | 22 |
| AF3 | Green | 26 |
| AF3 | Yellow | 28 |
| AF3 | Red | 30 |
| AF4 | Green | 34 |
| AF4 | Yellow | 36 |
| AF4 | Red | 38 |
| EF | Green | 46 |
| EF | Yellow | 46 |
| EF | Red | 46 |
| CS6 | Green | 48 |
| CS6 | Yellow | 48 |
| CS6 | Red | 48 |
| CS7 | Green | 56 |
| CS7 | Yellow | 56 |
| CS7 | Red | 56 |