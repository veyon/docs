Introduction
============

About this manual
-----------------
This manual describes the installation and configuration of Veyon in a computer network and is addressed to
system administrators and technically adept users. For end users there is a separate user manual explaining 
usage and specific functions of the user program (Veyon Master). 

The further sections of this chapter contain basic information about Veyon and its components which are paramount
for putting Veyon into operation. 

Chapter :ref:`Installation` deals with the installation von Veyon on a Windows or Linux computer. It also
contains hints on how to perform or implement an automated installation. 

Chapter :ref:`Cofiguration`describes configuration and integration using the graphical configuration tool, whereas
the :ref:`configuration reference` deals with the details of configuration options. Chapter :ref:`LDAP` explains
in detail how to connect to an existing LDAP-/ActiveDirectory server. 

Veyon is furthermore equipped with a command line interface (:index:`CLI`) that can be used for editing 
the configuration and for using or controlling specific program functions. 
All modules and commands of the command line tool are listed and explained in chapter :ref:`Command Line Interface`.  

If you are experiencing problems using Veyon, please see chapter :ref:`Troubleshooting` for help. Here you can find
measures for problem analysis and remedy. Frequently asked questions are answered in chapter :ref:`FAQ`. 


About Veyon
-----------

Veyon is a open source software for computer monitoring and class room administration. It permits observation and
control of computer rooms as well as interaction with the user. The core functions of Veyon are the following:

* Overview of a (class) room with all screen contents in a tile view
* Remote control of computers
* Mirroring of the teacher's sceen to all other computers in real time (full screen/window)
* Blocking workplaces (computers) to enhance attention
* Sending text messages to students
* Remote (re-)booting or shutdown of computers
* Logging out users
* Executing programs or opening websites

.. index:: teacher computer, student computer, master computer, client computer

.. _Components:

Components
----------

In essence Veyon consists of of a master and a service component that realize interaction between teacher computers
and student computers (often dubbed *master computer* and *client computer*):

.. image:: images/service-master-components.png
   :scale: 50 %
   :align: center

In a more detailed view there are several :index:`program components` that interact with each other in various ways:

.. image:: images/architecture.png
   :scale: 50 %
   :align: center

:index:`Veyon Master`
	An application program that can either be used for observing and controlling other computers or for utilizing
	functions within Veyon. In a regular case, this program is started by an enduser and accesses other computers
	through the Veyon service.

:index:`Veyon Service`
	A service that provides access to a computer, controlling functions and application functions. In a regular
	case the program is started by the operating system as a service with elevated privileges and can not be
	terminated by the user. The service is required to run on all computers including teacher computers.

:index:`Veyon Worker`
	A helper program started by the service to provide an environment for specific functions in an insulated way
	or in the context of the user that is currently logged in. Those specific functions include the demo server
	for the teacher computer and the demo client on the student computers. 

:index:`Veyon Configurator`
	A :index:`configuration tool` that allows configuration and customization of all components in a local
	Veyon installation through a graphical user interface. If needed, the program is started by the administrator
	with elevated privileges. 

:index:`Veyon Control`
	A command line tool serving as an addition to the Veyon configurator that allows reconfiguration and the use
	of some Veyon functions without	graphical interaction. This program is run either interactively on the 
	command line or script controlled with (usually) administrator's privileges. 
