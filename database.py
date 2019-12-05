
import sqlite3

conn = sqlite3.connect('patchpanels.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Patch_Panels (
	Room text NOT NULL,
	Rack text NOT NULL,
	Tray int,
	OppositeRoom text NOT NULL,
	OppositeRack text NOT NULL,
	OppositeTray int,
	Port1 int,
	Port2 int,
	Port3 int,
	Port4 int,
	Port5 int,
	Port6 int,
	Port7 int,
	Port8 int,
	Port9 int,
	Port10 int,
	Port11 int,
	Port12 int,
	Port13 int,
	Port14 int,
	Port15 int,
	Port16 int,
	Port17 int,
	Port18 int,
	Port19 int,
	Port20 int,
	Port21 int,
	Port22 int,
	Port23 int,
	Port24 int,
	Port25 int,
	Port26 int,
	Port27 int,
	Port28 int,
	Port29 int,
	Port30 int,
	Port31 int,
	Port32 int,
	Port33 int,
	Port34 int,
	Port35 int,
	Port36 int,
	Port37 int,
	Port38 int,
	Port39 int,
	Port40 int,
	Port41 int,
	Port42 int,
	Port43 int,
	Port44 int,
	Port45 int,
	Port46 int,
	Port47 int,
	Port48 int
	)""")


print("done")
conn.close()

def create_entry(room, rack, tray, oppositeRoom, oppositeRack, oppositeTray, ports):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT Room FROM Patch_Panels WHERE Room = ? AND Rack = ? AND Tray = ?", (room, rack, tray))
	existing = c.fetchall()
	if existing:
		message = "Tray entry already exists"
		return message
	c.execute("INSERT INTO Patch_Panels Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (room, rack, tray, oppositeRoom, oppositeRack, oppositeTray, ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8], ports[9], ports[10], ports[11], ports[12], ports[13], ports[14], ports[15], ports[16], ports[17], ports[18], ports[19], ports[20], ports[21], ports[22], ports[23], ports[24], ports[25], ports[26], ports[27], ports[28], ports[29], ports[30], ports[31], ports[32], ports[33], ports[34], ports[35], ports[36], ports[37], ports[38], ports[39], ports[40], ports[41], ports[42], ports[43], ports[44], ports[45], ports[46], ports[47], ports[48]))
	conn.commit()
	conn.close()
	message = "Tray added"
	return message

def check_opposite(room, rack, tray):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT Room, Rack, Tray FROM Patch_Panels WHERE OppositeRoom = ? AND OppositeRack = ? AND OppositeTray = ?", (room, rack, tray))
	oppositePanel = c.fetchall()
	if not oppositePanel:
		oppositePanel = [('', '', '')]
	conn.commit()
	conn.close()
	return oppositePanel

def refresh_rooms():
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT DISTINCT Room FROM Patch_Panels")
	rooms = c.fetchall()
	conn.commit()
	conn.close()
	return rooms

def refresh_racks(chosenRoom):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT DISTINCT Rack FROM Patch_Panels WHERE Room = ?", (chosenRoom,))
	racks = c.fetchall()
	conn.commit()
	conn.close()
	return racks
	
def refresh_trays(chosenRoom, chosenRack):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT DISTINCT Tray FROM Patch_Panels WHERE Room = ? AND Rack = ?", (chosenRoom, chosenRack))
	trays = c.fetchall()
	conn.commit()
	conn.close()
	return trays

def refresh_ports(chosenRoom, chosenRack, chosenTray):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT Port1, Port2, Port3, Port4, Port5, Port6, Port7, Port8, Port9, Port10, Port11, Port12, Port13, Port14, Port15, Port16, Port17, Port18, Port19, Port20, Port21, Port22, Port23, Port24, Port25, Port26, Port27, Port28, Port29, Port30, Port31, Port32, Port33, Port34, Port35, Port36, Port37, Port38, Port39, Port40, Port41, Port42, Port43, Port44, Port45, Port46, Port47, Port48 FROM Patch_Panels WHERE Room = ? AND Rack = ? AND Tray = ?", (chosenRoom, chosenRack, chosenTray))
	ports = c.fetchall()
	if not ports:
		ports = [(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)]
	conn.commit()
	conn.close()
	return ports

def refresh_opposite(chosenRoom, chosenRack, chosenTray):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT OppositeRoom, OppositeRack, OppositeTray FROM Patch_Panels WHERE Room = ? AND Rack = ? AND Tray = ?", (chosenRoom, chosenRack, chosenTray))
	oppositePanel = c.fetchall()
	conn.commit()
	conn.close()
	return oppositePanel

def update_entry(chosenRoom, chosenRack, chosenTray, ports):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("Update Patch_Panels Set Port1 = ?, Port2 = ?, Port3 = ?, Port4 = ?, Port5 = ?, Port6 = ?, Port7 = ?, Port8 = ?, Port9 = ?, Port10 = ?, Port11 = ?, Port12 = ?, Port13 = ?, Port14 = ?, Port15 = ?, Port16 = ?, Port17 = ?, Port18 = ?, Port19 = ?, Port20 = ?, Port21 = ?, Port22 = ?, Port23 = ?, Port24 = ?, Port25 = ?, Port26 = ?, Port27 = ?, Port28 = ?, Port29 = ?, Port30 = ?, Port31 = ?, Port32 = ?, Port33 = ?, Port34 = ?, Port35 = ?, Port36 = ?, Port37 = ?, Port38 = ?, Port39 = ?, Port40 = ?, Port41 = ?, Port42 = ?, Port43 = ?, Port44 = ?, Port45 = ?, Port46 = ?, Port47 = ?, Port48 = ? where Room = ? AND Rack = ? AND Tray = ?", (ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8], ports[9], ports[10], ports[11], ports[12], ports[13], ports[14], ports[15], ports[16], ports[17], ports[18], ports[19], ports[20], ports[21], ports[22], ports[23], ports[24], ports[25], ports[26], ports[27], ports[28], ports[29], ports[30], ports[31], ports[32], ports[33], ports[34], ports[35], ports[36], ports[37], ports[38], ports[39], ports[40], ports[41], ports[42], ports[43], ports[44], ports[45], ports[46], ports[47], ports[48],chosenRoom, chosenRack, chosenTray))
	conn.commit()
	conn.close()

def delete_tray(chosenRoom, chosenRack, chosenTray):
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("DELETE FROM Patch_Panels WHERE Room = ? AND Rack = ? AND Tray = ?", (chosenRoom, chosenRack, chosenTray))
	conn.commit()
	conn.close()

def fetch_rooms():
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT DISTINCT Room FROM Patch_Panels")
	rooms = c.fetchall()
	conn.commit()
	conn.close()
	return rooms

def fetch_racks():
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT DISTINCT Rack FROM Patch_Panels")
	racks = c.fetchall()
	conn.commit()
	conn.close()
	return racks

def fetch_trays():
	conn = sqlite3.connect('patchpanels.db')
	c = conn.cursor()
	c.execute("SELECT DISTINCT Tray FROM Patch_Panels")
	trays = c.fetchall()
	conn.commit()
	conn.close()
	return trays