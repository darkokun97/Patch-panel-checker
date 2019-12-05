


from tkinter import *
from tkinter import ttk
import database

trayPortsWidth = 300
trayPortsHeight = 150

checkButtonHeight = 1
checkButtonWidth = 6

listBoxWidth = 12
listBoxHeight = 6

buttonWidth = 10
buttonHeight = 1

labelWidth = 12
labelHeight = 1

comboboxWidth = 14

roomsRelx = 0.10
racksRelx = 0.25
traysRelx = 0.40
oppositeTrayRelx = 0.12
addEntrysRelx = 0.35
addLabelsRelx = 0.26

listsRelY = 0.12
selectedLabelsRely = 0.52
refreshAndUpdateRely = 0.61
deleteRely = 0.74
addRoomsRely = 0.1
addRacksRely = 0.2
addTraysRely = 0.3
addOppositeRoomsRely = 0.4
addOppositeRacksRely = 0.5
addOppositeTraysRely = 0.6
addButtonsRely = 0.7
statusLabelRely = 0.85

selectedRoom = ""
selectedRack = ""
selectedTray = ""

top = Tk()
top.title("Patch Panel Port Checker")
top.geometry('800x580')
top.resizable(0, 0)	

def new_checkbutton(frame, checkbutton):
	checkbutton['var'] = IntVar()
	checkbutton['item'] = Checkbutton(frame, text = "Port " + checkbutton['text'], variable = checkbutton['var'], onvalue = 1, offvalue = 0, height = 1, width = 8)
	return(Checkbutton)

def reset_rooms():
	global selectedRoom
	roomList.delete(0, END)
	selectedRoom = ""
	selectedRoomText.set("Room: ")

def reset_racks():
	global selectedRack
	rackList.delete(0, END)
	selectedRack = ""
	selectedRackText.set("Rack: ")

def reset_trays():
	global selectedTray
	trayList.delete(0, END)
	selectedTray = ""
	selectedTrayText.set("Tray: ")

def reset_ports():
	for item in portsMain:
		portsMain[item]['item'].deselect()
		portsMain[item]['item']['bg'] = '#d9d9d9'

def reset_opposite():
	global selectedRoom
	global selectedRack
	global selectedTray
	for item in portsOpposite:
		portsOpposite[item]['item'].deselect()
	oppositeSelectedRoomText.set("Room: ")
	oppositeSelectedRackText.set("Rack: ")
	oppositeSelectedTrayText.set("Tray: ")
	for item in portsOpposite:
		portsOpposite[item]['item'].deselect()
		portsOpposite[item]['item']['bg'] = '#d9d9d9'


tabParent = ttk.Notebook()
tabMain = Frame(tabParent)
tabAdd = Frame(tabParent)

tabParent.add(tabMain, text="Main")
tabParent.add(tabAdd, text="Add" )

tabParent.pack(expand=1, fill='both')

mainFrame = Frame(tabMain, bg = "grey", height='290', width ='750')
mainFrame.place(anchor = 'n', relx = 0.5, rely = 0.05)

mainFrameLabel = Label( mainFrame,bg = "grey", text = "Select Tray", anchor = 'w', relief = FLAT )
mainFrameLabel.place(anchor = 'nw', x = 2,y = 2)

def select_room():
	global selectedRoom
	reset_racks()
	reset_trays()
	reset_ports()
	reset_opposite()
	for item in roomList.get(roomList.curselection()):
		selectedRoom = item
	selectedRoomText.set("Room: " + selectedRoom)
	for item in portsMain:
		portsMain[item]['item'].deselect()
	rackListItems = database.refresh_racks(selectedRoom)
	for item in rackListItems:
		rackList.insert(0, item)

roomList = Listbox(mainFrame, width = listBoxWidth, height = listBoxHeight)
roomList.place(anchor = 'n', relx = roomsRelx, rely = listsRelY)
roomSelector = lambda event, tag= "selectroom": select_room()
roomList.bind("<Double-Button-1>", roomSelector)

def select_rack():
	global selectedRoom
	global selectedRack
	reset_trays()
	reset_ports()
	reset_opposite()
	for item in rackList.get(rackList.curselection()):
		selectedRack = item
	selectedRackText.set("Rack: " + selectedRack)
	trayListItems = database.refresh_trays(selectedRoom, selectedRack)
	for item in trayListItems:
		trayList.insert(0, item)

rackList = Listbox(mainFrame, width = listBoxWidth, height = listBoxHeight)
rackList.place(anchor = 'n', relx = racksRelx, rely = listsRelY)
rackSelector = lambda event, tag= "selectrack": select_rack()
rackList.bind("<Double-Button-1>", rackSelector)

def select_tray():
	global selectedRoom
	global selectedRack
	global selectedTray
	reset_ports()
	reset_opposite()
	for item in trayList.get(trayList.curselection()):
		selectedTray = item
	selectedTrayText.set("Tray: " + str(selectedTray))
	portListItems = database.refresh_ports(selectedRoom, selectedRack, selectedTray)
	oppositePanel = database.refresh_opposite(selectedRoom, selectedRack, selectedTray)
	selectedOppositeRoom = oppositePanel[0][0]
	selectedOppositeRack = oppositePanel[0][1]
	selectedOppositeTray = oppositePanel[0][2]
	oppositeSelectedRoomText.set("Room: " + selectedOppositeRoom)
	oppositeSelectedRackText.set("Rack: " + selectedOppositeRack)
	oppositeSelectedTrayText.set("Tray: " + str(selectedOppositeTray))
	portListOppositeItems = database.refresh_ports(selectedOppositeRoom, selectedOppositeRack, selectedOppositeTray)
	portNumber = 1
	portIndex = 0
	while portNumber <= 48:
		for value in portListItems:
			selected = value[portIndex]
			if selected == 1:
				portsMain[portNumber]['item'].select()
		for valueOpposite in portListOppositeItems:
			selectedOpposite = valueOpposite[portIndex]
			if selectedOpposite == 1:
				portsOpposite[portNumber]['item'].select()
			if selectedOpposite == 2:
				portsOpposite[portNumber]['item']['bg'] = 'black'
		if selected == selectedOpposite:
			portsMain[portNumber]['item']['bg'] = 'green'
		else:
			portsMain[portNumber]['item']['bg'] = 'red'
		portNumber += 1
		portIndex += 1

trayList = Listbox(mainFrame, width = listBoxWidth, height = listBoxHeight)
trayList.place(anchor = 'n', relx = traysRelx, rely = listsRelY)
traySelector = lambda event, tag= "selecttray": select_tray()
trayList.bind("<Double-Button-1>", traySelector)

selectedRoomText = StringVar()
roomListLabel = Label( mainFrame, textvariable = selectedRoomText, anchor = 'w', width = labelWidth, height = labelHeight, relief=RAISED )
selectedRoomText.set("Room: ")
roomListLabel.place(anchor = 'n', relx = roomsRelx, rely = selectedLabelsRely)

selectedRackText = StringVar()
rackListLabel = Label( mainFrame, textvariable = selectedRackText, anchor = 'w', width = labelWidth, height = labelHeight, relief=RAISED )
selectedRackText.set("Rack: ")
rackListLabel.place(anchor = 'n', relx = racksRelx, rely = selectedLabelsRely)

selectedTrayText = StringVar()
trayListLabel = Label( mainFrame, textvariable = selectedTrayText, anchor = 'w', width = labelWidth, height = labelHeight, relief=RAISED )
selectedTrayText.set("Tray: ")
trayListLabel.place(anchor = 'n', relx = traysRelx, rely = selectedLabelsRely)

def refresh_rooms_button():
	reset_rooms()
	reset_racks()
	reset_trays()
	reset_ports()
	reset_opposite()
	roomListItems = database.refresh_rooms()
	for item in roomListItems:
		roomList.insert(0, item)

refreshRoomsButton = Button(mainFrame, text="Refresh Rooms",height = buttonHeight, width = buttonWidth, command = refresh_rooms_button)
refreshRoomsButton.place(anchor = 'n', relx = roomsRelx, rely = refreshAndUpdateRely)

def update_tray():
	global selectedRoom
	global selectedRack
	global selectedTray
	room = selectedRoom
	rack = selectedRack
	tray = selectedTray
	portState= {}
	for item in portsMain:
		portState[item] = portsMain[item]['var'].get()
	database.update_entry(room, rack, tray, portState)
	select_tray()

UpdateTrayButton = Button(mainFrame, text="Update Tray",height = buttonHeight, width = buttonWidth, command = update_tray)
UpdateTrayButton.place(anchor = 'n', relx = traysRelx, rely = refreshAndUpdateRely)

def delete():
	global selectedRoom
	global selectedRack
	global selectedTray
	database.delete_tray(selectedRoom, selectedRack, selectedTray)
	reset_rooms()
	reset_racks()
	reset_trays()
	reset_ports()
	reset_opposite()


DeleteTrayButton = Button(mainFrame, text="Delete Tray",height = buttonHeight, width = buttonWidth, command = delete)
DeleteTrayButton.place(anchor = 'n', relx = traysRelx, rely = deleteRely)

trayPortsMain = Frame(mainFrame, bg = "#e4e4e4", height= trayPortsHeight, width = trayPortsWidth)
trayPortsMain.place(anchor = 'n', relx = 0.73, rely = 0.02)

portsMain = {1:{},
			2:{},
			3:{},
			4:{},
			5:{},
			6:{},
			7:{},
			8:{},
			9:{},
			10:{},
			11:{},
			12:{},
			13:{},
			14:{},
			15:{},
			16:{},
			17:{},
			18:{},
			19:{},
			20:{},
			21:{},
			22:{},
			23:{},
			24:{},
			25:{},
			26:{},
			27:{},
			28:{},
			29:{},
			30:{},
			31:{},
			32:{},
			33:{},
			34:{},
			35:{},
			36:{},
			37:{},
			38:{},
			39:{},
			40:{},
			41:{},
			42:{},
			43:{},
			44:{},
			45:{},
			46:{},
			47:{},
			48:{},}
portNumber = 1
gridColumn = 0
gridRow = 0
for item in portsMain:
	portsMain[item]['text'] = str(portNumber)
	new_checkbutton(trayPortsMain, portsMain[item])
	portsMain[item]['item'].grid(row = gridRow, column = gridColumn)
	portNumber += 1
	gridRow +=1
	if gridRow >= 12:
		gridRow = 0
		gridColumn += 1

#Second large frame for everything in the opposite patchpanel
oppositeFrame = Frame(tabMain, bg = "grey", height='200', width ='750')
oppositeFrame.place(anchor = 'n', relx = 0.5, rely = 0.62)

oppositeFrameLabel = Label( oppositeFrame,bg = "grey", text = "Oposite Tray", anchor = 'w', relief = FLAT )
oppositeFrameLabel.place(anchor = 'nw', x = 2,y = 2)

oppositeSelectedRoomText = StringVar()
oppositeRoomListLabel = Label( oppositeFrame, textvariable = oppositeSelectedRoomText, anchor = 'w', width = labelWidth, height = labelHeight, relief=RAISED )
oppositeSelectedRoomText.set("Room: ")
oppositeRoomListLabel.place(anchor = 'n', relx = oppositeTrayRelx, rely = 0.20)

oppositeSelectedRackText = StringVar()
oppositeRackListLabel = Label( oppositeFrame, textvariable = oppositeSelectedRackText, anchor = 'w', width = labelWidth, height = labelHeight, relief=RAISED )
oppositeSelectedRackText.set("Rack: ")
oppositeRackListLabel.place(anchor = 'n', relx = oppositeTrayRelx, rely = 0.40)

oppositeSelectedTrayText = StringVar()
oppositeTrayListLabel = Label( oppositeFrame, textvariable = oppositeSelectedTrayText, anchor = 'w', width = labelWidth, height = labelHeight, relief=RAISED )
oppositeSelectedTrayText.set("Tray: ")
oppositeTrayListLabel.place(anchor = 'n', relx = oppositeTrayRelx, rely = 0.60)

trayPortsOpposite = Frame(oppositeFrame, bg = "#e4e4e4", height= trayPortsHeight, width = trayPortsWidth)
trayPortsOpposite.place(anchor = 'n', relx = 0.61, rely = 0.04)

portsOpposite = {1:{},
			2:{},
			3:{},
			4:{},
			5:{},
			6:{},
			7:{},
			8:{},
			9:{},
			10:{},
			11:{},
			12:{},
			13:{},
			14:{},
			15:{},
			16:{},
			17:{},
			18:{},
			19:{},
			20:{},
			21:{},
			22:{},
			23:{},
			24:{},
			25:{},
			26:{},
			27:{},
			28:{},
			29:{},
			30:{},
			31:{},
			32:{},
			33:{},
			34:{},
			35:{},
			36:{},
			37:{},
			38:{},
			39:{},
			40:{},
			41:{},
			42:{},
			43:{},
			44:{},
			45:{},
			46:{},
			47:{},
			48:{},}

portNumber = 1
gridColumn = 0
gridRow = 0
for item in portsOpposite:
	portsOpposite[item]['text'] = str(portNumber)
	new_checkbutton(trayPortsOpposite, portsOpposite[item])
	portsOpposite[item]['item'].grid(row = gridRow, column = gridColumn)
	portNumber += 1
	gridRow +=1
	if gridRow >= 8:
		gridRow = 0
		gridColumn += 1


#things in the Add tab

addFrame = Frame(tabAdd, bg = "grey", height='300', width ='750')
addFrame.place(anchor = 'n', relx = 0.5, rely = 0.05)

addFrameLabel = Label( addFrame,bg = "grey", text = "Add Tray", anchor = 'w', relief = FLAT )
addFrameLabel.place(anchor = 'nw', x = 2,y = 2)

addRoomLabel = Label( addFrame,bg = "grey", text = "Room:", anchor = 'e', relief = FLAT )
addRoomLabel.place(anchor = 'ne', relx = addLabelsRelx, rely = addRoomsRely)

addRackLabel = Label( addFrame,bg = "grey", text = "Rack:", anchor = 'e', relief = FLAT )
addRackLabel.place(anchor = 'ne', relx = addLabelsRelx, rely = addRacksRely)

addTrayLabel = Label( addFrame,bg = "grey", text = "Tray Number:", anchor = 'e', relief = FLAT )
addTrayLabel.place(anchor = 'ne', relx = addLabelsRelx, rely = addTraysRely)

addOppositeRoomLabel = Label( addFrame,bg = "grey", text = "Opposite Room:", anchor = 'e', relief = FLAT )
addOppositeRoomLabel.place(anchor = 'ne', relx = addLabelsRelx, rely = addOppositeRoomsRely)

addOppositeRackLabel = Label( addFrame,bg = "grey", text = "Opposite Rack:", anchor = 'e', relief = FLAT )
addOppositeRackLabel.place(anchor = 'ne', relx = addLabelsRelx, rely = addOppositeRacksRely)

addOppositeTrayLabel = Label( addFrame,bg = "grey", text = "Opposite Tray Number:", anchor = 'e', relief = FLAT )
addOppositeTrayLabel.place(anchor = 'ne', relx = addLabelsRelx, rely = addOppositeTraysRely)

def get_rooms():
	rooms = database.fetch_rooms()
	addRoom['values'] = rooms
	addOppositeRoom['values'] = rooms

addRoom = ttk.Combobox(addFrame, values=[], width = comboboxWidth, background = 'red')
addRoom.place(anchor = 'n', relx = addEntrysRelx, rely = addRoomsRely)
insertRooms = lambda event, tag= "fetchroom": get_rooms()
addRoom.bind("<Button-1>", insertRooms)

def get_racks():
	racks = database.fetch_racks()
	addRack['values'] = racks
	addOppositeRack['values'] = racks

addRack = ttk.Combobox(addFrame, values=[], width = comboboxWidth)
addRack.place(anchor = 'n', relx = addEntrysRelx, rely = addRacksRely)
insertRacks = lambda event, tag= "fetchrack": get_racks()
addRack.bind("<Button-1>", insertRacks)

def get_trays():
	trays = database.fetch_trays()
	addTray['values'] = trays
	addOppositeTray['values'] = trays

addTray = ttk.Combobox(addFrame, values=[], width = comboboxWidth)
addTray.place(anchor = 'n', relx = addEntrysRelx, rely = addTraysRely)
insertTrays = lambda event, tag= "fetchroom": get_trays()
addTray.bind("<Button-1>", insertTrays)

addOppositeRoom = ttk.Combobox(addFrame, values=[], width = comboboxWidth)
addOppositeRoom.place(anchor = 'n', relx = addEntrysRelx, rely = addOppositeRoomsRely)
insertRoom = lambda event, tag= "fetchrack": get_rooms()
addOppositeRoom.bind("<Button-1>", insertRoom)

addOppositeRack = ttk.Combobox(addFrame, values=[], width = comboboxWidth)
addOppositeRack.place(anchor = 'n', relx = addEntrysRelx, rely = addOppositeRacksRely)
insertRacks = lambda event, tag= "fetchrack": get_racks()
addOppositeRack.bind("<Button-1>", insertRacks)

addOppositeTray = ttk.Combobox(addFrame, values=[], width = comboboxWidth)
addOppositeTray.place(anchor = 'n', relx = addEntrysRelx, rely = addOppositeTraysRely)
insertRacks = lambda event, tag= "fetchtray": get_racks()
addOppositeRack.bind("<Button-1>", insertRacks)

def add_button():
	room = addRoom.get()
	if room == '':
		addStatusLabelText.set("Room cant be left empty")
		return
	room = room.upper()	
	rack = addRack.get()
	if rack == '':
		addStatusLabelText.set("Rack cant be left empty")
		return
	rack = rack.upper()
	tray = addTray.get()
	if tray == '':
		addStatusLabelText.set("Tray cant be left empty")
		return
	tray = tray.upper()
	oppositeRoom = addOppositeRoom.get()
	if oppositeRoom == '':
		addStatusLabelText.set("Opposite Room cant be left empty")
		return
	oppositeRoom = oppositeRoom.upper()
	oppositeRack = addOppositeRack.get()
	if oppositeRack == '':
		addStatusLabelText.set("Opposite Rack cant be left empty")
		return
	oppositeRack = oppositeRack.upper()
	oppositeTray = addOppositeTray.get()
	if oppositeTray == '':
		addStatusLabelText.set("Opposite Tray cant be left empty")
		return
	oppositeTray = oppositeTray.upper()
	portState = {}
	for item in portsAdd:
		portState[item] = portsAdd[item]['var'].get()
	addStatusLabelText.set(database.create_entry(room, rack, tray, oppositeRoom, oppositeRack, oppositeTray, portState))
	for item in portsAdd:
		portsAdd[item]['item'].deselect()
	addRoom.delete(0, END)
	addRack.delete(0, END)
	addTray.delete(0, END)
	addOppositeRoom.delete(0, END)
	addOppositeRack.delete(0, END)
	addOppositeTray.delete(0, END)
	refresh_rooms_button

addButton = Button(addFrame, text="Add",height = buttonHeight, width = buttonWidth, command = add_button)
addButton.place(anchor = 'n', relx = addEntrysRelx, rely = addButtonsRely)

def check_opposite():
	room = addRoom.get()
	if room == '':
		return
	room = room.upper()	
	rack = addRack.get()
	if rack == '':
		return
	rack = rack.upper()
	tray = addTray.get()
	if tray == '':
		return
	tray = tray.upper()
	addOppositeRoom.delete(0, END)
	addOppositeRack.delete(0, END)
	addOppositeTray.delete(0, END)
	oppositePanel = database.check_opposite(room, rack, tray)
	addOppositeRoom.insert(0, oppositePanel[0][0])
	addOppositeRack.insert(0, oppositePanel[0][1])
	addOppositeTray.insert(0, oppositePanel[0][2])

checkOppositeButton = Button(addFrame, text="Check Opposite Tray ",height = buttonHeight, command = check_opposite)
checkOppositeButton.place(anchor = 'n', relx = 0.15, rely = addButtonsRely)

trayPortsAdd = Frame(addFrame, bg = "#e4e4e4", height= trayPortsHeight, width = trayPortsWidth)
trayPortsAdd.place(anchor = 'n', relx = 0.73, rely = 0.02)

addStatusLabelText = StringVar()
addStatusLabel = Label(addFrame, textvariable = addStatusLabelText,bg = "lightgrey", height = labelHeight)
addStatusLabelText.set("Adding Status")
addStatusLabel.place(anchor = 'n', relx = 0.25, rely = statusLabelRely)

portsAdd = {1:{},
			2:{},
			3:{},
			4:{},
			5:{},
			6:{},
			7:{},
			8:{},
			9:{},
			10:{},
			11:{},
			12:{},
			13:{},
			14:{},
			15:{},
			16:{},
			17:{},
			18:{},
			19:{},
			20:{},
			21:{},
			22:{},
			23:{},
			24:{},
			25:{},
			26:{},
			27:{},
			28:{},
			29:{},
			30:{},
			31:{},
			32:{},
			33:{},
			34:{},
			35:{},
			36:{},
			37:{},
			38:{},
			39:{},
			40:{},
			41:{},
			42:{},
			43:{},
			44:{},
			45:{},
			46:{},
			47:{},
			48:{},}

portNumber = 1
gridColumn = 0
gridRow = 0
for item in portsAdd:
	portsAdd[item]['text'] = str(portNumber)
	new_checkbutton(trayPortsAdd, portsAdd[item])
	portsAdd[item]['item'].grid(row = gridRow, column = gridColumn)
	portNumber += 1
	gridRow +=1
	if gridRow >= 12:
		gridRow = 0
		gridColumn += 1

top.mainloop()