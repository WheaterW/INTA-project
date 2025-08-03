RESTCONF Fundamentals
=====================

RESTCONF Fundamentals

#### RESTCONF Network Architecture

[Figure 1](#EN-US_CONCEPT_0000001563771141__fig_dc_vrp_netconf_feature_001901) shows the basic RESTCONF network architecture. The main elements in the RESTCONF network architecture are as follows:

* RESTCONF client:
  
  The RESTCONF client uses RESTCONF to manage network devices, and it sends a request to the server to create, delete, modify, or query one or more data records.

* RESTCONF server:
  
  The device functions as the RESTCONF server to maintain the data of the managed network devices, respond to client requests, and report requested data to the client. After receiving a request sent by the client, the server parses and processes the request, and then sends a response to the client.

**Figure 1** RESTCONF network architecture  
![](figure/en-us_image_0000001513170846.png)

The RESTCONF client obtains both configuration and status data from a running RESTCONF server.

* The RESTCONF client can query the status data and configuration data.
* The RESTCONF client can modify and operate configuration data, allowing the status of the RESTCONF server to migrate to a user-expected status.
* The RESTCONF client cannot modify status data, which includes the running status and statistics of the RESTCONF server.

#### RESTCONF Modeling Language

RESTCONF uses YANG as its modeling language. YANG is a data modeling language used to model both the configuration and status data in RESTCONF.

The YANG data model is a machine-oriented model interface, which defines data structures and constraints to provide more flexible and complete data description.


#### Related Concepts

The RESTCONF client and server run HTTP to establish a secure and connection-oriented session. The client sends a request to the server. After processing the user request, the server replies with a response to the client. The request and response messages are coded in either XML or JSON format.

**Message coding**

XML encoding

XML, the encoding format used by RESTCONF, enables the use of a text file to represent complex hierarchical data. A traditional text tool or XML-specific compilation tool can be used to read, save, and operate configuration data.

XML-based network management uses XML to describe managed data and management operations so that management information becomes a database comprehensible to computers. XML-based network management helps computers efficiently process network management data, improving network management capabilities.

* XML encoding
  
  XML, the encoding format used by RESTCONF, enables the use of a text file to represent complex hierarchical data. A traditional text tool or XML-specific compilation tool can be used to read, save, and operate configuration data.
  
  XML-based network management uses XML to describe managed data and management operations so that management information becomes a database comprehensible to computers. XML-based network management helps computers efficiently process network management data, improving network management capabilities.
  
  The XML encoding format file header is **<?xml version="1.0" encoding="UTF-8"?>**, where:
  + **<?**: indicates the start of an instruction.
  + **xml**: indicates an XML file.
  + **version="1.0"**: indicates the XML1.0 standard version.
  + **encoding**: indicates a character set encoding format. Only UTF-8 encoding is supported.
  + **?>**: indicates the end of an instruction.
* JSON encoding
  
  JSON is a lightweight text data exchange format. JSON uses JavaScript syntax to describe data objects, but JSON is still independent of languages and platforms, making it easier to understand.
  
  JSON is similar to XML, but JSON is shorter, faster, and easier to parse than XML.
  
  JSON syntax rules are as follows:
  + Data is in name:value pairs.
  + Data is separated by commas (,).
  + An object is saved in braces ({}).
  + An array is saved in brackets ([]).
  The JSON format is as follows:
  + JSON name:value pair. For example:
    ```
    "Name": "Apple"
    ```
  + JSON value. The value can be a number, string, logical value, array, object, or null. For example:
    ```
    "Price": 3.99
    ```
  + JSON object. An object is an unordered collection of name:value pairs. An object starts with a left brace ({) and ends with a right brace (}). Each name is followed by a colon (:), and name:value pairs are separated by commas (,). For example:
    ```
    { "firstName": "Brett", "lastName":"McLaughlin", "email": "aaaa" }
    ```
  + JSON array. An array is an ordered list of values. An array starts with a left bracket ([) and ends with a right bracket (]). Arrays are separated by commas (,). For example:
    
    ```
    { "people": [
          { "firstName": "Brett", "lastName":"McLaughlin", "email": "aaaa" }, 
    	  { "firstName": "Jason", "lastName":"Hunter", "email": "bbbb"}  
    	  ]
    }
    ```

**RESTCONF capability**

In addition to a group of basic operations, RESTCONF also provides extended capabilities supported by the device. The capability set is used to declare that the device supports these extended capabilities. Each capability set is identified by a uniform resource identifier (URI).

[Table 1](#EN-US_CONCEPT_0000001563771141__table_01) describes the standard capability sets supported by RESTCONF.

**Table 1** Capability set description
| Name | URI | Description of Capability Set Operations |
| --- | --- | --- |
| depth | urn:ietf:params:xml:restconf:capability:depth:1.0 | A device supports the "depth" query parameter of version 1.0. This capability indicates that the device supports a specified maximum number of data query times. |
| fields | urn:ietf:params:xml:restconf:capability:fields:1.0 | The device supports the "fields" query parameter of version 1.0. This capability indicates that a device can obtain the subset of the target data content. |
| with-defaults | urn:ietf:params:xml:restconf:capability:with-defaults:1.0 | The device supports the "with-defaults" query parameter of version 1.0. This capability indicates that a device is capable of specifying how information about default data nodes should be returned. |
| defaults | urn:ietf:params:restconf:capability:defaults:1.0 | This capability indicates the default value of the "with-defaults" query parameter.  NOTE:  If the "with-defaults" query parameter is not specified in the request URI, the default value is **report-all** (to query all nodes). |