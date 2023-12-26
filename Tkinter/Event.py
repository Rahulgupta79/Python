from tkinter import*
root=Tk()
root.title("Button Event")
root.minsize(300,280)
root.maxsize(800,600)
root.geometry("800x600")
def show2(event):
    root.configure(background="blue")


root.bind("<Button-1>",lambda e:root.configure(background="cyan"))
root.bind("<Button-2>",show2)
root.bind("<Shift_L>",show2)
root.mainloop()

'''Alt	The Alt key is held
Control	The Ctrl key is held
Shift	The Shift key is held
Any	This modifier makes an event type general. For example, the event pattern <Any-KeyPress> applies to the keypress of any key.
Event types

The following table shows the most commonly used event types:
Type	Name	Description
36	Activate	The state option of a widget changes from inactive to active.
4	Button	One mouse button is pressed
5	ButtonRelease	One mouse button is released
22	Configure	The size of the widget is changed
37	Deactivate	The state option of a widget changes from active to inactive.
17	Destroy	A widget is being destroyed.
7	Enter	The mouse pointer is moved into a visible part of a widget.
12	Expose	Some part of the widget or application is visible after having been covered up by another window.
9	FocusIn	The input focus was moved into a widget.
10	FocusOut	The input focus was moved out of a widget.
2	KeyPress	A key is pressed.
3	KeyRelease	A key is released
8	Leave	The mouse pointer is moved out of a widget.
19	Map	A widget is being placed on a container e.g., calling the pack() or grid() method.
6	Motion	The mouse pointer is moved entirely within a widget.
38	MouseWheel	The user moved the mouse wheel up or down.
18	Unmap	A widget is being unmapped and is no longer visible, for example when calling the grid_remove() method on the widget.
15	Visibility	At least some part of the application window becomes visible on the screen.
Event Detail

Alt_L	64	65513	The left-hand alt key
Alt_R	113	65514	The right-hand alt key
BackSpace	22	65288	backspace
Cancel	110	65387	break
Caps_Lock	66	65549	CapsLock
Control_L	37	65507	The left-hand control key
Control_R	109	65508	The right-hand control key
Delete	107	65535	Delete
Down	104	65364	↓
End	103	65367	end
Escape	9	65307	esc
Execute	111	65378	SysReq
F1	67	65470	Function key F1
F2	68	65471	Function key F2
Fi	66+i	65469+i	Function key Fi
F12	96	65481	Function key F12
Home	97	65360	home
Insert	106	65379	insert
Left	100	65361	←
Linefeed	54	106	Linefeed (control-J)
KP_0	90	65438	0 on the keypad
KP_1	87	65436	1 on the keypad
KP_2	88	65433	2 on the keypad
KP_3	89	65435	3 on the keypad
KP_4	83	65430	4 on the keypad
KP_5	84	65437	5 on the keypad
KP_6	85	65432	6 on the keypad
KP_7	79	65429	7 on the keypad
KP_8	80	65431	8 on the keypad
KP_9	81	65434	9 on the keypad
KP_Add	86	65451	+ on the keypad
KP_Begin	84	65437	The center key (same key as 5) on the keypad
KP_Decimal	91	65439	Decimal (.) on the keypad
KP_Delete	91	65439	delete on the keypad
KP_Divide	112	65455	/ on the keypad
KP_Down	88	65433	↓ on the keypad
KP_End	87	65436	end on the keypad
KP_Enter	108	65421	enter on the keypad
KP_Home	79	65429	home on the keypad
KP_Insert	90	65438	insert on the keypad
KP_Left	83	65430	← on the keypad
KP_Multiply	63	65450	× on the keypad
KP_Next	89	65435	PageDown on the keypad
KP_Prior	81	65434	PageUp on the keypad
KP_Right	85	65432	→ on the keypad
KP_Subtract	82	65453	- on the keypad
KP_Up	80	65431	↑ on the keypad
Next	105	65366	PageDown
Num_Lock	77	65407	NumLock
Pause	110	65299	pause
Print	111	65377	PrintScrn
Prior	99	65365	PageUp
Return	36	65293	Enter key
Right	102	65363	→
Scroll_Lock	78	65300	ScrollLock
Shift_L	50	65505	The left-hand shift key
Shift_R	62	65506	The right-hand shift key
Tab	23	65289	The tab key'''