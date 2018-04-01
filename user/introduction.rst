Introduction
============

Veyon is an application that allows you to map, keep track of, control, and perform various functions on a centralized computer (such as a teacher's PC), a cluster of computers (such as classrooms or labs) and modes to use.

Program start and registration
---------------------------

The program is started via the :index:`start menu` or an :index:`desktop icon`:

.. image:: images/desktop-symbol.png
   :align: center

Depending on the system configuration you will be prompted for :index:`username` and :index:`password`:

.. image:: images/logon-dialog.png
   :align: center

Enter here your username and password or, if given, the access data of a special teacher account. If the entered data is correct and you can log in, the program starts. Otherwise, the :index:`Login` is denied and an error message is displayed. You can try reentering in this case.


User Interface
----------------

After starting the program you will see :index:`User Interface` with :index:`Toolbar` (1), :index:`Desktop` (2) and the :index:`Status Bar` with various controls (3):

.. image:: images/master-user-interface.png
   :align: center

The toolbar contains a number of buttons for activating various functions. A detailed description of the individual functions can be found in the chapter :ref:`Program Functions`. The appearance and behavior of the toolbar can be adjusted as described in the section :ref:`Toolbar`.

In the workspace, all computers to be observed are displayed in a :index:`Tile view`. Depending on the system configuration and previous program launches, you will already see the computers of the current room here. You can use the `Computer Room Management`_ to show or hide computers or entire computer rooms.

The elements in the status bar are used to control the program interface. This allows you to enable views such as `Computer Room Management`_ or `Screenshot Management`_. Use the slider to control the size of the displayed computer screens. An automatic adjustment to an optimal size is done by pressing the button :guilabel:`Auto`. The button :guilabel:`About` opens a dialog with information about the program, such as Version, Author and License terms.

.. _Toolbar:

Toolbar
--------------

You can customize the look and feel of the toolbar to your liking. With a right-click on a free area as well as a button, a context menu opens for several entries:

.. image:: images/toolbar-contextmenu.png
   :align: center

If you click the entry :guilabel:`Disable Balloon Tooltips` you will no longer see any tooltips when you move the mouse over the buttons. You can open the context menu again at any time and remove the hook with a click.

The option :guilabel:`Show Icons Only` causes a compact representation of the buttons in the toolbar by hiding the labels and displaying only icons. On smaller screens, this option may be necessary to display all the buttons.

.. _`Computer Room Management`:

Computer Room Management
----------------------

.. index:: `Computer Room Management`

You can use the button :guilabel:`Computer Rooms` in the :index:`Status Bar` to open the Computer Space Administration. This view displays all available computer rooms in a tree view. Individual room entries can be expanded by means of a usually triangular symbol.

You can activate individual computers or entire rooms by clicking on them. All activated computers are displayed in the workspace.

.. image:: images/computer-room-management.png
   :align: center

With the button :guilabel:`Save computer/user List` you can save the list of computers and logged in users in a CSV file. A typical use case for this is a presence check at a later time.

Depending on the system configuration, the button :guilabel:`Add room` is also available. You can add more computer rooms to view. A click on the button opens a dialog in which you can see all available rooms:

.. image:: images/room-selection.png
   :align: center

You can filter the list using the input field, that is, enter a search term. In the list then only the room names are displayed, in which the entered search term occurs. Advanced users can also use regular expressions for the filter. Then you can select a room and confirm with :guilabel:`OK`. The selected room is now available in the room list until the next program restart. You can also remove an added room by clicking on a room and pressing the :kbd:`Del` key.

.. _`Screenshot Management`:

Screenshot Management
------------------------

.. index:: `Screenshot Management`

Screen Capture Management View allows you to view and delete captured screenshots. In the chapter :ref:`Program Functions` the function for creating a screenshot in the section: ref:` Screenshot` is explained.

.. image:: images/screenshot-management.png
   :align: center

You can now select individual screenshots in the list. It will then display details about the screen shot, such as shooting date, user name, and computer in the table below. The button :guilabel:`Show` or a double-click in the list displays the selected screenshot in full size. If you no longer need the screenshot, you can permanently delete it using the :guilabel:`Delete` button. Please note that this process can not be undone and the files are not moved to the trash.
