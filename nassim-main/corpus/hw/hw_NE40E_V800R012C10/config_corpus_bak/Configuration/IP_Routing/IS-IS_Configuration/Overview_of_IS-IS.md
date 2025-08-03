Overview of IS-IS
=================

IS-IS can be used to implement interworking on large-scale networks.

#### Definition

Intermediate System to Intermediate System (IS-IS) is a dynamic routing protocol initially designed by the International Organization for Standardization (ISO) for the Connectionless Network Protocol (CLNP).

To support IP routing, the IETF extends and modifies IS-IS in relevant standards, which enables IS-IS to be applied to both TCP/IP and Open System Interconnection (OSI) environments. The new type of IS-IS is called integrated IS-IS or dual IS-IS.

In this document, IS-IS refers to integrated IS-IS, unless otherwise stated.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Unless otherwise specified, IS-IS features that support both IPv4 and IPv6 are implemented in the same way.



#### Purpose

IS-IS is an Interior Gateway Protocol (IGP) and is used within an autonomous system (AS). IS-IS is a link state protocol, and it uses the shortest path first (SPF) algorithm to calculate routes.